from evennia import default_cmds
from evennia import Command
from evennia import InterruptCommand
from evennia.utils import evtable

from world.scroll import scroll

from world import data
from world.sidebars import changeling_template_block
from world.sidebars import mortal_template_block

import textwrap
import re

from world.stats.dictionary import typeclass_to_type

class parsed:
    def __init__(self,entry,subentry,statclass,value):
        self.entry = entry
        self.subentry = subentry
        self.statclass = statclass
        self.value = value
        
def parser(message):
    regex_string ='^(([:a-zA-Z0-9%\s\'-])+)(\((([a-z,A-Z0-9%\s\'-])+)\))?'
    regex_string = regex_string + '(\/(([a-zA-Z0-9%\s\'-])+))?\=?'
    regex_string = regex_string +'(([a-zA-Z0-9%\s\'-])+)?$'
    regex = re.compile(regex_string)
    reply = regex.findall(message)
    entry = reply[0][0].strip()
    if len(reply[0]) > 3:
        subentry = reply[0][3].strip()
    else:
        subentry = ''
    if len(reply[0]) > 6:
        statclass = reply[0][6].strip()
    else:
        statclass = ''
    if len(reply[0]) > 8:
        value = reply[0][8].strip()
        if value.isnumeric():
            value = int(value)
        elif value.lower() == 'true':
            value = True
        elif value.lower() == 'false':
            value = False
    else:
        value = 0
    result = parsed(entry,subentry,statclass,value)
    return result

def short_list(stats):
    message = 'Did you mean '
    for stat in stats:
        last_message = ('the ' + typeclass_to_type[stat.typeclass_path] + ' \'' + 
                        stat.db.longname + '\', ')
        message = message + last_message
    message = message.replace(', ' + last_message,'')
    message = message + ' or ' +last_message[:-2] +'?'
    return message

class CmdHurt(Command):
    
    key = '+hurt'
    arg_regex = '^/(([:a-zA-Z0-9%\s\'-])+)\=?(([0-9])+)$'
    
    def func(self):
        regex = re.compile('^/(([:a-zA-Z0-9%\s\'-])+)\=?(([0-9])+)$')
        #self.caller.msg(self.args)
        result = regex.findall(self.args)
        type = result[0][0].strip()
        amount = int(result[0][2].strip())
        health = self.caller.db.advantages['Health']
        max_health = self.caller.get('Health',statclass='Advantage',
                                     subentry='Permanent')
        
        if type in ['bashing','bash','b']:
            health[0] = health[0] + amount
            damage_type = 'bashing'
        elif type in ['lethal','l']:
            health[1] = health[1] + amount
            damage_type = 'lethal'
        elif type in ['aggravated','agg','a']:
            health[2] = health[2] + amount
            damage_type = 'aggravated'
        else:
            self.caller.msg('Incorrect damage type')
            raise InterruptCommand()
        
        while (health[0] + health[1] + health[2]) > max_health:
            adjust = (health[0] + health[1] + health[2]) - max_health
            if adjust > health[0]:
                health[1] = health[1] + health[0]
                health[0] = 0
            else: 
                health[1] = health[1] + adjust
                health[0] = health[0] - adjust * 2
            adjust = (health[1] + health[2]) - max_health
            if adjust > 0:
                if adjust > health[1]:
                    health[2] = health[2] + health[1]
                    health[1] = 0
                else:
                    health[2] = health[2] + adjust
                    health[1] = health[1] - adjust * 2
            adjust = health[2] - max_health
            if adjust > 0:
                health[2] = health[2] - adjust
        self.caller.db.advantages['Health'] = health
        message = (self.caller.name + ' takes ' + str(amount) + ' points of ' + damage_type +
                       ' damage.')
        self.caller.location.msg_contents(message)
        
        
                
