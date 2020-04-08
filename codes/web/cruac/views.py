# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_script_tag
from evennia.utils.utils import inherits_from
from evennia import create_script

from codes.web.cruac.forms import editForm
from django.http import HttpResponseRedirect
from datetime import datetime
from evennia.objects.models import ObjectDB
from django.conf import settings
from evennia.utils import create
from urllib.parse import unquote
from urllib.parse import quote

def string_to_list(string):
    if type(string) is list:
        result = String
    else:
        temp_string = string[1:-1]
        result=[]
        for item in temp_string.split(','):
            if item.strip().isnumeric():
                entry = int(item.strip())
            else:
                entry = item.strip()
            if entry != '':
                result.append(entry)
    return result

class cruac_class:
    longname = ''
    rank = 0
    prereq = ''
    reference = ''
    info = ''
    restricted = False
    
    def update(self,longname,rank,prereq,reference,info,restricted):
        self.longname = longname
        self.rank = rank
        self.prereq = prereq
        self.reference = reference
        self.info = info
        self.restricted = restricted
    
def sheet(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('cruac_rite_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'cruac/error.html', {'message': 'No matching cruac: '+object_id})
    if len(stats) > 1:
        return render(request, 'cruac/error.html', {'message': 'Too many matching cruac'})
    cruac = cruac_class()
    longname = stats[0].db.longname
    rank = stats[0].db.rank
    prereq = stats[0].db.prereq
    reference = stats[0].db.reference
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    restricted = stats[0].db.restricted
    cruac.update(longname,rank,prereq,reference,info,restricted)
    if request.method == 'POST':
         return render(request, 'cruac/error.html', {'message': 'POST'})
    return render(request, 'cruac/sheet.html', {'cruac': cruac, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('cruac_rite_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'cruac/error.html', {'message': 'No matching cruac'})
    if len(stats) > 1:
        return render(request, 'cruac/error.html', {'message': 'Too many matching cruac'})
    cruac = stats[0]
    starting_data = {'longname':cruac.db.longname, 
                     'rank':cruac.db.rank,
                     'prereq':cruac.db.prereq,
                     'reference':cruac.db.reference,
                     'info':cruac.db.info,
                     'restricted':cruac.db.restricted,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'cruac/editor.html', {'form': form, 'cruac_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('cruac_rite_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'cruac/error.html', {'message': len(data) + ' No matching cruac: ' + n})
                if len(stats) > 1:
                    return render(request, 'cruac/error.html', {'message': 'Too many matching cruac'})
                cruac = stats[0]
                app = cruac.update(longname=form.cleaned_data['longname'],
                                   rank=int(form.cleaned_data['rank']),
                                   prereq=form.cleaned_data['prereq'],
                                   reference=form.cleaned_data['reference'],
                                   info=form.cleaned_data['info'],
                                   restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/cruac/view/'+quote(n))
            else:
                return render(request, 'cruac/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'cruac/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'cruac/error.html', {'message': 'Not staff'})
    
def create(request):
    
    starting_data = {'longname':'', 
                     'rank':0, 
                     'prereq':'',
                     'reference':'',
                     'info':'',
                     'restricted':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'cruac/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                s = create_script('typeclasses.scripts.cruacRiteScript', 
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.rank=int(form.cleaned_data['rank'])
                s.db.prereq=form.cleaned_data['prereq']
                s.db.reference=form.cleaned_data['reference']
                s.db.info=form.cleaned_data['info']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/cruac/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'cruac/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'cruac/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'cruac/error.html', {'message': 'Not staff'})
    
def list(request):
    data = search_script_tag('cruac_rite_stat')
    cruac = []
    for stat in data:
        cruac.append(stat.db.longname)
    cruac.sort()
    return render(request, 'cruac/list.html', {'cruac':cruac })