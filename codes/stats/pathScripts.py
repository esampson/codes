from codes.stats.codesScript import CodesScript


class PathScript(CodesScript):

    # noinspection DuplicatedCode,PyAttributeOutsideInit
    def at_script_creation(self):
        self.persistent = True  # will survive reload
        self.db.longname = ''
        self.db.ruling_arcana = []
        self.db.inferior_arcana = ''
        self.db.reference = ''
        self.db.info = ''
        self.db.restricted = False
        self.tags.add('stat_data')
        self.tags.add('path_stat')

    def update(self, longname='', ruling_arcana=None, inferior_arcana='',
               info='', reference='', restricted=False):
        self.db.longname = longname
        self.db.ruling_arcana = ruling_arcana
        self.db.inferior_arcana = inferior_arcana
        self.db.info = info
        self.db.reference = reference
        self.db.restricted = restricted

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
