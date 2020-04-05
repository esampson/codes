from codes.data import get
from codes.data import set
from codes.data import find
from evennia.utils.utils import strip_control_sequences
from evennia.utils.search import search_script_tag

import time
  
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

anchors = { 'mortal' : 
              { 'virtue' : ['Charity', 'Competitive', 'Faith', 'Fortitude', 
                            'Generous', 'Hope', 'Justice', 'Loyal', 'Prudence',
                            'Temperance'],
                'vice' : ['Ambitious', 'Arrogant', 'Competitive', 'Envy',
                          'Gluttony', 'Greed', 'Lust', 'Pride', 'Sloth',
                          'Wrath'] },
            'changeling' :
              { 'needle' : ['Bon Vivant', 'Chess Master', 'Commander',
                            'Composer', 'Counselor', 'Daredevil', 'Dynamo',
                            'Protector', 'Provider', 'Scholar', 'Storyteller',
                            'Teacher', 'Traditionalist', 'Visionary'],
                'thread' : ['Acceptance', 'Anger', 'Family', 'Friendship',
                            'Hate', 'Honor', 'Joy', 'Love', 'Memory',
                            'Revenge'] } }

courts = ['Spring', 'Summer', 'Autumn', 'Winter', 'None']
regalia = ['Crown', 'Jewels', 'Mirror', 'Shield', 'Steed', 'Sword']

def get_stats(caller,type=''):
    ' Intelligence: 2     Strength: 5     Presence: 2'
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

def _set_stat(caller, raw_string, **kwargs):

    inp = strip_control_sequences(raw_string).strip()
    group = kwargs['group']
    
    return 'decide_stat', {'group': group }

def _set_skill_priorities(caller, raw_string, **kwargs):
    stats = [[],[11, 7, 4], [11, 4, 7], [7, 11, 4], [4, 11, 7], [7, 4, 11], 
             [4, 7, 11]]
    caller.ndb._menutree.att_points = stats[int(
                                          strip_control_sequences(raw_string))]
    return 'decide_skill'
    
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
        
def _remove_specialty(caller, raw_string, **kwargs):
    caller.db.specialties.remove(kwargs['item'])
    return 'assign_specialties'

def _set_template(caller, raw_string, **kwargs):
    if strip_control_sequences(raw_string) == '1':
        caller.db.basics['Sphere'] = 'Mortal'
        return 'mortal_template'

def merit_return(template):
    if template == 'mortal':
        return 'mortal_merits'
    elif template == 'changeling':
        return 'changeling_merits'
    
def _set_anchor(caller, raw_string, **kwargs):
    caller.db.sphere[kwargs['type'].capitalize()] = kwargs['value']
    if kwargs['template'] == 'mortal':
        return 'mortal_template'
    elif kwargs['template'] == 'changeling':
        return 'changeling_anchors'

def start(caller):
    
    if caller.db.finished_cg:
        caller.msg('You have already completed CG')
        return None
    else:
        text = "You are starting CG. Decide how to allocate your attributes."
        options = ( 
            { 'desc' : 'Mental, Physical, Social                             ',
             'goto' : _set_attribute_priorities },
            { 'desc' : 'Mental, Social, Physical                             ',
             'goto' : _set_attribute_priorities },
            { 'desc' : 'Physical, Mental, Social                             ',
             'goto' : _set_attribute_priorities },
            { 'desc' : 'Physical, Social, Mental                             ',
             'goto' : _set_attribute_priorities },
            { 'desc' : 'Social, Mental, Physical                             ',
             'goto' : _set_attribute_priorities },
            { 'desc' : 'Social, Physical, Mental                             ',
             'goto' : _set_attribute_priorities } )
        
        return text, options
    
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
    
