from codes.data import get
from codes.data import set
from evennia.utils.utils import strip_control_sequences
from codes.menus.menu_types import ExMenu

# TODO: Add ability to go backwards.

# TODO: Add ability to resume and reset.

stats = { 'attribute' : {'physical' : ['Strength', 'Dexterity', 'Stamina'],
              'mental' : ['Intelligence', 'Wits', 'Resolve'],
              'social' : ['Presence', 'Manipulation', 'Composure'] },
           'skill' : { 'mental' : ['Academics', 'Computer', 'Crafts',
                          'Investigation', 'Medicine', 'Occult', 'Politics',
                          'Science'],
             'physical' : ['Athletics', 'Brawl', 'Drive', 'Firearms',
                           'Larceny', 'Stealth', 'Survival', 'Weaponry'],
             'social' : ['Animal Ken', 'Empathy', 'Expression', 'Intimidation',
                         'Persuasion', 'Socialize', 'Streetwise',
                         'Subterfuge'] } }

def start(caller):

    if caller.db.finished_cg:
        caller.msg('You have already completed CG')
        return None
    else:
        text = 'You are starting CG. Decide your attribute priorities.'
        help = ('|/' + '_'*79 + '|/|/' +
                'A character starts with one dot in each Attribute for ' +
                'free. One dot represents someone who is below average in '+
                'that capability, while two dots represent someone ' +
                'average. A character with three or four dots is above' +
                'average or extremely talented, while five dots ' +
                'represents the peak of human ability.|/|/Attributes are ' +
                'divided into the Mental, Physical, and Social ' +
                'categories. For your character, consider which of the ' +
                'categories is most important. What sort of endeavors ' +
                'does your character excel at? Once you have picked a ' +
                'primary category, decide out of the remaining two which ' +
                'is your character\'s next-best category. You\'ll assign ' +
                'five dots to the Attributes in your primary category, ' +
                'four dots to the Attributes in your secondary category, ' +
                'and three dots to the Attributes in your tertiary ' +
                'category.' + '|/' + '_'*79)
        footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
        options_format = {'hide_keys' : ['q', 'Quit'],
                          'rows' : 6}
        display = {'text': text,
                   'help': help,
                   'options_format': options_format,
                   'footer': footer}
        options = (
            { 'desc' : 'Mental, Physical, Social',
             'goto' : _set_attribute_priorities },
            { 'desc' : 'Mental, Social, Physical',
             'goto' : _set_attribute_priorities },
            { 'desc' : 'Physical, Mental, Social',
             'goto' : _set_attribute_priorities },
            { 'desc' : 'Physical, Social, Mental',
             'goto' : _set_attribute_priorities },
            { 'desc' : 'Social, Mental, Physical',
             'goto' : _set_attribute_priorities },
            { 'desc' : 'Social, Physical, Mental',
             'goto' : _set_attribute_priorities },
            { 'key' : 'q',
              'desc' : 'Quit',
              'goto' : 'quit_menu'},
            { 'key' : 'Quit',
              'desc' : 'Quit',
              'goto' : 'quit_menu'})

        return display, options

def _set_attribute_priorities(caller, raw_string, **kwargs):
    stats = [[],[8, 7, 6], [8, 6, 7], [7, 8, 6], [6, 8, 7], [7, 6, 8],
                                                                     [6, 7, 8]]
    caller.ndb._menutree.att_points = stats[int(
                                          strip_control_sequences(raw_string))]
    return 'decide_attribute'

def decide_attribute(caller, raw_string, **kwargs):
    data = get_stats(caller, type='attribute')
    text = data['text'] + "|/|/Chose what to work on:"
    option_list = [
        { 'desc' : 'Mental',
         'goto' : ('decide_stat', {'group' : 'mental',
                                   'type' : 'attribute'} ) },
        { 'desc' : 'Physical',
         'goto' : ('decide_stat', {'group' : 'physical',
                                   'type' : 'attribute'} ) },
        { 'desc' : 'Social',
         'goto' : ('decide_stat', {'group' : 'social',
                                   'type' : 'attribute' } ) } ]
    if data['mental'] == 0 and data['physical'] == 0 and data['social'] == 0:
        option_list.append( {'key' : 'P',
                             'desc' : 'Proceed',
                             'goto' : 'start_skills' } )
    options = tuple(option_list)
    return text, options

