from evennia import default_cmds
from evennia import Command
from evennia import InterruptCommand
from operator import itemgetter
from evennia.utils.search import search_script_tag

from codes.frames import scroll
from codes.frames import top_bottom

from codes import data
from codes.sidebars import changeling_template_block
from codes.sidebars import mage_template_block
from codes.sidebars import mortal_template_block
from codes.sidebars import vampire_template_block
from codes.sidebars import werewolf_template_block
from codes.sidebars import blank_template_block

import textwrap
import re

def parser(message):
    regex_string ='^(\/\S+)?\s?([^(^=^\/]+)?(\((([^)]?)+)\))?\/?'
    regex_string = regex_string + '(([^=]?)+)?\=?(.+)?$'
    regex = re.compile(regex_string)
    reply = regex.findall(message.strip())
    args = reply[0][0][1:].strip()
    entry = reply[0][1].strip()
    subentry = reply[0][3].strip()
    statclass = reply[0][5].strip()
    value = reply[0][7].strip()
    if value.isnumeric():
        value = int(value)
    elif value.lower() == 'true':
        value = True
    elif value.lower() == 'false':
        value = False
    else:
        value = value
    result = { 'args' : args, 'entry': entry, 'subentry' : subentry,
               'statclass' : statclass, 'value' : value}
    return result

def short_list(stats):
    message = 'Did you mean '
    for stat in stats:
        last_message = ('the ' + stat.type() + ' \'' +
                        stat.db.longname + '\', ')
        message = message + last_message
    message = message.replace(', ' + last_message,'')
    message = message + ' or ' +last_message[:-2] +'?'
    return message

def send_message(target,message):
    input = '<OOC>: ' + message
    width = len(input) + 10
    if width > 60:
        width = 60
    padding = int((80-width)/2)
    text = top_bottom(input, width=width, padding=padding,
                      replacements=[['<OOC>:','|b<|gOOC|b>|w:|n']])
    target.location.msg_contents(text)

class CmdPool(Command):
    """
    Usage:
        +pool/<action> <pool>[/<amount>][=<reason>]

    Command to spend or regain points from a pool (e.g. Willpower, Vitae, Glamour,
    etc.) This command is |wnot|n used for altering health pools. Use +hurt or
    +heal for that.

        <action>: Spend, Gain, or Check
        <pool>: Specific pool being affected
        <amount>: Amount of change. Required for spend or gain
        <reason>: The reason for the change. Optional

    Examples:
        +pool/spend Vitae/2=Physical Intensity
        +pool/spend Willpower/1=+3 Bonus
        +pool/gain Glamor/3
        +pool/check Willpower
    """

    key = '+pool'
    arg_regex = '^(\/\S+)\s.+$'
    help_category = 'IC Commands'

    def func(self):                      #pragma: no cover
        pool_func(self.caller,self.args) #pragma: no cover

def pool_func(target,input):
    if input:
        parsed = parser(input)
    else:
        parsed = { 'args' : '',
                   'entry' : '',
                   'subentry' : '',
                   'statclass' : '',
                   'value' : 0 }
    temp_pool = data.find(parsed['entry'] )
    pool = []
    for item in temp_pool:
        if item.db.pool:
            pool.append(item)
    action = parsed['args'].lower()
    amount = parsed['statclass']
    reason = parsed['value']
    if len(pool) == 1:
        current = pool[0].get(target,subentry='temporary')
        max = pool[0].get(target,subentry='permanent')
    if (action in ['spend', 'expend', 'lose', 'gain', 'regain', 'recover']
                and len(pool) == 1 and amount.isnumeric() ):
        if action in ['spend', 'expend', 'lose'] and int(amount) > current:
            target.msg('You don\'t have that many points')
        else:
            if action in ['spend', 'expend', 'lose']:
                result = (target.name + ' spends ' + amount +
                          ' point')
                if int(amount) != 1:
                    result=result+'s'
                result = result + ' of ' + pool[0].db.longname
                if reason != '':
                    result = result + ' for ' + reason
                pool[0].set(target,current - int(amount))
            elif action in ['gain', 'regain', 'recover']:
                if current + int(amount) > max:
                    amount = max - current
                result = (target.name + ' gains ' + str(amount) +
                          ' point')
                if int(amount) != 1:
                    result = result + 's'
                result = result + ' of ' + pool[0].db.longname
                if reason != '':
                    result = result + ' for ' + reason
                pool[0].set(target,current + int(amount))
            send_message(target, result)
    elif action in ['check'] and len(pool) == 1:
          result = (pool[0].db.longname + ' Pool: '+ str(current) + '/' +
                    str(max))
          target.msg(result)
    else:
        target.msg('I can\'t tell what you want to do')

