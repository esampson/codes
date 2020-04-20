from codes.commands.stat_commands import produce_sheet
from codes.data import set

from evennia import Command
from evennia import CmdSet
from evennia.utils.search import object_search

import re
        
def parser(message):
    regex_string ='^\/?(\S+)\s([^(^=^\/]+)(\((([^)])+)\))?\/?(([^=])+)?\=(.+)$'
    regex = re.compile(regex_string)
    reply = regex.findall(message)
    args = reply[0][0].strip()
    if len(reply[0]) > 1:
        entry = reply[0][1].strip()
    else:
        entry = ''
    if len(reply[0]) > 3:
        subentry = reply[0][3].strip()
    else:
        subentry = ''
    if len(reply[0]) > 5:
        statclass = reply[0][5].strip()
    else:
        statclass = ''
    if len(reply[0]) > 7:
        value = reply[0][7].strip()
        if value.isnumeric():
            value = int(value)
        elif value.lower() == 'true':
            value = True
        elif value.lower() == 'false':
            value = False
    else:
        value = 0
    result = { 'args' : args, 'entry': entry, 'subentry' : subentry,
               'statclass' : statclass, 'value' : value}
    return result

class staff_commands(CmdSet):
    
    key = 'staff_commands'
    
    def at_cmdset_creation(self):
        self.add(CmdSheetStaff())
        self.add(CmdSetStaff())

class CmdSheetStaff(Command):
    """
    Usage:
        +sheet <character>
        
    Command to retrieve current character sheet for <character>
        
    Examples:
        +sheet Chester
            
    """
    
    key = '+sheet'
    arg_regex='^\s.+$'
    help_category = 'Staff'
    
    
    def func(self):
        request = self.args.strip()
        try:
            character = object_search(
                request, typeclass='typeclasses.characters.Character' )
        except:
            self.caller.msg('Something went wrong with the search')
        else:
            if len(character) == 0:
                self.caller.msg('I can\'t find character ' + request)
            elif len(character) > 1:
                self.caller.msg('Too many possible matches for ' + request)
            else:
                result = produce_sheet(character[0])
                self.caller.msg(result)
                
class CmdSetStaff(Command):
    """
    Usage:
        +set/<character> <entry>[(<subentry>)][/<category>]=<value>
        
    Command used by staff to set stats on a target.

        <character>: The character in question
        <entry>: The stat being set
        <subentry>: Notes for Merits, Seeming Benefits for Contracts. Optional
        <category>: Category of stat to help with name collisions. Optional
        <value>: Value stat is being set to.
    
    Examples:
        +set/Chester Resources=5
        +set/Chester Status(Clan)/Merit=2
        +set/Chester Athletics: Running=True
        +set/Chester Firearms: Nuclear Weapons=False
        +set/Chester Regalia=['Steed', 'Sword']
        +set/Chester Health(Bashing)=2
    """
    
    key = '+set'
    arg_regex='^/.+$'
    help_category = 'Staff'
    
    
    def func(self):
        parsed = parser(self.args)
        try:
            character = object_search(
                parsed['args'], typeclass='typeclasses.characters.Character')
        except:
            self.caller.msg('Something went wrong with the search')
        else:
            if len(character) == 0:
                self.caller.msg('I can\'t find character ' + parsed['args'])
            elif len(character) > 1:
                self.caller.msg('Too many possible matches for ' +
                                parsed['args'])
            else:
                try:
                    set(character[0],parsed['entry'],
                        subentry=parsed['subentry'],
                        statclass=parsed['statclass'],
                        value=parsed['value'])
                except:
                    self.caller.msg('Something went wrong setting the value:\n'
                                    + str(parsed))
                else:
                    message = parsed['entry']
                    if parsed['subentry'] != '':
                        message = message + '(' + parsed['subentry'] + ')'
                    message = message + ' set to ' + str(parsed['value']) + \
                              ' for ' + parsed['args']
                    self.caller.msg(message)
        
        