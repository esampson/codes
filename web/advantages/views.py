# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_script_tag
from evennia.utils.utils import inherits_from
from evennia import create_script

from web.advantages.forms import editForm
from django.http import HttpResponseRedirect
from datetime import datetime
from evennia.objects.models import ObjectDB
from django.conf import settings
from evennia.utils import create
from urllib.parse import unquote
from urllib.parse import quote
import stat

class advantage_class:
    longname = ''
    category = ''
    reference = ''
    info = ''
    simple_gauge = False
    
    def update(self,longname,category,reference,info,simple_gauge):
        self.longname = longname
        self.category = category
        self.reference = reference
        self.info = info
        self.simple_gauge = simple_gauge
    
def sheet(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('advantage_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'advantages/error.html', {'message': 'No matching advantages: '+object_id})
    if len(stats) > 1:
        return render(request, 'advantages/error.html', {'message': 'Too many matching advantages'})
    advantage = advantage_class()
    longname = stats[0].db.longname
    category = stats[0].db.category
    reference = stats[0].db.reference
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = ''
    simple_gauge = stats[0].db.simple_gauge
    advantage.update(longname,category,reference,info,simple_gauge)
    return render(request, 'advantages/sheet.html', {'advantage': advantage, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('advantage_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'advantages/error.html', {'message': 'No matching advantage'})
    if len(stats) > 1:
        return render(request, 'advantages/error.html', {'message': 'Too many matching advantages'})
    advantage = stats[0]
    starting_data = {'longname':advantage.db.longname, 
                     'category':advantage.db.category, 
                     'reference':advantage.db.reference,
                     'info':advantage.db.info,
                     'simple_gauge':advantage.db.simple_gauge,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'advantages/editor.html', {'form': form, 'advantage_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('advantage_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'advantages/error.html', {'message': len(data) + ' No matching advantages: ' + n})
                if len(stats) > 1:
                    return render(request, 'advantages/error.html', {'message': 'Too many matching advantages'})
                advantage = stats[0]
                app = advantage.update(longname=form.cleaned_data['longname'],
                                   category=form.cleaned_data['category'],
                                   reference=form.cleaned_data['reference'],
                                   info=form.cleaned_data['info'],
                                   simple_gauge=form.cleaned_data['simple_gauge'])
                return HttpResponseRedirect('/advantages/view/'+quote(n))
            else:
                return render(request, 'advantages/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'advantages/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'advantages/error.html', {'message': 'Not staff'})
    
def create(request):
    
    starting_data = {'longname':'', 
                     'category':'', 
                     'reference':'',
                     'info':'',
                     'simple_gauge':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'advantages/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].longname.replace('\'','').replace(' ','_')
                s = create_script('typeclasses.scripts.advantageScript', 
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.category=form.cleaned_data['category']
                s.db.reference=form.cleaned_data['reference']
                s.db.info=form.cleaned_data['info']
                s.db.simple_gauge=form.cleaned_data['simple_gauge']
                return HttpResponseRedirect('/advantages/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'advantages/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'advantages/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'advantages/error.html', {'message': 'Not staff'})
    
def list(request):
    data = search_script_tag('advantage_stat')
    groups = []
    for stat in data:
        if stat.db.category:
            if stat.db.category.capitalize() not in groups:
                groups.append(stat.db.category.capitalize())
    groups.sort()
    advantages = []
    for group in groups:
        temp_list = []
        for stat in data:
            if stat.db.category:
                if stat.db.category.capitalize() == group:
                    temp_list.append(stat.db.longname)
            else:
                temp_list.append(stat.db.longname)
        temp_list.sort()
        advantages.append([group] + temp_list)
    return render(request, 'advantages/list.html', {'advantages':advantages })
