from codes.data import get
from codes.data import set
from codes.data import find
from evennia.utils.utils import strip_control_sequences
from evennia.utils.search import search_script_tag
from operator import itemgetter

import time

def mage_template(caller, raw_string, **kwargs):
    caller.db.basics = { 'Sphere' : 'Mage' }
    caller.db.power = { 'Gnosis' : 1 }
    caller.db.sphere = {'Obsessions':[]}
    caller.db.arcana = {}
    caller.db.rotes = {}
    caller.db.praxes = {}
    text = 'Select Path:'
    option_list = []
    auspices_list = search_script_tag('path_stat')
    paths=[]
    for item in path_list:
        if item.db.restricted == False:
            pathss.append([item.db.longname,item])
    paths = sorted(paths,key=itemgetter(0))
    for item in paths:
        option_list.append( {'desc' : item[0],
                             'goto' : ( _mage_set_path,
                                        { 'path' : item[1] } ) } )
    options = tuple(option_list)
    return text, options

def _mage_set_path(caller, raw_string, **kwargs):
    auspice = kwargs['path']
    caller.db.sphere['Path'] = path.db.longname
    caller.db.renown[auspice.db.renown] = 1
    return "mage_order"

def mage_order(caller, raw_string, **kwargs):

    text = 'Select Order:'
    orders_list = search_script_tag('order_stat')
    orders = []
    for item in orders_list:
        if item.db.restricted == False:
            orders.append([item.db.longname, item])
    orders = sorted(orders, key=itemgetter(0))
    option_list = []
    for item in orders:
        option_list.append( {'desc' : item[0],
                             'goto' : ( _set_order,
                                        { 'order' : item[1] } ) } )
    options = tuple(option_list)
    return text, options

def _set_order(caller, raw_string, **kwargs):
    order = kwargs['order']
    caller.db.sphere['Order'] = order.db.longname
    return "mage_arcana"

def mage_arcana(caller,raw_string,**kwargs):
    path = find(caller.get('Path', statclass='Sphere'),
                   statclass='Path')[0]
    ruling_arcana = path.db.ruling_arcana
    remaining_arcana = []
    for item in list(caller.db.arcana.keys()):
        if item not in ruling_arcana:
            remaining_arcana.append(item)
    inferior_arcana = path.db.inferior_arcana

    # Do we have six dots spent?
    spent_all = True
    total_spent = 0
    for item in list(caller.db.arcana.keys()):
        total_spent = total_spent + caller.get(item,statclass='Arcana')
    if total_spent != 6:
        spent_all = False

    # Do we have more than one Arcana at 3?
    one_three_test = True
    no_three = True
    for item in list(caller.db.arcana.keys()):
        if caller.get(item,statclass='Arcana') == 3:
            if no_three:
                no_three = False
            else
                one_three_test = False

    # Three to five dots in ruling arcana?
    three_to_five_test = True
    ruling_total = 0
    for item in ruling_arcana:
        ruling_total = ruling_total + caller.get(item,statclass='Arcana')
    if ruling_total < 3 or ruling_total > 5:
        three_to_five_test = False

    # Both ruling arcana have at least one dot?
    both_test = True
    for item in ruling_arcana:
       if caller.get(item,statclass='Arcana') < 1:
           both_test = False

    text = 'Arcana:|/|/Required: 6 total. Only one at 3. 3 to 5 points in Ruling Arcana. At least 1 point in each Ruling Arcana'
    text = text + '|/|/|_|_|_|_Ruling Arcana:|/'
    for item in ruling_arcana:
        text = (text + '|_|_|_|_|_|_|_|_' + item + ': ' +
               str(caller.get(item,statclass='Arcana')) + '|/')
    text = text + '|/'
    if len(remaining_arcana) > 0:
        text = text + '|_|_|_|_Other Arcana:|/'
        for item in remaining_arcana:
            text = text + '|_|_|_|_|_|_|_|_' + item + ': ' +
            str(caller.get(item, statclass='Arcana')) + '|/'
        text = text + '|/'

    arcana_list = search_script_tag('arcana_stat')
    arcana = []
    for item in arcana_list:
        if item.db.restricted == False and item.db.longname != inferior_arcana:
            arcana.append([item.db.longname, item])
    arcana = sorted(orders, key=itemgetter(0))
    option_list = []
    for item in arcana:
        option_list.append({'desc': item[0],'goto': ('get_arcana_value',
                                                     {'stat': item[1]})})

    if spent_all and one_three and three_to_five and both_arcana:
        option_list.append( { 'key' : 'P',
                              'desc' : 'Proceed',
                              'goto' : 'mage_rotes' } )

    options = tuple(option_list)
    return text,options

