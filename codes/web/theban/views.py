# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_script_tag
from evennia.utils.utils import inherits_from
from evennia import create_script

from codes.web.theban.forms import editForm
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

class theban_class:
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
        data = search_script_tag('theban_rite_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'theban/error.html', {'message': 'No matching theban: '+object_id})
    if len(stats) > 1:
        return render(request, 'theban/error.html', {'message': 'Too many matching theban'})
    theban = theban_class()
    longname = stats[0].db.longname
    rank = stats[0].db.rank
    prereq = stats[0].db.prereq
    reference = stats[0].db.reference
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    restricted = stats[0].db.restricted
    theban.update(longname,rank,prereq,reference,info,restricted)
    if request.method == 'POST':
         return render(request, 'theban/error.html', {'message': 'POST'})
    return render(request, 'theban/sheet.html', {'theban': theban, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('theban_rite_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'theban/error.html', {'message': 'No matching theban'})
    if len(stats) > 1:
        return render(request, 'theban/error.html', {'message': 'Too many matching theban'})
    theban = stats[0]
    starting_data = {'longname':theban.db.longname, 
                     'rank':theban.db.rank,
                     'prereq':theban.db.prereq,
                     'reference':theban.db.reference,
                     'info':theban.db.info,
                     'restricted':theban.db.restricted,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'theban/editor.html', {'form': form, 'theban_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('theban_rite_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'theban/error.html', {'message': len(data) + ' No matching theban: ' + n})
                if len(stats) > 1:
                    return render(request, 'theban/error.html', {'message': 'Too many matching theban'})
                theban = stats[0]
                app = theban.update(longname=form.cleaned_data['longname'],
                                   rank=int(form.cleaned_data['rank']),
                                   prereq=form.cleaned_data['prereq'],
                                   reference=form.cleaned_data['reference'],
                                   info=form.cleaned_data['info'],
                                   restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/theban/view/'+quote(n))
            else:
                return render(request, 'theban/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'theban/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'theban/error.html', {'message': 'Not staff'})
    
def create(request):
    
    starting_data = {'longname':'', 
                     'rank':0, 
                     'prereq':'',
                     'reference':'',
                     'info':'',
                     'restricted':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'theban/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                s = create_script('typeclasses.scripts.thebanRiteScript', 
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.rank=int(form.cleaned_data['rank'])
                s.db.prereq=form.cleaned_data['prereq']
                s.db.reference=form.cleaned_data['reference']
                s.db.info=form.cleaned_data['info']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/theban/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'theban/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'theban/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'theban/error.html', {'message': 'Not staff'})
    
def list(request):
    data = search_script_tag('theban_rite_stat')
    theban = []
    for stat in data:
        theban.append(stat.db.longname)
    theban.sort()
    return render(request, 'theban/list.html', {'theban':theban })