from codes.data import get
from codes.data import set
from evennia.utils.utils import strip_control_sequences
from codes.menus.menu_types import ExMenu

# TODO: Add ability to go backwards.

# TODO: Add ability to resume and reset.

stats = { 'attribute' : {
                'mental' : ['Intelligence', 'Wits', 'Resolve'],
                'physical' : ['Strength', 'Dexterity', 'Stamina'],
                'social' : ['Presence', 'Manipulation', 'Composure'] },
           'skill' : {
                'mental' : ['Academics', 'Computer', 'Crafts',
                            'Investigation', 'Medicine', 'Occult', 'Politics',
                            'Science'],
                'physical' : ['Athletics', 'Brawl', 'Drive', 'Firearms',
                              'Larceny', 'Stealth', 'Survival', 'Weaponry'],
                'social' : ['Animal Ken', 'Empathy', 'Expression',
                            'Intimidation', 'Persuasion', 'Socialize',
                            'Streetwise', 'Subterfuge'] } }

def start(caller):

    if caller.db.finished_cg:
        caller.msg('You have already completed CG')
        return None
    else:
        caller.db.cg = {'start_menu': 'cg',
                        'start_node': 'start'}
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
    caller.db.cg['act_points'] = stats[int(strip_control_sequences(raw_string))]
    caller.db.cg['att_points'] = list(caller.db.cg['act_points']).copy()
    return 'decide_stat',{'type':'attribute'}

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
    mental_left = caller.db.cg['act_points'][0] - mental_total
    physical_left = caller.db.cg['act_points'][1] - physical_total
    social_left = caller.db.cg['act_points'][2] - social_total
    text = ( text + 'Unspent:' + str(mental_left).rjust(8) +
            str(physical_left).rjust(16) +
            str(social_left).rjust(16) )
    reply = { 'text' : text, 'mental' : mental_left, 'physical' : physical_left,
             'social' : social_left }
    return reply

def decide_stat(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'decide_stat'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    if kwargs['type'] == 'attribute':
        help = ('|/' + '_' * 79 + '|/|/' +
            'A character starts with one dot in each Attribute for ' +
            'free. One dot represents someone who is below average in ' +
            'that capability, while two dots represent someone ' +
            'average. A character with three or four dots is above' +
            'average or extremely talented, while five dots ' +
            'represents the peak of human ability.' + '|/' + '_' * 79)
    else:
        help =('|/' + '_' * 79 + '|/|/' +
            'Skills represent applications of your abilities. These are ' +
            'things you have learned from training, books, or teachers. ' +
            'Having no dots in a Skill means that you have no training with ' +
            'it, and are barely capable. One dot means you have cursory ' +
            'training or dabble in the Skill, while two dots means that you ' +
            'can use the Skill at a professional level. Three dots ' +
            'represents excellent training or experience, four is ' +
            'outstanding, and five dots means you are one of the absolute ' +
            'best in the world.' + '|/' + '_' * 79)
    options_list=[]
    data = get_stats(caller, type=kwargs['type'])
    for group in stats[kwargs['type']]:
        for item in stats[kwargs['type']][group]:
            options_list.append({ 'desc' : item,
                                 'goto' : ('enter_value' ,
                                           {'att' : item.lower(),
                                            'group' : group,
                                            'type' : kwargs['type'],
                                            'points_left' :
                                            data[group] } ) } )
    if kwargs['type'] == 'attribute':
        options_list.append( { 'desc' : 'Back',
                              'key' : 'B',
                              'goto' : _clear_attribute_priorities } )
        options_list.append({'desc': 'Back',
                             'key': 'back',
                             'goto': _clear_attribute_priorities})
    else:
        options_list.append( { 'desc' : 'Back',
                              'key' : 'B',
                              'goto' : _clear_skill_priorities } )
        options_list.append({'desc': 'Back',
                             'key': 'back',
                             'goto': _clear_skill_priorities})

    options_list.append( {'key': 'q',
                          'desc': 'Quit',
                          'goto': 'quit_menu'})
    options_list.append( {'key': 'Quit',
                          'desc': 'Quit',
                          'goto': 'quit_menu'})
    if data['mental'] == 0 and data['physical'] == 0 and data['social'] == 0:
        if kwargs['type'] == 'attribute':
            options_list.append( {'key' : 'P',
                                 'desc' : 'Proceed',
                                 'goto' : 'start_skills' } )
        else:
            options_list.append({'key': 'P',
                                 'desc': 'Proceed',
                                 'goto': 'assign_specialties'})
    text = '|_' + data['text']
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'P']}
    if kwargs['type'] == 'attribute':
        options_format['rows'] = 3
    else:
        options_format['rows'] = 8
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    options =tuple(options_list)

    return display,options