def get_stats(caller,type=''):
    count = 0
    mental_total = 0
    physical_total = 0
    social_total = 0
    if type == 'attribute':
        text = '   ' + 'Attributes:'.center(48,' ') + '|/'
    elif type == 'skill':
        text = '   ' + 'Skills:'.center(48) + '|/'
    for item in stats[type]['mental']:
        mental = stats[type]['mental'][count]
        mental_value = caller.get(mental,statclass=type)
        physical = stats[type]['physical'][count]
        physical_value = caller.get(physical,statclass=type)
        social = stats[type]['social'][count]
        social_value = caller.get(social,statclass=type)
        mental_total = mental_total + mental_value
        physical_total = physical_total + physical_value
        social_total = social_total + social_value
        text = text + mental.rjust(13) + ':' + str(mental_value).rjust(2)
        text = text + physical.rjust(13) + ':' + str(physical_value).rjust(2)
        text = text + social.rjust(13) + ':' + str(social_value).rjust(2) + '|/'
        count = count + 1
    mental_left = caller.ndb._menutree.att_points[0] - mental_total
    physical_left = caller.ndb._menutree.att_points[1] - physical_total
    social_left = caller.ndb._menutree.att_points[2] - social_total
    text = ( text + 'Unspent:' + str(mental_left).rjust(8) +
            str(physical_left).rjust(16) +
            str(social_left).rjust(16) )
    reply = { 'text' : text, 'mental' : mental_left, 'physical' : physical_left,
             'social' : social_left }
    return reply

def decide_stat(caller, raw_string, **kwargs):

    options_list=[]
    data = get_stats(caller, type=kwargs['type'])
    for item in stats[kwargs['type']][kwargs['group']]:
            options_list.append({ 'desc' : item,
                                 'goto' : ('enter_value' ,
                                           {'att' : item.lower(),
                                            'group' : kwargs['group'],
                                            'type' : kwargs['type'],
                                            'points_left' :
                                            data[kwargs['group']] } ) } )
    if kwargs['type'] == 'attribute':
        options_list.append( { 'desc' : 'Back',
                              'key' : 'B',
                              'goto' : 'decide_attribute' } )
    else:
        options_list.append( { 'desc' : 'Back',
                              'key' : 'B',
                              'goto' : 'decide_skill' } )
    text = '|_' + data['text']
    options =tuple(options_list)

    return text,options

def enter_value(caller, raw_string, **kwargs):
    text = 'Enter new value'
    options = ( { 'key' : '_default',
         'goto' : ( _set_stat, {'group' : kwargs['group'],
                                'att' : kwargs['att'],
                                'type' : kwargs ['type'],
                                'points_left' : kwargs['points_left'] } ) } )
    return text, options

def _set_stat(caller, raw_string, **kwargs):

    inp = strip_control_sequences(raw_string).strip()
    group = kwargs['group']
    att = kwargs['att']
    type = kwargs['type']
    points_left = kwargs['points_left']
    if inp.isnumeric():
        current = caller.get(att,statclass=type)
        if points_left + current - int(inp) < 0:
            caller.msg('You don\'t have enough points for that')
            return None, { 'group' : group,
                               'att' : att,
                               'type' : type,
                               'points_left' : points_left }
        elif type == 'attribute' and int(inp) < 1:
            caller.msg('You can\'t set ' + att + 'to less than 1')
            return None, { 'group' : group,
                               'att' : att,
                               'type' : type,
                               'points_left' : points_left }
        elif type == 'skill' and int(inp) < 0:
            caller.msg('You can\'t set ' + att + 'to less than 0')
            return None, { 'group' : group,
                               'att' : att,
                               'type' : type,
                               'points_left' : points_left }
        elif int(inp) > 5:
            caller.msg('You can\'t set ' + att + 'to more than 5')
            return None, { 'group' : group,
                               'att' : att,
                               'type' : type,
                               'points_left' : points_left }
        else:
            set(caller,att,statclass=type,value=int(inp))
            return 'decide_stat',   {'group' : group,
                                      'type' : type,
                                      'att' : att }
    else:
        caller.msg('Invalid value')
        return None, { 'group' : group,
                               'att' : att,
                               'type' : type,
                               'points_left' : points_left }

def start_skills(caller, raw_string, **kwargs):

    text = "Decide how to allocate your skills."
    options = (
        { 'desc' : 'Mental, Physical, Social                                 ',
         'goto' : _set_skill_priorities },
        { 'desc' : 'Mental, Social, Physical                                 ',
         'goto' : _set_skill_priorities },
        { 'desc' : 'Physical, Mental, Social                                 ',
         'goto' : _set_skill_priorities },
        { 'desc' : 'Physical, Social, Mental                                 ',
         'goto' : _set_skill_priorities },
        { 'desc' : 'Social, Mental, Physical                                 ',
         'goto' : _set_skill_priorities },
        { 'desc' : 'Social, Physical, Mental                                 ',
         'goto' : _set_skill_priorities } )

    return text, options

def _set_skill_priorities(caller, raw_string, **kwargs):
    stats = [[],[11, 7, 4], [11, 4, 7], [7, 11, 4], [4, 11, 7], [7, 4, 11],
             [4, 7, 11]]
    caller.ndb._menutree.att_points = stats[int(
                                          strip_control_sequences(raw_string))]
    return 'decide_skill'

