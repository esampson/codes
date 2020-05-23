from codes.stats.codesScript import codesScript


class ClanScript(codesScript):

    def __init__(self):
        self.persistent = True  # will survive reload

    def at_script_creation(self):
        self.db.longname = ''
        self.db.favored_attributes = []
        self.db.favored_disciplines = []
        self.db.reference = ''
        self.db.info = ''
        self.db.bloodline = False
        self.db.restricted = False
        self.tags.add('stat_data')
        self.tags.add('clan_stat')

    # noinspection DuplicatedCode
    def update(self, longname='', favored_attributes=None,
               favored_disciplines=None, bloodline=False, restricted=False,
               reference='', info=''):
        if favored_disciplines is None:
            favored_disciplines = []
        if favored_attributes is None:
            favored_attributes = []
        self.db.longname = longname
        self.db.favored_attributes = favored_attributes
        self.db.favored_disciplines = favored_disciplines
        self.db.bloodline = bloodline
        self.db.restricted = restricted
        self.db.reference = reference
        self.db.info = info

    # noinspection PyUnusedLocal
    @staticmethod
    def get(target, subentry=''):
        """
        get


        Gets the value of a given sphere attribute from a target.


        target: The character being checked
        subentry: Dummy for overloading,

        """

        return False

    # noinspection PyUnusedLocal
    @staticmethod
    def meets_prereqs(target, value=0, subentry=''):
        """
        meets_prereqs


        This is a dummy function since there are no prereqs for these
        stats


        """
        return True

    # noinspection PyUnusedLocal
    @staticmethod
    def cost(target, value=True, subentry=''):
        """
        cost


        This is a dummy function since there are no costs for these
        stats


        """
        return 0

    # noinspection PyUnusedLocal
    @staticmethod
    def set(target, value, subentry=''):
        """
        set


        Sets the value of a stat on a character sheet. Adds the stat if
        the character does not currently possess it. Removes the stat if
        the value is False.


        target: The character the stat is being set for
        value: The value the stat is being set to
        subentry: Does nothing. Placeholder for overloading


        """

        return False
