from evennia import default_cmds
from evennia import Command
from evennia import InterruptCommand
from evennia.utils import evtable
from operator import itemgetter

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
    """
    Usage:
        +hurt/<type>=<amount>
        
    Basic command for recording damage.
    
        <type>: Bashing, Lethal, or Aggravated
        <amount>: Amount of damage taken. Damage will spill over appropriately 
            (Bashing turning into Lethal, Lethal turning into Aggravated)
            
    Example:
        +hurt/lethal=3
            
    """
    
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
    """
    Usage:
        +heal/<type>=<amount>
        
    Basic command for recovering damage.
    
        <type>: Bashing, Lethal, or Aggravated
        <amount>: Amount of damage healed. Unlike +hurt there is no spillover
            mechanism for recovered health.
            
    Examples:
        +heal/bashing=2
            
    """
    
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
    """
    Usage:
        +sheet
        
    Command to retrieve current character sheet
        
    Examples:
        +sheet
            
    """
    
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
        if not(frailties == False):
            if len(frailties) != 0:
                sub_block = ['Frailties:']
                for item in frailties:
                    for line in textwrap.wrap(item,width=24,subsequent_indent=' '):
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
        if (len(sub_block) % 2) == 1:                        #Adding extra line if total
            sub_block.append(' ')                             #number of lines is odd
            adjust = 0
        counter = 0
        merit_blocks = [ [], [' '] ]
        for item in range(half):
            merit_blocks[0].append(sub_block[counter])
            merit_blocks[1].append(sub_block[counter + half + adjust])
            counter = counter + 1
        block.append(merit_blocks[1][:-1])
        block.append(merit_blocks[0])
        #target.msg(block)
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
                result = results.append(contract)
            else:
                result = results.append(contract+' ('+contracts[contract]+')')
        return results
    
def build_bottom_block(sub_blocks):
    columns = [ [], [], [] ]
    column_lengths = [ 0, 0, 0 ]
    blocks_with_lengths = []
    for item in sub_blocks:
        blocks_with_lengths.append( [ len(item), item ] )
    blocks_with_lengths = sorted(blocks_with_lengths, key=itemgetter(0), reverse=True)
    for block in blocks_with_lengths:
        if column_lengths[2] <= column_lengths[1] and column_lengths[2] <= column_lengths[0]:
            if column_lengths[2] == 0:
                for item in block[1]:
                    columns[2].append(item)
                    column_lengths[2] = column_lengths[2] + block[0]
            else:
                columns[2].append(' ')
                for item in block[1]:
                    columns[2].append(item)
                    column_lengths[2] = column_lengths[2] + block[0] + 1
        elif column_lengths[1] <= column_lengths[2] and column_lengths[1] <= column_lengths[0]:
            if column_lengths[1] == 0:
                for item in block[1]:
                    columns[1].append(item)
                    column_lengths[1] = column_lengths[1] + block[0]
            else:
                columns[1].append(' ')
                for item in block[1]:
                    columns[1].append(item)
                    column_lengths[1] = column_lengths[1] + block[0] + 1
        elif column_lengths[0] <= column_lengths[1] and column_lengths[0] <= column_lengths[2]:
            if column_lengths[0] == 0:
                for item in block[1]:
                    columns[0].append(item)
                    column_lengths[0] = column_lengths[0] + block[0]
            else:
                columns[0].append(' ')
                for item in block[1]:
                    columns[0].append(item)
                    column_lengths[0] = column_lengths[0] + block[0] + 1
    result = []
    counter = 0
    while counter<len(columns[0]) or counter<len(columns[1]) or counter<len(columns[2]):
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
    
    