def decide_stat(caller, raw_string, **kwargs):
    
    options_list=[]
    data = get_stats(caller, type=kwargs['type'])
    for item in stats[kwargs['type']][kwargs['group']]:
            options_list.append({ 'desc' : item,
                                 'goto' : ('enter_value' , {'att' : item.lower(),
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

def assign_template(caller, raw_string, **kwargs):
    text = 'Choose template'
    options = (
        { 'desc' : 'Mortal',
          'goto' : 'mortal_template' },
        { 'desc' : 'Changeling',
          'goto' : 'changeling_template' } )
    return text, options

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
          'goto' : ('choose_anchor', { 'type' : 'virtue', 
                                      'template' : 'mortal'} ) },
        { 'desc' : 'Vice',
          'goto' : ('choose_anchor', { 'type' : 'vice', 
                                      'template' : 'mortal'} ) } ]
    if virtue and vice:
        option_list.append ( { 'key' : 'P',
                              'desc' : 'Proceed',
                              'goto' : 'mortal_merits' } )
    options = tuple(option_list)
    return text, options
    
def choose_anchor(caller, raw_string, **kwargs):
    option_list = []
    for item in anchors[kwargs['template']][kwargs['type']]:
        option_list.append( {'desc' : item ,
                             'goto' : ( _set_anchor,
                                    {'type' : kwargs['type'],
                                     'value' : item,
                                     'template' : kwargs['template'] } ) } )
    text = 'Set ' + kwargs['type'].capitalize() + ':'
    options = tuple(option_list)
    return text, options

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
                                        { 'template' : 'mortal',
                                         'total' : total,
                                         'max' : 7} ) } )
    if total > 0:
        option_list.append( {'key' : 'R',
                             'desc' : 'Remove a merit',
                             'goto' : ('remove_merit',
                                       {'template' : 'mortal',
                                        'total' : total,
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
                            { 'template' : kwargs['template'],
                             'total' : kwargs['total'],
                             'max' : kwargs['max'] } ) } )
    return text,options
    
def _check_merit(caller, raw_string, **kwargs):
    merits = find(strip_control_sequences(raw_string), statclass='Merit')
    if len(merits) < 1:
        caller.msg('I can\'t find ' + strip_control_sequences(raw_string))
        return merit_return(kwargs['template'])
    elif len(merits) > 1:
        caller.msg('Too many matches found')
        return merit_return(kwargs['template'])
    else:
        merit = merits[0]
        if len(merit.db.noteRestrictions) == 0:
            return 'get_merit_value', { 'template' : kwargs['template'],
                                   'total' : kwargs['total'],
                                   'note' : '',
                                   'merit' : merit,
                                   'max' : kwargs['max']}
        else:
            return 'get_merit_note', {'template' : kwargs['template'],
                                  'total' : kwargs['total'],
                                  'merit' : merit,
                                  'max' : kwargs['max']}
        
def get_merit_note(caller, raw_string, **kwargs):
    text = 'This merit requires some form of note such as who the contacts '
    text = text + 'are or what the area of expertise is in:'
    options = ( {'key' : '_default',
                 'goto' : ( _check_merit_note, 
                            { 'template' : kwargs['template'],
                             'total' : kwargs['total'],
                             'merit' : kwargs['merit'],
                             'max' : kwargs['max'] } ) } )
    return text, options

def _check_merit_note(caller, raw_string, **kwargs):
    merit = kwargs['merit']
    if merit.db.noteRestrictions[0] == '*':
        return 'get_merit_value', { 'template' : kwargs['template'],
                                'total' : kwargs['total'],
                                'note' : strip_control_sequences(raw_string),
                                'merit' : merit,
                                'max' : kwargs['max']}
    elif strip_control_sequences(raw_string) in merit.db.noteRestrictions:
        return 'get_merit_value', { 'template' : kwargs['template'],
                                'total' : kwargs['total'],
                                'note' : strip_control_sequences(raw_string),
                                'merit' : merit,
                                'max' : kwargs['max']}
    else:
        caller.msg('Invalid note for that merit')
        return merit_return(kwargs['template'])
    
def get_merit_value(caller, raw_string, **kwargs):
    text = 'Enter value:'
    options = ( {'key' : '_default',
                 'goto' : ( _check_merit_value, 
                            { 'template' : kwargs['template'],
                             'total' : kwargs['total'],
                             'note' : kwargs['note'],
                             'merit' : kwargs['merit'],
                             'max' : kwargs['max'] } ) } )
    return text,options

def _check_merit_value(caller, raw_string, **kwargs):
    if not strip_control_sequences(raw_string).isnumeric():
        caller.msg('Invalid value')
        return merit_return(kwargs['template'])
    else:
        value=int(strip_control_sequences(raw_string)) 
        if value < 1:
            caller.msg('Invalid value')
            return merit_return(kwargs['template'])
        elif value + kwargs['total'] - kwargs['merit'].get(caller,
                                    subentry=kwargs['note']) >  kwargs['max']:
            caller.msg('You don\'t have enough points')
            return merit_return(kwargs['template'])
        elif kwargs['merit'].meets_prereqs(caller,value=value,
                                           subentry=kwargs['note']):
            kwargs['merit'].set(caller,value=value,subentry=kwargs['note'])
            return merit_return(kwargs['template'])
        else:
            caller.msg('You don\'t meet the prerequisites for that merit')
            return merit_return(kwargs['template'])
    
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
                                      'subentry' : item[2],
                                      'template' : kwargs['template'] } ) } )
    options = tuple(option_list)
    return text,options

