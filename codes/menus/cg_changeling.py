from codes.data import get
from codes.data import set
from codes.data import find
from evennia.utils.utils import strip_control_sequences
from evennia.utils.search import search_script_tag
from operator import itemgetter

import time

anchors = { 'needle' : ['Bon Vivant', 'Chess Master', 'Commander',
                            'Composer', 'Counselor', 'Daredevil', 'Dynamo',
                            'Protector', 'Provider', 'Scholar', 'Storyteller',
                            'Teacher', 'Traditionalist', 'Visionary'],
                'thread' : ['Acceptance', 'Anger', 'Family', 'Friendship',
                            'Hate', 'Honor', 'Joy', 'Love', 'Memory',
                            'Revenge'] } 

courts = ['Spring', 'Summer', 'Autumn', 'Winter', 'None']
regalia = ['Crown', 'Jewels', 'Mirror', 'Shield', 'Steed', 'Sword']

def changeling_template(caller, raw_string, **kwargs):
    caller.db.basics = { 'Sphere' : 'Changeling' }
    caller.db.sphere = { 'Frailties' : [] }
    caller.db.power = { 'Wyrd' : 1 }
    text = 'Select Seeming:'
    option_list = []
    seemings_list = search_script_tag('seeming_stat')
    seemings=[]
    for item in seemings_list:
        seemings.append([item.db.longname,item])
    seemings = sorted(seemings,key=itemgetter(0))
    for item in seemings:
        option_list.append( {'desc' : item[0],
                             'goto' : ( 'changeling_stat',
                                        { 'seeming' : item[1] } ) } )
    options = tuple(option_list)
    return text, options

def changeling_stat(caller, raw_string, **kwargs):
    seeming = kwargs['seeming']
    option_list=[]
    caller.db.sphere['Seeming'] = seeming.db.longname
    caller.db.sphere['Regalia'] = [seeming.db.regalia]
    for attribute in seeming.db.favored_attributes:
        option_list.append( { 'desc' : attribute.capitalize(),
                              'goto' : (_raise_stat,
                                        {'stat' : attribute.lower() } ) } )
    options = tuple(option_list)
    text = 'Select one attribute to boost:'
    return text,options

def _raise_stat(caller, raw_string, **kwargs):
    start_value = caller.get(kwargs['stat'],statclass='Attribute')
    if start_value == 5:
        caller.msg('|/Can\'t boost a stat to over 5')
        return "changeling_stats"
    else:
        set(caller, kwargs['stat'], statclass='Attribute', value=start_value+1)
        return "changeling_kith"
    
def changeling_kith(caller, raw_string, **kwargs):

    text = 'Select Kith:'
    kiths_list = search_script_tag('kith_stat')
    kiths = []
    for item in kiths_list:
        kiths.append([item.db.longname, item])
    kiths = sorted(kiths, key=itemgetter(0))
    option_list = []
    for item in kiths:
        option_list.append( {'desc' : item[0],
                             'goto' : ( 'changeling_court',
                                        { 'kith' : item[1] } ) } )
    options = tuple(option_list)
    return text, options

def changeling_court(caller, raw_string, **kwargs):
    kith = kwargs['kith']
    caller.db.sphere['Kith'] = kith.db.longname
    text = 'Select Court:'
    option_list = []
    for item in courts:
        option_list.append( {'desc' : item,
                             'goto' : ( _changeling_set_court,
                                        { 'court' : item } ) } )
    options = tuple(option_list)
    return text, options
    
def _changeling_set_court(caller, raw_string, **kwargs):
    caller.db.sphere['Court'] = kwargs['court']
    set(caller,'Mantle',statclass='Merit',subentry=kwargs['court'],value=1)
    return 'changeling_anchors'

def changeling_anchors(caller, raw_string, **kwargs):
    
    needle = get(caller,'Needle',statclass='Sphere')
    thread = get(caller,'Thread',statclass='Sphere')
    text = 'Needle: ' 
    if needle:
        text = text + needle + '|/'
    else:
        text = text + 'Unset|/'
    text = text + 'Thread: '
    if thread:
        text = text + thread + '|/'
    else:
        text = text + 'Unset|/'
    text = text + '|/Chose what to work on'
    option_list = [
        { 'desc' : 'Needle',
          'goto' : ('choose_anchor', { 'type' : 'needle' } ) },
        { 'desc' : 'Thread',
          'goto' : ('choose_anchor', { 'type' : 'thread' } ) } ]
    if needle and thread:
        option_list.append ( { 'key' : 'P',
                              'desc' : 'Proceed',
                              'goto' : 'changeling_regalia' } )
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
    return 'changeling_anchors'
    
