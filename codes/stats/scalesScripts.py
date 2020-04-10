from codes.stats.codesScript import codesScript

class scaleScript(codesScript):
    
    def at_script_creation(self):
            self.persistent = True  # will survive reload
            self.tags.add('stat_data')
            self.tags.add('scale_stat')
                
    def update(self,longname='', mystery='', rank=1, 
               prereq='', restricted=False, reference='',
               info=''):
        self.db.longname = longname
        self.db.mystery = mystery
        self.db.rank = rank
        self.db.prereq = prereq
        self.db.restricted = restricted
        self.db.reference = reference
        self.db.info = info
    
    def get(self, target, subentry=''):
        """
        get


        Determines if a character has a given scale. Should only return True or
        False


        target: The character being checked
        subentry: Dummy for overloading

        """
        if target.db.scales:
            if self.db.longname in target.db.scales:
                result = True
        else:
            result = False
        return result
        
    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to purchase a scale. Should
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
            if target.get(self.db.mystery,statclass='Coil') > 0:
                result = True
            else:
                result = False
        return result
    
    def cost(self, target, value, subentry=''):
        """
        cost


        Determines the cost for a character to purchase a scale.


        target: The character being checked
        value: Dummy for overloading
        subentry: Dummy for overloading


        """
        if (target.get(self.db.mystery,statclass='Coil') >= 
            self.db.rank):
            result = 1
        else:
            result = 2
        return result
    
    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of a scale on a character sheet if value is True. Removes
        the scale if the value is False.


        target: The character the scale is being set for
        value: The value the scale is being set to
        subentry: Dummy for overloading


        """
        if not target.db.scales:
            target.db.scales = {}
        name = self.db.longname
        if  name not in target.db.scales and value == True:
            target.db.scales[name] = True
            result = True
        elif name in target.db.scales and value == False:
            del target.db.scales[name]
            result = True
        elif name not in target.db.scales and value == False:
            result = True
        elif name in target.db.scales and value == True:
            result = True
        else:
            result = False
        return result
                
    
    
    