def _clear_attribute_priorities(caller, raw_string, **kwargs):
    del caller.db.cg['att_points']
    del caller.db.cg['act_points']
    return 'start'

def _clear_skill_priorities(caller, raw_string, **kwargs):
    caller.db.cg['act_points'] = caller.db.cg['att_points']
    del caller.db.cg['skill_points']
    return 'start_skills'

def enter_value(caller, raw_string, **kwargs):
    text = 'Enter new value'
    option_list = [ { 'key' : '_default',
         'goto' : ( _set_stat, {'group' : kwargs['group'],
                                'att' : kwargs['att'],
                                'type' : kwargs ['type'],
                                'points_left' : kwargs['points_left'] } ) } ]
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    help = '|/' + '_' * 29 + '|/|/'
    if kwargs['type'] == 'attribute':
        help = help + 'Enter a value between 1 and 5'
    else:
        help = help + 'Enter a value between 0 and 5'
    help = help + '|/' + '_' * 29
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B', 'F'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

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


# noinspection DuplicatedCode
def start_skills(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'start_skills'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    text = "Decide how to allocate your skills."
    help = ('|/' + '_' * 79 + '|/|/' +
            'Skills represent applications of your abilities. These are ' +
            'things you have learned from training, books, or teachers. ' +
            'Having no dots in a Skill means that you have no training with ' +
            'it, and are barely capable. One dot means you have cursory ' +
            'training or dabble in the Skill, while two dots means that you ' +
            'can use the Skill at a professional level. Three dots ' +
            'represents excellent training or experience, four is ' +
            'outstanding, and five dots means you are one of the absolute ' +
            'best in the world.|/|/Like Attributes, select a primary, ' +
            'secondary, and tertiary category for your Skills. You have ' +
            'eleven dots to assign for your primary category, seven dots for ' +
            'you secondary, and four dots for your tertiary. As always, ' +
            'consider your character and concept when assigning dots. Maybe ' +
            'your blogger has two dots in Athletics because he is a ' +
            'marathoner, or your med student has a dot in Animal Ken from ' +
            'volunteering at a local shelter.' + '|/' + '_' * 79)
    options_list = [
        { 'desc' : 'Mental, Physical, Social',
         'goto' : _set_skill_priorities },
        { 'desc' : 'Mental, Social, Physical',
         'goto' : _set_skill_priorities },
        { 'desc' : 'Physical, Mental, Social',
         'goto' : _set_skill_priorities },
        { 'desc' : 'Physical, Social, Mental',
         'goto' : _set_skill_priorities },
        { 'desc' : 'Social, Mental, Physical',
         'goto' : _set_skill_priorities },
        { 'desc' : 'Social, Physical, Mental',
         'goto' : _set_skill_priorities } ]
    options_list.append({'desc': 'Back',
                         'key': 'B',
                         'goto': _return_to_attributes})
    options_list.append({'desc': 'Back',
                         'key': 'back',
                         'goto': _return_to_attributes})
    options_list.append({'key': 'q',
                     'desc': 'Quit',
                     'goto': 'quit_menu'})
    options_list.append({'key': 'Quit',
                     'desc': 'Quit',
                     'goto': 'quit_menu'})

    options = tuple (options_list)

    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B'],
                      'rows': 6}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}

    return display, options

def _return_to_attributes(caller, raw_string, **kwargs):
    caller.db.cg['act_points'] = caller.db.cg['att_points']
    return 'decide_stat',{'type':'attribute'}

def _set_skill_priorities(caller, raw_string, **kwargs):
    stats = [[],[11, 7, 4], [11, 4, 7], [7, 11, 4], [4, 11, 7], [7, 4, 11],
             [4, 7, 11]]
    caller.db.cg['skill_points'] = stats[int(
                                          strip_control_sequences(raw_string))]
    caller.db.cg['act_points'] = list(caller.db.cg['skill_points']).copy()
    return 'decide_stat',{'type':'skill'}

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