class CmdProve(Command):
    """
    Usage:
        +prove <stat>[(<subentry>)][/<statclass>][=<value>]

    Command to prove a character's abilities to other people.

        <stat>: Stat being proven
        <subentry>: Subentry for the stat if needed
        <statclass>: Optional. Helps in case of naming conflicts
        <value>: Optional. Proves the character possesses at least that value but
            does not prove entire value

    Examples:
        +prove Strength
        +prove Willpower=6
        +prove Crafts: Blacksmithing
        +prove Str/Skill
        +prove Status(Ordo Dracul)
    """

    key = '+prove'
    arg_regex = '^(\/\S+)?\s.+$'
    help_category = 'IC Commands'

    def func(self):                         #pragma: no cover
        prove_func(self.caller,self.args)   #pragma: no cover

def prove_func(target,input):
    if input:
        parsed = parser(input)
    else:
        parsed = { 'args' : '',
                   'entry' : '',
                   'subentry' : '',
                   'statclass' : '',
                   'value' : 0 }
    if len(parsed['entry'].split(':')) == 2:
        value = data.get(target,parsed['entry'])
        if value == 1:
            message = (target.name + ' possesses the specialty ' +
                       parsed['entry'])
            send_message(target,message)
        else:
            target.msg('I can\'t do that')
    elif parsed['statclass'].lower() == 'rote':
        if target.get(parsed['entry'],statclass='Rote'):
            message = (target.name + ' possesses the rote ' +
                    data.find(parsed['entry'],statclass='Spell')[0].db.longname)
            send_message(target,message)
        else:
            target.msg('I can\'t do that.')
    elif parsed['statclass'].lower() == 'praxis':
        if target.get(parsed['entry'],statclass='Praxis'):
            message = (target.name + ' possesses the praxis ' +
                    data.find(parsed['entry'],statclass='Spell')[0].db.longname)
            send_message(target,message)
        else:
            target.msg('I can\'t do that.')
    elif parsed['entry'] != '':
        stats = data.find(parsed['entry'],statclass=parsed['statclass'])
        if len(stats) == 0:
            target.msg('Nothing found')
        elif len(stats) < 5 and len(stats) > 1:
            message = short_list(stats)
            target.msg(message)
        elif len(stats) > 4:
            target.msg('Too many found')
        else:
            stat = stats[0]
            value = stat.get(target,subentry=parsed['subentry'])
            name = stat.db.longname
            if parsed['subentry'] != '':
                name = name + '(' + parsed['subentry'] + ')'
            if str(value) == 'True':
                message = (target.name + ' possesses the ' + stat.type() +
                           ' of ' + name)
                send_message(target,message)
            elif (parsed['value'] != '' and value >= parsed['value'] and
                  value != 0):
                message = (target.name + ' possesses at least ' + name + ': ' +
                           str(parsed['value']) )
                send_message(target,message)
            elif value != 0:
                message = target.name + ' possesses '
                if type(value) != type(1) :
                    message = message + 'the ' + name + ' of ' + str(value)
                else:
                    message = message + name + ': ' + str(value)
                send_message(target,message)
            else:
                target.msg('I can\'t do that.')
    else:
        target.msg('No entry')

