from codes.data import get
from codes.data import set
from codes.data import find
from evennia.utils.utils import strip_control_sequences
from evennia.utils.search import search_script_tag
from operator import itemgetter

from codes.menus.menu_types import ExMenu

import time


# noinspection DuplicatedCode
def mage_template(caller, raw_string, **kwargs):
    caller.db.cg['start_menu'] = 'cg_mage'
    caller.db.cg['start_node'] = 'mage_template'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    caller.db.basics = { 'Sphere' : 'Mage' }
    caller.db.power = { 'Gnosis' : 1 }
    caller.db.sphere = {'Obsessions':[]}
    caller.db.arcana = {}
    caller.db.rotes = {}
    caller.db.praxes = {}

    text = 'Select Path:'
    option_list = []
    path_list = search_script_tag('path_stat')
    paths=[]
    for item in path_list:
        if item.db.restricted == False:
            paths.append([item.db.longname,item])
    paths = sorted(paths,key=itemgetter(0))
    for item in paths:
        option_list.append( {'desc' : item[0],
                             'goto' : ( _mage_set_path,
                                        { 'path' : item[1] } ) } )
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
            'Theoretical models of the cosmos give infinite numbers of ' +
            'Supernal Realms, hidden deep beyond the Supernal World revealed' +
            'through Mage Sight. Other, rival, theories state that there is ' +
            'only one Supernal Realm, and that all seeming division is ' +
            'imposed on magic by mortal minds. Despite the debates, for all ' +
            'intents and purposes mages count five different facets or Paths ' +
            'of the Supernal World: five ways to see through the Lie, five ' +
            'ways to achieve magic, five kinds of mages.' + '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options


# noinspection DuplicatedCode
def return_to_main_cg(caller, raw_string, **kwargs):
    caller.db.basics = {}
    caller.db.sphere = {}
    del caller.db.power
    del caller.db.arcana
    del caller.db.rotes
    del caller.db.praxes
    ExMenu(caller, 'codes.menus.cg', startnode='assign_template',
           cmdset_mergetype='Union', cmd_on_exit=None, auto_quit=False)
    text = {'format': 'suppress'}
    return text, None

def _mage_set_path(caller, raw_string, **kwargs):
    path = kwargs['path']
    caller.db.sphere['Path'] = path.db.longname
    return "mage_order"

