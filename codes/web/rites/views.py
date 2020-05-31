from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render

from evennia.utils.search import search_script_tag
from evennia import create_script

from codes.web.rites.forms import EditForm

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

class rite_class:
    longname = ''
    rite_type = ''
    rank = 0
    prereq = ''
    info = ''
    reference = ''
    restricted = False

    def update(self,longname,rite_type,rank,prereq,info,reference,restricted):
        self.longname = longname
        self.rite_type = rite_type
        self.rank = rank
        self.prereq = prereq
        self.info = info
        self.reference = reference
        self.restricted = restricted

def sheet(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('werewolf_rite_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'rites/error.html', {'message': 'No matching rites: '+object_id})
    if len(stats) > 1:
        return render(request, 'rites/error.html', {'message': 'Too many matching rites'})
    rite = rite_class()
    longname = stats[0].db.longname
    rite_type = stats[0].db.type
    rank = stats[0].db.rank
    prereq = stats[0].db.prereq
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    reference = stats[0].db.reference
    restricted = stats[0].db.restricted
    rite.update(longname,rite_type,rank,prereq,info,reference,restricted)
    if request.method == 'POST':
         return render(request, 'rites/error.html', {'message': 'POST'})
    return render(request, 'rites/sheet.html', {'rite': rite, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('werewolf_rite_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'rites/error.html', {'message': 'No matching rites'})
    if len(stats) > 1:
        return render(request, 'rites/error.html', {'message': 'Too many matching rites'})
    rite = stats[0]
    starting_data = {'longname':rite.db.longname,
                     'type':rite.db.type,
                     'rank':rite.db.rank,
                     'prereq':rite.db.prereq,
                     'info':rite.db.info,
                     'reference':rite.db.reference,
                     'restricted':rite.db.restricted,
                     'link':object_id}
    form = EditForm(initial = starting_data)
    return render(request, 'rites/editor.html', {'form': form, 'rite_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = EditForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('werewolf_rite_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'rites/error.html', {'message': len(data) + ' No matching rites: ' + n})
                if len(stats) > 1:
                    return render(request, 'rites/error.html', {'message': 'Too many matching rites'})
                rite = stats[0]
                app = rite.update(longname=form.cleaned_data['longname'],
                                  type=form.cleaned_data['type'],
                                  rank=int(form.cleaned_data['rank']),
                                  prereq=form.cleaned_data['prereq'],
                                  info=form.cleaned_data['info'],
                                  reference=form.cleaned_data['reference'],
                                  restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/rites/view/'+quote(n))
            else:
                return render(request, 'rites/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'rites/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'rites/error.html', {'message': 'Not staff'})

def create(request):

    starting_data = {'longname':'',
                     'type':'',
                     'rank':0,
                     'prereq':'',
                     'info':'',
                     'reference':'',
                     'restricted':False,
                     'link':''}
    form = EditForm(initial = starting_data)
    return render(request, 'rites/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = EditForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                s = create_script('typeclasses.scripts.WerewolfRiteScript',
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.type=form.cleaned_data['type']
                s.db.rank=int(form.cleaned_data['rank'])
                s.db.prereq=form.cleaned_data['prereq']
                s.db.info=form.cleaned_data['info']
                s.db.reference=form.cleaned_data['reference']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/rites/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'rites/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'rites/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'rites/error.html', {'message': 'Not staff'})

def list(request):
    data = search_script_tag('werewolf_rite_stat')
    rites = []
    for stat in data:
        rites.append(stat.db.longname)
    rites.sort()
    return render(request, 'rites/list.html', {'rites':rites })
