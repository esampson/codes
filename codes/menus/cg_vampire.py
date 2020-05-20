from codes.data import get
from codes.data import set
from codes.data import find
from evennia.utils.utils import strip_control_sequences
from evennia.utils.search import search_script_tag
from operator import itemgetter

from codes.menus.menu_types import ExMenu

import time

anchors = { 'mask' : ['Authoritarian', 'Child', 'Competitor', 'Conformist',
                      'Conspirator', 'Courtesan', 'Cult Leader', 'Deviant',
                      'Follower', 'Guru', 'Idealist', 'Jester', 'Junkie',
                      'Martyr', 'Masochist', 'Monster', 'Nomad', 'Nurturer',
                      'Perfectionist', 'Penitent', 'Questioner', 'Rebel',
                      'Scholar', 'Social Chameleon', 'Spy', 'Survivor',
                      'Visionary'],
            'dirge' : ['Authoritarian', 'Child', 'Competitor', 'Conformist',
                      'Conspirator', 'Courtesan', 'Cult Leader', 'Deviant',
                      'Follower', 'Guru', 'Idealist', 'Jester', 'Junkie',
                      'Martyr', 'Masochist', 'Monster', 'Nomad', 'Nurturer',
                      'Perfectionist', 'Penitent', 'Questioner', 'Rebel',
                      'Scholar', 'Social Chameleon', 'Spy', 'Survivor',
                      'Visionary'] }

def vampire_template(caller, raw_string, **kwargs):
    caller.db.cg['start_menu'] = 'cg_vampire'
    caller.db.cg['start_node'] = 'vampire_template'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    caller.db.basics = { 'Sphere' : 'Vampire' }
    caller.db.sphere = { 'Banes' : [] }
    caller.db.power = { 'Blood Potency' : 1 }
    text = 'Select Clan:'
    option_list = []
    clans_list = search_script_tag('clan_stat')
    clans=[]
    for item in clans_list:
        if item.db.restricted == False:
            clans.append([item.db.longname,item])
    clans = sorted(clans,key=itemgetter(0))
    for item in clans:
        option_list.append( {'desc' : item[0],
                             'goto' : ( _vampire_set_clan,
                                        { 'clan' : item[1] } ) } )
    option_list.append({'desc': 'Back',
                        'key': 'B',
                        'goto': 'return_to_main_cg'})
    option_list.append({'desc': 'Back',
                        'key': 'back',
                        'goto': 'return_to_main_cg'})
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 79 + '|/|/' +
            'Clan is more archetype than personality. While the Disciplines ' +
            'and banes of the various clans may influence behavior, any ' +
            'person could be Embraced into any clan. There\'s something to ' +
            'be said for playing into stereotypes, but challenging ' +
            'established norms can be very fulfilling.|/|/Your choice of ' +
            'clan determines the Disciplines with which your character has ' +
            'an affinity. As well, every clan has two favored Attributes. ' +
            'Take an additional dot in one of these. This can only take an ' +
            'Attribute to five dots.' + '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def return_to_main_cg(caller, raw_string, **kwargs):
    caller.db.basics = {}
    caller.db.sphere = {}
    del caller.db.power
    del caller.db.disciplines
    del caller.db.coils
    ExMenu(caller, 'codes.menus.cg', startnode='assign_template',
           cmdset_mergetype='Union', cmd_on_exit=None, auto_quit=False)
    text = {'format': 'suppress'}
    return text, None

def _vampire_set_clan(caller, raw_string, **kwargs):
    clan = kwargs['clan']
    caller.db.sphere['Clan'] = clan.db.longname
    return ("vampire_stat", { 'clan' : clan })