def mage_order(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'mage_order'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
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
    option_list.append ( {'desc' : 'Nameless',
                          'goto' : _set_nameless } )
    option_list.append({'desc': 'Back',
                        'key': 'B',
                        'goto': 'mage_template'})
    option_list.append({'desc': 'Back',
                        'key': 'back',
                        'goto': 'mage_template'})
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 79 + '|/|/' +
            'Although smaller, isolated groups of mages cling on in some ' +
            'parts of the world, catering to regional interests or ' +
            'unwholesome practices other mages frown upon, the global ' +
            'society of magic is largely divided among six great Orders. ' +
            'Each Order is made up of thousands of smaller organizations ' +
            'with attached mystery cults, secret societies, and associations ' +
            'that give them an occult "footprint" in the Fallen World. ' +
            'Although most Sleeper occultists wouldn\'t know them by name, ' +
            'those "in the know" are aware that the Orders exist even if ' +
            'only by rumor and inference.' + '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _set_order(caller, raw_string, **kwargs):
    order = kwargs['order']
    caller.db.sphere['Order'] = order.db.longname
    set(caller,'Status',value=1,subentry=order.db.longname,statclass='Merit')
    set(caller, 'Language', value=1, subentry='High Speech', statclass='Merit')
    current_occult = caller.get('Occult', statclass='Skill')
    caller.db.cg['starting_occult'] = current_occult
    if current_occult < 5:
        set(caller, 'Occult', value=current_occult + 1, statclass='Skill')
    return "mage_stat"

def _set_nameless(caller, raw_string, **kwargs):
    caller.db.sphere['Order'] = 'Nameless'
    current_occult = caller.get('Occult', statclass='Skill')
    caller.db.cg['starting_occult'] = current_occult
    return "mage_stat"


# noinspection DuplicatedCode
def mage_stat(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'mage_stat'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    text = 'Select one attribute to boost:'
    option_list = []
    for attribute in ['Composure', 'Resolve', 'Stamina']:
        option_list.append({'desc': attribute,
                            'goto': (_raise_stat,
                                     {'stat': attribute.lower()})})
    option_list.append({'desc': 'Back',
                        'key': 'B',
                        'goto': _return_to_order})
    option_list.append({'desc': 'Back',
                        'key': 'back',
                        'goto': _return_to_order})
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 79 + '|/|/' +
            'The Awakening is tough on the mind, body, and soul. Every ' +
            'Awakened character begins play with one additional dot of ' +
            'Composure, Resolve, or Stamina, which may not raise the ' +
            'Attribute chosen above five dots.' + '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _return_to_order(caller, raw_string, **kwargs):
    caller.db.merits = []
    set(caller, 'Occult', value=caller.db.cg['starting_occult'],
        statclass='Skill')
    return 'mage_order'


def _raise_stat(caller, raw_string, **kwargs):
    start_value = caller.get(kwargs['stat'], statclass='Attribute')
    if start_value == 5:
        caller.msg('|/Can\'t boost a stat to over 5')
        return ('mage_stat', kwargs)
    else:
        set(caller, kwargs['stat'], statclass='Attribute',
            value=start_value + 1)
        caller.db.cg['stat_boost'] = {'stat': kwargs['stat'],
                                      'start': start_value}
    return 'mage_obsession'


# noinspection DuplicatedCode
def mage_obsession(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'mage_stat'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    text = 'Choose an obsession:'
    option_list = [ {'key' : '_default',
                 'goto' : _mage_set_obsession } ]
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
            'Obsessions are just like long-term Aspirations, except they ' +
            'relate specifically to a mage\'s compulsion to explore the ' +
            'mystical in her life. They could be goals to learn or research ' +
            'specific things. They could be player goals for the character ' +
            'to encounter certain strangeness in the world. They could be ' +
            'goals to use magic in new or extreme ways.' + '|/' + '_' * 79)
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
    return 'mage_stat',{'seeming': find(caller.get('Seeming',
                                                         statclass='Sphere'),
                                              statclass='Seeming')[0]}

def _mage_set_obsession(caller, raw_string, **kwargs):
    f = find('Obsessions',statclass='Sphere')[0]
    f.set(caller,[str(strip_control_sequences(raw_string))])
    return 'mage_arcana'


# noinspection DuplicatedCode
def mage_arcana(caller,raw_string,**kwargs):
    caller.db.cg['start_node'] = 'mage_arcana'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
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
    one_three = True
    no_three = True
    for item in list(caller.db.arcana.keys()):
        if caller.get(item,statclass='Arcana') == 3:
            if no_three:
                no_three = False
            else:
                one_three = False

    # Three to five dots in ruling arcana?
    three_to_five = True
    ruling_total = 0
    for item in ruling_arcana:
        ruling_total = ruling_total + caller.get(item,statclass='Arcana')
    if ruling_total < 3 or ruling_total > 5:
        three_to_five = False

    # Both ruling arcana have at least one dot?
    both_arcana = True
    for item in ruling_arcana:
       if caller.get(item,statclass='Arcana') < 1:
           both_arcana = False

    text = ('Arcana:|/|/Required: 6 total. Only one at 3. 3 to 5 points in ' +
            'Ruling Arcana. At least 1 point in each Ruling Arcana')
    text = text + '|/|/|_|_|_|_Ruling Arcana:|/'
    for item in ruling_arcana:
        text = (text + '|_|_|_|_|_|_|_|_' + item + ': ' +
               str(caller.get(item,statclass='Arcana')) + '|/')
    text = text + '|/'
    if len(remaining_arcana) > 0:
        text = text + '|_|_|_|_Other Arcana:|/'
        for item in remaining_arcana:
            text = (text + '|_|_|_|_|_|_|_|_' + item + ': ' +
                    str(caller.get(item, statclass='Arcana')) + '|/')
        text = text + '|/'

    arcana_list = search_script_tag('arcana_stat')
    arcana = []
    for item in arcana_list:
        if item.db.restricted == False and item.db.longname != inferior_arcana:
            arcana.append([item.db.longname, item])
    arcana = sorted(arcana, key=itemgetter(0))
    option_list = []
    for item in arcana:
        option_list.append({'desc': item[0],'goto': ('get_arcana_value',
                                                     {'stat': item[1]})})

    if spent_all and one_three and three_to_five and both_arcana:
        option_list.append( { 'key' : 'P',
                              'desc' : 'Proceed',
                              'goto' : 'mage_rotes' } )

    option_list.append({'desc': 'Back',
                        'key': 'B',
                        'goto': _return_to_obsession})
    option_list.append({'desc': 'Back',
                        'key': 'back',
                        'goto': _return_to_obsession})
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 79 + '|/|/' +
            'The ten elemental principles through which mages understand the ' +
            'Tapestry. A mage\'s Arcanum lore is the mechanism by which she ' +
            'draws down the laws of a Supernal Realm. Her Gnosis provides ' +
            'her connection to that Realm.' + '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P'],
                      'rows': 3}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _return_to_obsession(caller, raw_string, **kwargs):
    caller.db.sphere['Obsession'] = []
    return 'mage_obsession'