# noinspection DuplicatedCode
def assign_specialties(caller, raw_string, **kwargs):
    caller.db.cg['start_node'] = 'assign_specialties'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    data = caller.db.specialties
    text = ''
    for item in data:
        text = text + item + '|/'
    help = ('|/' + '_' * 79 + '|/|/' +
            'Skills represent broad categories of training. Someone with the ' +
            'Science Skill is equally familiar with particle physics, basic ' +
            'chemistry, and genetics. Skill Specialties allow you to '+
            'differentiate more, focusing on a specific area of a Skill that ' +
            'your character is more knowledgeable or proficient in.|/|/A ' +
            'character\'s Specialties say a lot about her. For example, a ' +
            'character with a Socialize Specialty in Formal Events is very '+
            'different from one with a Specialty in Dive Bars.|/|/Pick three ' +
            'Skill Specialties for your character and enter them by typing ' +
            'the skill name, a colon, and the specialty.|/|/(e.g. Computers: ' +
            'Excel Spreadsheets)' + '|/' + '_' * 79)
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
    option_list.append({'desc': 'Back',
                         'key': 'B',
                         'goto': _return_to_skills})
    option_list.append({'desc': 'Back',
                         'key': 'back',
                         'goto': _return_to_skills})
    option_list.append({'key': 'q',
                         'desc': 'Quit',
                         'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                         'desc': 'Quit',
                         'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B'],
                      'rows': 6}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}

    return display, options

def _return_to_skills(caller, raw_string, **kwargs):
    caller.db.cg['act_points'] = caller.db.cg['skill_points']
    caller.db.specialties = []
    return 'decide_stat',{'type':'skill'}

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
    caller.db.cg['start_menu'] = 'cg'
    caller.db.cg['start_node'] = 'assign_template'
    caller.db.cg['raw_string'] = strip_control_sequences(raw_string)
    caller.db.cg['kwargs'] = kwargs
    text = 'Choose template'
    help = ('|/' + '_' * 79 + '|/|/' +
            'Character generation up to this point has been a generic ' +
            'affair. Every character created must pass through these steps. ' +
            'At this point it is now necessary to chose what group the ' +
            'character belongs to so that the more specialized attributes ' +
            'can be assigned.' + '|/' + '_' * 79)
    option_list = [
        { 'desc' : 'Mortal',
          'goto' : 'mortal_template' },
        { 'desc' : 'Changeling',
          'goto' : 'changeling_template' },
        {'desc': 'Mage',
         'goto': 'mage_template'},
        { 'desc' : 'Vampire',
          'goto' : 'vampire_template' },
        { 'desc' : 'Werewolf',
          'goto' : 'werewolf_template'} ]
    option_list.append({'desc': 'Back',
                        'key': 'B',
                        'goto': 'assign_specialties'})
    option_list.append({'desc': 'Back',
                        'key': 'back',
                        'goto': 'assign_specialties'})
    option_list.append({'key': 'q',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    option_list.append({'key': 'Quit',
                        'desc': 'Quit',
                        'goto': 'quit_menu'})
    options = tuple(option_list)
    footer = '|/(Additional options include |w\'help\'|n and |w\'quit\'|n)'
    options_format = {'hide_keys': ['q', 'Quit', 'back'],
                      'move_keys': ['B'],
                      'rows': 10}
    display = {'text': text,
               'help': help,
               'options_format': options_format,
               'footer': footer}
    return display, options

def mortal_template(caller, raw_string, **kwargs):
    caller.db.sphere={}
    ExMenu(caller, 'codes.menus.cg_mortal', startnode = 'mortal_template',
           cmdset_mergetype='Union',  cmd_on_exit=None, auto_quit=False)
    text = {'format' : 'suppress'}
    return text,None

def changeling_template(caller, raw_string, **kwargs):
    caller.db.sphere = {}
    ExMenu(caller, 'codes.menus.cg_changeling', startnode='changeling_template',
           cmdset_mergetype='Union', cmd_on_exit=None, auto_quit=False)
    text = {'format': 'suppress'}
    return text, None

def mage_template(caller, raw_string, **kwargs):
    caller.db.sphere = {}
    ExMenu(caller, 'codes.menus.cg_mage', startnode='mage_template',
           cmdset_mergetype='Union', cmd_on_exit=None, auto_quit=False)
    text = {'format' : 'suppress'}
    return text,None

def vampire_template(caller, raw_string, **kwargs):
    caller.db.sphere = {}
    ExMenu(caller, 'codes.menus.cg_vampire', startnode='vampire_template',
           cmdset_mergetype='Union', cmd_on_exit=None, auto_quit=False)
    text = {'format' : 'suppress'}
    return text,None

def werewolf_template(caller, raw_string, **kwargs):
    caller.db.sphere = {}
    ExMenu(caller, 'codes.menus.cg_werewolf', startnode = 'werewolf_template',
           cmdset_mergetype='Union', cmd_on_exit=None, auto_quit=False)
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

