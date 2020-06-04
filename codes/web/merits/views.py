# Views for our character app

from django.shortcuts import render

from evennia.utils.search import search_script_tag
from evennia import create_script

from codes.web.merits.forms import EditForm
from codes import data

from django.http import HttpResponseRedirect

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

class merit_class:
    longname = ''
    category = ''
    range = []
    noteRestrictions = []
    prereq = ''
    reference = ''
    info = ''
    cg_only = False
    restricted = False

    def update(self,longname,category,meritrange,noterestrictions,prereq,reference,info,cg_only,restricted):
        self.longname = longname
        self.category = category
        self.range = meritrange
        self.noteRestrictions = noterestrictions
        self.prereq = prereq
        self.reference = reference
        self.info = info
        self.cg_only = cg_only
        self.restricted = restricted

def sheet(request, object_id):

    object_id = unquote(object_id)
    stats = data.find(object_id,statclass='Merit')
    if len(stats) == 0:
        return render(request, 'merits/error.html', {'message': 'No matching merits: '+object_id})
    if len(stats) > 1:
        return render(request, 'merits/error.html', {'message': 'Too many matching merits'})
    merit = merit_class()
    longname = stats[0].db.longname
    category = stats[0].db.category
    meritrange = stats[0].db.range
    noterestrictions = stats[0].db.noteRestrictions
    prereq = stats[0].db.prereq
    reference = stats[0].db.reference
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    cg_only = stats[0].db.cg_only
    restricted = stats[0].db.restricted
    merit.update(longname,category,meritrange,noterestrictions,prereq,reference,info,cg_only,restricted)
    if request.method == 'POST':
         return render(request, 'merits/error.html', {'message': 'POST'})
    return render(request, 'merits/sheet.html', {'merit': merit, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):

    object_id = unquote(object_id)
    stats = data.find(object_id,statclass='Merit')
    if len(stats) == 0:
        return render(request, 'merits/error.html', {'message': 'No matching merits'})
    if len(stats) > 1:
        return render(request, 'merits/error.html', {'message': 'Too many matching merits'})
    merit = stats[0]
    if len(merit.db.noteRestrictions) == 0:
        noteRestrictions='[]'
    else:
        noteRestrictions = merit.db.noteRestrictions
    starting_data = {'longname':merit.db.longname,
                     'category':merit.db.category,
                     'range':merit.db.range,
                     'noteRestrictions':noteRestrictions,
                     'prereq':merit.db.prereq,
                     'reference':merit.db.reference,
                     'info':merit.db.info,
                     'cg_only':merit.db.cg_only,
                     'restricted':merit.db.restricted,
                     'link':object_id}
    form = EditForm(initial = starting_data)
    return render(request, 'merits/editor.html', {'form': form, 'merit_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = EditForm(request.POST)
            if form.is_valid():
                n = form.cleaned_data['link']
                stats = data.find(n,statclass='Merit')
                if len(stats) == 0:
                    return render(request, 'merits/error.html', {'message': len(data) + ' No matching merits: ' + n})
                if len(stats) > 1:
                    return render(request, 'merits/error.html', {'message': 'Too many matching merits'})
                merit = stats[0]
                range = []
                for item in form.cleaned_data['range'][1:-1].split(','):
                        range.append(int(item))
                noteRestrictions = []
                if form.cleaned_data['noteRestrictions'] != '[]':
                    for item in form.cleaned_data['noteRestrictions'][1:-1].split(','):
                        noteRestrictions.append(item.strip()[1:-1])
                app = merit.update(longname=form.cleaned_data['longname'],
                                   category=form.cleaned_data['category'],
                                   range=range,
                                   noteRestrictions=noteRestrictions,
                                   prereq=form.cleaned_data['prereq'],
                                   reference=form.cleaned_data['reference'],
                                   info=form.cleaned_data['info'],
                                   cg_only=form.cleaned_data['cg_only'],
                                   restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/merits/view/'+quote(n))
            else:
                return render(request, 'merits/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'merits/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'merits/error.html', {'message': 'Not staff'})

def create(request):

    starting_data = {'longname':'',
                     'category':'',
                     'range':'',
                     'noteRestrictions':'',
                     'prereq':'',
                     'reference':'',
                     'info':'',
                     'cg_only':False,
                     'restricted':False,
                     'link':''}
    form = EditForm(initial = starting_data)
    return render(request, 'merits/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = EditForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                range = []
                for item in form.cleaned_data['range'][1:-1].split(','):
                        range.append(int(item))
                noteRestrictions = []
                if form.cleaned_data['noteRestrictions'] != '[]':
                    for item in form.cleaned_data['noteRestrictions'][1:-1].split(','):
                        noteRestrictions.append(item.strip()[1:-1])
                s = create_script('typeclasses.scripts.MeritScript',
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.category=form.cleaned_data['category']
                d = search_script_tag('dictionary_data')[0]
                d.insert(s)
                s.db.range=range
                s.db.noteRestrictions= noteRestrictions
                s.db.prereq=form.cleaned_data['prereq']
                s.db.reference=form.cleaned_data['reference']
                s.db.info=form.cleaned_data['info']
                s.db.cg_only=form.cleaned_data['cg_only']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/merits/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'merits/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'merits/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'merits/error.html', {'message': 'Not staff'})

def list(request):
    data = search_script_tag('merit_stat')
    groups = []
    for stat in data:
        if stat.db.category.capitalize() not in groups:
            groups.append(stat.db.category.capitalize())
    groups.sort()
    merits = []
    for group in groups:
        temp_list = []
        for stat in data:
            if stat.db.category.capitalize() == group:
                temp_list.append(stat.db.longname)
        temp_list.sort()
        merits.append([group] + temp_list)
    return render(request, 'merits/list.html', {'merits':merits })