class CmdHeal(Command):
    
    key = '+heal'
    arg_regex = '^/(([:a-zA-Z0-9%\s\'-])+)\=?(([0-9])+)$'
    
    def func(self):
        regex = re.compile('^/(([:a-zA-Z0-9%\s\'-])+)\=?(([0-9])+)$')
        #self.caller.msg(self.args)
        result = regex.findall(self.args)
        type = result[0][0].strip()
        amount = int(result[0][2].strip())
        health = self.caller.db.advantages['Health']
        max_health = self.caller.get('Health',statclass='Advantage',
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
            self.caller.msg('Incorrect damage type')
            raise InterruptCommand()
        self.caller.db.advantages['Health'] = health
        message = (self.caller.name + ' heals ' + str(amount) + ' points of ' + damage_type +
                       ' damage.')
        self.caller.location.msg_contents(message)
    
    
class CmdInfo(default_cmds.MuxCommand):
    
    key = '+info'
    arg_regex = '^\s(([a-zA-Z0-9%\s\'-/])+)$'
    
    def func(self):
        
        parsed = parser(self.args)
        temp_stats = data.find(parsed.entry,statclass=parsed.statclass)
        stats = []
        for entry in temp_stats:
            if typeclass_to_type[entry.typeclass_path] not in ['sphere', 'basic']:
                stats.append(entry)
        if len(stats) == 0:
            self.caller.msg('Nothing found')
        elif len(stats) == 1:
            message = stats[0].db.longname + '\\n\\n'
            message = message + typeclass_to_type[stats[0].typeclass_path].capitalize()
            if stats[0].db.info:
                if len(stats[0].db.info) > 0:
                    message = (message + '\\n\\n' +
                      stats[0].db.info.replace('\r\n','\\n').replace('’','\'').replace('|/','\\n'))
            if stats[0].db.reference:
                    if len(stats[0].db.reference) > 0:
                        message = message + '\\n\\n' +stats[0].db.reference
            if len(message) > 999:
                table = scroll(message,width=74,padding=0)
            elif len(message) >499:
                table = scroll(message,width=64,padding=5)
            else:
                table = scroll(message,width=54, padding=10, top=0, bottom=0)
            self.caller.msg(table)
        elif len(stats) < 5:
            message = short_list(stats)              
            self.caller.msg(message)
        else:
            self.caller.msg('Too many found')
                
class CmdSheet(default_cmds.MuxCommand):
    
    key = '+sheet'
    
    
    def func(self):
        result = produce_sheet(self.caller)
        self.caller.msg(result)
                
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
        (str(target.get('Willpower',statclass='Advantage',subentry='perm')
        - target.get('Willpower',statclass='Advantage',subentry='temp')) 
        + '/' + 
        str(target.get('Willpower',statclass='Advantage',
                       subentry='perm'))).rjust(7) +
        (' ' * gap2) + 'Speed:' + str(target.get('Speed',
                        statclass='Advantage')).rjust(3) + ' ')
    
    #Get the template block
    if target.template().lower() == 'changeling':
        block_t = changeling_template_block(target)
    elif target.template().lower() == 'mortal':
        block_t = mortal_template_block(target)          
        
    #Build the bottom block
    temp = target.specialties_list()
    c1 = ['Specialties:']
    for item in temp:
        for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
            c1.append(' ' + line)
    if target.template().lower() == 'changeling':
        c2 = ['Contracts:']
        temp = target.contracts_list()
    elif target.template().lower() == 'mortal':
        c2 = []
        temp = []
    for item in temp:
        for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
            c2.append(' ' + line)
    temp = target.merits_list()
    c3 = ['Merits:']
    for item in temp:
        for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
            c3.append(' ' + line)
    final = []
    counter = 0
    while counter<len(c1) or counter<len(c2) or counter<len(c3):
        out = ''
        if counter<len(c1):
            out = out + c1[counter].ljust(25)
        else:
            out = out + ''.ljust(25)
        if counter<len(c2):
            out = out + ' ' + c2[counter].ljust(25)
        else:
            out = out + ''.ljust(26)
        if counter<len(c3):
            out = out + ' ' + c3[counter].ljust(25)
        else:
            out = out + ''.ljust(26)
        final.append(out)
        counter = counter + 1
    block4 = ''
    for item in final:
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
                
        
        
                