from codes.data import get
from codes.data import set
from codes.data import find
from evennia.utils.utils import strip_control_sequences
from operator import itemgetter
import time

anchors = { 'virtue' : ['Charity', 'Competitive', 'Faith', 'Fortitude', 
                            'Generous', 'Hope', 'Justice', 'Loyal', 'Prudence',
                            'Temperance'],
                'vice' : ['Ambitious', 'Arrogant', 'Competitive', 'Envy',
                          'Gluttony', 'Greed', 'Lust', 'Pride', 'Sloth',
                          'Wrath'] }

def mortal_template(caller, raw_string, **kwargs):
    caller.db.basics['Sphere'] = 'Mortal'
    virtue = get(caller,'Virtue',statclass='Sphere')
    vice = get(caller,'Vice',statclass='Sphere')
    text = 'Virtue: ' 
    if virtue:
        text = text + virtue + '|/'
    else:
        text = text + 'Unset|/'
    text = text + 'Vice: '
    if vice:
        text = text + vice + '|/'
    else:
        text = text + 'Unset|/'
    text = text + '|/Chose what to work on'
    option_list = [
        { 'desc' : 'Virtue',
          'goto' : ('choose_anchor', { 'type' : 'virtue' } ) },
        { 'desc' : 'Vice',
          'goto' : ('choose_anchor', { 'type' : 'vice' } ) } ]
    if virtue and vice:
        option_list.append ( { 'key' : 'P',
                              'desc' : 'Proceed',
                              'goto' : 'mortal_merits' } )
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
    return 'mortal_template'
    
def mortal_merits(caller, raw_string, **kwargs):
    total = 0
    text = 'Merits:|/|/'
    for item in caller.db.merits:
        out = item[0]
        total = total +  item[1]
        if len(item[2]) > 0:
            out = out + ' (' + item[2] + ')'
        out = out + ': ' + str(item[1])
        text = text + out + '|/'
    text = text + '|/Points remaining: ' + str(7 - total)
    option_list = []
    if total < 7:
        option_list.append( {'key' : 'A',
                             'desc' : 'Add a merit',
                             'goto' : ( 'add_merit',
                                        { 'total' : total,
                                         'max' : 7} ) } )
    if total > 0:
        option_list.append( {'key' : 'R',
                             'desc' : 'Remove a merit',
                             'goto' : ('remove_merit',
                                       {'total' : total,
                                        'max' : 7} ) } )
    if total == 7:
        option_list.append( {'key' : 'F',
                             'desc' : 'Finish character generation',
                             'goto' : 'mortal_finish_cg'})
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
        caller.msg('I can\'t find ' + strip_control_sequences(raw_string))
        return 'mortal_merits'
    elif len(merits) > 1:
        caller.msg('Too many matches found')
        return 'mortal_merits'
    else:
        merit = merits[0]
        if len(merit.db.noteRestrictions) == 0:
            return 'get_merit_value', { 'total' : kwargs['total'],
                                   'note' : '',
                                   'merit' : merit,
                                   'max' : kwargs['max']}
        else:
            return 'get_merit_note', {'total' : kwargs['total'],
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
        caller.msg('Invalid note for that merit')
        return 'mortal_merits'
    
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
        caller.msg('Invalid value')
        return 'mortal_merits'
    else:
        value=int(strip_control_sequences(raw_string)) 
        if value < 1:
            caller.msg('Invalid value')
            return 'mortal_merits'
        elif value + kwargs['total'] - kwargs['merit'].get(caller,
                                    subentry=kwargs['note']) >  kwargs['max']:
            caller.msg('You don\'t have enough points')
            return 'mortal_merits'
        elif kwargs['merit'].meets_prereqs(caller,value=value,
                                           subentry=kwargs['note']):
            kwargs['merit'].set(caller,value=value,subentry=kwargs['note'])
            return 'mortal_merits'
        else:
            caller.msg('You don\'t meet the prerequisites for that merit')
            return 'mortal_merits'

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
        caller.msg('You can\'t remove your court mantle')
    else:
        set(caller, kwargs['entry'], subentry=kwargs['subentry'], value=0)
    return 'mortal_merits'
    
def quit(caller, raw_string, **kwargs):
    
    text = {'format' : 'suppress'}
    return text,None

def mortal_finish_cg(caller, raw_string, **kwargs):
    caller.cmdset.add('codes.character_commands.finished_character', 
                      permanent=True)
    caller.cmdset.delete('codes.character_commands.unfinished_character')
    set(caller,'Integrity',statclass='Advantage', value=7)
    caller.db.finished_cg = time.asctime(time.localtime(time.time()))
    caller.db.xp = { 'earned' : 75,
                     'spent' : 0,
                     'log' : {} }
    return None