def get_arcana_value(caller, raw_string, **kwargs):
    text = 'Enter value:'
    option_list = [ {'key' : '_default',
                 'goto' : ( _check_stat_value,
                            { 'stat' : kwargs['stat'] } ) } ]
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 29 + '|/|/Enter a value between 1 and 3' + '|/' +
            '_' * 29)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'F'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

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


# noinspection DuplicatedCode
def mage_rotes(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'mage_rotes'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    text = 'Rotes:|/|/Choose three rotes|/'
    for item in list(caller.db.rotes.keys()):
        text = text + '|_|_|_|_' + item + '|/'
    text = text + '|/'

    option_list = []
    if len(caller.db.rotes) < 3:
        option_list.append({'key': 'A',
                            'desc': 'Add a rote',
                            'goto': 'mage_add_rote'})
    if len(caller.db.rotes) > 1:
        option_list.append( { 'key' : 'R',
                              'desc' : 'Remove a rote',
                              'goto' : 'mage_remove_rote' } )
    if len(caller.db.rotes)  == 3:
        option_list.append( { 'key' : 'P',
                              'desc' : 'Proceed',
                               'goto' : 'mage_merits' } )
    option_list.append({'desc': 'Back',
                        'key': 'B',
                        'goto': _return_to_arcana})
    option_list.append({'desc': 'Back',
                        'key': 'back',
                        'goto': _return_to_arcana})
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 79 + '|/|/' +
            'Experienced mages perfect their grasp of spell Imagos over ' +
            'time, learning the complexity of the spell and developing ' +
            'skills to recall and cast it with ease. Masters call these ' +
            'specialized Imagos Rotes, codifying and recording their methods ' +
            'to later teach less experienced mages. Orders teach Rotes to ' +
            'their members using a set of mnemonic techniques - mudras - to ' +
            'compress, memorize, recall, and cast the spell as quickly and ' +
            'efficiently as improvised spells.' + '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P'],
                      'rows': 4}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _return_to_arcana(caller, raw_string, **kwargs):
    caller.db.rotes = {}
    return 'mage_arcane'

def mage_remove_rote(caller, raw_string, **kwargs):
    text = 'Select rote to remove:'
    option_list = []
    if caller.db.rotes:
        rotes = list(caller.db.rotes.keys())
    else:
        rotes = []
    rotes.sort()
    for item in rotes:
        option_list.append( { 'desc' : item,
                              'goto' : ( _remove_rote,
                                       { 'rote' : item } ) } )
    options = tuple(option_list)
    return text,options

def _remove_rote(caller, raw_string, **kwargs):
    set(caller,kwargs['rote'],value=False, statclass='Rote')
    return 'mage_rotes'


