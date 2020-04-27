from codes.data import get
from codes.data import set
from codes.data import find
from evennia.utils.utils import strip_control_sequences
from evennia.utils.search import search_script_tag
from operator import itemgetter

import time

anchors = { 'blood' : ['Alpha','Challenger','Destroyer','Fox','The Monster',
                       'Soldier'],
            'bone' : ['Community Organizer','Cub','Guru','Hedonist',
                      'Lone Wolf','Wallflower'] }

moon_list = { 'crescent moon' : ['Shadow Gaze','Spirit Whispers'],
               'full moon' : ['Killer Instinct', 'Warrior\'s Hide'],
               'gibbous moon' : ['War Howl', 'Voice of Glory'],
               'half moon' : ['Scent Beneath the Surface', 'Binding Oath'],
               'new moon' : ['Eviscerate', 'Slip Away']}

def werewolf_template(caller, raw_string, **kwargs):
    caller.db.basics = { 'Sphere' : 'Werewolf' }
    caller.db.renown = {'Cunning': 0, 'Glory': 0, 'Honor': 0, 'Purity': 0,
                        'Wisdom': 0}
    caller.db.power = { 'Primal Urge' : 1 }
    caller.db.gifts = {}
    caller.db.werewolfRites = {}
    text = 'Select Auspice:'
    option_list = []
    auspices_list = search_script_tag('auspice_stat')
    auspices=[]
    for item in auspices_list:
        if item.db.restricted == False:
            auspices.append([item.db.longname,item])
    auspices = sorted(auspices,key=itemgetter(0))
    for item in auspices:
        option_list.append( {'desc' : item[0],
                             'goto' : ( _werewolf_set_auspice,
                                        { 'auspice' : item[1] } ) } )
    options = tuple(option_list)
    return text, options

def _werewolf_set_auspice(caller, raw_string, **kwargs):
    auspice = kwargs['auspice']
    caller.db.sphere['Auspice'] = auspice.db.longname
    caller.db.renown[auspice.db.renown] = 1
    return "werewolf_stat", { 'auspice' : auspice }
    
def werewolf_stat(caller, raw_string, **kwargs):
    auspice = kwargs['auspice']
    option_list=[]
    for attribute in auspice.db.auspice_skills:
        option_list.append( { 'desc' : attribute.capitalize(),
                              'goto' : (_raise_stat,
                                        {'stat' : attribute.lower(),
                                         'auspice' : kwargs['auspice'] } ) } )
    options = tuple(option_list)
    text = 'Select one skill to boost:'
    return text,options

def _raise_stat(caller, raw_string, **kwargs):
    start_value = caller.get(kwargs['stat'],statclass='Skill')
    if start_value == 5:
        caller.msg('|/Can\'t boost a stat to over 5')
        return "werewolf_stat", kwargs
    else:
        set(caller, kwargs['stat'], statclass='Skill', value=start_value+1)
        return "werewolf_tribe"
    
def werewolf_tribe(caller, raw_string, **kwargs):

    text = 'Select Tribe:'
    tribes_list = search_script_tag('tribe_stat')
    tribes = []
    for item in tribes_list:
        if item.db.restricted == False:
            tribes.append([item.db.longname, item])
    tribes = sorted(tribes, key=itemgetter(0))
    option_list = []
    for item in tribes:
        option_list.append( {'desc' : item[0],
                             'goto' : ( _set_tribe,
                                        { 'tribe' : item[1] } ) } )
    options = tuple(option_list)
    return text, options

def _set_tribe(caller, raw_string, **kwargs):
    tribe = kwargs['tribe']
    caller.db.sphere['Tribe'] = tribe.db.longname
    if tribe.db.renown != '':
        renown = tribe.db.renown
        renown_score = caller.get(renown,statclass='Renown') + 1
        caller.db.renown[renown] = renown_score
    return "werewolf_renown"

def werewolf_renown(caller, raw_string, **kwargs):
    text = ('Select one renown to boost:' +
            '|/|_|_|_|_Cunning: ' +
            str(caller.get('Cunning', statclass='Renown')) +
            '|/|_|_|_|_Glory: ' +
            str(caller.get('Glory', statclass='Renown')) +
            '|/|_|_|_|_Honor: ' +
            str(caller.get('Honor', statclass='Renown')) +
            '|/|_|_|_|_Purity: ' +
            str(caller.get('Purity', statclass='Renown')) +
            '|/|_|_|_|_Wisdom: ' +
            str(caller.get('Wisdom', statclass='Renown')))
    renown_list = search_script_tag('renown_stat')
    renown = []
    for item in renown_list:
        renown.append([item.db.longname, item])
    renown = sorted(renown, key=itemgetter(0))
    option_list = []
    for item in renown:
        option_list.append({'desc': item[0],
                            'goto': (_raise_renown,
                                     {'renown': item[1]})})
    options = tuple(option_list)
    return text, options


def _raise_renown(caller, raw_string, **kwargs):
    start_value = caller.get(kwargs['renown'].db.longname, statclass='Renown')
    if start_value >= 2:
        caller.msg('|/Can\'t boost a starting renown to over 2')
        return "werewolf_stat", kwargs
    else:
        set(caller, kwargs['renown'].db.longname, statclass='Renown', value=start_value + 1)
        return "werewolf_anchors"

