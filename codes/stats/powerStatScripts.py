from codes.stats.codesScript import CodesScript


class PowerStatScript(CodesScript):

    # noinspection PyAttributeOutsideInit
    def at_script_creation(self):
        self.persistent = True  # will survive reload
        self.tags.add('stat_data')
        self.tags.add('power_stat')

    def update(self, longname='', category='', info='', reference='',
               restricted=False,):
        self.db.longname = longname
        self.db.category = category
        self.db.reference = reference
        self.db.info = info
        self.db.restricted = restricted

    # noinspection PyUnusedLocal
    def get(self, target, subentry=''):
        """
        get


        Gets the value of a given powerStat from a target.


        target: The character being checked
        subentry: Dummy for overloading,

        """
        powers = target.db.power
        name = self.db.longname
        if name in powers:
            result = powers[name]
        else:
            result = 0
        return result

    # noinspection PyUnusedLocal
    @staticmethod
    def meets_prereqs(target, value=0, subentry=''):
        """
        meets_prereqs


        Just a dummy function for overloading


        target: The character being checked
        value: Dummy for overloading
        subentry: Dummy for overloading


        """
        result = True
        return result

    def cost(self, target, value, subentry=''):
        """
        cost


        Determines the cost for a character to raise a power stat.


        target: The character being checked
        value: The level being checked.
        subentry: Dummy for overloading


        """
        result = (value - self.get(target, subentry)) * 5
        return result

    # noinspection PyUnusedLocal
    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of an power stat on a character sheet. Adds the
        power stat if the character does not currently possess it.


        target: The character the stat is being set for
        value: The value the stat is being set to
        subentry: Dummy for overloading


        """
        name = self.db.longname
        target.db.power[name] = value
        return True



