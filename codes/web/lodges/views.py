
from django.http import Http404
from django.shortcuts import render

from evennia.utils.search import search_script_tag
from evennia import create_script

from codes.web.lodges.forms import EditForm

from django.http import HttpResponseRedirect

from urllib.parse import unquote
from urllib.parse import quote

class lodge_class:
    longname = ''
    info = ''
    reference = ''
    restricted = False

    def update(self,longname,info,reference,restricted):
        self.longname = longname
        self.info = info
        self.reference = reference
        self.restricted = restricted

def sheet(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('lodge_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'lodges/error.html', {'message': 'No matching lodge: '+object_id})
    if len(stats) > 1:
        return render(request, 'lodges/error.html', {'message': 'Too many matching lodges'})
    lodge = lodge_class()
    longname = stats[0].db.longname
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    reference = stats[0].db.reference
    restricted = stats[0].db.restricted
    lodge.update(longname,info,reference,restricted)
    return render(request, 'lodges/sheet.html', {'lodge': lodge, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('lodge_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'lodges/error.html', {'message': 'No matching lodge'})
    if len(stats) > 1:
        return render(request, 'lodges/error.html', {'message': 'Too many matching lodges'})
    stat = stats[0]
    starting_data = {'longname':stat.db.longname,
                     'info': stat.db.info,
                     'reference':stat.db.reference,
                     'restricted':stat.db.restricted,
                     'link':object_id}
    form = EditForm(initial = starting_data)
    return render(request, 'lodges/editor.html', {'form': form, 'lodge_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = EditForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('lodge_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'lodges/error.html', {'message': len(data) + ' No matching lodges: ' + n})
                if len(stats) > 1:
                    return render(request, 'lodges/error.html', {'message': 'Too many matching lodges'})
                lodge = stats[0]
                lodge = lodge.update(
                    longname=form.cleaned_data['longname'],
                    info=form.cleaned_data['info'],
                    reference=form.cleaned_data['reference'],
                    restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/lodges/view/'+quote(n))
            else:
                return render(request, 'lodges/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'lodges/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'lodges/error.html', {'message': 'Not staff'})

def create(request):

    starting_data = {'longname':'',
                     'info': '',
                     'reference':'',
                     'restricted':False,
                     'link':''}
    form = EditForm(initial = starting_data)
    return render(request, 'lodges/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = EditForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                s = create_script('typeclasses.scripts.lodgeScript',
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.info = form.cleaned_data['info']
                s.db.reference=form.cleaned_data['reference']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/lodges/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'lodges/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'lodges/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'lodges/error.html', {'message': 'Not staff'})

def list(request):
    data = search_script_tag('lodge_stat')
    lodges = []
    for stat in data:
        lodges.append(stat.db.longname)
    lodges.sort()
    return render(request, 'lodges/list.html', {'lodges':lodges })