def changeling_regalia(caller, raw_string, **kwargs):
    text = 'Select second Regalia:'
    option_list = []
    for item in regalia:
        if item != caller.db.sphere['Regalia'][0]:
            option_list.append( {'desc' : item,
                                 'goto' : ( _changeling_set_regalia,
                                          { 'regalia' : item } ) } )
    options = tuple(option_list)
    return text, options

def _changeling_set_regalia(caller, raw_string, **kwargs):
    caller.db.sphere['Regalia'].append(kwargs['regalia'])
    return "changeling_merits"
    
def changeling_merits(caller, raw_string, **kwargs):
    if caller.db.sphere['Court'] != 'None':
        max = 11
    else:
        max = 10
    total = 0
    text = 'Wyrd: ' + str(caller.db.power['Wyrd']) + '|/Merits:|/|/'
    for item in caller.db.merits:
        out = item[0]
        total = total +  item[1]
        if len(item[2]) > 0:
            out = out + ' (' + item[2] + ')'
        out = out + ': ' + str(item[1])
        text = text + out + '|/'
    total = total + (caller.get('Wyrd',statclass='Power') - 1) * 5
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
                              'desc' : 'Increase Wyrd',
                              'goto' : _increase_power } )
    if get(caller,'Wyrd',statclass='Power') > 1:
        option_list.append ( {'key' : 'D',
                              'desc' : 'Decrease Wyrd',
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
                             'goto' : 'changeling_contracts'})
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
        return 'changeling_merits'
    elif len(merits) > 1:
        caller.msg('|/Too many matches found')
        return 'changeling_merits'
    else:
        merit = merits[0]
        if len(merit.db.noteRestrictions) == 0:
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
        return 'changeling_merits'
    
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
        return 'changeling_merits'
    else:
        value=int(strip_control_sequences(raw_string)) 
        if value < 1:
            caller.msg('|/Invalid value')
            return 'changeling_merits'
        elif value + kwargs['total'] - kwargs['merit'].get(caller,
                                    subentry=kwargs['note']) >  kwargs['max']:
            caller.msg('|/You don\'t have enough points')
            return 'changeling_merits'
        elif kwargs['merit'].meets_prereqs(caller,value=value,
                                           subentry=kwargs['note']):
            kwargs['merit'].set(caller,value=value,subentry=kwargs['note'])
            return 'changeling_merits'
        else:
            caller.msg('|/You don\'t meet the prerequisites for that merit')
            return 'changeling_merits'

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
    if ( kwargs['entry'] == 'Mantle' and 
         kwargs['subentry'] == caller.db.sphere['Court'] ):
        caller.msg('|/You can\'t remove your court mantle')
    else:
        set(caller, kwargs['entry'], subentry=kwargs['subentry'], value=0)
    return 'changeling_merits'
    
def _increase_power(caller, raw_string, **kwargs):
    if caller.db.power['Wyrd'] < 10:
        caller.db.power['Wyrd'] = caller.db.power['Wyrd'] + 1
        send_kwargs = kwargs
        if caller.db.power['Wyrd'] in [2, 4, 8]:
            send_kwargs['message'] = 'You must add a minor frailty'
            return 'changeling_add_frailty', send_kwargs
        elif caller.db.power['Wyrd'] in [6, 10]:
            send_kwargs['message'] = 'You must add a major frailty'
            return 'changeling_add_frailty', send_kwargs
    return 'changeling_merits'

def changeling_add_frailty(caller, raw_string, **kwargs):
    send_kwargs=kwargs
    send_kwargs['special']='frailty'
    text = kwargs['message']
    options = ( {'key' : '_default',
                 'goto' : ( _changeling_new_frailty, kwargs) } )
    return text,options 

def _changeling_new_frailty(caller, raw_string, **kwargs):
    f = find('Frailties',statclass='Sphere')[0]
    current_frailties = f.get(caller)
    if current_frailties == False:
        current_frailties = []
    current_frailties.append(strip_control_sequences(raw_string))
    caller.msg(current_frailties)
    f.set(caller,str(current_frailties))
    return 'changeling_merits'

def _decrease_power(caller, raw_string, **kwargs):
    if caller.db.power['Wyrd'] > 1:
        caller.db.power['Wyrd'] = caller.db.power['Wyrd'] - 1
        if caller.db.power['Wyrd'] in [1, 3, 5, 7, 9]:
            f = find('Frailties',statclass='Sphere')[0]
            current_frailties = f.get(caller,subentry='')[:-1]
            f.set(caller,current_frailties)
    return 'changeling_merits'
    
