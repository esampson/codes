from evennia.utils.utils import strip_control_sequences
from evennia.utils.search import search_script_tag
from codes.data import find

import time
import stat

def start(caller):
    if caller.db.finished_cg:    
        text = ("You currently have " + str(caller.db.xp['earned'] - 
                                caller.db.xp['spent']) + ' available')
        options = ( 
            { 'desc' : 'XP Log                                        ',
             'goto' : _xp_log },
            { 'desc' : 'Spend XP                                        ',
             'goto' : 'xp_spend' },
            { 'key' : 'Q',
             'desc' : 'Quit                                        ',
             'goto' : 'xp_exit' } )
        
        return text, options
    else:
        caller.msg('You have not yet completed CG')
        return None

def _xp_log(caller, raw_string, **kwargs):
    xp_list=list(caller.db.xp['log'].keys())
    xp_list.sort()
    reply = '-------------------------|/'
    reply = reply + '     XP Log|/-------------------------|/'
    for item in xp_list:
        data = caller.db.xp['log'][item]
        reply = (reply + time.asctime(time.localtime(item)) + ': '+data[1] + 
                 ' for ' + str(data[0]) + ' XP.|/')
    caller.msg(reply)
    return 'start'
        
def xp_spend(caller, raw_string, **kwargs):
    text = 'What do you want to buy:'
    option_list = []
    option_list.append( { 'desc' : 'Increase Attribute',
                          'goto' : ('xp_buy_flat_stat',
                                    {'type' : 'Attribute' } ) } )
    option_list.append( { 'desc' : 'Increase Skill',
                          'goto' : ('xp_buy_flat_stat',
                                    {'type' : 'Skill' } ) } )
    option_list.append( { 'desc' : 'Buy Specialty',
                          'goto' : 'xp_buy_specialty' } )
    option_list.append( { 'desc' : 'Buy or Increase Merit',
                          'goto' : 'xp_buy_merit' } )
    if caller.template().lower() == 'changeling':
        option_list.append ( { 'desc' : 'Increase Wyrd', 
                               'goto' : ( _xp_buy_power, 
                                          { 'power' : 'Wyrd' } ) } )
        option_list.append ( { 'desc' : 'Buy Contract or Seeming Blessing',
                               'goto' : 'xp_buy_contract' } )
    option_list.append ( { 'key' : 'Q',
                           'desc' : 'Quit',
                           'goto' : 'xp_exit' } )
    options = tuple(option_list)
    return text,options

def xp_buy_contract(caller, raw_string, **kwargs):
    text = 'Contract:'
    options = ( {'key' : '_default',
                 'goto' :  _xp_check_contract } )
    return text,options

def _xp_check_contract(caller, raw_string, **kwargs):
    contracts = find(strip_control_sequences(raw_string), statclass='Contract')
    if len(contracts) < 1:
        caller.msg('I can\'t find ' + strip_control_sequences(raw_string))
        return 'xp_spend'
    elif len(contracts) > 1:
        caller.msg('Too many matches found')
        return 'xp_spend'
    elif contracts[0].db.group.lower() == 'regalia':
        contract = contracts[0]
        return 'xp_get_contract_note', { 'stat' : contract }
    else:
        contract = contracts[0]
        current = caller.db.xp['earned'] - caller.db.xp['spent']
        cost = contract.cost(caller, subentry='', value=True)
        name = contract.db.longname
        if cost < 1:
            return 'xp_spend'
        elif cost > current:
            caller.msg('You don\'t have enough XP')
            return 'xp_spend'
        elif contract.meets_prereqs(caller,value=True,subentry=''):
                return 'xp_increase', { 'type' : 'contract',
                                       'stat' : contract,
                                       'name' : name,
                                       'value' : True,
                                       'subentry' : '',
                                       'cost' : cost  }
        else:
            caller.msg('You don\'t meet the prerequisites for that contract')
            return 'xp_spend'
    
