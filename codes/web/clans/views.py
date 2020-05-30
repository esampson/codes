# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_script_tag
from evennia.utils.utils import inherits_from
from evennia import create_script

from codes.web.clans.forms import editForm
from django.http import HttpResponseRedirect
from datetime import datetime
from evennia.objects.models import ObjectDB
from django.conf import settings
from evennia.utils import create
from urllib.parse import unquote
from urllib.parse import quote

class clan_class:
    longname = ''
    favored_attributes = []
    favored_disciplines = []
    reference = ''
    info = ''
    bloodline = False
    restricted = False

    def update(self,longname,favored_attributes,favored_disciplines,reference,info,bloodline,restricted):
        self.longname = longname
        self.favored_attributes = favored_attributes
        self.favored_disciplines = favored_disciplines
        self.reference = reference
        self.info = info
        self.bloodline = bloodline
        self.restricted = restricted


def sheet(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('clan_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'clans/error.html', {'message': 'No matching clan: '+object_id})
    if len(stats) > 1:
        return render(request, 'clans/error.html', {'message': 'Too many matching clans'})
    clan = clan_class()
    longname = stats[0].db.longname
    favored_attributes = stats[0].db.favored_attributes
    favored_disciplines = stats[0].db.favored_disciplines
    reference = stats[0].db.reference
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    bloodline = stats[0].db.bloodline
    restricted = stats[0].db.restricted
    clan.update(longname,favored_attributes,favored_disciplines,reference,info,bloodline,restricted)
    return render(request, 'clans/sheet.html', {'clan': clan, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('clan_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'clans/error.html', {'message': 'No matching clan'})
    if len(stats) > 1:
        return render(request, 'clans/error.html', {'message': 'Too many matching clans'})
    stat = stats[0]
    starting_data = {'longname':stat.db.longname,
                     'favored_attributes':stat.db.favored_attributes,
                     'favored_disciplines': stat.db.favored_disciplines,
                     'reference':stat.db.reference,
                     'info':stat.db.info,
                     'bloodline':stat.db.bloodline,
                     'restricted':stat.db.restricted,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'clans/editor.html', {'form': form, 'clan_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('clan_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'clans/error.html', {'message': len(data) + ' No matching clans: ' + n})
                if len(stats) > 1:
                    return render(request, 'clans/error.html', {'message': 'Too many matching clans'})
                clan = stats[0]
                favored_attributes = []
                if form.cleaned_data['favored_attributes'] != '[]':
                    for item in form.cleaned_data['favored_attributes'][1:-1].split(','):
                        favored_attributes.append(item.strip()[1:-1])
                favored_disciplines = []
                if form.cleaned_data['favored_disciplines'] != '[]':
                    for item in form.cleaned_data['favored_disciplines'][1:-1].split(','):
                        favored_disciplines.append(item.strip()[1:-1])
                app = clan.update(longname=form.cleaned_data['longname'],
                                   favored_attributes=favored_attributes,
                                   favored_disciplines = favored_disciplines,
                                   reference=form.cleaned_data['reference'],
                                   info=form.cleaned_data['info'],
                                   bloodline=form.cleaned_data['bloodline'],
                                   restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/clans/view/'+quote(n))
            else:
                return render(request, 'clans/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'clans/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'clans/error.html', {'message': 'Not staff'})

def create(request):

    starting_data = {'longname':'',
                     'favored_attributes':[],
                     'reference':'',
                     'favored_disciplines' : [],
                     'info':'',
                     'bloodline':False,
                     'restricted':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'clans/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                favored_attributes = []
                if form.cleaned_data['favored_attributes'] != '[]':
                    for item in form.cleaned_data['favored_attributes'][1:-1].split(','):
                        favored_attributes.append(item.strip()[1:-1])
                favored_disciplines = []
                if form.cleaned_data['favored_disciplines'] != '[]':
                    for item in form.cleaned_data['favored_disciplines'][1:-1].split(','):
                        favored_disciplines.append(item.strip()[1:-1])
                s = create_script('typeclasses.scripts.ClanScript',
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.favored_attributes=favored_attributes
                s.db.favored_disciplines = favored_disciplines
                s.db.reference=form.cleaned_data['reference']
                s.db.info=form.cleaned_data['info']
                s.db.bloodline=form.cleaned_data['bloodline']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/clans/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'clans/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'clans/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'clans/error.html', {'message': 'Not staff'})

def list(request):
    data = search_script_tag('clan_stat')
    groups = []
    clans = []
    for stat in data:
        clans.append(stat.db.longname)
    clans.sort()
    return render(request, 'clans/list.html', {'clans':clans })
