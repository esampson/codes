# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_script_tag
from evennia.utils.utils import inherits_from
from evennia import create_script

from codes.web.covenants.forms import editForm
from django.http import HttpResponseRedirect
from datetime import datetime
from evennia.objects.models import ObjectDB
from django.conf import settings
from evennia.utils import create
from urllib.parse import unquote
from urllib.parse import quote

class covenant_class:
    longname = ''
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
        data = search_script_tag('covenant_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'covenants/error.html', {'message': 'No matching covenant: '+object_id})
    if len(stats) > 1:
        return render(request, 'covenants/error.html', {'message': 'Too many matching covenants'})
    covenant = covenant_class()
    longname = stats[0].db.longname
    reference = stats[0].db.reference
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info=chr(160)
    restricted = stats[0].db.restricted
    covenant.update(longname,reference=reference,info=info,restricted=restricted)
    return render(request, 'covenants/sheet.html', {'covenant': covenant, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('covenant_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'covenants/error.html', {'message': 'No matching covenant'})
    if len(stats) > 1:
        return render(request, 'covenants/error.html', {'message': 'Too many matching covenants'})
    stat = stats[0]
    starting_data = {'longname':stat.db.longname,
                     'reference':stat.db.reference,
                     'info':stat.db.info,
                     'restricted':stat.db.restricted,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'covenants/editor.html', {'form': form, 'covenant_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('covenant_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'covenants/error.html', {'message': len(data) + ' No matching covenants: ' + n})
                if len(stats) > 1:
                    return render(request, 'covenants/error.html', {'message': 'Too many matching covenants'})
                covenant = stats[0]
                app = covenant.update(longname=form.cleaned_data['longname'],
                                   reference=form.cleaned_data['reference'],
                                   info=form.cleaned_data['info'],
                                   restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/covenants/view/'+quote(n))
            else:
                return render(request, 'covenants/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'covenants/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'covenants/error.html', {'message': 'Not staff'})

def create(request):

    starting_data = {'longname':'',
                     'reference':'',
                     'info':'',
                     'restricted':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'covenants/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                s = create_script('typeclasses.scripts.CovenantScript',
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.reference=form.cleaned_data['reference']
                s.db.info=form.cleaned_data['info']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/covenants/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'covenants/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'covenants/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'covenants/error.html', {'message': 'Not staff'})

def list(request):
    data = search_script_tag('covenant_stat')
    groups = []
    covenants = []
    for stat in data:
        covenants.append(stat.db.longname)
    covenants.sort()
    return render(request, 'covenants/list.html', {'covenants':covenants })
