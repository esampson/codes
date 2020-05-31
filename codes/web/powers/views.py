# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_script_tag
from evennia.utils.utils import inherits_from
from evennia import create_script

from codes.web.powers.forms import EditForm
from django.http import HttpResponseRedirect
from datetime import datetime
from evennia.objects.models import ObjectDB
from django.conf import settings
from evennia.utils import create
from urllib.parse import unquote
from urllib.parse import quote

class power_class:
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
        data = search_script_tag('power_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'powers/error.html', {'message': 'No matching powers: '+object_id})
    if len(stats) > 1:
        return render(request, 'powers/error.html', {'message': 'Too many matching powers'})
    power = power_class()
    longname = stats[0].db.longname
    category = stats[0].db.category
    reference = stats[0].db.reference
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    restricted = stats[0].db.restricted
    power.update(longname,category,reference,info,restricted)
    return render(request, 'powers/sheet.html', {'power': power, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('power_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'powers/error.html', {'message': 'No matching power'})
    if len(stats) > 1:
        return render(request, 'powers/error.html', {'message': 'Too many matching powers'})
    power = stats[0]
    starting_data = {'longname':power.db.longname,
                     'category':power.db.category,
                     'reference':power.db.reference,
                     'info':power.db.info,
                     'restricted':power.db.restricted,
                     'link':object_id}
    form = EditForm(initial = starting_data)
    return render(request, 'powers/editor.html', {'form': form, 'power_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = EditForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('power_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'powers/error.html', {'message': len(data) + ' No matching powers: ' + n})
                if len(stats) > 1:
                    return render(request, 'powers/error.html', {'message': 'Too many matching powers'})
                power = stats[0]
                app = power.update(longname=form.cleaned_data['longname'],
                                   category=form.cleaned_data['category'],
                                   reference=form.cleaned_data['reference'],
                                   info=form.cleaned_data['info'],
                                   restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/powers/view/'+quote(n))
            else:
                return render(request, 'powers/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'powers/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'powers/error.html', {'message': 'Not staff'})

def create(request):

    starting_data = {'longname':'',
                     'category':'',
                     'reference':'',
                     'info':'',
                     'restricted':False,
                     'link':''}
    form = EditForm(initial = starting_data)
    return render(request, 'powers/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = EditForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                s = create_script('typeclasses.scripts.PowerStatScript',
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.category=form.cleaned_data['category']
                s.db.reference=form.cleaned_data['reference']
                s.db.info=form.cleaned_data['info']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/powers/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'powers/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'powers/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'powers/error.html', {'message': 'Not staff'})

def list(request):
    data = search_script_tag('power_stat')
    groups = []
    for stat in data:
        if stat.db.category:
            if stat.db.category.capitalize() not in groups:
                groups.append(stat.db.category.capitalize())
    groups.sort()
    powers = []
    for group in groups:
        temp_list = []
        for stat in data:
            if stat.db.category.capitalize() == group:
                temp_list.append(stat.db.longname)
        temp_list.sort()
        powers.append([group] + temp_list)
    return render(request, 'powers/list.html', {'powers':powers })