def changeling_contracts(caller, raw_string, **kwargs):
    common_list = ['|/Common Contracts:']
    royal_list = ['|/Royal Contracts:']
    goblin_list = ['|/Goblin Contracts:']
    favored_common = 0
    favored_royal = 0
    contracts = list(caller.db.contracts.keys())
    contracts.sort()
    for item in contracts:
        result = find(item,statclass='Contract')
        entry = '|_|_|_|_' + result[0].db.longname
        if (result[0].db.category in caller.db.sphere['Regalia'] and 
            result[0].db.subgroup == 'Common'):
            entry = entry + ' (f)'
            favored_common = favored_common + 1
        elif ( (result[0].db.category in caller.db.sphere['Regalia'] or 
                result[0].db.category == caller.db.sphere['Court']) and 
                result[0].db.subgroup) == 'Royal':
            entry = entry + ' (f)'
            favored_royal = favored_royal + 1
        if result[0].db.subgroup == 'Common':
            common_list.append(entry)
        elif result[0].db.subgroup == 'Royal':
            royal_list.append(entry)
        elif result[0].db.subgroup == 'Goblin':
            goblin_list.append(entry)
    text = 'Contracts (Four Common or goblin; two must be favored Regalia. '
    text = text + 'Two Royal; both must be favored Regalia or Court'
    for item in common_list:
        text = text + '|/|_|_|_|_' + item
    for item in royal_list:
        text = text + '|/|_|_|_|_' + item
    if len(goblin_list) > 1:
        for item in goblin_list:
            text = text + '|/|_|_|_|_' + item
    option_list = []
    if len(common_list) + len(royal_list) + len(goblin_list) < 9:
        option_list.append( { 'key' : 'A',
                              'desc' : 'Add a contract',
                              'goto' : 'changeling_add_contract' } ) 
    if len(common_list) + len(royal_list) + len(goblin_list) > 3:
        option_list.append( { 'key' : 'R',
                              'desc' : 'Remove a contract',
                              'goto' : 'changeling_remove_contract' } ) 
    if (len(common_list) + len(goblin_list) == 6 and len(royal_list) == 3 and 
                                  favored_common >= 2 and favored_royal == 2):
        option_list.append( { 'key' : 'F',
                              'desc' : 'Finish character generation',
                               'goto' : 'changeling_finish_cg' } )
    options = tuple(option_list)
    return text,options

def changeling_remove_contract(caller, raw_string, **kwargs):
    text = 'Select contract to remove:'
    option_list = []
    contracts = list(caller.db.contracts.keys())
    contracts.sort()
    for item in contracts:
        option_list.append( { 'desc' : item,
                              'goto' : ( _remove_contract,
                                       { 'contract' : item } ) } )
    options = tuple(option_list)
    return text,options

def _remove_contract(caller, raw_string, **kwargs):
    set(caller,kwargs['contract'],statclass='Contract',value=False)
    return 'changeling_contracts'

def changeling_add_contract(caller, raw_string, **kwargs):
    text = 'Contract:'
    options = ( {'key' : '_default',
                 'goto' : _check_contract } )
    return text,options

def _check_contract(caller, raw_string, **kwargs):
    contracts = find(strip_control_sequences(raw_string), statclass='Contract')
    if len(contracts) < 1:
        caller.msg('|/I can\'t find ' + strip_control_sequences(raw_string))
        return 'changeling_contracts'
    elif len(contracts) > 1:
        caller.msg('|/Too many matches found')
        return 'changeling_contracts'
    else:
        contract = contracts[0]
        if contract.meets_prereqs(caller,value=True):
            contract.set(caller,value=True)
            return 'changeling_contracts'
        else:
            caller.msg('|/You don\'t meet the prerequisites for that contract')
            return 'changeling_contracts'
        
def quit(caller, raw_string, **kwargs):
    
    text = {'format' : 'suppress'}
    return text,None

def changeling_finish_cg(caller, raw_string, **kwargs):
    caller.cmdset.add('codes.commands.character_commands.finished_character',permanent=True)
    caller.cmdset.delete('unfinished_character')
    set(caller,'Clarity',statclass='Advantage', value=caller.get('Clarity',subentry='Permanent',statclass='Advantage'))
    set(caller,'Glamour',statclass='Advantage', value=caller.get('Glamour',subentry='Permanent',statclass='Advantage'))
    set(caller,'Willpower',statclass='Advantage', value=caller.get('Willpower',subentry='Permanent',statclass='Advantage'))
    caller.db.finished_cg = time.asctime(time.localtime(time.time()))
    caller.db.xp = { 'earned' : 75,
                     'spent' : 0,
                     'log' : {} }
    text = {'format' : 'suppress'}
    return text,None
