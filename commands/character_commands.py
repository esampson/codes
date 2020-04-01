from commands.stat_commands import CmdSheet
from commands.character_menus import CmdXP
from commands.dice import CmdRoll

from evennia import CmdSet

class finished_character(CmdSet):
    
    key = 'finished_character'
    
    def at_cmdset_creation(self):
        self.add(CmdSheet())
        self.add(CmdXP())
        self.add(CmdRoll())