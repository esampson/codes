# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render

from evennia.utils.search import search_script_tag
from evennia import create_script

from codes.web.tribes.forms import EditForm

from django.http import HttpResponseRedirect

from urllib.parse import unquote
from urllib.parse import quote

class tribe_class:
    longname = ''
    renown = ''
    tribe_gifts = []
    info = ''
    reference = ''
    restricted = False

    def update(self,longname,renown,tribe_gifts,info,reference,restricted):
        self.longname = longname
        self.renown = renown
        self.tribe_gifts = tribe_gifts
        self.info = info
        self.reference = reference
        self.restricted = restricted

def sheet(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('tribe_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'tribes/error.html', {'message': 'No matching tribe: '+object_id})
    if len(stats) > 1:
        return render(request, 'tribes/error.html', {'message': 'Too many matching tribes'})
    tribe = tribe_class()
    longname = stats[0].db.longname
    renown= stats[0].db.renown
    tribe_gifts = stats[0].db.tribe_gifts
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    reference = stats[0].db.reference
    restricted = stats[0].db.restricted
    tribe.update(longname,renown,tribe_gifts,info,reference,restricted)
    return render(request, 'tribes/sheet.html', {'tribe': tribe, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('tribe_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'tribes/error.html', {'message': 'No matching tribe'})
    if len(stats) > 1:
        return render(request, 'tribes/error.html', {'message': 'Too many matching tribes'})
    stat = stats[0]
    starting_data = {'longname':stat.db.longname,
                     'renown': stat.db.renown,
                     'tribe_gifts' : stat.db.tribe_gifts,
                     'info': stat.db.info,
                     'reference':stat.db.reference,
                     'restricted':stat.db.restricted,
                     'link':object_id}
    form = EditForm(initial = starting_data)
    return render(request, 'tribes/editor.html', {'form': form, 'tribe_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = EditForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('tribe_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'tribes/error.html', {'message': len(data) + ' No matching tribes: ' + n})
                if len(stats) > 1:
                    return render(request, 'tribes/error.html', {'message': 'Too many matching tribes'})
                tribe = stats[0]
                tribe_gifts = []
                if form.cleaned_data['tribe_gifts'] != '[]':
                    for item in form.cleaned_data['tribe_gifts'][1:-1].split(','):
                        tribe_gifts.append(item.strip()[1:-1])
                tribe = tribe.update(
                    longname=form.cleaned_data['longname'],
                    renown = form.cleaned_data['renown'],
                    tribe_gifts = form.cleaned_data['tribe_gifts'],
                    info=form.cleaned_data['info'],
                    reference=form.cleaned_data['reference'],
                    restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/tribes/view/'+quote(n))
            else:
                return render(request, 'tribes/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'tribes/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'tribes/error.html', {'message': 'Not staff'})

def create(request):

    starting_data = {'longname':'',
                     'renown':'',
                     'tribe_gifts':[],
                     'info': '',
                     'reference':'',
                     'restricted':False,
                     'link':''}
    form = EditForm(initial = starting_data)
    return render(request, 'tribes/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = EditForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                tribe_gifts = []
                if form.cleaned_data['tribe_gifts'] != '[]':
                    for item in form.cleaned_data['tribe_gifts'][1:-1].split(','):
                        tribe_gifts.append(item.strip()[1:-1])
                s = create_script('typeclasses.scripts.TribeScript',
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.renown = form.cleaned_data['renown']
                s.db.tribe_gifts = tribe_gifts
                s.db.info = form.cleaned_data['info']
                s.db.reference=form.cleaned_data['reference']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/tribes/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'tribes/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'tribes/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'tribes/error.html', {'message': 'Not staff'})

def list(request):
    data = search_script_tag('tribe_stat')
    tribes = []
    for stat in data:
        tribes.append(stat.db.longname)
    tribes.sort()
    return render(request, 'tribes/list.html', {'tribes':tribes })
