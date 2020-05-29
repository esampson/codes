from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render

from evennia.utils.search import search_script_tag
from evennia import create_script

from codes.web.gifts.forms import editForm

from urllib.parse import unquote
from urllib.parse import quote


class gift_class:
    longname = ''
    category = ''
    group = ''
    rank = ''
    renown = ''
    info = ''
    reference = ''
    restricted = False

    def update(self, longname, category, group, rank, renown, info, reference,
               restricted):
        self.longname = longname
        self.category = category
        self.group = group
        self.rank = rank
        self.renown = renown
        self.info = info
        self.reference = reference
        self.restricted = restricted


def sheet(request, object_id):
    object_id = unquote(object_id)

    try:
        data = search_script_tag('gift_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'gifts/error.html',
                      {'message': 'No matching gifts: ' + object_id})
    if len(stats) > 1:
        return render(request, 'gifts/error.html',
                      {'message': 'Too many matching gifts'})
    gift = gift_class()
    longname = stats[0].db.longname
    category = stats[0].db.category
    group = stats[0].db.group
    rank = stats[0].db.rank
    renown = stats[0].db.renown
    if stats[0].db.info:
        info = stats[0].db.info.replace('|/', '\n')
    else:
        info = chr(160)
    reference = stats[0].db.reference
    restricted = stats[0].db.restricted
    gift.update(longname, category, group, rank, renown, info, reference,
                restricted)
    return render(request, 'gifts/sheet.html',
                  {'gift': gift, 'request': request, 'id': quote(object_id)})


def editor(request, object_id):
    object_id = unquote(object_id)

    try:
        data = search_script_tag('gift_stat')
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")

    stats = []
    for stat in data:
        if stat.db.longname[0:len(object_id)].lower() == object_id.lower():
            stats.append(stat)
    if len(stats) == 0:
        return render(request, 'gifts/error.html',
                      {'message': 'No matching gift'})
    if len(stats) > 1:
        return render(request, 'gifts/error.html',
                      {'message': 'Too many matching gifts'})
    gift = stats[0]
    starting_data = {'longname': gift.db.longname,
                     'category': gift.db.category,
                     'group': gift.db.group,
                     'rank': gift.db.rank,
                     'renown': gift.db.renown,
                     'info': gift.db.info,
                     'reference': gift.db.reference,
                     'restricted': gift.db.restricted,
                     'link': object_id}
    form = editForm(initial=starting_data)
    return render(request, 'gifts/editor.html',
                  {'form': form, 'gift_id': object_id})


def editted(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                try:
                    data = search_script_tag('gift_stat')
                except IndexError:
                    raise Http404("I couldn't find a character with that ID.")
                stats = []
                n = form.cleaned_data['link']
                for stat in data:
                    if stat.db.longname[0:len(n)].lower() == n.lower():
                        stats.append(stat)
                if len(stats) == 0:
                    return render(request, 'gifts/error.html',
                                  {'message': len(data) +
                                              ' No matching gifts: ' + n})
                if len(stats) > 1:
                    return render(request, 'gifts/error.html',
                                  {'message': 'Too many matching gifts'})
                gift = stats[0]
                app = gift.update(longname=form.cleaned_data['longname'],
                                  category=form.cleaned_data['category'],
                                  group=form.cleaned_data['group'],
                                  rank=form.cleaned_data['rank'],
                                  renown=form.cleaned_data['renown'],
                                  info=form.cleaned_data['info'],
                                  reference=form.cleaned_data['reference'],
                                  restricted=form.cleaned_data['restricted'])
                return HttpResponseRedirect('/gifts/view/' + quote(n))
            else:
                return render(request, 'gifts/error.html',
                              {'message': 'Invalid form'})
        else:
            return render(request, 'gifts/error.html',
                          {'message': 'Not POST'})
    else:
        return render(request, 'gifts/error.html',
                      {'message': 'Not staff'})


def create(request):
    starting_data = {'longname': '',
                     'category': '',
                     'group': '',
                     'rank': '',
                     'renown': '',
                     'info': '',
                     'reference': '',
                     'restricted': False,
                     'link': ''}
    form = editForm(initial=starting_data)
    return render(request, 'gifts/create.html', {'form': form})


def created(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = editForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['longname'].replace('\'', '').replace(' ', '_')
                s = create_script('typeclasses.scripts.GiftScript',
                                  key=name)
                s.db.longname = form.cleaned_data['longname']
                s.db.category = form.cleaned_data['category']
                s.db.group = form.cleaned_data['group']
                s.db.rank = form.cleaned_data['rank']
                s.db.renown = form.cleaned_data['renown']
                s.db.info = form.cleaned_data['info']
                s.db.reference = form.cleaned_data['reference']
                s.db.restricted = form.cleaned_data['restricted']
                return HttpResponseRedirect('/gifts/view/' + quote(s.db.longname))
            else:
                M = str(form)
                return render(request, 'gifts/error.html',
                              {'message': 'Invalid form\n' + M})
        else:
            return render(request, 'gifts/error.html', {'message': 'Not POST'})
    else:
        return render(request, 'gifts/error.html', {'message': 'Not staff'})


def list(request):
    data = search_script_tag('gift_stat')
    groups = []
    for stat in data:
        if stat.db.group.capitalize() not in groups:
            groups.append(stat.db.group.capitalize())
    groups.sort()
    gifts = []
    for group in groups:
        temp_list = []
        for stat in data:
            if stat.db.group.capitalize() == group:
                temp_list.append(stat.db.longname)
        temp_list.sort()
        gifts.append([group] + temp_list)
    return render(request, 'gifts/list.html', {'gifts': gifts})