def xp_get_contract_note(caller, raw_string, **kwargs):
    text = 'Select any additional Seeming Blessings:'
    contract_list = list(caller.db.contracts.keys())
    if kwargs['stat'].db.longname in contract_list:
        blessings = caller.db.contracts[kwargs['stat'].db.longname]
        blessings_list = blessings.split(',')
        if len(blessings) > 0:
            append = blessings + ', '
        else:
            append = ''
    else:
        blessings_list = []
        append = ''
    option_list = []
    character_seeming = caller.get('Seeming',statclass='Sphere')
    seemings = search_script_tag('seeming_stat')
    for item in seemings:
        if item.db.longname != character_seeming and item.db.longname not in blessings_list:
            option_list.append( { 'desc' : item.db.longname,
                                  'goto' : (_xp_check_contract_value,
                                            {'stat' : kwargs['stat'],
                                             'subentry' : append + item.db.longname,
                                             'type' : 'contract' } ) } )
    option_list.append( { 'key' : 'N',
                          'desc' : 'None',
                          'goto' : (_xp_check_contract_value,
                                    {'stat' : kwargs['stat'],
                                     'subentry' : '',
                                     'type' : 'contract' } ) } )
    options = tuple(option_list)
    return text, options

def _xp_check_contract_value(caller, raw_string, **kwargs):
    current = caller.db.xp['earned'] - caller.db.xp['spent']
    cost = kwargs['stat'].cost(caller, subentry=kwargs['subentry'], value=True)
    name = kwargs['stat'].db.longname
    if kwargs['subentry'] != '':
        name = name + ' (' + kwargs['subentry'] + ')'
    if cost < 1:
        return 'xp_spend'
    elif cost > current:
        caller.msg('You don\'t have enough XP')
        return 'xp_spend'
    elif kwargs['stat'].meets_prereqs(caller,value=True,
                                      subentry=kwargs['subentry']):
            return 'xp_increase', { 'type' : 'contract',
                                   'stat' : kwargs['stat'],
                                   'name' : name,
                                   'value' : True,
                                   'subentry' : kwargs['subentry'],
                                   'cost' : cost  }
    else:
        caller.msg('You don\'t meet the prerequisites for that contract')
        return 'xp_spend'

def _xp_check_merit_note(caller, raw_string, **kwargs):
    merit = kwargs['stat']
    if merit.db.noteRestrictions[0] == '*':
        return 'xp_get_merit_value', { 'subentry' : 
                                          strip_control_sequences(raw_string),
                                       'stat' : merit }
    
def _xp_buy_power(caller, raw_string, **kwargs):
    if caller.db.xp['earned'] - caller.db.xp['spent'] < 5:
        caller.msg('Not enough XP')
        return 'xp_spend'
    else:
        stats = find(kwargs['power'], statclass='Power')
        stat = stats[0]
        value = stat.get(caller,subentry='') + 1
        send_kwargs={ 'type' : 'power',
                                    'stat' : stat,
                                    'name' : kwargs['power'],
                                    'value' : value,
                                    'subentry' : '',
                                    'cost' : 5 }
        if stat.db.longname == 'Wyrd' and value in [2, 4, 8]:
            send_kwargs['message'] = 'You must add a minor frailty'
            return 'xp_add_frailty', send_kwargs
        elif stat.db.longname == 'Wyrd' and value in [6, 10]:
            send_kwargs['message'] = 'You must add a major frailty'
            return 'xp_add_frailty', send_kwargs
        else:
            return 'xp_increase', send_kwargs

def xp_add_frailty(caller, raw_string, **kwargs):
    send_kwargs=kwargs
    send_kwargs['special']='frailty'
    text = kwargs['message']
    options = ( {'key' : '_default',
                 'goto' : ( _xp_check_known_stat, kwargs) } )
    return text,options
    
def xp_buy_flat_stat(caller, raw_string, **kwargs):
    text = kwargs['type'] + ':'
    options = ( {'key' : '_default',
                 'goto' :  ( _xp_check_order,
                             { 'type' : kwargs['type'],
                               'subentry' : '' } ) } )
    return text,options
    
def _xp_check_order(caller, raw_string, **kwargs):
    stats = find(strip_control_sequences(raw_string), statclass=kwargs['type'])
    if len(stats) < 1:
        caller.msg('I can\'t find ' + strip_control_sequences(raw_string))
        return 'xp_spend'
    elif len(stats) > 1:
        caller.msg('Too many matches found')
        return 'xp_spend'
    else:
        stat = stats[0]
        value = stat.get(caller, subentry=kwargs['subentry']) + 1
        cost = stat.cost(caller, subentry=kwargs['subentry'], value=value)
        current = caller.db.xp['earned'] - caller.db.xp['spent']
        if cost > current:
            caller.msg('You do not have enough XP')
            return 'xp_spend'
        else:
            if stat.meets_prereqs(caller, 
                                  subentry=kwargs['subentry'], value=value):
                name = stat.db.longname
                if kwargs['subentry'] != '':
                    name = name + ' ('+kwargs['subentry']+ ')'
                send_kwargs = kwargs
                send_kwargs['stat'] = stat
                send_kwargs['name'] = name
                send_kwargs['value'] = value
                send_kwargs['cost'] = cost
                return 'xp_increase', send_kwargs
            else:
                message = 'You do not meet the '
                message = message + 'prerequisites to purchase that.|/'
                caller.msg(message)
                return 'xp_spend'

