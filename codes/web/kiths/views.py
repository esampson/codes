# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_script_tag
from evennia.utils.utils import inherits_from
from evennia import create_script

from codes.web.kiths.forms import editForm
from django.http import HttpResponseRedirect
from datetime import datetime
from evennia.objects.models import ObjectDB
from django.conf import settings
from evennia.utils import create
from urllib.parse import unquote
from urllib.parse import quote

class kith_class:
    longname = ''
    bonus_attributes = []
    reference = ''
    info = ''
    restricted = False
    
    def update(self,longname,reference,info,restricted):
        self.longname = longname
        self.reference = reference
        self.info = info
        self.restricted = restricted
    
def sheet(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('kith_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'kiths/error.html', {'message': 'No matching kith: '+object_id})
    if len(stats) > 1:
        return render(request, 'kiths/error.html', {'message': 'Too many matching kiths'})
    kith = kith_class()
    longname = stats[0].db.longname
    bonus_attributes = stats[0].db.bonus_attributes
    reference = stats[0].db.reference
    info = stats[0].db.info.replace('|/','\n')
    restricted = stats[0].db.restricted
    kith.update(longname,reference=reference,info=info,restricted=restricted)
    return render(request, 'kiths/sheet.html', {'kith': kith, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('kith_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'kiths/error.html', {'message': 'No matching kith'})
    if len(stats) > 1:
        return render(request, 'kiths/error.html', {'message': 'Too many matching kiths'})
    stat = stats[0]
    starting_data = {'longname':stat.db.longname, 
                     'reference':stat.db.reference,
                     'info':stat.db.info,
                     'restricted':stat.db.restricted,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'kiths/editor.html', {'form': form, 'kith_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('kith_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'kiths/error.html', {'message': len(data) + ' No matching kiths: ' + n})
                if len(stats) > 1:
                    return render(request, 'kiths/error.html', {'message': 'Too many matching kiths'})
                kith = stats[0]
                app = kith.update(longname=form.cleaned_data['longname'],
                                   reference=form.cleaned_data['reference'],
                                   info=form.cleaned_data['info'],
                                   restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/kiths/view/'+quote(n))
            else:
                return render(request, 'kiths/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'kiths/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'kiths/error.html', {'message': 'Not staff'})
    
def create(request):
    
    starting_data = {'longname':'', 
                     'bonus_attributes':[], 
                     'reference':'',
                     'info':'',
                     'restricted':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'kiths/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                s = create_script('typeclasses.scripts.kithScript', 
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.reference=form.cleaned_data['reference']
                s.db.info=form.cleaned_data['info']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/kiths/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'kiths/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'kiths/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'kiths/error.html', {'message': 'Not staff'})
    
def list(request):
    data = search_script_tag('kith_stat')
    groups = []
    kiths = []
    for stat in data:
        kiths.append(stat.db.longname)
    kiths.sort()
    return render(request, 'kiths/list.html', {'kiths':kiths })
