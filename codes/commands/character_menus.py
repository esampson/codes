from evennia import Command
from evennia import CmdSet

from world.evmenu import EvMenu


class CmdCG(Command):
    """
    Usage:
        +cg

    Begins character generation for those who have not completed it.
    Does not support any arguments.

    Examples:
        +cg

    """

    key = '+cg'
    help_category = 'OOC Commands'

    def func(self):
        obj_menu = 'codes.commands.character_menus.CharacterInMenu'
        act_menu = 'codes.commands.character_menus.AccountInMenu'
        self.caller.cmdset.add(obj_menu)
        self.caller.account.cmdset.add(act_menu)
        if self.caller.db.cg:
            menu = 'codes.menus.' + self.caller.db.cg['start_menu']
            node = self.caller.db.cg['start_node']
            if 'raw_string' in self.caller.db.cg:
                raw_string = self.caller.db.cg['raw_string']
            else:
                raw_string = ''
            if 'kwargs' in self.caller.db.cg:
                kwargs = dict(self.caller.db.cg['kwargs'])
            else:
                kwargs = dict()
            EvMenu(self.caller, menu, startnode=node,
                   cmdset_mergetype='Union', cmd_on_exit=None, auto_quit=False,
                   startnode_input=('p', kwargs))
        else:
            EvMenu(self.caller, 'codes.menus.cg', startnode='start',
                   cmdset_mergetype='Union', cmd_on_exit=None, auto_quit=False)


class CmdXP(Command):
    """
    Usage:
        +xp

    Shows current XP and leads to a menu for spending XP. Does not
    support any arguments.


    Examples:
        +xp

    """

    key = '+xp'
    help_category = 'OOC Commands'

    def func(self):
        EvMenu(self.caller, 'codes.menus.xp_menu', startnode='start',
               cmdset_mergetype='Union')


class CmdHelp(Command):
    """
    Dummy command so that menu help gets priority
    """

    key = 'help'

    def func(self):  # pragma: no cover
        pass  # pragma: no cover


class CmdQuit(Command):
    """
    Dummy command so that menu help gets priority
    """

    key = 'quit'

    def func(self):  # pragma: no cover
        pass  # pragma: no cover


class CmdInventory(Command):
    """
    Dummy command so that menu help gets priority
    """

    key = 'inventory'

    def func(self):  # pragma: no cover
        pass  # pragma: no cover


class CharacterInMenu(CmdSet):
    key = 'For use in menus'
    priority = 4
    mergetype = "Remove"

    def at_cmdset_creation(self):
        self.add(CmdHelp())
        self.add(CmdInventory())


class AccountInMenu(CmdSet):
    key = 'quit suppress'
    priority = 5
    mergetype = "Remove"

    def at_cmdset_creation(self):
        self.add(CmdQuit())