# noinspection DuplicatedCode
def mage_add_rote(caller, raw_string, **kwargs):
    text = 'Enter name of spell:'
    option_list = [ {'key' : '_default',
                 'goto' : _check_rote } ]
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 79 + '|/|/' +
            'Because rotes apply to specific spells you will need to state ' +
            'the name of an approved spell which the rote is for. Approved ' +
            'spells can be found at either http://13.52.78.93/spells/list/ ' +
            'or by typing |w+list spell|n. (Warning: The list is very long.)' +
            '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P'],
                      'rows': 4}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _check_rote(caller, raw_string, **kwargs):
    stat = find(strip_control_sequences(raw_string),statclass='Spell')
    if len(stat) < 1:
        caller.msg('|/I can\'t find ' + strip_control_sequences(raw_string))
        return 'mage_rotes'
    elif len(stat) > 1:
        caller.msg('|/Too many matches found')
        return 'mage_rotes'
    else:
        stat = stat[0]
        if stat.db.restricted == True:
            caller.msg('|/That ' + stat.type() + ' is restricted')
            return 'mage_rotes'
        elif stat.meets_prereqs(caller) == False:
            caller.msg('|/You aren\'t able to cast ' + stat.db.longname)
        else:
            set(caller, stat.db.longname, value=True, statclass='rote')
            return 'mage_rotes'


# noinspection DuplicatedCode,DuplicatedCode
def mage_merits(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'mage_merits'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    if caller.get('Order',statclass='Sphere') == 'Nameless':
        max = 10
    else:
        max = 12
    total = 0
    text = 'Gnosis: ' + str(caller.db.power['Gnosis'])
    text = text + '|/|_|_Merits:|/'
    removable_merits = []
    for item in caller.db.merits:
        out = item[0]
        total = total + item[1]
        if len(item[2]) > 0:
            out = out + ' (' + item[2] + ')'
        out = out + ': ' + str(item[1])
        text = text + '|_|_|_|_' + out + '|/'
        removable = True
        if caller.get('Order', statclass='Sphere') != 'Nameless':
            if item[0] == 'Language' and item[2] == 'High Speech':
                removable = False
            elif (item[0] == 'Status' and
                  item[2] == caller.get('Order',statclass='Sphere')):
                removable = False
        if removable:
            removable_merits.append(item)
    total = total + (caller.get('Gnosis',statclass='Power') - 1) * 5
    text = text + '|/Points remaining: ' + str(max - total)
    option_list = []
    if total < max:
        option_list.append( {'desc' : 'Add a merit',
                             'goto' : ( 'add_merit',
                                        { 'total' : total,
                                         'max' : max} ) } )
    if max - total > 4:
        option_list.append ( {'desc' : 'Increase Gnosis',
                              'goto' : _increase_power } )
    if get(caller,'Gnosis',statclass='Power') > 1:
        option_list.append ( {'desc' : 'Decrease Gnosis',
                              'goto' : _decrease_power } )
    if len(removable_merits) > 0:
        option_list.append( {'desc' : 'Remove a merit',
                             'goto' : ('remove_merit',
                                       {'total' : total,
                                        'max' : max,
                                        'removable' : removable_merits} ) } )
    if total == max:
        option_list.append( {'key' : 'P',
                             'desc' : 'Proceed',
                             'goto' : 'mage_praxes'})
    option_list.append({'desc': 'Back',
                        'key': 'B',
                        'goto': _return_to_rotes})
    option_list.append({'desc': 'Back',
                        'key': 'back',
                        'goto': _return_to_rotes})
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
                      'rows': 4}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _return_to_rotes(caller, raw_string, **kwargs):
    caller.db.sphere['Obsessions'] = [caller.db.sphere['Obsessions'][0]]
    caller.db.merits=[]
    if caller.db.sphere['Order'] != 'Nameless':
        set(caller, 'Status', value=1, subentry=order.db.longname,
            statclass='Merit')
        set(caller, 'Language', value=1, subentry='High Speech',
            statclass='Merit')
    caller.db.power={'Gnosis': 1}
    return 'mage_rotes'


