# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_script_tag
from evennia.utils.utils import inherits_from
from evennia import create_script

from codes.web.arcana.forms import editForm
from django.http import HttpResponseRedirect
from datetime import datetime
from evennia.objects.models import ObjectDB
from django.conf import settings
from evennia.utils import create
from urllib.parse import unquote
from urllib.parse import quote

class arcana_class:
    longname = ''
    prereq = ''
    reference = ''
    info = ''
    restricted = False
    
    def update(self,longname,prereq,reference,info,restricted):
        self.longname = longname
        self.prereq = prereq
        self.reference = reference
        self.info = info
        self.restricted = restricted
    
def sheet(request, object_id):
    object_id = unquote(object_id)

    try:
        data = search_script_tag('arcana_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) > 1:
        itemlist = stats.copy()
        stats = []
        for item in itemlist:
            if item.db.longname.lower() == object_id.lower():
                stats.append(item)
        if len(stats) == 0:
            stats = itemlist.copy()
    if len(stats) == 0:
        return render(request, 'arcana/error.html', {'message': 'No matching arcana: '+object_id})
    if len(stats) > 1:
        return render(request, 'arcana/error.html', {'message': 'Too many matching arcana'})
    arcanum = arcana_class()
    longname = stats[0].db.longname
    prereq = stats[0].db.prereq
    reference = stats[0].db.reference
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    restricted = stats[0].db.restricted
    arcanum.update(longname,prereq,reference,info,restricted)
    return render(request, 'arcana/sheet.html', {'arcanum': arcanum, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('arcana_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'arcana/error.html', {'message': 'No matching arcanum'})
    if len(stats) > 1:
        return render(request, 'arcana/error.html', {'message': 'Too many matching arcana'})
    arcanum = stats[0]
    starting_data = {'longname':arcanum.db.longname,
                     'info':arcanum.db.info,
                     'reference':arcanum.db.reference,
                     'restricted':arcanum.db.restricted,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'arcana/editor.html', {'form': form, 'arcanum_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('arcana_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) > 1:
                    itemlist = stats.copy()
                    stats = []
                    for item in itemlist:
                        if item.db.longname.lower() == n:
                            stats.append(item)
                    if len(stats) == 0:
                        stats = itemlist.copy()
                if len(stats) == 0:
                    return render(request, 'arcana/error.html', {'message': len(data) + ' No matching arcana: ' + n})
                if len(stats) > 1:
                    return render(request, 'arcana/error.html', {'message': 'Too many matching arcana'})
                arcanum = stats[0]
                app = arcanum.update(longname=form.cleaned_data['longname'],
                                     info=form.cleaned_data['info'],
                                     reference=form.cleaned_data['reference'],
                                     restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/arcana/view/'+quote(n))
            else:
                return render(request, 'arcana/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'arcana/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'arcana/error.html', {'message': 'Not staff'})
    
def create(request):
    
    starting_data = {'longname':'',
                     'info':'',
                     'reference':'',
                     'restricted':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'arcana/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                s = create_script('typeclasses.scripts.arcanaScript',
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.info=form.cleaned_data['info']
                s.db.reference=form.cleaned_data['reference']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/arcana/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'arcana/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'arcana/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'arcana/error.html', {'message': 'Not staff'})
    
def list(request):
    data = search_script_tag('arcana_stat')
    arcana = []
    for stat in data:
        arcana.append(stat.db.longname)
    arcana.sort()
    return render(request, 'arcana/list.html', {'arcana':arcana })