def werewolf_anchors(caller, raw_string, **kwargs):

    blood = get(caller,'Blood',statclass='Sphere')
    bone = get(caller,'Bone',statclass='Sphere')
    text = 'Blood: '
    if blood:
        text = text + blood + '|/'
    else:
        text = text + 'Unset|/'
    text = text + 'Bone: '
    if bone:
        text = text + bone + '|/'
    else:
        text = text + 'Unset|/'
    text = text + '|/Chose what to work on'
    option_list = [
        { 'desc' : 'Blood',
          'goto' : ('choose_anchor', { 'type' : 'blood' } ) },
        { 'desc' : 'Bone',
          'goto' : ('choose_anchor', { 'type' : 'bone' } ) } ]
    if blood and bone:
        option_list.append ( { 'key' : 'P',
                              'desc' : 'Proceed',
                              'goto' : _starting_gifts } )
    options = tuple(option_list)
    return text, options

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
    return 'werewolf_anchors'

def _starting_gifts(caller, raw_string, **kwargs):
    auspice = find(caller.get('Auspice',statclass='Sphere'),
                   statclass='Auspice')[0]
    moon = auspice.db.auspice_gifts[0].lower()
    set(caller, moon_list[moon][0], statclass='Gift', value=True)
    if caller.get(auspice.db.renown,statclass='Renown') == 2:
        set(caller, moon_list[moon][1], statclass='Gift', value=True)
    return 'werewolf_gifts'

def werewolf_gifts(caller,raw_string,**kwargs):
    auspice = find(caller.get('Auspice', statclass='Sphere'),
                   statclass='Auspice')[0]
    if caller.get(auspice.db.renown,statclass='Renown') == 2:
        wolf_gifts = 0
        moon_gifts = 2
    else:
        wolf_gifts = 1
        moon_gifts = 1
    moon_list = []
    shadow_list = []
    wolf_list = []
    for item in list(caller.db.gifts.keys()):
        gift = find(item,statclass='Gift')[0]
        if gift.db.category.lower() == 'moon':
            moon_list.append(gift.db.longname)
        elif gift.db.category.lower() == 'shadow':
            shadow_list.append(gift.db.longname)
        else:
            wolf_list.append(gift.db.longname)
    if moon_gifts == 1:
        text = 'Gifts:|/|/Required: 1 moon gift, 2 shadow gifts and 1 wolf gift.'
    else:
        text = 'Gifts:|/|/Required: 2 moon gifts and 2 shadow gifts.'
    text = text + '|/|/|_|_|_|_Moon Gifts:|/'
    for item in moon_list:
        text = text + '|_|_|_|_|_|_|_|_' + item + '|/'
    text = text + '|/'
    if len(shadow_list) > 0:
        text = text + '|_|_|_|_Shadow Gifts:|/'
        for item in shadow_list:
            text = text + '|_|_|_|_|_|_|_|_' + item + '|/'
        text = text + '|/'
    if len(wolf_list) > 0:
        text = text + '|_|_|_|_Wolf Gifts:|/'
        for item in wolf_list:
            text = text + '|_|_|_|_|_|_|_|_' + item + '|/'
        text = text + '|/'
    option_list = []
    if len(wolf_list) < wolf_gifts or len(shadow_list) < 2:
        option_list.append( { 'key' : 'A',
                              'desc' : 'Add a gift',
                              'goto' : 'werewolf_add_gift' } )
    if len(wolf_list) > 0 or len(shadow_list) > 0:
        option_list.append( { 'key' : 'R',
                              'desc' : 'Remove a gift',
                              'goto' : 'werewolf_remove_gift' } )
    if len(wolf_list) == wolf_gifts and len(shadow_list) == 2:
        option_list.append( { 'key' : 'P',
                              'desc' : 'Proceed',
                              'goto' : 'werewolf_merits' } )
    options = tuple(option_list)
    return text,options

def werewolf_add_gift(caller, raw_string, **kwargs):
    text = 'Gift:'
    options = ( {'key' : '_default',
                 'goto' : _check_gift } )
    return text,options

def _check_gift(caller, raw_string, **kwargs):
    gifts = find(strip_control_sequences(raw_string), statclass='Gift')
    if len(gifts) < 1:
        caller.msg('|/I can\'t find ' + strip_control_sequences(raw_string))
    elif len(gifts) > 1:
        caller.msg('|/Too many matches found')
    else:
        gift = gifts[0]
        auspice_gifts = find(caller.get('Auspice',statclass='Sphere'),
                            statclass='Auspice')[0].db.auspice_gifts
        tribe_gifts = find(caller.get('Tribe', statclass='Sphere'),
                            statclass='Tribe')[0].db.tribe_gifts
        if gift.meets_prereqs(caller,value=True) and gift.db.type != 'moon':
            if (gift.db.group in auspice_gifts or
              gift.db.group in tribe_gifts or
              gift.db.category.lower() == 'wolf'):
                gift.set(caller,value=True)
            else:
                caller.msg('|/You cannot take that gift in character generation.')
        else:
            caller.msg('|/You cannot take that gift in character generation.')
    return 'werewolf_gifts'

def werewolf_remove_gift(caller, raw_string, **kwargs):
    text = 'Select contract to remove:'
    option_list = []
    gifts = list(caller.db.gifts.keys())
    gifts.sort()
    for item in gifts:
        gift = find(item,statclass='Gift')[0]
        if gift.db.category.lower() != 'moon':
            option_list.append( { 'desc' : item,
                              'goto' : ( _remove_gift, {'gift' : item} ) } )
    options = tuple(option_list)
    return text,options

def _remove_gift(caller, raw_string, **kwargs):
    set(caller,kwargs['gift'],statclass='Gift',value=False)
    return 'werewolf_gifts'

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