def _delete_merit(caller, raw_string, **kwargs):
    if ( kwargs['entry'] == 'Mantle' and 
         kwargs['subentry'] == caller.db.sphere['Court'] ):
        caller.msg('You can\'t remove your court mantle')
    else:
        set(caller, kwargs['entry'], subentry=kwargs['subentry'], value=0)
    return merit_return(kwargs['template'])

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

    
def changeling_template(caller, raw_string, **kwargs):
    caller.db.basics['Sphere'] = 'Changeling'
    caller.db.sphere['Frailties']=[]
    caller.db.power['Wyrd'] = 1
    text = 'Select Seeming:'
    option_list = []
    seemings = search_script_tag('seeming_stat')
    for item in seemings:
        option_list.append( {'desc' : item.db.longname,
                             'goto' : ( 'changeling_stat',
                                        { 'template' : 'changeling',
                                         'seeming' : item } ) } )
    options = tuple(option_list)
    return text, options

def changeling_stat(caller, raw_string, **kwargs):
    seeming = kwargs['seeming']
    option_list=[]
    caller.db.sphere['Seeming'] = seeming.db.longname
    caller.db.sphere['Regalia'] = [seeming.db.regalia]
    for attribute in seeming.db.bonus_attributes:
        option_list.append( { 'desc' : attribute.capitalize(),
                              'goto' : (_raise_stat,
                                        {'stat' : attribute.lower() } ) } )
    options = tuple(option_list)
    text = 'Select one attribute to boost:'
    return text,options

def _raise_stat(caller, raw_string, **kwargs):
    start_value = caller.get(kwargs['stat'],statclass='Attribute')
    if start_value == 5:
        caller.msg('Can\'t boost a stat to over 5')
        return "changeling_stats"
    else:
        set(caller, kwargs['stat'], statclass='Attribute', value=start_value+1)
        return "changeling_kith"
    
def changeling_kith(caller, raw_string, **kwargs):

    text = 'Select Kith:'
    kiths = search_script_tag('kith_stat')
    option_list = []
    for item in kiths:
        option_list.append( {'desc' : item.db.longname.capitalize(),
                             'goto' : ( 'changeling_court',
                                        { 'template' : 'changeling',
                                         'kith' : item.db.longname.lower() } ) } )
    options = tuple(option_list)
    return text, options

def changeling_court(caller, raw_string, **kwargs):
    kith = kwargs['kith']
    caller.db.sphere['Kith'] = kith
    text = 'Select Court:'
    option_list = []
    for item in courts:
        option_list.append( {'desc' : item,
                             'goto' : ( _changeling_set_court,
                                        { 'template' : 'changeling',
                                         'court' : item } ) } )
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
          'goto' : ('choose_anchor', { 'type' : 'needle', 
                                      ''
                                      'template' : 'changeling'} ) },
        { 'desc' : 'Thread',
          'goto' : ('choose_anchor', { 'type' : 'thread', 
                                      'template' : 'changeling'} ) } ]
    if needle and thread:
        option_list.append ( { 'key' : 'P',
                              'desc' : 'Proceed',
                              'goto' : 'changeling_regalia' } )
    options = tuple(option_list)
    return text, options

