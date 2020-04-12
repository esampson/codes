from codes.commands.stat_commands import CmdHurt
from codes.commands.stat_commands import CmdHeal
from codes.commands.stat_commands import CmdSheet
from codes.commands.stat_commands import CmdList
from codes.commands.stat_commands import CmdInfo
from codes.commands.stat_commands import CmdProve

from codes.commands.character_menus import CmdCG
from codes.commands.character_menus import CmdXP

from codes.commands.dice import CmdRoll

from evennia import CmdSet

class all_characters(CmdSet):
    
    key = 'all_characters'
    
    def at_cmdset_creation(self):
        self.add(CmdInfo())
        self.add(CmdList())

class finished_character(CmdSet):
    
    key = 'finished_character'
    
    def at_cmdset_creation(self):
        self.add(CmdSheet())
        self.add(CmdXP())
        self.add(CmdRoll())
        self.add(CmdHurt())
        self.add(CmdHeal())
        self.add(CmdProve())
        
class unfinished_character(CmdSet):
    
    key = 'unfinished_character'
    
    def at_cmdset_creation(self):
        self.add(CmdCG())