def get_arcana_value(caller, raw_string, **kwargs):
    text = 'Enter value:'
    options = ( {'key' : '_default',
                 'goto' : ( _check_stat_value,
                            { 'stat' : kwargs['stat'] } ) } )
    return text,options

def _check_stat_value(caller, raw_string, **kwargs):
    if not strip_control_sequences(raw_string).isnumeric():
        caller.msg('|/Invalid value')
        return 'mage_arcana'
    else:
        value=int(strip_control_sequences(raw_string))
        if value < 0:
            caller.msg('|/Invalid value')
            return 'mage_arcana'
        elif kwargs['stat'].meets_prereqs(caller,value=value):
            kwargs['stat'].set(caller,value=value)
            return 'mage_arcana'
        else:
            caller.msg('|/You don\'t meet the prerequisites for that '+
                       kwargs['stat'].type())
            return 'mage_arcana'

def mage_rotes(caller, raw_string, **kwargs):
    text = 'Rotes:|/|/Choose three rotes|/'
    for item in list(caller.db.rotes.keys()):
        text = text + '|_|_|_|_' + item + '|/'
    text = text + '|/'

    option_list = []
    if len(caller.db.rotes) < 3:
        option_list.append({'key': 'A',
                            'desc': 'Add a rote',
                            'goto': 'mage_add_rote'})

def werewolf_merits(caller, raw_string, **kwargs):
    max = 10
    total = 0
    rites_list = []
    rites_points = 0
    for item in list(caller.db.werewolfRites.keys()):
        rites_list.append(item)
        rite = find(item,statclass='werewolf rite')[0]
        rites_points = rites_points + rite.db.rank
    if len(rites_list) > 0:
        rites_list.sort()
    text = 'Primal Urge: ' + str(caller.db.power['Primal Urge']) + \
           '|/|/|_|_Rites:|/'
    for item in rites_list:
        text = text + '|_|_|_|_' + item + '|/'
    text = text + '|/|_|_Merits:|/'
    for item in caller.db.merits:
        out = item[0]
        total = total + item[1]
        if len(item[2]) > 0:
            out = out + ' (' + item[2] + ')'
        out = out + ': ' + str(item[1])
        text = text + '|_|_|_|_' + out + '|/'
    total = total + (caller.get('Primal Urge',statclass='Power') - 1) * 5
    if rites_points > 2:
        total = total + rites_points - 2
    text = text + '|/Points remaining: ' + str(max - total)
    option_list = []
    if total < max:
        option_list.append( {'desc' : 'Add a merit',
                             'goto' : ( 'add_merit',
                                        { 'total' : total,
                                         'max' : max} ) } )
    if total < max and rites_points < 7:
        option_list.append({'desc': 'Add a rite',
                            'goto': ('add_rite',
                                     {'total': total,
                                      'rites_points': rites_points,
                                      'max': max})})
    if max - total > 4:
        option_list.append ( {'desc' : 'Increase Primal Urge',
                              'goto' : _increase_power } )
    if get(caller,'Primal Urge',statclass='Power') > 1:
        option_list.append ( {'desc' : 'Decrease Primal Urge',
                              'goto' : _decrease_power } )
    if len(caller.db.merits) > 0:
        option_list.append( {'desc' : 'Remove a merit',
                             'goto' : ('remove_merit',
                                       {'total' : total,
                                        'max' : max} ) } )
    if rites_points > 0:
        option_list.append({'desc': 'Remove a rite',
                            'goto': ('remove_rite',
                                     {'total': total,
                                      'max': max})})
    if total == max and rites_points >= 2:
        option_list.append( {'key' : 'F',
                             'desc' : 'Finish',
                             'goto' : 'werewolf_finish_cg'})
    options = tuple(option_list)
    return text, options

def add_merit(caller, raw_string, **kwargs):
    text = 'Merit:'
    options = ( {'key' : '_default',
                 'goto' : ( _check_merit,
                            { 'total' : kwargs['total'],
                             'max' : kwargs['max'] } ) } )
    return text,options

def _check_merit(caller, raw_string, **kwargs):
    merits = find(strip_control_sequences(raw_string), statclass='Merit')
    if len(merits) < 1:
        caller.msg('|/I can\'t find ' + strip_control_sequences(raw_string))
        return 'werewolf_merits'
    elif len(merits) > 1:
        caller.msg('|/Too many matches found')
        return 'werewolf_merits'
    else:
        merit = merits[0]
        if merit.db.restricted == True:
            caller.msg('|/That merit is restricted')
            return 'werewolf_merits'
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
    options = ( {'key' : '_default',
                 'goto' : ( _check_merit_note,
                            { 'total' : kwargs['total'],
                             'merit' : kwargs['merit'],
                             'max' : kwargs['max'] } ) } )
    return text, options

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
        return 'werewolf_merits'

