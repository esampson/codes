from codes.stats.codesScript import codesScript

class lodgeScript(codesScript):
    
    def at_script_creation(self):
            self.persistent = True  # will survive reload
            self.db.longname = ''
            self.db.reference = ''
            self.db.info = ''
            self.db.restricted = False
            self.tags.add('stat_data')
            self.tags.add('lodge_stat')
    
    def update(self,longname='', renown = '', tribe_gifts=[],
               info='', reference='', restricted=False):
        self.db.longname = longname
        self.db.info = info
        self.db.reference = reference
        self.db.restricted = restricted
        
    def get(self, target, subentry=''):
        """
        get


        Gets the value of a given sphere attribute from a target. 


        target: The character being checked
        subentry: Dummy for overloading,

        """

        return False
    
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


        target: The character the statis being set for
        value: The value the stat is being set to
        subentry: Does nothing. Placeholder for overloading


        """
        
        return False
    