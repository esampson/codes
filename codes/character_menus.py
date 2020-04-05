from evennia.utils.evmenu import EvMenu
from evennia import Command
from codes.menus.menu_types import ExMenu


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
        ExMenu(self.caller, 'codes.menus.character_generation_menu', startnode = 'start')
        
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
        ExMenu(self.caller, 'codes.menus.xp_menu', startnode = 'start')
        