def decide_skill(caller, raw_string, **kwargs):
    data = get_stats(caller, type='skill')
    text = '|_' + data['text'] + "|/|/Chose what to work on:"
    option_list = [
        { 'desc' : 'Mental',
         'goto' : ('decide_stat', {'group' : 'mental', 'type' : 'skill'} ) },
        { 'desc' : 'Physical',
         'goto' : ('decide_stat', {'group' : 'physical', 'type' : 'skill'} ) },
        { 'desc' : 'Social',
         'goto' : ('decide_stat', {'group' : 'social', 'type' : 'skill' } ) } ]
    if data['mental'] == 0 and data['physical'] == 0 and data['social'] == 0:
        option_list.append({ 'key' : 'P',
                             'desc' : 'Proceed',
                             'goto' : 'assign_specialties'})
    options = tuple(option_list)
    return text, options

def assign_specialties(caller, raw_string, **kwargs):
    data = caller.db.specialties
    text = ''
    for item in data:
        text = text + item + '|/'
    option_list = []
    if len(data) < 3:
        if len(data) > 0:
            text = text + '|/'
        text = text + 'Enter new specialty as <skill>: <specialty>'
        option_list.append( {'key' : '_default',
                             'goto' : _enter_specialty } )
    if len(data) > 0:
        option_list.append( {'key' : 'R',
                             'desc' : 'Remove specialty',
                             'goto' : 'remove_specialty' } )
    if len(data) > 2:
        option_list.append( {'key' : 'P',
                             'desc' : 'Proceed',
                             'goto' : 'assign_template' } )
    options = tuple(option_list)
    return text,options

def _enter_specialty(caller, raw_string, **kwargs):
    if len(strip_control_sequences(raw_string).split(':')) != 2:
        caller.msg('Invalid entry')
        return None
    else:
        skill = strip_control_sequences(raw_string).split(':')[0]
        if get(caller,skill,statclass='skill') < 1:
            caller.msg('You need at least 1 point in ' + skill)
            return None
        else:
            caller.db.specialties.append(strip_control_sequences(raw_string))
            return 'assign_specialties'

def remove_specialty(caller, raw_string, **kwargs):
    data = caller.db.specialties
    option_list = []
    for item in data:
        option_list.append ( {'desc' : item,
                              'goto' : ( _remove_specialty,
                                         {'item' : item} ) } )
    options = tuple(option_list)
    text = 'Remove which specialty?'
    return text, options

def _remove_specialty(caller, raw_string, **kwargs):
    caller.db.specialties.remove(kwargs['item'])
    return 'assign_specialties'

def assign_template(caller, raw_string, **kwargs):
    text = 'Choose template'
    options = (
        { 'desc' : 'Mortal',
          'goto' : 'mortal_template' },
        { 'desc' : 'Changeling',
          'goto' : 'changeling_template' },
        {'desc': 'Mage',
         'goto': 'mage_template'},
        { 'desc' : 'Vampire',
          'goto' : 'vampire_template' },
        { 'desc' : 'Werewolf',
          'goto' : 'werewolf_template'} )
    return text, options

def mortal_template(caller, raw_string, **kwargs):
    caller.db.sphere={}
    ExMenu(caller, 'codes.menus.cg_mortal', startnode = 'mortal_template',
           cmdset_mergetype='Union')
    text = {'format' : 'suppress'}
    return text,None

def changeling_template(caller, raw_string, **kwargs):
    ExMenu(caller, 'codes.menus.cg_changeling',
           startnode = 'changeling_template', cmdset_mergetype='Union')
    text = {'format' : 'suppress'}
    return text,None

def mage_template(caller, raw_string, **kwargs):
    ExMenu(caller, 'codes.menus.cg_mage', startnode = 'mage_template',
           cmdset_mergetype='Union')
    text = {'format' : 'suppress'}
    return text,None

def vampire_template(caller, raw_string, **kwargs):
    ExMenu(caller, 'codes.menus.cg_vampire', startnode = 'vampire_template',
           cmdset_mergetype='Union')
    text = {'format' : 'suppress'}
    return text,None

def werewolf_template(caller, raw_string, **kwargs):
    ExMenu(caller, 'codes.menus.cg_werewolf', startnode = 'werewolf_template',
           cmdset_mergetype='Union')
    text = {'format' : 'suppress'}
    return text,None

def quit_menu(caller, raw_string, **kwargs):
    obj_menu = 'codes.commands.character_menus.object_in_menu'
    act_menu = 'codes.commands.character_menus.account_in_menu'
    caller.cmdset.delete(obj_menu)
    caller.account.cmdset.delete(act_menu)
    caller.execute_cmd('look')
    text = {'format' : 'suppress'}
    return text,None

