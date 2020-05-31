from codes.stats.codesScript import CodesScript


class WerewolfRiteScript(CodesScript):

    # noinspection PyAttributeOutsideInit
    def at_script_creation(self):
        self.persistent = True  # will survive reload
        self.tags.add('stat_data')
        self.tags.add('werewolf_rite_stat')

    def update(self, longname='', rite_type='', rank=1, prereq='', info='',
               reference='', restricted=False):
        self.db.longname = longname
        self.db.type = rite_type
        self.db.rank = rank
        self.db.prereq = prereq
        self.db.info = info
        self.db.reference = reference
        self.db.restricted = restricted

    # noinspection PyUnusedLocal
    def get(self, target, subentry=''):
        """
        get


        Determines if a character has a given rite. Should only return
        True or False


        target: The character being checked
        subentry: Dummy for overloading

        """
        if target.db.werewolfRites:
            if self.db.longname in target.db.werewolfRites:
                result = True
            else:
                result = False
        else:
            result = False
        return result

    # noinspection PyUnusedLocal
    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to purchase a
        rite. Should only return True or False.


        target: The character being checked
        value: Dummy for overloading
        subentry: Dummy for overloading


        """
        if self.db.prereq and self.db.prereq != '':
            if eval(self.db.prereq):
                result = True
            else:
                result = False
        elif target.template().lower() == 'werewolf':
            result = True
        else:
            result = False
        return result

    # noinspection PyUnusedLocal
    def cost(self, target, value, subentry=''):
        """
        cost


        Determines the cost for a character to purchase a rite.


        target: The character being checked
        value: Dummy for overloading
        subentry: Dummy for overloading


        """
        result = self.db.rank
        return result

    # noinspection DuplicatedCode,PyUnusedLocal
    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of a rite on a character sheet if value is True.
        Removes the rite if the value is False.


        target: The character the rite is being set for
        value: The value the rite is being set to
        subentry: Dummy for overloading


        """
        if not target.db.werewolfRites:
            target.db.werewolfRites = {}
        name = self.db.longname
        if name not in target.db.werewolfRites and value is True:
            target.db.werewolfRites[name] = True
            result = True
        elif name in target.db.werewolfRites and value is False:
            del target.db.werewolfRites[name]
            result = True
        elif name not in target.db.werewolfRites and value is False:
            result = True
        else:
            result = True
        return result
