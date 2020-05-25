# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_script_tag
from evennia.utils.utils import inherits_from
from evennia import create_script

from codes.web.coils.forms import editForm
from django.http import HttpResponseRedirect
from datetime import datetime
from evennia.objects.models import ObjectDB
from django.conf import settings
from evennia.utils import create
from urllib.parse import unquote
from urllib.parse import quote

class coil_class:
    longname = ''
    prereq = ''
    reference = ''
    info = ''
    restricted = False

    def update(self,longname,prereq,reference,info,restricted):
        self.longname = longname
        self.prereq = prereq
        self.reference = reference
        self.info = info
        self.restricted = restricted

def sheet(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('coil_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'coils/error.html', {'message': 'No matching coils: '+object_id})
    if len(stats) > 1:
        return render(request, 'coils/error.html', {'message': 'Too many matching coils'})
    coil = coil_class()
    longname = stats[0].db.longname
    prereq = stats[0].db.prereq
    reference = stats[0].db.reference
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    restricted = stats[0].db.restricted
    coil.update(longname,prereq,reference,info,restricted)
    return render(request, 'coils/sheet.html', {'coil': coil, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('coil_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'coils/error.html', {'message': 'No matching coil'})
    if len(stats) > 1:
        return render(request, 'coils/error.html', {'message': 'Too many matching coils'})
    coil = stats[0]
    starting_data = {'longname':coil.db.longname,
                     'reference':coil.db.reference,
                     'prereq':coil.db.prereq,
                     'info':coil.db.info,
                     'restricted':coil.db.restricted,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'coils/editor.html', {'form': form, 'coil_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('coil_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'coils/error.html', {'message': len(data) + ' No matching coils: ' + n})
                if len(stats) > 1:
                    return render(request, 'coils/error.html', {'message': 'Too many matching coils'})
                coil = stats[0]
                app = coil.update(longname=form.cleaned_data['longname'],
                                        prereq=form.cleaned_data['prereq'],
                                        reference=form.cleaned_data['reference'],
                                        info=form.cleaned_data['info'],
                                        restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/coils/view/'+quote(n))
            else:
                return render(request, 'coils/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'coils/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'coils/error.html', {'message': 'Not staff'})

def create(request):

    starting_data = {'longname':'',
                     'prereq' :'',
                     'reference':'',
                     'info':'',
                     'restricted':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'coils/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                s = create_script('typeclasses.scripts.CoilScript',
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.prereq=form.cleaned_data['prereq']
                s.db.reference=form.cleaned_data['reference']
                s.db.info=form.cleaned_data['info']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/coils/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'coils/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'coils/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'coils/error.html', {'message': 'Not staff'})

def list(request):
    data = search_script_tag('coil_stat')
    coils = []
    for stat in data:
        coils.append(stat.db.longname)
    coils.sort()
    return render(request, 'coils/list.html', {'coils':coils })
