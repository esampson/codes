from codes.stats.codesScript import CodesScript

class devotionScript(CodesScript):

    def at_script_creation(self):
            self.persistent = True  # will survive reload
            self.tags.add('stat_data')
            self.tags.add('devotion_stat')

    def update(self,longname='', cost=0,
               prereq='', restricted=False, reference='',
               info=''):
        self.db.longname = longname
        self.db.cost = cost
        self.db.prereq = prereq
        self.db.restricted = restricted
        self.db.reference = reference
        self.db.info = info

    def get(self, target, subentry=''):
        """
        get


        Determines if a character has a given devotion. Should only return True or
        False


        target: The character being checked
        subentry: Dummy for overloading

        """
        if target.db.devotions:
            if self.db.longname in target.db.devotions:
                result = True
            else:
                result = False
        else:
            result = False
        return result

    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to purchase a devotion. Should
        only return True or False.


        target: The character being checked
        value: The level being checked.
        subentry: Dummy for overloading


        """
        if eval(self.db.prereq):
            result = True
        else:
            result = False
        return result

    def cost(self, target, value, subentry=''):
        """
        cost


        Determines the cost for a character to purchase a devotion.


        target: The character being checked
        value: Dummy for overloading
        subentry: Dummy for overloading


        """
        result = self.db.cost
        return result

    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of a devotion on a character sheet if value is True. Removes
        the devotion if the value is False.


        target: The character the devotion is being set for
        value: The value the devotion is being set to
        subentry: Dummy for overloading


        """
        if not target.db.devotions:
            target.db.devotions = {}
        name = self.db.longname
        if  name not in target.db.devotions and value == True:
            target.db.devotions[name] = True
            result = True
        elif name in target.db.devotions and value == False:
            del target.db.devotions[name]
            result = True
        elif name not in target.db.devotions and value == False:
            result = True
        else:
            result = True
        return result



