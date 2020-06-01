from codes.data import get
from codes.data import set
from codes.data import find

from codes.menus.menu_types import ExMenu

from evennia.utils.utils import strip_control_sequences

import time

anchors = { 'virtue' : ['Charity', 'Competitive', 'Faith', 'Fortitude',
                            'Generous', 'Hope', 'Justice', 'Loyal', 'Prudence',
                            'Temperance'],
                'vice' : ['Ambitious', 'Arrogant', 'Competitive', 'Envy',
                          'Gluttony', 'Greed', 'Lust', 'Pride', 'Sloth',
                          'Wrath'] }


# noinspection DuplicatedCode
def mortal_template(caller, raw_string, **kwargs):
    caller.db.cg['start_menu'] = 'cg_mortal'
    caller.db.cg['start_node'] = 'mortal_template'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    caller.db.basics = { 'Sphere' : 'Mortals' }
    caller.db.power = {}
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
            'All Chronicles of Darkness characters have defining personality ' +
            'traits. These traits not only tell a character who she is, but ' +
            'also allow her to regain Willpower (for more information on ' +
            'spending and regaining Willpower, see Chapter 2). These traits '+
            'are called Anchors. For a mortal character, these Anchors are ' +
            'her Virtue and her Vice.' + '|/' + '_' * 79)
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
    caller.db.power = {}
    caller.db.sphere = {}
    ExMenu(caller, 'codes.menus.cg', startnode='assign_template',
           cmdset_mergetype='Union', cmd_on_exit=None, auto_quit=False)
    text = {'format': 'suppress'}
    return text, None


# noinspection DuplicatedCode
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


# noinspection DuplicatedCode,DuplicatedCode
def mortal_merits(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'mortal_merits'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
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
                      'move_keys': ['B', 'F'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _return_to_anchors(caller, raw_string, **kwargs):
    caller.db.merits = []
    return 'mortal_template'


# noinspection DuplicatedCode
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


# noinspection DuplicatedCode
def _check_merit(caller, raw_string, **kwargs):
    merits = find(strip_control_sequences(raw_string), statclass='Merit')
    if len(merits) < 1:
        caller.msg('|/I can\'t find ' + strip_control_sequences(raw_string))
        return 'mortal_merits'
    elif len(merits) > 1:
        caller.msg('|/Too many matches found')
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


# noinspection DuplicatedCode
def get_merit_note(caller, raw_string, **kwargs):
    text = 'This merit requires some form of note such as who the contacts '
    text = text + 'are or what the area of expertise is in:'
    option_list = [ {'key' : '_default',
                 'goto' : ( _check_merit_note,
                            { 'total' : kwargs['total'],
                             'merit' : kwargs['merit'],
                             'max' : kwargs['max'] } ) } ]
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
        return 'mortal_merits'


# noinspection DuplicatedCode
def get_merit_value(caller, raw_string, **kwargs):
    text = 'Enter value:'
    option_list = [ {'key' : '_default',
                 'goto' : ( _check_merit_value,
                            { 'total' : kwargs['total'],
                             'note' : kwargs['note'],
                             'merit' : kwargs['merit'],
                             'max' : kwargs['max'] } ) } ]
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
        return 'mortal_merits'
    else:
        value=int(strip_control_sequences(raw_string))
        if value < 1:
            caller.msg('|/Invalid value')
            return 'mortal_merits'
        elif value + kwargs['total'] - kwargs['merit'].get(caller,
                                    subentry=kwargs['note']) >  kwargs['max']:
            caller.msg('|/You don\'t have enough points')
            return 'mortal_merits'
        elif kwargs['merit'].meets_prereqs(caller,value=value,
                                           subentry=kwargs['note']):
            kwargs['merit'].set(caller,value=value,subentry=kwargs['note'])
            return 'mortal_merits'
        else:
            caller.msg('|/You don\'t meet the prerequisites for that merit')
            return 'mortal_merits'


# noinspection DuplicatedCode
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
    return 'mortal_merits'

def quit_menu(caller, raw_string, **kwargs):
    obj_menu = 'codes.commands.character_menus.CharacterInMenu'
    act_menu = 'codes.commands.character_menus.AccountInMenu'
    caller.cmdset.delete(obj_menu)
    caller.account.cmdset.delete(act_menu)
    caller.execute_cmd('look')
    text = {'format': 'suppress'}
    return text, None


# noinspection DuplicatedCode
def mortal_finish_cg(caller, raw_string, **kwargs):
    obj_menu = 'codes.commands.character_menus.CharacterInMenu'
    act_menu = 'codes.commands.character_menus.AccountInMenu'
    caller.cmdset.delete(obj_menu)
    caller.account.cmdset.delete(act_menu)
    del caller.db.cg
    caller.cmdset.add(
        'codes.commands.character_commands.FinishedCharacter',
                      permanent=True)
    caller.cmdset.delete('UnfinishedCharacter')
    set(caller,'Integrity',statclass='Advantage', value=7)
    set(caller,'Willpower',statclass='Advantage',
        value=caller.get('Willpower',subentry='Permanent',
                         statclass='Advantage'))
    caller.db.finished_cg = time.asctime(time.localtime(time.time()))
    caller.db.xp = { 'earned' : 75,
                     'spent' : 0,
                     'log' : {} }
    caller.execute_cmd('look')
    text = {'format': 'suppress'}
    return text, None

