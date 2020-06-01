from codes.commands.stat_commands import CmdHurt
from codes.commands.stat_commands import CmdHeal
from codes.commands.stat_commands import CmdSheet
from codes.commands.stat_commands import CmdList
from codes.commands.stat_commands import CmdInfo
from codes.commands.stat_commands import CmdProve
from codes.commands.stat_commands import CmdPool

from codes.commands.character_menus import CmdCG
from codes.commands.character_menus import CmdXP

from codes.commands.dice import CmdRoll

from evennia import CmdSet


class AllCharacters(CmdSet):
    key = 'all_characters'

    def at_cmdset_creation(self):
        self.add(CmdInfo())
        self.add(CmdList())


class FinishedCharacter(CmdSet):
    key = 'finished_character'

    def at_cmdset_creation(self):
        self.add(CmdSheet())
        self.add(CmdXP())
        self.add(CmdRoll())
        self.add(CmdHurt())
        self.add(CmdHeal())
        self.add(CmdProve())
        self.add(CmdPool())


class UnfinishedCharacter(CmdSet):
    key = 'unfinished_character'

    def at_cmdset_creation(self):
        self.add(CmdCG())
