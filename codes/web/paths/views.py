# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render

from evennia.utils.search import search_script_tag
from evennia import create_script

from codes.web.paths.forms import editForm

from django.http import HttpResponseRedirect

from urllib.parse import unquote
from urllib.parse import quote

class path_class:
    longname = ''
    ruling_arcana = []
    inferior_arcana = ''
    info = ''
    reference = ''
    restricted = False
    
    def update(self,longname,ruling_arcana,inferior_arcana,info,reference,restricted):
        self.longname = longname
        self.ruling_arcana = ruling_arcana
        self.inferior_arcana = inferior_arcana
        self.info = info
        self.reference = reference
        self.restricted = restricted
    
def sheet(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('path_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'paths/error.html', {'message': 'No matching path: '+object_id})
    if len(stats) > 1:
        return render(request, 'paths/error.html', {'message': 'Too many matching paths'})
    path = path_class()
    longname = stats[0].db.longname
    ruling_arcana = stats[0].db.ruling_arcana
    inferior_arcana = stats[0].db.inferior_arcana
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    reference = stats[0].db.reference
    restricted = stats[0].db.restricted
    path.update(longname,ruling_arcana,inferior_arcana,info,reference,restricted)
    return render(request, 'paths/sheet.html', {'path': path, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):
    
    object_id = unquote(object_id)

    try:
        data = search_script_tag('path_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    
    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'paths/error.html', {'message': 'No matching path'})
    if len(stats) > 1:
        return render(request, 'paths/error.html', {'message': 'Too many matching paths'})
    stat = stats[0]
    starting_data = {'longname':stat.db.longname,
                     'ruling_arcana': stat.db.ruling_arcana,
                     'inferior_arcana' : stat.db.inferior_arcana,
                     'info': stat.db.info,
                     'reference':stat.db.reference,
                     'restricted':stat.db.restricted,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'paths/editor.html', {'form': form, 'path_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('path_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'paths/error.html', {'message': len(data) + ' No matching paths: ' + n})
                if len(stats) > 1:
                    return render(request, 'paths/error.html', {'message': 'Too many matching paths'})
                path = stats[0]
                ruling_arcana = []
                if form.cleaned_data['ruling_arcana'] != '[]':
                    for item in form.cleaned_data['ruling_arcana'][1:-1].split(','):
                        ruling_arcana.append(item.strip()[1:-1])
                path = path.update(
                    longname=form.cleaned_data['longname'],
                    ruling_arcana = ruling_arcana,
                    inferior_arcana = form.cleaned_data['inferior_arcana'],
                    info=form.cleaned_data['info'],
                    reference=form.cleaned_data['reference'],
                    restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/paths/view/'+quote(n))
            else:
                return render(request, 'paths/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'paths/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'paths/error.html', {'message': 'Not staff'})
    
def create(request):
    
    starting_data = {'longname':'',
                     'ruling_arcana':[],
                     'inferior_arcana':'',
                     'info': '',
                     'reference':'',
                     'restricted':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'paths/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                ruling_arcana = []
                if form.cleaned_data['ruling_arcana'] != '[]':
                    for item in form.cleaned_data['ruling_arcana'][1:-1].split(','):
                        ruling_arcana.append(item.strip()[1:-1])
                s = create_script('typeclasses.scripts.pathScript',
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.ruling_arcana = ruling_arcana
                s.db.inferior_arcana = form.cleaned_data['inferior_arcana']
                s.db.info = form.cleaned_data['info']
                s.db.reference=form.cleaned_data['reference']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/paths/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'paths/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'paths/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'paths/error.html', {'message': 'Not staff'})
    
def list(request):
    data = search_script_tag('path_stat')
    paths = []
    for stat in data:
        paths.append(stat.db.longname)
    paths.sort()
    return render(request, 'paths/list.html', {'paths':paths })