class CmdList(Command):
    """
    Usage:
        +list [<category>]

    Command to get a list of stats of a given category. When no category is entered
    it will return a list of all categories.

        <category>: Category being listed

    Examples:
        +list
        +list Skills
    """

    key = '+list'
    help_category = 'OOC Commands'

    def func(self):                                         #pragma: no cover
        list_func(self.caller,self.args)                    #pragma: no cover

def list_func(target,input):
    if input:
        parsed = parser(input)
    else:
        parsed = { 'args' : '',
                   'entry' : '',
                   'subentry' : '',
                   'statclass' : '',
                   'value' : 0 }

    d = search_script_tag('dictionary_data')[0]
    if not hasattr(d, 'lists'):
        d.at_server_reload()                                #pragma: no cover
    if parsed['entry'] == '':
        temp = sorted(list(d.lists.keys()))
        results = 'Lists:\n\n'
        for item in temp:
            results = results + proper_caps(item) + ', '
        results = results[:-2]
        if len(results) > 999:
            results = scroll(results,width=73,padding=0)    #pragma: no cover
        elif len(results) >499:
            results = scroll(results,width=64,padding=5)    #pragma: no cover
        else:
            results = scroll(results,width=54, padding=10, top=0, bottom=0)
    elif parsed['entry'].lower() in d.lists:
        results = proper_caps(parsed['entry'])  + ' List\n\n'
        for item in sorted(d.lists[parsed['entry'].lower()]):
            results = results + proper_caps(item) + ', '
        results = results[:-2]
        if len(results) > 999:
            results = scroll(results,width=73,padding=0)
        elif len(results) >499:
            results = scroll(results,width=64,padding=5)
        else:
            results = scroll(results,width=54, padding=10, top=0, bottom=0)
    else:
        results = 'Could not find ' + parsed['entry']
    target.msg(results)

class CmdHurt(Command):
    """
    Usage:
        +hurt <type>=<amount>

    Basic command for recording damage.

        <type>: Bashing, Lethal, or Aggravated
        <amount>: Amount of damage taken. Damage will spill over appropriately
            (Bashing turning into Lethal, Lethal turning into Aggravated)

    Example:
        +hurt lethal=3

    """

    key = '+hurt'
    help_category = 'IC Commands'
    arg_regex = '^(\/\S+)?\s.+$'

    def func(self):                                         #pragma: no cover
        hurt_func(self.caller, self.args)                   #pragma: no cover

def hurt_func(target,input):
    if input:
        parsed = parser(input)
    else:
        parsed = { 'args' : '',
                   'entry' : '',
                   'subentry' : '',
                   'statclass' : '',
                   'value' : 0 }
    type = parsed['entry'].lower()
    amount = parsed['value']
    health = target.db.advantages['Health']
    starting_health = list(health).copy()
    damage = [0,0,0]
    max_health = target.get('Health',statclass='Advantage',
                                 subentry='Permanent')

    if type in ['bashing','bash','b']:
        damage[0] = amount
    elif type in ['lethal','l']:
        damage[1] = amount
    elif type in ['aggravated','agg','a']:
        damage[2] = amount
    else:
        target.msg('Incorrect damage type')
        raise InterruptCommand()

    if health[0] + health[1] + health [2] + damage[0] > max_health:
        upgrade = damage[0] - (max_health - (health[0] + health[1] +
                                             health [2]))
        damage[1] = damage[1] + upgrade
        damage[0] = damage[0] - upgrade
    if health[1] + health [2] + damage[1] > max_health:
        upgrade = damage[1] - (max_health - (health[1] + health [2]))
        damage[2] = damage[2] + upgrade
        damage[1] = damage[1] - upgrade
    if health [2] + damage[2] > max_health:
        upgrade = damage[2] - (max_health - health[2])
        damage[2] = damage[2] - upgrade
    health[2] = health[2] + damage[2]
    health[1] = health[1] + damage[1]

    health[0] = health[0] + damage[0]
    if health[2] + health[1] > max_health:
        health[1] = max_health - health[2]
    if health[2] + health[1] + health[0] > max_health:
        health[0] = max_health - (health[2] + health[1])
    damage[2] = health[2] - starting_health[2]
    damage[1] = health[1] - starting_health[1]
    damage[0] = health[0] - starting_health[0]
    target.db.advantages['Health'] = health
    message = target.name + ' takes '
    if damage[2] > 0:
        message = message + str(damage[2]) + ' point'
        if damage[2] > 1:
            message = message + 's'
        message = message + ' of aggravated'
        if damage[1] > 0:
            message = message + ' and ' + str(damage[1]) + ' point'
            if damage[1] > 1:
                message = message + 's'
            message = message + ' of lethal'
        message = message + ' damage.'
    elif damage[1] > 0:
        message = message + str(damage[1]) + ' point'
        if damage[1] > 1:
            message = message + 's'
        message = message + ' of lethal'
        if damage[0] > 0:
            message = message + ' and ' + str(damage[0]) + ' point'
            if damage[0] > 1:
                message = message + 's'
            message = message + ' of bashing'
        message = message + ' damage.'
    else:
        message = message + str(damage[0]) + ' point'
        if damage[0] > 1:
            message = message + 's'
        message = message + ' of bashing damage.'
    send_message(target,message)