def _xp_check_known_stat(caller, raw_string, **kwargs):
    stat = kwargs['stat']
    value = stat.get(caller, subentry=kwargs['subentry']) + 1
    cost = stat.cost(caller, subentry=kwargs['subentry'], value=value)
    current = caller.db.xp['earned'] - caller.db.xp['spent']
    if cost > current:
        caller.msg('You do not have enough XP')
        return 'xp_spend'
    else:
        if stat.meets_prereqs(caller, 
                              subentry=kwargs['subentry'], value=value):
            name = stat.db.longname
            if kwargs['subentry'] != '':
                name = name + ' ('+kwargs['subentry']+ ')'
            send_kwargs = kwargs
            send_kwargs['stat'] = stat
            send_kwargs['name'] = name
            send_kwargs['value'] = value
            send_kwargs['cost'] = cost
            if kwargs['special'] == 'frailty':
                kwargs['frailty'] = strip_control_sequences(raw_string)
            return 'xp_increase', send_kwargs
        else:
            message = 'You do not meet the '
            message = message + 'prerequisites to purchase that.|/'
            caller.msg(message)
            return 'xp_spend'
            
def xp_increase(caller, raw_string, **kwargs):
    text = 'Buy ' + kwargs['name']
    if kwargs['type'] not in ['specialty', 'contract']:
        text = text + ': ' + str(kwargs['value'])
    text = text + ' for ' + str(kwargs['cost']) + ' XP?'
    if 'special' in kwargs:
        if kwargs['message'] == 'You must add a minor frailty':
            text = (text + '|/( You will gain the minor frailty of ' + 
                    kwargs['frailty'] +')')
        elif kwargs['message'] == 'You must add a major frailty':
            text = (text + '|/( You will gain the major frailty of ' + 
                    kwargs['frailty'] +')')
    '|/|/Confirm:'
    options = ( 
        { 'key' : 'Y',
          'desc' : 'Yes',
          'goto' : ( _xp_purchase, kwargs ) },
        { 'key' : 'N',
          'desc' : 'No',
          'goto' : 'xp_spend' },
        { 'key' : 'Q',
         'desc' : 'Quit',
         'goto' : 'xp_exit' } )
    return text,options

def xp_buy_merit(caller, raw_string, **kwargs):
    text = 'Merit:'
    options = ( {'key' : '_default',
                 'goto' :  _xp_check_merit } )
    return text,options
    
def _xp_check_merit(caller, raw_string, **kwargs):
    merits = find(strip_control_sequences(raw_string), statclass='Merit')
    if len(merits) < 1:
        caller.msg('I can\'t find ' + strip_control_sequences(raw_string))
        return 'xp_spend'
    elif len(merits) > 1:
        caller.msg('Too many matches found')
        return 'xp_spend'
    else:
        merit = merits[0]
        if merit.db.cg_only:
            caller.msg(merit.db.longname + ' is only available in CG.')
            return 'xp_spend'
        elif merit.db.restricted:
            caller.msg(merit.db.longname + 'is restricted.')
            return 'xp_spend'
        else:
            if len(merit.db.noteRestrictions) == 0:
                return 'xp_get_merit_value', { 'subentry' : '',
                                            'stat' : merit }
            else:
                return 'xp_get_merit_note', { 'stat' : merit }
        
def xp_get_merit_note(caller, raw_string, **kwargs):
    text = 'This merit requires some form of note such as who the contacts '
    text = text + 'are or what the area of expertise is in:'
    options = ( {'key' : '_default',
                 'goto' : ( _xp_check_merit_note, 
                            { 'stat' : kwargs['stat'] } ) } )
    return text, options

def _xp_check_merit_note(caller, raw_string, **kwargs):
    merit = kwargs['stat']
    if merit.db.noteRestrictions[0] == '*':
        return 'xp_get_merit_value', { 'subentry' : 
                                       strip_control_sequences(raw_string),
                                       'stat' : merit }
    elif strip_control_sequences(raw_string) in merit.db.noteRestrictions:
        return 'xp_get_merit_value', { 'subentry' : 
                                       strip_control_sequences(raw_string),
                                       'stat' : merit }
    else:
        caller.msg('Invalid note for that merit')
        return 'xp_spend'
    
