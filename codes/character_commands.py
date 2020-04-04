from codes.stat_commands import CmdHurt
from codes.stat_commands import CmdHeal
from codes.character_menus import CmdCG
from codes.stat_commands import CmdSheet
from codes.character_menus import CmdXP
from codes.dice import CmdRoll

from evennia import CmdSet

class finished_character(CmdSet):
    
    key = 'finished_character'
    
    def at_cmdset_creation(self):
        self.add(CmdSheet())
        self.add(CmdXP())
        self.add(CmdRoll())
        self.add(CmdHurt())
        self.add(CmdHeal())
        
class unfinished_character(CmdSet):
    
    key = 'unfinished_character'
    
    def at_cmdset_creation(self):
        self.add(CmdCG())