class CmdHeal(Command):
    """
    Usage:
        +heal <type>=<amount>

    Basic command for recovering damage.

        <type>: Bashing, Lethal, or Aggravated
        <amount>: Amount of damage healed. Unlike +hurt there is no spillover
            mechanism for recovered health.

    Examples:
        +heal/bashing=2

    """

    key = '+heal'
    help_category = 'IC Commands'
    arg_regex = '^(\/\S+)?\s.+$'

    def func(self):                                         #pragma: no cover
        heal_func(self.caller, self.args)                   #pragma: no cover

def heal_func(target,input):
    if input:
        parsed = parser(input)
    else:
        parsed = { 'args' : '',
                   'entry' : '',
                   'subentry' : '',
                   'statclass' : '',
                   'value' : 0 }
    type = parsed['entry'].lower()
    amount = parsed['value']
    health = target.db.advantages['Health']
    max_health = target.get('Health',statclass='Advantage',
                                 subentry='Permanent')

    if type in ['bashing','bash','b']:
        if amount > health[0]:
            health[0] = 0
        else:
            health[0] = health[0] - amount
        damage_type = 'bashing'
    elif type in ['lethal','l']:
        if amount > health[1]:
            health[1] = 0
        else:
            health[1] = health[1] - amount
        damage_type = 'lethal'
    elif type in ['aggravated','agg','a']:
        if amount > health[2]:
            health[2] = 0
        else:
            health[2] = health[2] - amount
        damage_type = 'aggravated'
    else:
        target.msg('Incorrect damage type')
        raise InterruptCommand()
    target.db.advantages['Health'] = health
    message = (target.name + ' heals ' + str(amount) + ' points of ' +
               damage_type + ' damage.')
    send_message(target,message)


class CmdInfo(Command):
    """
    Usage:
        +info <stat>[/<class>]

    Command to get information about a stat. Partial matching of names is
    supported. To help deal with name collisions the class may be specified to
    narrow the search. Class also suppports partial name matching.

        <stat>: The stat being searched for.
        <class>: Advantage, Attribute, Contract, Merit, or Skill

    Examples:
        +info Dexterity
        +info Str/Skill

    """

    key = '+info'
    help_category = 'OOC Commands'


    def func(self):                                         #pragma: no cover
        info_func(self.caller, self.args)                   #pragma: no cover

