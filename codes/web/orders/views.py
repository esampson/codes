# Views for our character app

from django.http import HttpResponseNotFound
from django.http import Http404
from django.shortcuts import render

from evennia.utils.search import search_script_tag
from evennia import create_script

from codes.web.orders.forms import editForm

from django.http import HttpResponseRedirect

from urllib.parse import unquote
from urllib.parse import quote

class order_class:
    longname = ''
    rote_skills = []
    info = ''
    reference = ''
    restricted = False

    def update(self,longname,rote_skills,info,reference,restricted):
        self.longname = longname
        self.rote_skills = rote_skills
        self.info = info
        self.reference = reference
        self.restricted = restricted

def sheet(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('order_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'orders/error.html', {'message': 'No matching order: '+object_id})
    if len(stats) > 1:
        return render(request, 'orders/error.html', {'message': 'Too many matching orders'})
    order = order_class()
    longname = stats[0].db.longname
    rote_skills = stats[0].db.rote_skills
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/','\n')
    else:
        info = chr(160)
    reference = stats[0].db.reference
    restricted = stats[0].db.restricted
    order.update(longname,rote_skills,info,reference,restricted)
    return render(request, 'orders/sheet.html', {'order': order, 'request':request, 'id':quote(object_id)})

def editor(request, object_id):

    object_id = unquote(object_id)

    try:
        data = search_script_tag('order_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'orders/error.html', {'message': 'No matching order'})
    if len(stats) > 1:
        return render(request, 'orders/error.html', {'message': 'Too many matching orders'})
    stat = stats[0]
    starting_data = {'longname':stat.db.longname,
                     'rote_skills': stat.db.rote_skills,
                     'info': stat.db.info,
                     'reference':stat.db.reference,
                     'restricted':stat.db.restricted,
                     'link':object_id}
    form = editForm(initial = starting_data)
    return render(request, 'orders/editor.html', {'form': form, 'order_id':object_id })

def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('order_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'orders/error.html', {'message': len(data) + ' No matching orders: ' + n})
                if len(stats) > 1:
                    return render(request, 'orders/error.html', {'message': 'Too many matching orders'})
                order = stats[0]
                rote_skills = []
                if form.cleaned_data['rote_skills'] != '[]':
                    for item in form.cleaned_data['rote_skills'][1:-1].split(','):
                        rote_skills.append(item.strip()[1:-1])
                order = order.update(
                    longname=form.cleaned_data['longname'],
                    rote_skills = rote_skills,
                    info=form.cleaned_data['info'],
                    reference=form.cleaned_data['reference'],
                    restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/orders/view/'+quote(n))
            else:
                return render(request, 'orders/error.html', {'message': 'Invalid form'})
        else:
            return render(request, 'orders/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'orders/error.html', {'message': 'Not staff'})

def create(request):

    starting_data = {'longname':'',
                     'rote_skills':[],
                     'info': '',
                     'reference':'',
                     'restricted':False,
                     'link':''}
    form = editForm(initial = starting_data)
    return render(request, 'orders/create.html', {'form': form})

def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'','').replace(' ','_')
                rote_skills = []
                if form.cleaned_data['rote_skills'] != '[]':
                    for item in form.cleaned_data['rote_skills'][1:-1].split(','):
                        rote_skills.append(item.strip()[1:-1])
                s = create_script('typeclasses.scripts.OrderScript',
                                   key=name)
                s.db.longname=form.cleaned_data['longname']
                s.db.rote_skills = rote_skills
                s.db.info = form.cleaned_data['info']
                s.db.reference=form.cleaned_data['reference']
                s.db.restricted=form.cleaned_data['restricted']
                return HttpResponseRedirect('/orders/view/'+quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'orders/error.html', {'message': 'Invalid form\n'+M})
        else:
            return render(request, 'orders/error.html', {'message': 'Not POST'})
    else:
         return render(request, 'orders/error.html', {'message': 'Not staff'})

def list(request):
    data = search_script_tag('order_stat')
    orders = []
    for stat in data:
        orders.append(stat.db.longname)
    orders.sort()
    return render(request, 'orders/list.html', {'orders':orders })
