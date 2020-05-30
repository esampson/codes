# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_script_tag
from evennia.utils.utils import inherits_from
from evennia import create_script

from codes.web.auspices.forms import editForm
from django.http import HttpResponseRedirect
from datetime import datetime
from evennia.objects.models import ObjectDB
from django.conf import settings
from evennia.utils import create
from urllib.parse import unquote
from urllib.parse import quote

class auspice_class:
    longname = ''
    auspice_skills = []
    renown = ''
    auspice_gifts = []
    info = ''
    reference = ''
    restricted = False

    def update(self,longname,auspice_skills,renown,auspice_gifts,info,reference,restricted):
        self.longname = longname
        self.auspice_skills = auspice_skills
        self.renown = renown
        self.auspice_gifts = auspice_gifts
        self.info = info
        self.reference = reference
        self.restricted = restricted

def sheet(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('auspice_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'auspices/error.html', {'message': 'No matching auspice: '+object_id})
    if len(stats) > 1:
        return render(request, 'auspices/error.html', {'message': 'Too many matching auspices'})
    auspice = auspice_class()
    longname = stats[0].db.longname
    auspice_skills = stats[0].db.auspice_skills
    renown= stats[0].db.renown
    auspice_gifts = stats[0].db.auspice_gifts
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    reference = stats[0].db.reference
    restricted = stats[0].db.restricted
    auspice.update(longname,auspice_skills,renown,auspice_gifts,info,reference,restricted)
    return render(request, 'auspices/sheet.html', {'auspice': auspice, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('auspice_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'auspices/error.html', {'message': 'No matching auspice'})
    if len(stats) > 1:
        return render(request, 'auspices/error.html', {'message': 'Too many matching auspices'})
    stat = stats[0]
    starting_data = {'longname':stat.db.longname,
                     'auspice_skills':stat.db.auspice_skills,
                     'renown': stat.db.renown,
                     'auspice_gifts' : stat.db.auspice_gifts,
                     'info': stat.db.info,
                     'reference':stat.db.reference,
                     'restricted':stat.db.restricted,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'auspices/editor.html', {'form': form, 'auspice_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('auspice_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'auspices/error.html', {'message': len(data) + ' No matching auspices: ' + n})
                if len(stats) > 1:
                    return render(request, 'auspices/error.html', {'message': 'Too many matching auspices'})
                auspice = stats[0]
                auspice_skills = []
                if form.cleaned_data['auspice_skills'] != '[]':
                    for item in form.cleaned_data['auspice_skills'][1:-1].split(','):
                        auspice_skills.append(item.strip()[1:-1])
                auspice_gifts = []
                if form.cleaned_data['auspice_gifts'] != '[]':
                    for item in form.cleaned_data['auspice_gifts'][1:-1].split(','):
                        auspice_gifts.append(item.strip()[1:-1])
                auspice = auspice.update(
                    longname=form.cleaned_data['longname'],
                    auspice_skills=auspice_skills,
                    renown = form.cleaned_data['renown'],
                    auspice_gifts = form.cleaned_data['auspice_gifts'],
                    info=form.cleaned_data['info'],
                    reference=form.cleaned_data['reference'],
                    restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/auspices/view/'+quote(n))
            else:
                return render(request, 'auspices/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'auspices/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'auspices/error.html', {'message': 'Not staff'})

def create(request):

    starting_data = {'longname':'',
                     'auspice_skills':[],
                     'renown':'',
                     'auspice_gifts':[],
                     'info': '',
                     'reference':'',
                     'restricted':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'auspices/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                auspice_skills = []
                if form.cleaned_data['auspice_skills'] != '[]':
                    for item in form.cleaned_data['auspice_skills'][1:-1].split(','):
                        auspice_skills.append(item.strip()[1:-1])
                auspice_gifts = []
                if form.cleaned_data['auspice_gifts'] != '[]':
                    for item in form.cleaned_data['auspice_gifts'][1:-1].split(','):
                        auspice_gifts.append(item.strip()[1:-1])
                s = create_script('typeclasses.scripts.AuspiceScript',
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.auspice_skills=auspice_skills
                s.db.renown = form.cleaned_data['renown']
                s.db.auspice_gifts = auspice_gifts
                s.db.info = form.cleaned_data['info']
                s.db.reference=form.cleaned_data['reference']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/auspices/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'auspices/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'auspices/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'auspices/error.html', {'message': 'Not staff'})

def list(request):
    data = search_script_tag('auspice_stat')
    auspices = []
    for stat in data:
        auspices.append(stat.db.longname)
    auspices.sort()
    return render(request, 'auspices/list.html', {'auspices':auspices })