def info_func(target,input):
    parsed = parser(input)
    temp_stats = data.find(parsed['entry'],statclass=parsed['statclass'])
    stats = []
    for entry in temp_stats:
        if entry.type() not in ['sphere', 'basic']:
            stats.append(entry)
    if len(stats) == 0:
        target.msg('Nothing found')
    elif len(stats) == 1:
        message = stats[0].db.longname + '\n\n'
        message = message + proper_caps(stats[0].type())
        if stats[0].db.info:
            if len(stats[0].db.info) > 0:
                info_string = stats[0].db.info.replace('\r\n','\n')
                info_string = info_string.replace('’','\'').replace('|/','\n')
                message = message + '\n\n' + info_string
        if stats[0].db.reference:
            if len(stats[0].db.reference) > 0:
                message = message + '\n\n' +stats[0].db.reference
        if len(message) > 999:
            table = scroll(message,width=74,padding=0)
        elif len(message) >499:
            table = scroll(message,width=64,padding=5)
        else:
            table = scroll(message,width=54, padding=10, top=0, bottom=0)
        target.msg(table)
    elif len(stats) < 5:
        message = short_list(stats)
        target.msg(message)
    else:
        target.msg('Too many found')

class CmdSheet(default_cmds.MuxCommand):
    """
    Usage:
        +sheet

    Command to retrieve current character sheet

    Examples:
        +sheet

    """

    key = '+sheet'
    arg_regex='^$'
    help_category = 'OOC Commands'


    def func(self):
        result = produce_sheet(self.caller)                 #pragma: no cover
        self.caller.msg(result)                             #pragma: no cover

