# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_script_tag
from evennia.utils.utils import inherits_from
from evennia import create_script

from web.spheres.forms import editForm
from django.http import HttpResponseRedirect
from datetime import datetime
from evennia.objects.models import ObjectDB
from django.conf import settings
from evennia.utils import create
from urllib.parse import unquote
from urllib.parse import quote
import stat

class sphere_class:
    longname = ''
    category = ''
    reference = ''
    info = ''
    restricted = False
    
    def update(self,longname,category,reference,info,restricted):
        self.longname = longname
        self.category = category
        self.reference = reference
        self.info = info
        self.restricted = restricted
    
def sheet(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('sphere_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'spheres/error.html', {'message': 'No matching spheres: '+object_id})
    if len(stats) > 1:
        return render(request, 'spheres/error.html', {'message': 'Too many matching spheres'})
    sphere = sphere_class()
    longname = stats[0].db.longname
    category = stats[0].db.category
    reference = stats[0].db.reference
    info = stats[0].db.info.replace('|/','\n')
    restricted = stats[0].db.restricted
    sphere.update(longname,category,reference,info,restricted)
    return render(request, 'spheres/sheet.html', {'sphere': sphere, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('sphere_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'spheres/error.html', {'message': 'No matching sphere'})
    if len(stats) > 1:
        return render(request, 'spheres/error.html', {'message': 'Too many matching spheres'})
    sphere = stats[0]
    starting_data = {'longname':sphere.db.longname, 
                     'category':sphere.db.category, 
                     'reference':sphere.db.reference,
                     'info':sphere.db.info,
                     'restricted':sphere.db.restricted,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'spheres/editor.html', {'form': form, 'sphere_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('sphere_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'spheres/error.html', {'message': len(data) + ' No matching spheres: ' + n})
                if len(stats) > 1:
                    return render(request, 'spheres/error.html', {'message': 'Too many matching spheres'})
                sphere = stats[0]
                app = sphere.update(longname=form.cleaned_data['longname'],
                                   category=form.cleaned_data['category'],
                                   reference=form.cleaned_data['reference'],
                                   info=form.cleaned_data['info'],
                                   restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/spheres/view/'+quote(n))
            else:
                return render(request, 'spheres/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'spheres/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'spheres/error.html', {'message': 'Not staff'})
    
def create(request):
    
    starting_data = {'longname':'', 
                     'category':'', 
                     'reference':'',
                     'info':'',
                     'restricted':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'spheres/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                s = create_script('typeclasses.scripts.sphereStatScript', 
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.category=form.cleaned_data['category']
                s.db.reference=form.cleaned_data['reference']
                s.db.info=form.cleaned_data['info']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/spheres/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'spheres/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'spheres/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'spheres/error.html', {'message': 'Not staff'})
    
def list(request):
    data = search_script_tag('sphere_stat')
    groups = []
    for stat in data:
        if stat.db.category.capitalize() not in groups:
            groups.append(stat.db.category.capitalize())
    groups.sort()
    spheres = []
    for group in groups:
        temp_list = []
        for stat in data:
            if stat.db.category.capitalize() == group:
                temp_list.append(stat.db.longname)
        temp_list.sort()
        spheres.append([group] + temp_list)
    return render(request, 'spheres/list.html', {'spheres':spheres })
