from codes.stats.codesScript import CodesScript

class cruacRiteScript(CodesScript):

    def at_script_creation(self):
            self.persistent = True  # will survive reload
            self.tags.add('stat_data')
            self.tags.add('cruac_rite_stat')

    def update(self,longname='', rank=1,
               prereq='', restricted=False, reference='',
               info=''):
        self.db.longname = longname
        self.db.rank = rank
        self.db.prereq = prereq
        self.db.restricted = restricted
        self.db.reference = reference
        self.db.info = info

    def get(self, target, subentry=''):
        """
        get


        Determines if a character has a given rite. Should only return True or
        False


        target: The character being checked
        subentry: Dummy for overloading

        """
        if target.db.cruacRites:
            if self.db.longname in target.db.cruacRites:
                result = True
            else:
                result = False
        else:
            result = False
        return result

    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to purchase a rite. Should
        only return True or False.


        target: The character being checked
        value: The level being checked.
        subentry: Dummy for overloading


        """
        if self.db.prereq:
            if eval(self.db.prereq):
                result = True
            else:
                result = False
        else:
            if (target.get('Cruac',statclass='Discipline') >= self.db.rank and
                target.get('Status', subentry='Circle of the Crone', statclass='Merit') >= 1):
                result = True
            else:
                result = False
        return result

    def cost(self, target, value, subentry=''):
        """
        cost


        Determines the cost for a character to purchase a rite.


        target: The character being checked
        value: Dummy for overloading
        subentry: Dummy for overloading


        """
        result = 2
        return result

    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of a rite on a character sheet if value is True. Removes
        the rite if the value is False.


        target: The character the rite is being set for
        value: The value the rite is being set to
        subentry: Dummy for overloading


        """
        if not target.db.cruacRites:
            target.db.cruacRites = {}
        name = self.db.longname
        if  name not in target.db.cruacRites and value == True:
            target.db.cruacRites[name] = True
            result = True
        elif name in target.db.cruacRites and value == False:
            del target.db.cruacRites[name]
            result = True
        elif name not in target.db.cruacRites and value == False:
            result = True
        else:
            result = True
        return result