def produce_sheet(target):

    # Build the Attribute block
    block1=[]
    block1.append('  Intelligence:'
                  + str(target.intelligence()).rjust(2) +
                  '   Strength:' + str(target.strength()).rjust(2) +
                  '      Presence:'
                  + str(target.presence()).rjust(2) + ' ')
    block1.append('          Wits:' + str(target.wits()).rjust(2) +
                  '  Dexterity:' + str(target.dexterity()).rjust(2) +
                  '  Manipulation:'
                  + str(target.manipulation()).rjust(2) + ' ')
    block1.append('       Resolve:' + str(target.resolve()).rjust(2) +
                  '    Stamina:' + str(target.stamina()).rjust(2) +
                  '     Composure:'
                  + str(target.composure()).rjust(2) + ' ')

    #build the Skill block
    block2=[]
    block2.append('     Academics:' + str(target.academics()).rjust(2) +
                  '  Athletics:' + str(target.athletics()).rjust(2) +
                  '    Animal Ken:'
                  + str(target.animal_ken()).rjust(2) + ' ')
    block2.append('      Computer:' + str(target.computer()).rjust(2) +
                  '      Brawl:' + str(target.brawl()).rjust(2) +
                  '       Empathy:'
                  + str(target.empathy()).rjust(2) + ' ')
    block2.append('        Crafts:' + str(target.crafts()).rjust(2) +
                  '      Drive:' + str(target.drive()).rjust(2) +
                  '    Expression:'
                  + str(target.expression()).rjust(2) + ' ')
    block2.append(' Investigation:'
                  + str(target.investigation()).rjust(2) +
                  '   Firearms:' + str(target.firearms()).rjust(2) +
                  '  Intimidation:'
                  + str(target.intimidation()).rjust(2) + ' ')
    block2.append('      Medicine:' + str(target.medicine()).rjust(2) +
                  '    Larceny:' + str(target.larceny()).rjust(2) +
                  '    Persuasion:'
                  + str(target.persuasion()).rjust(2) + ' ')
    block2.append('        Occult:' + str(target.occult()).rjust(2) +
                  '    Stealth:' + str(target.stealth()).rjust(2) +
                  '     Socialize:'
                  + str(target.socialize()).rjust(2) + ' ')
    block2.append('      Politics:' + str(target.politics()).rjust(2) +
                  '   Survival:' + str(target.survival()).rjust(2) +
                  '    Streetwise:'
                  + str(target.streetwise()).rjust(2) + ' ')
    block2.append('       Science:' + str(target.science()).rjust(2) +
                  '   Weaponry:' + str(target.weaponry()).rjust(2) +
                  '    Subterfuge:'
                  + str(target.subterfuge()).rjust(2) + ' ')

    #build the Advantages block
    block3 = []
    health_bar = target.get('Health',subentry='bar')
    gap = 22-len(health_bar)
    gap1 = int(round(gap/2,0))+1
    gap2 = gap - gap1 + 2
    block3.append(' Health:' + (' ' * (len(health_bar) + gap1 - 5)) +
        'Defense:' +
        str(target.get('Defense',statclass='Advantage')).rjust(4) +
        (' ' * gap2) + 'Init:'
        + str(target.get('Init',statclass='Advantage')).rjust(4) + ' ')
    block3.append('   ' + health_bar + (' ' * gap1) + 'Will:' +
        str(str(target.get('Willpower',statclass='Advantage',subentry='temp'))
        + '/' +
        str(target.get('Willpower',statclass='Advantage',
                       subentry='perm'))).rjust(7) +
        (' ' * gap2) + 'Speed:' + str(target.get('Speed',
                        statclass='Advantage')).rjust(3) + ' ')

    #Get the template block
    if target.template().lower() == 'changeling':
        block_t = changeling_template_block(target)
    elif target.template().lower() == 'mage':
        block_t = mage_template_block(target)
    elif target.template().lower() == 'mortal':
        block_t = mortal_template_block(target)
    elif target.template().lower() == 'vampire':
        block_t = vampire_template_block(target)
    elif target.template().lower() == 'werewolf':
        block_t = werewolf_template_block(target)
    else:
        block_t = blank_template_block()

    #Build the bottom block
    block = []
    if target.template().lower() == 'changeling':
        sub_block = ['Merits:']
        temp = merits_list(target)
        for item in temp:
            for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
                sub_block.append(' ' + line)
        block.append(sub_block)
        sub_block = ['Contracts:']
        temp = contracts_list(target)
        for item in temp:
            for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
                sub_block.append(' ' + line)
        block.append(sub_block)
        frailties = target.get('Frailties', 'Sphere')
        if frailties != -1 and frailties != False:
            if len(frailties) != 0:
                sub_block = ['Frailties:']
                for item in frailties:
                    for line in textwrap.wrap(item,width=24,
                                              subsequent_indent=' '):
                        sub_block.append(' ' + line)
                block.append(sub_block)
    elif target.template().lower() == 'mage':
        sub_block = ['Merits:']
        temp = merits_list(target)
        for item in temp:
            for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
                sub_block.append(' ' + line)
        block.append(sub_block)

        # Arcana
        if target.db.arcana:
            sub_block = ['Arcana:']
            temp = simple_list(target.db.arcana)
            for item in temp:
                for line in textwrap.wrap(item, width=24, subsequent_indent=' '):
                    sub_block.append(' ' + line)
            block.append(sub_block)

        # Obsessions
        obsessions = target.get('Obsessions', 'Sphere')
        if obsessions != -1 and obsessions != False:
            if len(obsessions) != 0:
                sub_block = ['Obsessions:']
                for item in obsessions:
                    for line in textwrap.wrap(item,width=24,
                                              subsequent_indent=' '):
                        sub_block.append(' ' + line)
                block.append(sub_block)

        # Rotes
        if target.db.rotes:
            sub_block = ['Rotes:']
            temp = simple_list(target.db.rotes)
            for item in temp:
                for line in textwrap.wrap(item, width=24, subsequent_indent=' '):
                    sub_block.append(' ' + line)
            block.append(sub_block)

        # Praxes
        if target.db.Praxes:
            sub_block = ['Praxes:']
            temp = simple_list(target.db.praxes)
            for item in temp:
                for line in textwrap.wrap(item, width=24, subsequent_indent=' '):
                    sub_block.append(' ' + line)
            block.append(sub_block)

    elif target.template().lower() == 'mortal':
        sub_block = ['Merits:']
        temp = merits_list(target)
        for item in temp:
            for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
                sub_block.append(' ' + line)
        half = int(len(sub_block) / 2) + 1
        sub_block.append(' ')
        adjust = 0
        if (len(sub_block) % 2) == 1:               #Adding extra line if total
            sub_block.append(' ')                   #number of lines is odd
            adjust = 0
        counter = 0
        merit_blocks = [ [], [' '] ]
        for item in range(half):
            merit_blocks[0].append(sub_block[counter])
            merit_blocks[1].append(sub_block[counter + half + adjust])
            counter = counter + 1
        block.append(merit_blocks[1][:-1])
        block.append(merit_blocks[0])
    if target.template().lower() == 'vampire':
        sub_block = ['Merits:']
        temp = merits_list(target)
        for item in temp:
            for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
                sub_block.append(' ' + line)
        block.append(sub_block)

        #disciplines
        if target.db.disciplines:
            sub_block = ['Disciplines:']
            temp = simple_list(target.db.disciplines)
            for item in temp:
                for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
                    sub_block.append(' ' + line)
            block.append(sub_block)

        #devotions
        if target.db.devotions:
            sub_block = ['Devotions:']
            temp = simple_list(target.db.devotions)
            for item in temp:
                for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
                    sub_block.append(' ' + line)
            block.append(sub_block)

        #coils
        if target.db.coils:
            sub_block = ['Coils:']
            temp = simple_list(target.db.coils)
            for item in temp:
                for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
                    sub_block.append(' ' + line)
            block.append(sub_block)

        #Cruac Rites
        if target.db.cruacRites:
            sub_block = ['Rites:']
            temp = simple_list(target.db.cruacRites)
            for item in temp:
                for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
                    sub_block.append(' ' + line)
            block.append(sub_block)

        #Theban Miracles
        if target.db.thebanRites:
            sub_block = ['Miracles:']
            temp = simple_list(target.db.thebanRites)
            for item in temp:
                for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
                    sub_block.append(' ' + line)
            block.append(sub_block)

        #Scales
        if target.db.scales:
            sub_block = ['Scales:']
            temp = simple_list(target.db.scales)
            for item in temp:
                for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
                    sub_block.append(' ' + line)
            block.append(sub_block)

        banes = target.get('Banes', 'Sphere')
        if banes != -1 and banes != False:
            if len(banes) != 0:
                sub_block = ['Banes:']
                for item in banes:
                    for line in textwrap.wrap(item,width=24,
                                              subsequent_indent=' '):
                        sub_block.append(' ' + line)
                block.append(sub_block)

    # Werewolves
    if target.template().lower() == 'werewolf':

        # Merits
        sub_block = ['Merits:']
        temp = merits_list(target)
        for item in temp:
            for line in textwrap.wrap(item, width=24, subsequent_indent=' '):
                sub_block.append(' ' + line)
        block.append(sub_block)

        # Gifts
        if target.db.gifts:
            sub_block = ['Gifts:']
            temp = list(target.db.gifts.keys())
            temp.sort()
            for item in temp:
                for line in textwrap.wrap(item, width=24, subsequent_indent=' '):
                    sub_block.append(' ' + line)
            block.append(sub_block)

        # Rites
        if target.db.werewolfRites:
            sub_block = ['Rites:']
            temp = list(target.db.werewolfRites.keys())
            temp.sort()
            for item in temp:
                for line in textwrap.wrap(item, width=24, subsequent_indent=' '):
                    sub_block.append(' ' + line)
            block.append(sub_block)

    temp = specialties_list(target)
    sub_block = ['Specialties:']
    for item in temp:
        for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
            sub_block.append(' ' + line)
    block.append(sub_block)

    final_block = build_bottom_block(block)
    block4 = ''
    for item in final_block:
        block4 = block4 + '| ' + item + '|||/|'

    #Assemble blocks
    result = ('+-------------------------------------------------+--' +
              '--------------------------+|/' +
              '|' + block1[0] + '||' + block_t[0] + '|||/|' +
              block1[1] + '||' + block_t[1] + '|||/|' +
              block1[2] + '||' + block_t[2] + '|||/' +
              '+-------------------------------------------------+' +
              block_t[3] + '|||/|' +
              block2[0] + '||' + block_t[4] + '|||/|' +
              block2[1] + '||' + block_t[5] + '|||/|' +
              block2[2] + '||' + block_t[6] + '|||/|' +
              block2[3] + '||' + block_t[7] + '|||/|' +
              block2[4] + '||' + block_t[8] + '|||/|' +
              block2[5] + '||' + block_t[9] + '|||/|' +
              block2[6] + '||' + block_t[10] + '|||/|' +
              block2[7] + '||' + block_t[11] + '|||/' +
              '+-------------------------------------------------+' +
              block_t[12] + '|||/|' +
              block3[0] + '||' + block_t[13] + '|||/|' +
              block3[1] + '||' + block_t[14] + '|||/' +
              '+-------------------------------------------------+--' +
              '--------------------------+|/' +
              block4[:-1] + '+---------------------------------' +
              '---------------------------------------------+')

    return result

