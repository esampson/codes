from evennia.utils.evmenu import EvMenu
from evennia import Command
from character_menus.menu_types import XPMenu


class CmdCG(Command):
    """
    Usage:
        +cg
        
    Begins character generation for those who have not completed it. Does not 
    support any arguments.
        
    Examples:
        +cg
            
    """
    
    key = '+cg'
    
    def func(self):
        XPMenu(self.caller, 'character_menus.character_generation_menu', startnode = 'start')
        
class CmdXP(Command):
    """
    Usage:
        +xp
        
    Shows current XP and leads to a menu for spending XP. Does not support any
    arguments.
    
        
    Examples:
        +xp
            
    """
    
    key = '+xp'
    
    def func(self):
        XPMenu(self.caller, 'character_menus.xp_menu', startnode = 'start')
    