def get_merit_value(caller, raw_string, **kwargs):
    text = 'Enter value:'
    options = ( {'key' : '_default',
                 'goto' : ( _check_merit_value,
                            { 'total' : kwargs['total'],
                             'note' : kwargs['note'],
                             'merit' : kwargs['merit'],
                             'max' : kwargs['max'] } ) } )
    return text,options

def _check_merit_value(caller, raw_string, **kwargs):
    if not strip_control_sequences(raw_string).isnumeric():
        caller.msg('|/Invalid value')
        return 'werewolf_merits'
    else:
        value=int(strip_control_sequences(raw_string))
        if value < 1:
            caller.msg('|/Invalid value')
            return 'werewolf_merits'
        elif value + kwargs['total'] - kwargs['merit'].get(caller,
                                    subentry=kwargs['note']) >  kwargs['max']:
            caller.msg('|/You don\'t have enough points')
            return 'werewolf_merits'
        elif kwargs['merit'].meets_prereqs(caller,value=value,
                                           subentry=kwargs['note']):
            kwargs['merit'].set(caller,value=value,subentry=kwargs['note'])
            return 'werewolf_merits'
        else:
            caller.msg('|/You don\'t meet the prerequisites for that merit')
            return 'werewolf_merits'

def add_rite(caller, raw_string, **kwargs):
    text = 'Rite:'
    options = ( {'key' : '_default',
                 'goto' : ( _check_rite,
                            kwargs ) } )
    return text,options

def _check_rite(caller, raw_string, **kwargs):
    rites = find(strip_control_sequences(raw_string), statclass='Werewolf Rite')
    if len(rites) < 1:
        caller.msg('|/I can\'t find ' + strip_control_sequences(raw_string))
        return 'werewolf_merits'
    elif len(rites) > 1:
        caller.msg('|/Too many matches found')
        return 'werewolf_merits'
    else:
        rite = rites[0]
        if rite.db.restricted == True:
            caller.msg('|/That rite is restricted')
            return 'werewolf_merits'
        else:
            value = rite.db.rank
            if (value + kwargs['total'] > kwargs['max'] or
                    value + kwargs['rites_points'] > 7):
                caller.msg('|/You don\'t have enough points')
                return 'werewolf_merits'
            elif rite.meets_prereqs(caller, value=True):
                rite.set(caller, value=True)
                return 'werewolf_merits'
            else:
                caller.msg('|/You don\'t meet the prerequisites for that rite')
                return 'werewolf_merits'

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
    return 'werewolf_merits'

def remove_rite(caller, raw_string, **kwargs):
    text = 'Remove which rite:'
    option_list = []
    rites_list = list(caller.db.werewolfRites.keys())
    rites_list.sort()
    for item in rites_list:
        rite = item
        option_list.append( {'desc' : rite ,
                             'goto' : ( _delete_rite,
                                    { 'rite' : rite } ) } )
    options = tuple(option_list)
    return text,options

def _delete_rite(caller, raw_string, **kwargs):
    set(caller, kwargs['rite'], value=False)
    return 'werewolf_merits'

def _increase_power(caller, raw_string, **kwargs):
    if caller.db.power['Primal Urge'] < 10:
        caller.db.power['Primal Urge'] = caller.db.power['Primal Urge'] + 1
        send_kwargs = kwargs
    return 'werewolf_merits'

def _decrease_power(caller, raw_string, **kwargs):
    if caller.db.power['Primal Urge'] > 1:
        caller.db.power['Primal Urge'] = caller.db.power['Primal Urge'] - 1
    return 'werewolf_merits'

def quit(caller, raw_string, **kwargs):

    text = {'format' : 'suppress'}
    return text,None

def werewolf_finish_cg(caller, raw_string, **kwargs):
    caller.cmdset.delete('unfinished_character')
    caller.cmdset.add(
        'codes.commands.character_commands.finished_character',permanent=True)
    set(caller,'Harmony',statclass='Advantage', value=7)
    set(
        caller,'Essence',statclass='Advantage',
        value=caller.get('Essence',subentry='Permanent',statclass='Advantage'))
    set(
        caller,'Willpower',statclass='Advantage',
        value=caller.get('Willpower',
                         subentry='Permanent',statclass='Advantage'))
    caller.db.finished_cg = time.asctime(time.localtime(time.time()))
    caller.db.xp = { 'earned' : 75,
                     'spent' : 0,
                     'log' : {} }
    text = {'format' : 'suppress'}
    return text,None
