from codes.stats.codesScript import codesScript

class basicStatScript(codesScript):
    
    def at_script_creation(self):
            self.persistent = True  # will survive reload
            self.db.longname = ''
            self.db.category = ''
            self.db.reference = ''
            self.db.info = ''
            self.db.restricted = False
            self.tags.add('stat_data')
            self.tags.add('basic_stat')
    
    def update(self,longname='', category='',restricted=False,reference='',
               info=''):
        self.db.longname = longname
        self.db.category = category
        self.db.restricted = restricted
        self.db.reference = reference
        self.db.info = info
        
    def get(self, target, subentry=''):
        """
        get


        Gets the value of a given basic attribute from a target. 


        target: The character being checked
        subentry: Dummy for overloading,

        """
        if self.db.longname in target.db.basics:
            result = target.db.basics[self.db.longname]
        else:
            result = False
        return result
    
    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        This is a dummy function since there are no prereqs for these stats
        
        
        """
        return True
    
    def cost(self, target, value=True, subentry=''):
        """
        cost


        This is a dummy function since there are no costs for these stats


        """
        return 0
                
    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of a stat on a character sheet. Adds the stat if the
        character does not currently possess it. Removes the stat if the value is
        False.


        target: The character the stat is being set for
        value: The value the stat is being set to
        subentry: Does nothing. Placeholder for overloading


        """
        name = self.db.longname
        if  name not in target.db.basics and value != False:
            target.db.basics[name] = value
            result = True
        elif name in target.db.basics and value == False:
            del target.db.basics[name]
            result = True
        elif name in target.db.basics and value != True:
            target.db.basics[name] = value
            result = True
        else:
            result = False
        return result