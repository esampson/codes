# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_script_tag
from evennia.utils.utils import inherits_from
from evennia import create_script

from codes.web.devotions.forms import editForm
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

class devotion_class:
    longname = ''
    cost = ''
    prereq = ''
    reference = ''
    info = ''
    restricted = False
    
    def update(self,longname,cost,prereq,reference,info,restricted):
        self.longname = longname
        self.cost = cost
        self.prereq = prereq
        self.reference = reference
        self.info = info
        self.restricted = restricted
    
def sheet(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('devotion_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'devotions/error.html', {'message': 'No matching devotions: '+object_id})
    if len(stats) > 1:
        return render(request, 'devotions/error.html', {'message': 'Too many matching devotions'})
    devotion = devotion_class()
    longname = stats[0].db.longname
    cost = stats[0].db.cost
    prereq = stats[0].db.prereq
    reference = stats[0].db.reference
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    restricted = stats[0].db.restricted
    devotion.update(longname,cost,prereq,reference,info,restricted)
    if request.method == 'POST':
         return render(request, 'devotions/error.html', {'message': 'POST'})
    return render(request, 'devotions/sheet.html', {'devotion': devotion, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('devotion_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'devotions/error.html', {'message': 'No matching devotions'})
    if len(stats) > 1:
        return render(request, 'devotions/error.html', {'message': 'Too many matching devotions'})
    devotion = stats[0]
    starting_data = {'longname':devotion.db.longname, 
                     'cost':devotion.db.cost,
                     'prereq':devotion.db.prereq,
                     'reference':devotion.db.reference,
                     'info':devotion.db.info,
                     'restricted':devotion.db.restricted,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'devotions/editor.html', {'form': form, 'devotion_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('devotion_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'devotions/error.html', {'message': len(data) + ' No matching devotions: ' + n})
                if len(stats) > 1:
                    return render(request, 'devotions/error.html', {'message': 'Too many matching devotions'})
                devotion = stats[0]
                app = devotion.update(longname=form.cleaned_data['longname'],
                                   cost=form.cleaned_data['cost'],
                                   prereq=form.cleaned_data['prereq'],
                                   reference=form.cleaned_data['reference'],
                                   info=form.cleaned_data['info'],
                                   restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/devotions/view/'+quote(n))
            else:
                return render(request, 'devotions/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'devotions/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'devotions/error.html', {'message': 'Not staff'})
    
def create(request):
    
    starting_data = {'longname':'', 
                     'cost':'', 
                     'prereq':'',
                     'reference':'',
                     'info':'',
                     'restricted':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'devotions/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                s = create_script('typeclasses.scripts.devotionScript', 
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.cost=form.cleaned_data['cost']
                s.db.prereq=form.cleaned_data['prereq']
                s.db.reference=form.cleaned_data['reference']
                s.db.info=form.cleaned_data['info']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/devotions/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'devotions/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'devotions/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'devotions/error.html', {'message': 'Not staff'})
    
def list(request):
    data = search_script_tag('devotion_stat')
    devotions = []
    for stat in data:
        devotions.append(stat.db.longname)
    devotions.sort()
    return render(request, 'devotions/list.html', {'devotions':devotions })