def xp_get_merit_value(caller, raw_string, **kwargs):
    text = 'Enter value:'
    options = ( {'key' : '_default',
                 'goto' : ( _xp_check_merit_value, 
                            { 'stat' : kwargs['stat'],
                             'subentry' : kwargs['subentry'] } ) } )
    return text,options

def _xp_check_merit_value(caller, raw_string, **kwargs):
    if not strip_control_sequences(raw_string).isnumeric():
        caller.msg('Invalid value')
        return 'xp_spend'
    else:
        current = caller.db.xp['earned'] - caller.db.xp['spent']
        value=int(strip_control_sequences(raw_string))
        cost = kwargs['stat'].cost(caller, 
                                   subentry=kwargs['subentry'], value=value)
        name = kwargs['stat'].db.longname
        if kwargs['subentry'] != '':
            name = name + ' (' + kwargs['subentry'] + ')'
        if cost < 1:
            caller.msg('Invalid value')
            return 'xp_spend'
        elif cost > current:
            caller.msg('You don\'t have enough XP')
            return 'xp_spend'
        elif kwargs['stat'].meets_prereqs(caller,value=value,
                                          subentry=kwargs['subentry']):
            return 'xp_increase', { 'type' : 'Merit',
                                   'stat' : kwargs['stat'],
                                   'name' : name,
                                   'value' : value,
                                   'subentry' : kwargs['subentry'],
                                   'cost' : cost  }
        else:
            caller.msg('You don\'t meet the prerequisites for that merit')
            return 'xp_spend'
        
def _xp_purchase(caller, raw_string, **kwargs):
    message = 'Purchasing ' + kwargs['name']
    if kwargs['type'] not in ['specialty', 'contract']:
        message = message + ': ' + str(kwargs['value']) 
    message = message + ' for ' +str(kwargs['cost']) + ' XP.'
    caller.msg(message)
    log = kwargs['name']
    if not(kwargs['type'] in ['specialty','contract']):
        log = log + ': ' +str(kwargs['value'] ) 
    caller.db.xp['log'][time.time()] = [kwargs['cost'],log ]
    caller.db.xp['spent'] = caller.db.xp['spent'] + kwargs['cost']
    if kwargs['type'] == 'specialty':
        caller.db.specialties.append(kwargs['name'])
    else:
        kwargs['stat'].set(caller,subentry=kwargs['subentry'],
                           value=kwargs['value'])
        
    if 'frailty' in kwargs:
        f = find('Frailties',statclass='Sphere')[0]
        current_frailties = f.get(caller,subentry='')
        if current_frailties == False:
            current_frailties = []
        current_frailties.append(kwargs['frailty'])
        f.set(caller,current_frailties)
        
    return 'start'

def xp_buy_specialty(caller, raw_string, **kwargs):
    text = 'Enter the skill the specialty will be in:'
    options = ( {'key' : '_default',
                 'goto' : 'xp_check_skill' } )
    return text, options

def xp_check_skill(caller, raw_string, **kwargs):
    skills = find(strip_control_sequences(raw_string), statclass='Skill')
    if len(skills) < 1:
        caller.msg('I can\'t find ' + strip_control_sequences(raw_string))
        return 'xp_spend'
    elif len(skills) > 1:
        caller.msg('Too many matches found')
        return 'xp_spend'
    elif caller.get(skills[0].db.longname,statclass='Skill') == 0:
        caller.msg('You need at least 1 point in that skill')
        return 'xp_spend'
    else:
        skill = skills[0]
        text = 'Enter specialty:'
        options = ( {'key' : '_default',
                 'goto' : ( _xp_check_specialties, 
                            { 'stat' : skill } ) } )
        return text,options
    
def _xp_check_specialties(caller, raw_string, **kwargs):
    name = (kwargs['stat'].db.longname + ': ' + 
            strip_control_sequences(raw_string))
    current = caller.db.xp['earned'] - caller.db.xp['spent']
    if name in caller.db.specialties:
        caller.msg('You already possess that specialty')
        return "xp_spend"
    elif current < 1:
        caller.msg('You don\'t have enough XP')
        return "xp_spend"
    else:
        return 'xp_increase', { 'type' : 'specialty',
                                'stat' : kwargs['stat'],
                                'name' : name,
                                'value' : True,
                                'subentry' : '',
                                'cost' : 1 }
    
def xp_exit(caller, raw_string, **kwargs):
    caller.msg('Exitting')
    return None
    
def xp_quit(caller, raw_string, **kwargs):
    return None
                        