# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_script_tag
from evennia.utils.utils import inherits_from
from evennia import create_script

from codes.web.seemings.forms import editForm
from django.http import HttpResponseRedirect
from datetime import datetime
from evennia.objects.models import ObjectDB
from django.conf import settings
from evennia.utils import create
from urllib.parse import unquote
from urllib.parse import quote

class seeming_class:
    longname = ''
    bonus_attributes = []
    regalia = ''
    reference = ''
    info = ''
    restricted = False
    
    def update(self,longname,bonus_attributes,regalia,reference,info,restricted):
        self.longname = longname
        self.bonus_attributes = bonus_attributes
        self.regalia = regalia
        self.reference = reference
        self.info = info
        self.restricted = restricted
    
def sheet(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('seeming_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'seemings/error.html', {'message': 'No matching seeming: '+object_id})
    if len(stats) > 1:
        return render(request, 'seemings/error.html', {'message': 'Too many matching seemings'})
    seeming = seeming_class()
    longname = stats[0].db.longname
    bonus_attributes = stats[0].db.bonus_attributes
    regalia = stats[0].db.regalia
    reference = stats[0].db.reference
    info = stats[0].db.info.replace('|/','\n')
    restricted = stats[0].db.restricted
    seeming.update(longname,bonus_attributes,regalia,reference,info,restricted)
    return render(request, 'seemings/sheet.html', {'seeming': seeming, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('seeming_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'seemings/error.html', {'message': 'No matching seeming'})
    if len(stats) > 1:
        return render(request, 'seemings/error.html', {'message': 'Too many matching seemings'})
    stat = stats[0]
    starting_data = {'longname':stat.db.longname, 
                     'bonus_attributes':stat.db.bonus_attributes,
                     'regalia': stat.db.regalia,
                     'reference':stat.db.reference,
                     'info':stat.db.info,
                     'restricted':stat.db.restricted,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'seemings/editor.html', {'form': form, 'seeming_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('seeming_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'seemings/error.html', {'message': len(data) + ' No matching seemings: ' + n})
                if len(stats) > 1:
                    return render(request, 'seemings/error.html', {'message': 'Too many matching seemings'})
                seeming = stats[0]
                bonus_attributes = []
                if form.cleaned_data['bonus_attributes'] != '[]':
                    for item in form.cleaned_data['bonus_attributes'][1:-1].split(','):
                        bonus_attributes.append(item.strip()[1:-1])
                app = seeming.update(longname=form.cleaned_data['longname'],
                                   bonus_attributes=bonus_attributes,
                                   regalia = form.cleaned_data['regalia'],
                                   reference=form.cleaned_data['reference'],
                                   info=form.cleaned_data['info'],
                                   restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/seemings/view/'+quote(n))
            else:
                return render(request, 'seemings/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'seemings/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'seemings/error.html', {'message': 'Not staff'})
    
def create(request):
    
    starting_data = {'longname':'', 
                     'bonus_attributes':[], 
                     'reference':'',
                     'regalia' : '',
                     'info':'',
                     'restricted':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'seemings/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                bonus_attributes = []
                if form.cleaned_data['bonus_attributes'] != '[]':
                    for item in form.cleaned_data['bonus_attributes'][1:-1].split(','):
                        bonus_attributes.append(item.strip()[1:-1])
                s = create_script('typeclasses.scripts.seemingScript', 
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.bonus_attributes=bonus_attributes
                s.db.regalia = form.cleaned_data['regalia']
                s.db.reference=form.cleaned_data['reference']
                s.db.info=form.cleaned_data['info']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/seemings/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'seemings/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'seemings/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'seemings/error.html', {'message': 'Not staff'})
    
def list(request):
    data = search_script_tag('seeming_stat')
    groups = []
    seemings = []
    for stat in data:
        seemings.append(stat.db.longname)
    seemings.sort()
    return render(request, 'seemings/list.html', {'seemings':seemings })