# noinspection DuplicatedCode
def add_merit(caller, raw_string, **kwargs):
    text = 'Merit:'
    option_list = [{'key': '_default',
                    'goto': (_check_merit,
                             {'total': kwargs['total'],
                              'max': kwargs['max']})}]
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
        return 'mage_merits'
    elif len(merits) > 1:
        caller.msg('|/Too many matches found')
        return 'mage_merits'
    else:
        merit = merits[0]
        if merit.db.restricted == True:
            caller.msg('|/That merit is restricted')
            return 'mage_merits'
        elif len(merit.db.noteRestrictions) == 0:
            return 'get_merit_value', { 'total' : kwargs['total'],
                                   'note' : '',
                                   'merit' : merit,
                                   'max' : kwargs['max']}
        else:
            return 'get_merit_note', { 'total' : kwargs['total'],
                                  'merit' : merit,
                                  'max' : kwargs['max']}


# noinspection DuplicatedCode
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
        return 'mage_merits'


# noinspection DuplicatedCode
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
        return 'mage_merits'
    else:
        value=int(strip_control_sequences(raw_string))
        if value < 1:
            caller.msg('|/Invalid value')
            return 'mage_merits'
        elif value + kwargs['total'] - kwargs['merit'].get(caller,
                                    subentry=kwargs['note']) >  kwargs['max']:
            caller.msg('|/You don\'t have enough points')
            return 'mage_merits'
        elif kwargs['merit'].meets_prereqs(caller,value=value,
                                           subentry=kwargs['note']):
            kwargs['merit'].set(caller,value=value,subentry=kwargs['note'])
            return 'mage_merits'
        else:
            caller.msg('|/You don\'t meet the prerequisites for that merit')
            return 'mage_merits'


# noinspection DuplicatedCode
def remove_merit(caller, raw_string, **kwargs):
    text = 'Remove which merit:'
    merit_list = kwargs['removable']
    option_list = []
    for item in merit_list:
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
    return 'mage_merits'

def _increase_power(caller, raw_string, **kwargs):
    if caller.db.power['Gnosis'] < 10:
        caller.db.power['Gnosis'] = caller.db.power['Gnosis'] + 1
        if caller.db.power['Gnosis'] in [3, 6, 9]:
            return 'mage_add_obsession'
    return 'mage_merits'

def mage_add_obsession(caller, raw_string, **kwargs):
    text = 'Add another obsession'
    options = ( {'key' : '_default',
                 'goto' : _mage_new_obsession } )
    return text,options

def _mage_new_obsession(caller, raw_string, **kwargs):
    f = find('Obsessions',statclass='Sphere')[0]
    current_obsessions = f.get(caller)
    if current_obsessions == False:
        current_obsessions = []
    current_obsessions.append(strip_control_sequences(raw_string))
    f.set(caller,current_obsessions)
    return 'mage_merits'

def _decrease_power(caller, raw_string, **kwargs):
    if caller.db.power['Gnosis'] > 1:
        caller.db.power['Gnosis'] = caller.db.power['Gnosis'] - 1
        if caller.db.power['Gnosis'] in [2, 5, 8]:
            f = find('Obsessions',statclass='Sphere')[0]
            current_obsessions = f.get(caller,subentry='')[:-1]
            f.set(caller,current_obsessions)
    return 'mage_merits'


# noinspection DuplicatedCode
def mage_praxes(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'mage_praxes'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    text = 'Praxes:|/|/One per dot of Gnosis|/'
    for item in list(caller.db.praxes.keys()):
        text = text + '|_|_|_|_' + item + '|/'
    text = text + '|/'

    option_list = []
    if len(caller.db.praxes) < caller.get('Gnosis',statclass='Power'):
        option_list.append({'key': 'A',
                            'desc': 'Add a praxis',
                            'goto': 'mage_add_praxis'})
    if len(caller.db.praxes) > 1:
        option_list.append( { 'key' : 'R',
                              'desc' : 'Remove a praxis',
                              'goto' : 'mage_remove_praxis' } )
    if len(caller.db.praxes)  == caller.get('Gnosis',statclass='Power'):
        option_list.append( { 'key' : 'F',
                              'desc' : 'Finish',
                               'goto' : 'mage_finish_cg' } )
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
            'Through dedicated practice or repetitive use of certain spells, ' +
            'a mage may develop a Praxis. Praxes are spell Imagos the mage ' +
            'has gained special insight into, learning the symbols of the ' +
            'spell by heart. She is more adept at casting these spells, and ' +
            'they shape her growing Gnosis.' + '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P'],
                      'rows': 4}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _return_to_merits(caller, raw_string, **kwargs):
    caller.db.praxes={}
    return 'mage_merits'

