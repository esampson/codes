from evennia.utils.evmenu import EvMenu
from evennia import Command
from character_menus.menu_types import XPMenu


class CmdCG(Command):
    
    key = '+cg'
    
    def func(self):
        XPMenu(self.caller, 'character_menus.character_generation_menu', startnode = 'start')
        
class CmdXP(Command):
    
    key = '+xp'
    
    def func(self):
        XPMenu(self.caller, 'character_menus.xp_menu', startnode = 'start')
    