def vampire_stat(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'vampire_stat'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    clan = kwargs['clan']
    text = 'Select one attribute to boost:'
    option_list=[]
    for attribute in clan.db.favored_attributes:
        option_list.append( { 'desc' : attribute.capitalize(),
                              'goto' : (_raise_stat,
                                        {'stat' : attribute.lower(),
                                         'clan' : kwargs['clan'] } ) } )
    option_list.append({'desc': 'Back',
                        'key': 'B',
                        'goto': 'vampire_template'})
    option_list.append({'desc': 'Back',
                        'key': 'back',
                        'goto': 'vampire_template'})
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 79 + '|/|/' +
            'Every clan has two favored Attributes. ' +
            'Take an additional dot in one of these. This can only take an ' +
            'Attribute to five dots.' + '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _raise_stat(caller, raw_string, **kwargs):
    start_value = caller.get(kwargs['stat'], statclass='Attribute')
    if start_value == 5:
        caller.msg('|/Can\'t boost a stat to over 5')
        return ('vampire_stat', kwargs)
    else:
        set(caller, kwargs['stat'], statclass='Attribute',
            value=start_value + 1)
        caller.db.cg['stat_boost'] = {'stat': kwargs['stat'],
                                      'start': start_value}
        return "vampire_covenant"

def vampire_covenant(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'vampire_covenant'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    text = 'Select Covenant:'
    covenants_list = search_script_tag('covenant_stat')
    covenants = []
    for item in covenants_list:
        if item.db.restricted == False:
            covenants.append([item.db.longname, item])
    covenants = sorted(covenants, key=itemgetter(0))
    option_list = []
    for item in covenants:
        option_list.append( {'desc' : item[0],
                             'goto' : ( _set_covenant,
                                        { 'covenant' : item[1] } ) } )
    option_list.append( {'desc' : 'Unaligned',
                             'goto' : _no_covenant } )
    option_list.append({'desc': 'Back',
                        'key': 'B',
                        'goto': _return_to_stat})
    option_list.append({'desc': 'Back',
                        'key': 'back',
                        'goto': _return_to_stat})
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 79 + '|/|/' +
            'Covenants are Kindred social orders. While your character\'s ' +
            'sire may influence her covenant choice, ultimately the choice ' +
            'is hers. Also, it may change with time. You may choose to start ' +
            'play without a covenant. Kindred without covenants are often ' +
            'seen as untrustworthy, but they have more freedom to negotiate ' +
            'their own alliances.' + '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _return_to_stat(caller, raw_string, **kwargs):
    set(caller, caller.db.cg['stat_boost']['stat'], statclass='Attribute',
        value=caller.db.cg['stat_boost']['start'])
    return 'vampire_stat',{'clan': find(caller.get('Clan',
                                                         statclass='Sphere'),
                                              statclass='Clan')[0]}

def _set_covenant(caller, raw_string, **kwargs):
    covenant = kwargs['covenant']
    caller.db.sphere['Covenant'] = covenant.db.longname
    return "vampire_anchors"

def _no_covenant(caller, raw_string, **kwargs):
    caller.db.sphere['Covenant'] = 'Unaligned'
    return "vampire_anchors"

def vampire_anchors(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'vampire_anchors'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    mask = get(caller,'Mask',statclass='Sphere')
    dirge = get(caller,'Dirge',statclass='Sphere')
    text = 'Mask: '
    if mask:
        text = text + mask + '|/'
    else:
        text = text + 'Unset|/'
    text = text + 'Dirge: '
    if dirge:
        text = text + dirge + '|/'
    else:
        text = text + 'Unset|/'
    text = text + '|/Chose what to work on'
    option_list = [
        { 'desc' : 'Mask',
          'goto' : ('choose_anchor', { 'type' : 'mask' } ) },
        { 'desc' : 'Dirge',
          'goto' : ('choose_anchor', { 'type' : 'dirge' } ) } ]
    if mask and dirge:
        option_list.append ( { 'key' : 'P',
                              'desc' : 'Proceed',
                              'goto' : 'vampire_merits' } )
    option_list.append({'desc': 'Back',
                        'key': 'B',
                        'goto': 'vampire_covenant'})
    option_list.append({'desc': 'Back',
                        'key': 'back',
                        'goto': 'vampire_covenant'})
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 79 + '|/|/' +
            'Choose a Mask and a Dirge for your character. Whereas a mortal ' +
            'character has a Virtue and a Vice, Kindred characters have ' +
            'Masks and Dirges.|/|/Kindred wear Masks in public. A Mask is ' +
            'the persona she shows the prey. The Mask is the pretty lie, the ' +
            'identity that keeps her walking among the flock as an insider, ' +
            'even though she\'s nothing of the sort. It reflects how she ' +
            'deals with human society.|/|/The Dirge is who she is behind ' +
            'closed doors, and when dealing with other Kindred. A Dirge is ' +
            'the harsh truth to which she clings. It\'s the grounding point ' +
            'to which she always returns. When she walks the halls of ' +
            'Elysium, and works within her covenant, she presents her Dirge.' +
            '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def choose_anchor(caller, raw_string, **kwargs):
    option_list = []
    for item in anchors[kwargs['type']]:
        option_list.append( {'desc' : item ,
                             'goto' : ( _set_anchor,
                                    {'type' : kwargs['type'],
                                     'value' : item } ) } )
    text = 'Set ' + kwargs['type'].capitalize() + ':'
    options = tuple(option_list)
    return text, options

def _set_anchor(caller, raw_string, **kwargs):
    caller.db.sphere[kwargs['type'].capitalize()] = kwargs['value']
    return 'vampire_anchors'

def vampire_merits(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'vampire_merits'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    max = 10
    total = 0
    text = 'Blood Potency: ' + str(caller.db.power['Blood Potency']) + \
           '|/Merits:|/|/'
    for item in caller.db.merits:
        out = item[0]
        total = total +  item[1]
        if len(item[2]) > 0:
            out = out + ' (' + item[2] + ')'
        out = out + ': ' + str(item[1])
        text = text + out + '|/'
    total = total + (caller.get('Blood Potency',statclass='Power') - 1) * 5
    text = text + '|/Points remaining: ' + str(max - total)
    option_list = []
    if total < max:
        option_list.append( {'key' : 'A',
                             'desc' : 'Add a merit',
                             'goto' : ( 'add_merit',
                                        { 'total' : total,
                                         'max' : max} ) } )
    if max - total > 4:
        option_list.append ( {'key' : 'I',
                              'desc' : 'Increase Blood Potency',
                              'goto' : _increase_power } )
    if get(caller,'Blood Potency',statclass='Power') > 1:
        option_list.append ( {'key' : 'D',
                              'desc' : 'Decrease Blood Potency',
                              'goto' : _decrease_power } )
    if total > 0:
        option_list.append( {'key' : 'R',
                             'desc' : 'Remove a merit',
                             'goto' : ('remove_merit',
                                       {'total' : total,
                                        'max' : max} ) } )
    if total == max:
        option_list.append( {'key' : 'P',
                             'desc' : 'Proceed',
                             'goto' : 'vampire_disciplines'})
    option_list.append({'desc': 'Back',
                        'key': 'B',
                        'goto': _return_to_anchors})
    option_list.append({'desc': 'Back',
                        'key': 'back',
                        'goto': _return_to_anchors})
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 79 + '|/|/' +
            'Merits are important facets of your character that do not fall ' +
            'under other traits. A Merit can represent a knack, special ' +
            'training, people your character knows, or even things that he ' +
            'owns. They add unique capabilities to your character beyond ' +
            'Attributes and Skills.' + '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _return_to_anchors(caller, raw_string, **kwargs):
    caller.db.merits = []
    return 'vampire_anchors'

def add_merit(caller, raw_string, **kwargs):
    text = 'Merit:'
    option_list = [ {'key' : '_default',
                 'goto' : ( _check_merit,
                            { 'total' : kwargs['total'],
                             'max' : kwargs['max'] } ) } ]
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 49 + '|/|/' +
            'Enter the name of the merit you want to purchase.' +
            '|/' + '_' * 49)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'F'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _check_merit(caller, raw_string, **kwargs):
    merits = find(strip_control_sequences(raw_string), statclass='Merit')
    if len(merits) < 1:
        caller.msg('|/I can\'t find ' + strip_control_sequences(raw_string))
        return 'vampire_merits'
    elif len(merits) > 1:
        caller.msg('|/Too many matches found')
        return 'vampire_merits'
    else:
        merit = merits[0]
        if merit.db.restricted == True:
            caller.msg('|/That merit is restricted')
            return 'vampire_merits'
        elif len(merit.db.noteRestrictions) == 0:
            return 'get_merit_value', { 'total' : kwargs['total'],
                                   'note' : '',
                                   'merit' : merit,
                                   'max' : kwargs['max']}
        else:
            return 'get_merit_note', { 'total' : kwargs['total'],
                                  'merit' : merit,
                                  'max' : kwargs['max']}

def get_merit_note(caller, raw_string, **kwargs):
    text = 'This merit requires some form of note such as who the contacts '
    text = text + 'are or what the area of expertise is in:'
    option_list = [{'key': '_default',
                    'goto': (_check_merit_note,
                             {'total': kwargs['total'],
                              'merit': kwargs['merit'],
                              'max': kwargs['max']})}]
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 79 + '|/|/' + 'Some merits can be purchased ' +
            'multiple times to represent different things. One good example ' +
            'of this is the Status merit. Characters can have Status with ' +
            'multiple groups so each time Status is purchased a note ' +
            'will need to be provided to specify what group it applies to.' +
            '|/|/Some merits allow open ended notes while others will ' +
            'restrict possible notes to a given list.' +
            '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'F'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _check_merit_note(caller, raw_string, **kwargs):
    merit = kwargs['merit']
    if merit.db.noteRestrictions[0] == '*':
        return 'get_merit_value', { 'total' : kwargs['total'],
                                'note' : strip_control_sequences(raw_string),
                                'merit' : merit,
                                'max' : kwargs['max']}
    elif strip_control_sequences(raw_string) in merit.db.noteRestrictions:
        return 'get_merit_value', { 'total' : kwargs['total'],
                                'note' : strip_control_sequences(raw_string),
                                'merit' : merit,
                                'max' : kwargs['max']}
    else:
        caller.msg('|/Invalid note for that merit')
        return 'vampire_merits'

def get_merit_value(caller, raw_string, **kwargs):
    text = 'Enter value:'
    option_list = [{'key': '_default',
                    'goto': (_check_merit_value,
                             {'total': kwargs['total'],
                              'note': kwargs['note'],
                              'merit': kwargs['merit'],
                              'max': kwargs['max']})}]
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 29 + '|/|/Enter a value between 1 and 5' + '|/' +
            '_' * 29)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'F'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _check_merit_value(caller, raw_string, **kwargs):
    if not strip_control_sequences(raw_string).isnumeric():
        caller.msg('|/Invalid value')
        return 'vampire_merits'
    else:
        value=int(strip_control_sequences(raw_string))
        if value < 1:
            caller.msg('|/Invalid value')
            return 'vampire_merits'
        elif value + kwargs['total'] - kwargs['merit'].get(caller,
                                    subentry=kwargs['note']) >  kwargs['max']:
            caller.msg('|/You don\'t have enough points')
            return 'vampire_merits'
        elif kwargs['merit'].meets_prereqs(caller,value=value,
                                           subentry=kwargs['note']):
            kwargs['merit'].set(caller,value=value,subentry=kwargs['note'])
            return 'vampire_merits'
        else:
            caller.msg('|/You don\'t meet the prerequisites for that merit')
            return 'vampire_merits'

def remove_merit(caller, raw_string, **kwargs):
    text = 'Remove which merit:'
    option_list = []
    for item in caller.db.merits:
        merit = item[0]
        if len(item[2]) > 0:
            merit = merit + ' (' + item[2] + ')'
        merit = merit + ': ' + str(item[1])
        option_list.append( {'desc' : merit ,
                             'goto' : ( _delete_merit,
                                    { 'entry' : item[0],
                                      'subentry' : item[2] } ) } )
    options = tuple(option_list)
    return text,options

def _delete_merit(caller, raw_string, **kwargs):
    set(caller, kwargs['entry'], subentry=kwargs['subentry'], value=0)
    return 'vampire_merits'

def _increase_power(caller, raw_string, **kwargs):
    if caller.db.power['Blood Potency'] < 10:
        caller.db.power['Blood Potency'] = caller.db.power['Blood Potency'] + 1
        send_kwargs = kwargs
    return 'vampire_merits'

def _decrease_power(caller, raw_string, **kwargs):
    if caller.db.power['Blood Potency'] > 1:
        caller.db.power['Blood Potency'] = caller.db.power['Blood Potency'] - 1
    return 'vampire_merits'

def vampire_disciplines(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'vampire_disciplines'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    clan_msg = ['|/Clan Disciplines:']
    out_msg = ['|/Out of Clan Disciplines:']
    clan_list = []
    out_list = []
    clan_count = 0
    total_count = 0
    clan = find(caller.db.sphere['Clan'],statclass='Clan')[0]
    if caller.db.disciplines:
        disciplines = list(caller.db.disciplines.keys())
    else:
        disciplines = []
    for item in disciplines:
        value = caller.db.disciplines[item]
        entry = '|_|_|_|_' + item + ': ' + str(value)
        if item in clan.db.favored_disciplines:
            clan_count = clan_count + value
            clan_list.append(entry)
        else:
            out_list.append(entry)
        total_count = total_count + value

    if caller.db.coils:
        coils = list(caller.db.coils.keys())
    else:
        coils = []
    for item in coils:
        value = caller.db.coils[item]
        entry = '|_|_|_|_' + item + ': ' + str(value)
        out_list.append(entry)
        total_count = total_count + value

    clan_list.sort()
    out_list.sort()
    for item in clan_list:
        clan_msg.append(item)
    for item in out_list:
        out_msg.append(item)
    text = 'Disciplines: 3 Dots. (2 must be spent on clan disciplines)'
    for item in clan_msg:
        text = text + '|/|_|_|_|_' + item
    for item in out_msg:
        text = text + '|/|_|_|_|_' + item
    option_list = []
    if total_count < 3:
        option_list.append( { 'key' : 'A',
                              'desc' : 'Add a discipline or coil',
                              'goto' : 'vampire_add_discipline' } )
    if len(clan_msg) + len(out_msg) > 2:
        option_list.append( { 'key' : 'R',
                              'desc' : 'Remove a discipline or coil',
                              'goto' : 'vampire_remove_discipline' } )
    if clan_count >= 2 and total_count == 3:
        option_list.append( { 'key' : 'F',
                              'desc' : 'Finish character generation',
                               'goto' : 'vampire_finish_cg' } )
    option_list.append({'desc': 'Back',
                        'key': 'B',
                        'goto': _return_to_merits})
    option_list.append({'desc': 'Back',
                        'key': 'back',
                        'goto': _return_to_merits})
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 79 + '|/|/' +
            'Disciplines are extensions of the Blood. They are ways the ' +
            'Beast\'s tendrils creep out into the world to manipulate, to ' +
            'pervert, and to destroy. These unholy tricks can accomplish ' +
            'nefarious and terrifying things, from changing the vampire into ' +
            'an animal to forcing a victim into an artificial love.|/|/If ' +
            'the character starts with Status in the Circle of the Crone, ' +
            'Lancea et Sanctum, or Ordo Dracul, she may use one dot to ' +
            'begin play with Cruac, Theban Sorcery, or the Coils of the ' +
            'Dragon, respectively.' + '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _return_to_merits(caller, raw_string, **kwargs):
    caller.db.disciplines = {}
    caller.db.coils = {}
    return 'vampire_merits'

def vampire_remove_discipline(caller, raw_string, **kwargs):
    text = 'Select discipline to remove:'
    option_list = []
    if caller.db.disciplines:
        disciplines = list(caller.db.disciplines.keys())
    else:
        disciplines = []
    disciplines.sort()
    if caller.db.coils:
        coils = list(caller.db.coils.keys())
        coils.sort()
        for item in coils:
            disciplines.append(item)
    for item in disciplines:
        option_list.append( { 'desc' : item,
                              'goto' : ( _remove_discipline,
                                       { 'discipline' : item } ) } )
    options = tuple(option_list)
    return text,options

def _remove_discipline(caller, raw_string, **kwargs):
    if ('Mystery Coil' in caller.db.sphere and
        caller.db.sphere['Mystery Coil'] == kwargs['discipline']):
        caller.msg('|/Removal of favored coil required a reset of all coils')
        del caller.db.coils
        del caller.db.sphere['Mystery Coil']
    else:
        set(caller,kwargs['discipline'],value=False)
    return 'vampire_disciplines'

def vampire_add_discipline(caller, raw_string, **kwargs):
    text = 'Discipline or Coil:'
    options = ( {'key' : '_default',
                 'goto' : _check_discipline } )
    return text,options

def _check_discipline(caller, raw_string, **kwargs):
    stat = (find(strip_control_sequences(raw_string),statclass='Discipline') +
            find(strip_control_sequences(raw_string),statclass='Coil'))
    if len(stat) < 1:
        caller.msg('|/I can\'t find ' + strip_control_sequences(raw_string))
        return 'vampire_disciplines'
    elif len(stat) > 1:
        caller.msg('|/Too many matches found')
        return 'vampire_disciplines'
    else:
        stat = stat[0]
        if stat.db.restricted == True:
            caller.msg('|/That ' + stat.type() + ' is restricted')
            return 'vampire_disciplines'
        else:
            return 'get_discipline_value', { 'stat' : stat }

def get_discipline_value(caller, raw_string, **kwargs):
    text = 'Enter value:'
    options = ( {'key' : '_default',
                 'goto' : ( _check_stat_value,
                            { 'stat' : kwargs['stat'] } ) } )
    return text,options

def _check_stat_value(caller, raw_string, **kwargs):
    if not strip_control_sequences(raw_string).isnumeric():
        caller.msg('|/Invalid value')
        return 'vampire_disciplines'
    else:
        value=int(strip_control_sequences(raw_string))
        if value < 1:
            caller.msg('|/Invalid value')
            return 'vampire_disciplines'
        elif kwargs['stat'].meets_prereqs(caller,value=value):
            kwargs['stat'].set(caller,value=value)
            return 'vampire_disciplines'
        else:
            caller.msg('|/You don\'t meet the prerequisites for that '+
                       kwargs['stat'].type())
            return 'vampire_disciplines'

def quit_menu(caller, raw_string, **kwargs):
    obj_menu = 'codes.commands.character_menus.object_in_menu'
    act_menu = 'codes.commands.character_menus.account_in_menu'
    caller.cmdset.delete(obj_menu)
    caller.account.cmdset.delete(act_menu)
    caller.execute_cmd('look')
    text = {'format': 'suppress'}
    return text, None

def vampire_finish_cg(caller, raw_string, **kwargs):
    obj_menu = 'codes.commands.character_menus.object_in_menu'
    act_menu = 'codes.commands.character_menus.account_in_menu'
    caller.cmdset.delete(obj_menu)
    caller.account.cmdset.delete(act_menu)
    del caller.db.cg
    caller.cmdset.delete('unfinished_character')
    caller.cmdset.add(
        'codes.commands.character_commands.finished_character',permanent=True)
    set(caller,'Humanity',statclass='Advantage', value=7)
    set(
        caller,'Vitae',statclass='Advantage',
        value=caller.get('Vitae',subentry='Permanent',statclass='Advantage'))
    set(
        caller,'Willpower',statclass='Advantage',
        value=caller.get('Willpower',
                         subentry='Permanent',statclass='Advantage'))
    caller.db.finished_cg = time.asctime(time.localtime(time.time()))
    caller.db.xp = { 'earned' : 75,
                     'spent' : 0,
                     'log' : {} }
    caller.execute_cmd('look')
    text = {'format' : 'suppress'}
    return text,None