def mage_remove_praxis(caller, raw_string, **kwargs):
    text = 'Select praxis to remove:'
    option_list = []
    if caller.db.praxs:
        praxes = list(caller.db.praxes.keys())
    else:
        praxes = []
    praxes.sort()
    for item in praxes:
        option_list.append( { 'desc' : item,
                              'goto' : ( _remove_praxis,
                                       { 'praxis' : item } ) } )
    options = tuple(option_list)
    return text,options

def _remove_praxis(caller, raw_string, **kwargs):
    set(caller,kwargs['praxis'],value=False, statclass='Praxis')
    return 'mage_praxes'


# noinspection DuplicatedCode
def mage_add_praxis(caller, raw_string, **kwargs):
    text = 'Enter name of spell:'
    option_list = [ {'key' : '_default',
                 'goto' : _check_praxis } ]
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = ('|/' + '_' * 79 + '|/|/' +
            'Because praxes apply to specific spells you will need to state ' +
            'the name of an approved spell which the praxis is for. Approved ' +
            'spells can be found at either http://13.52.78.93/spells/list/ ' +
            'or by typing |w+list spell|n. (Warning: The list is very long.)' +
            '|/' + '_' * 79)
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P'],
                      'rows': 4}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def _check_praxis(caller, raw_string, **kwargs):
    stat = find(strip_control_sequences(raw_string),statclass='Spell')
    if len(stat) < 1:
        caller.msg('|/I can\'t find ' + strip_control_sequences(raw_string))
        return 'mage_praxes'
    elif len(stat) > 1:
        caller.msg('|/Too many matches found')
        return 'mage_praxes'
    else:
        stat = stat[0]
        if stat.db.restricted == True:
            caller.msg('|/That ' + stat.type() + ' is restricted')
            return 'mage_praxes'
        elif stat.meets_prereqs(caller) == False:
            caller.msg('|/You aren\'t able to cast ' + stat.db.longname)
        else:
            set(caller, stat.db.longname, value=True, statclass='Praxis')
            return 'mage_praxes'

def quit_menu(caller, raw_string, **kwargs):
    obj_menu = 'codes.commands.character_menus.object_in_menu'
    act_menu = 'codes.commands.character_menus.account_in_menu'
    caller.cmdset.delete(obj_menu)
    caller.account.cmdset.delete(act_menu)
    caller.execute_cmd('look')
    text = {'format': 'suppress'}
    return text, None

def mage_finish_cg(caller, raw_string, **kwargs):
    obj_menu = 'codes.commands.character_menus.object_in_menu'
    act_menu = 'codes.commands.character_menus.account_in_menu'
    caller.cmdset.delete(obj_menu)
    caller.account.cmdset.delete(act_menu)
    del caller.db.cg
    caller.cmdset.delete('unfinished_character')
    caller.cmdset.add(
        'codes.commands.character_commands.finished_character',permanent=True)
    set(caller,'Wisdom',statclass='Advantage', value=7)
    set(
        caller,'Mana',statclass='Advantage',
        value=caller.get('Mana',subentry='Permanent',statclass='Advantage'))
    set(
        caller,'Willpower',statclass='Advantage',
        value=caller.get('Willpower',
                         subentry='Permanent',statclass='Advantage'))
    caller.db.finished_cg = time.asctime(time.localtime(time.time()))
    caller.db.xp = { 'earned' : 35,
                     'spent' : 0,
                     'arcane_earned' : 40,
                     'arcane_spent' : 0,
                     'log' : {} }
    caller.execute_cmd('look')
    text = {'format': 'suppress'}
    return text, None
