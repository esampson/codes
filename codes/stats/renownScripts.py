from codes.stats.codesScript import CodesScript


class RenownScript(CodesScript):

    # noinspection PyAttributeOutsideInit
    def at_script_creation(self):
        self.persistent = True  # will survive reload
        self.tags.add('stat_data')
        self.tags.add('renown_stat')

    def update(self, longname='', info="", reference="", restricted=False):
        self.db.longname = longname
        self.db.info = info
        self.db.reference = reference
        self.db.restricted = restricted

    # noinspection PyUnusedLocal
    def get(self, target, subentry=''):
        """
        get


        Gets the value of a given renown from a target.


        target: The character being checked
        subentry: Dummy for overloading,

        """
        renown = target.db.renown
        name = self.db.longname
        if renown and name in renown:
            result = renown[name]
        else:
            result = 0
        return result

    # noinspection PyUnusedLocal
    @staticmethod
    def meets_prereqs(target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to purchase a renown. Should
        only return True or False.


        target: The character being checked
        value: The level being checked.
        subentry: Dummy for overloading


        """
        if target.template().lower() == 'werewolf':
            if value >= 6 or value <= 0:
                result = False
            else:
                result = True
        else:
            result = False
        return result

    def cost(self, target, value, subentry=''):
        """
        cost


        Determines the cost for a character to raise a renown.


        target: The character being checked
        value: The level being checked.
        subentry: Dummy for overloading


        """
        result = (value - self.get(target, subentry)) * 3
        return result

    # noinspection PyUnusedLocal
    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of a renown on a character sheet. Adds the renown if the
        character does not currently possess it.


        target: The character the renown is being set for
        value: The value the renown is being set to
        subentry: Dummy for overloading


        """
        name = self.db.longname
        if target.db.renown:
            target.db.renown[name] = value
        else:
            target.db.renown = {name: value}
        return True
