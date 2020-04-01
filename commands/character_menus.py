from evennia.utils.evmenu import EvMenu
from evennia import Command




class CmdCG(Command):
    
    key = '+cg'
    
    def func(self):
        EvMenu(self.caller, 'character_menus.character_generation_menu', startnode = 'start')
        
class CmdXP(Command):
    
    key = '+xp'
    
    def func(self):
        EvMenu(self.caller, 'character_menus.xp_menu', startnode = 'start')
    