def merits_list(target):
    try:
        sorted_list = sorted(target.db.merits, key=lambda merit: merit[0])
    except:
        return []
    else:
        results = list()
        for merit in sorted_list:
            if merit[2] == '':
                results.append(merit[0]+': '+str(merit[1]))
            else:
                results.append(merit[0]+' ('+merit[2]+'): '+ str(merit[1]))
        return results

def specialties_list(target):
    results = sorted(target.db.specialties)
    return results

def contracts_list(target):
    contracts = target.db.contracts
    try:
        contract_list = sorted(list(contracts.keys()))
    except:
        return []
    else:
        results = []
        for contract in contract_list:
            if contracts[contract] == '':
                results.append(contract)
            else:
                results.append(contract+' ('+contracts[contract]+')')
        return results

def simple_list(attribute):
    results = []
    item_list = sorted(list(attribute.keys()))
    for item in item_list:
        if str(attribute[item]) == 'True':
            new_line = item
        else:
            new_line = item + ': ' + str(attribute[item])
        results.append(new_line)
    return results

def build_bottom_block(sub_blocks):
    columns = [ [], [], [] ]
    column_lengths = [ 0, 0, 0 ]
    blocks_with_lengths = []
    for item in sub_blocks:
        blocks_with_lengths.append( [ len(item), item ] )
    blocks_with_lengths = sorted(blocks_with_lengths, key=itemgetter(0),
                                 reverse=True)
    for block in blocks_with_lengths:
        if (column_lengths[2] <= column_lengths[1] and
                column_lengths[2] <= column_lengths[0]):
            if column_lengths[2] == 0:
                for item in block[1]:
                    columns[2].append(item)
            else:
                columns[2].append(' ')
                for item in block[1]:
                    columns[2].append(item)
            column_lengths[2] = len(columns[2])
        elif (column_lengths[1] <= column_lengths[2] and
              column_lengths[1] <= column_lengths[0]):
            if column_lengths[1] == 0:
                for item in block[1]:
                    columns[1].append(item)
            else:
                columns[1].append(' ')
                for item in block[1]:
                    columns[1].append(item)
            column_lengths[1] = len(columns[1])
        elif (column_lengths[0] <= column_lengths[1] and
              column_lengths[0] <= column_lengths[2]):
            if column_lengths[0] == 0:
                for item in block[1]:
                    columns[0].append(item)
            else:
                columns[0].append(' ')
                for item in block[1]:
                    columns[0].append(item)
            column_lengths[0] = len(columns[0])
    result = []
    counter = 0
    while (counter<len(columns[0]) or counter<len(columns[1]) or
           counter<len(columns[2]) ):
        out = ''
        if counter<len(columns[0]):
            out = out + columns[0][counter].ljust(25)
        else:
            out = out + ''.ljust(25)
        if counter<len(columns[1]):
            out = out + ' ' + columns[1][counter].ljust(25)
        else:
            out = out + ''.ljust(26)
        if counter<len(columns[2]):
            out = out + ' ' + columns[2][counter].ljust(25)
        else:
            out = out + ''.ljust(26)
        result.append(out)
        counter = counter + 1
    return result

def proper_caps(string):
    result = ''
    counter = 0
    for item in string.split(' '):
        if item not in ('of', 'the', 'or') or counter == 0:
            result = result + item.capitalize() + ' '
        else:
            result = result + item.lower() + ' '
        counter = counter + 1
    result = result[:-1]
    return result