def changeling_regalia(caller, raw_string, **kwargs):
    text = 'Select second Regalia:'
    option_list = []
    for item in regalia:
        if item != caller.db.sphere['Regalia'][0]:
            option_list.append( {'desc' : item,
                                 'goto' : ( _changeling_set_regalia,
                                          { 'template' : 'changeling',
                                            'regalia' : item } ) } )
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
                                        { 'template' : 'changeling',
                                         'total' : total,
                                         'max' : max} ) } )
    if max - total > 4:
        option_list.append ( {'key' : 'I',
                              'desc' : 'Increase Wyrd',
                              'goto' : ( _increase_power,
                                         { 'template' : 'changeling'} ) } )
    if get(caller,'Wyrd',statclass='Power') > 1:
        option_list.append ( {'key' : 'D',
                              'desc' : 'Decrease Wyrd',
                              'goto' : ( _decrease_power,
                                         { 'template' : 'changeling'} ) } )
    if total > 0:
        option_list.append( {'key' : 'R',
                             'desc' : 'Remove a merit',
                             'goto' : ('remove_merit',
                                       {'template' : 'changeling',
                                        'total' : total,
                                        'max' : max} ) } )
    if total == max:
        option_list.append( {'key' : 'P',
                             'desc' : 'Proceed',
                             'goto' : 'changeling_contracts'})
    options = tuple(option_list)
    return text, options

def _increase_power(caller, raw_string, **kwargs):
    if kwargs['template'] == 'changeling' and caller.db.power['Wyrd'] < 10:
        caller.db.power['Wyrd'] = caller.db.power['Wyrd'] + 1
        send_kwargs = kwargs
        if caller.db.power['Wyrd'] in [2, 4, 8]:
            send_kwargs['message'] = 'You must add a minor frailty'
            return 'changeling_add_frailty', send_kwargs
        elif caller.db.power['Wyrd'] in [6, 10]:
            send_kwargs['message'] = 'You must add a major frailty'
            return 'changeling_add_frailty', send_kwargs
    return merit_return(kwargs['template'])

def changeling_add_frailty(caller, raw_string, **kwargs):
    send_kwargs=kwargs
    send_kwargs['special']='frailty'
    text = kwargs['message']
    options = ( {'key' : '_default',
                 'goto' : ( _changeling_new_frailty, kwargs) } )
    return text,options 

def _changeling_new_frailty(caller, raw_string, **kwargs):
    f = find('Frailties',statclass='Sphere')[0]
    current_frailties = f.get(caller,subentry='')
    if current_frailties == False:
        current_frailties = []
    current_frailties.append(strip_control_sequences(raw_string))
    f.set(caller,current_frailties)
    return merit_return(kwargs['template'])

def _decrease_power(caller, raw_string, **kwargs):
    if kwargs['template'] == 'changeling' and caller.db.power['Wyrd'] > 1:
        caller.db.power['Wyrd'] = caller.db.power['Wyrd'] - 1
        if caller.db.power['Wyrd'] in [1, 3, 5, 7, 9]:
            f = find('Frailties',statclass='Sphere')[0]
            current_frailties = f.get(caller,subentry='')[:-1]
            f.set(caller,current_frailties)
    return merit_return(kwargs['template'])
    
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
                              'goto' : ( 'changeling_add_contract',
                                       { 'template' : 'changeling' } ) } )
    if len(common_list) + len(royal_list) + len(goblin_list) > 3:
        option_list.append( { 'key' : 'R',
                              'desc' : 'Remove a contract',
                              'goto' : ( 'changeling_remove_contract',
                                        { 'template' : 'changeling' } ) } )
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
        caller.msg('I can\'t find ' + strip_control_sequences(raw_string))
        return 'changeling_contracts'
    elif len(contracts) > 1:
        caller.msg('Too many matches found')
        return 'changeling_contracts'
    else:
        contract = contracts[0]
        if contract.meets_prereqs(caller,value=True):
            contract.set(caller,value=True)
            return 'changeling_contracts'
        else:
            caller.msg('You don\'t meet the prerequisites for that contract')
            return 'changeling_contracts'
        
def changeling_finish_cg(caller, raw_string, **kwargs):
    caller.cmdset.add('codes.character_commands.finished_character',permanent=True)
    caller.cmdset.delete('codes.character_commands.unfinished_character')
    set(caller,'Clarity',statclass='Advantage', value=0)
    set(caller,'Glamour',statclass='Advantage', value=0)
    caller.db.finished_cg = time.asctime(time.localtime(time.time()))
    caller.db.xp = { 'earned' : 75,
                     'spent' : 0,
                     'log' : {} }
    return None
    
def quit(caller, raw_string, **kwargs):
    return None
    
        