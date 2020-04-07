# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_script_tag
from evennia.utils.utils import inherits_from
from evennia import create_script

from codes.web.contracts.forms import editForm
from django.http import HttpResponseRedirect
from datetime import datetime
from evennia.objects.models import ObjectDB
from django.conf import settings
from evennia.utils import create
from urllib.parse import unquote
from urllib.parse import quote

class contract_class:
    longname = ''
    group = ''
    category = ''
    subgroup = ''
    reference = ''
    info = ''
    restricted = False
    
    def update(self,longname,group,category,subgroup,reference,info,restricted):
        self.longname = longname
        self.group = group
        self.category = category
        self.subgroup = subgroup
        self.reference = reference
        self.info = info
        self.restricted = restricted
    
def sheet(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('contract_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'contracts/error.html', {'message': 'No matching contracts: '+object_id})
    if len(stats) > 1:
        return render(request, 'contracts/error.html', {'message': 'Too many matching contracts'})
    contract = contract_class()
    longname = stats[0].db.longname
    group = stats[0].db.group
    category = stats[0].db.category
    subgroup = stats[0].db.subgroup
    reference = stats[0].db.reference
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    restricted = stats[0].db.restricted
    contract.update(longname,group,category,subgroup,reference,info,restricted)
    return render(request, 'contracts/sheet.html', {'contract': contract, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('contract_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'contracts/error.html', {'message': 'No matching contract'})
    if len(stats) > 1:
        return render(request, 'contracts/error.html', {'message': 'Too many matching contracts'})
    contract = stats[0]
    starting_data = {'longname':contract.db.longname,
                     'group':contract.db.group, 
                     'category':contract.db.category,
                     'subgroup':contract.db.subgroup,
                     'reference':contract.db.reference,
                     'info':contract.db.info,
                     'restricted':contract.db.restricted,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'contracts/editor.html', {'form': form, 'contract_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('contract_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'contracts/error.html', {'message': len(data) + ' No matching contracts: ' + n})
                if len(stats) > 1:
                    return render(request, 'contracts/error.html', {'message': 'Too many matching contracts'})
                contract = stats[0]
                app = contract.update(longname=form.cleaned_data['longname'],
                                      group=form.cleaned_data['group'],
                                      category=form.cleaned_data['category'],
                                      subgroup=form.cleaned_data['subgroup'],
                                      reference=form.cleaned_data['reference'],
                                      info=form.cleaned_data['info'],
                                      restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/contracts/view/'+quote(n))
            else:
                return render(request, 'contracts/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'contracts/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'contracts/error.html', {'message': 'Not staff'})
    
def create(request):
    
    starting_data = {'longname':'', 
                     'group':'',
                     'category':'',
                     'subgroup':'', 
                     'reference':'',
                     'info':'',
                     'restricted':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'contracts/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].longname.replace('\'','').replace(' ','_')
                s = create_script('typeclasses.scripts.contractScript', 
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.group=form.cleaned_data['group']
                s.db.category=form.cleaned_data['category']
                s.db.subgroup=form.cleaned_data['subgroup']
                s.db.reference=form.cleaned_data['reference']
                s.db.info=form.cleaned_data['info']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/contracts/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'contracts/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'contracts/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'contracts/error.html', {'message': 'Not staff'})
    
def list(request):
    data = search_script_tag('contract_stat')
    groups = []
    for stat in data:
        if stat.db.category.capitalize() not in groups:
            groups.append(stat.db.category.capitalize())
    groups.sort()
    contracts = []
    for group in groups:
        temp_list = []
        for stat in data:
            if stat.db.category.capitalize() == group:
                temp_list.append(stat.db.longname)
        temp_list.sort()
        contracts.append([group] + temp_list)
    return render(request, 'contracts/list.html', {'contracts':contracts })
