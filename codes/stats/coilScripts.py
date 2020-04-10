from codes.stats.codesScript import codesScript
from evennia.utils.search import search_script_tag
from codes.data import find

class coilScript(codesScript):
    
    def at_script_creation(self):
            self.persistent = True  # will survive reload
            self.db.longname = ''
            self.db.prereq = ''
            self.db.reference = ''
            self.db.info = ''
            self.db.restricted = False
            self.tags.add('stat_data')
            self.tags.add('coil_stat')
    
    def update(self,longname='', prereq='',
               restricted=False,reference='',info=''):
                self.db.longname = longname
                self.db.prereq = prereq
                self.db.restricted = restricted
                self.db.reference = reference
                self.db.info = info
        
    def get(self, target, subentry=''):
        """
        get


        Returns the value of a coil on a character.


        target: The character being checked
        subentry: Dummy for overloading

        """
        if target.db.coils:
            if self.db.longname in target.db.coils:
                result = target.coils[self.db.longname]
        else:
            result = 0
        return result
        
    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to purchase a coil. 
        Should only return True or False.


        target: The character being checked
        value: The level being checked.
        subentry: Seeming benefits
        
        
        """
        name = self.db.longname
        if (target.db.sphere and 
            'Covenant' in target.db.sphere and 
            target.db.sphere['Covenant'] == 'Ordo Dracul'):
            
            #Coil is mystery coil
            if ('Mystery Coil' in target.db.sphere and 
                target.db.sphere['Mystery Coil'] == name):
                if self.db.prereq:
                    if eval(self.db.prereq) and value <= 5:
                        result = True
                    else:
                        result = False
                if value <= 5:
                    result = True
                else:
                    result = False
            
            #coil is not Mystery Coil
            else:
                if target.db.coils:
                    if 'Mystery Coil' in target.db.sphere:
                        mystery = target.db.sphere['Mystery Coil']
                    else:
                        mystery = ''
                    non_mystery = 0
                    if target.db.coils:
                        for item in list(target.db.coils.keys()):
                            if item != name and item != mystery:
                                non_mystery = (non_mystery + 
                                    target.db.sphere['Mystery Coil'])
                    non_mystery = non_mystery + value
                    if non_mystery > target.get('Status', 
                                                subentry='Ordo Dracul', 
                                                statclass='Merit'):
                        result = False
                    else:
                        if self.db.prereq:
                            if eval(self.db.prereq) and value <= 5:
                                result = True
                            else:
                                result = False
                        if value <= 5:
                            result = True
                        else:
                            result = False
        else:
            result = False

        return result
    
    def cost(self, target, value=True, subentry=''):
        """
        cost


        Determines the cost for a character to purchase a coil.


        target: The character being checked
        value: The level being checked.
        subentry: Dummy for overloading


        """
        name = self.db.longname
        if target.db.coils and name in target.db.coils:
            current = target.db.coils[name]
        else:
            current = 0
        amount = value - current
        if (target.db.sphere and 'Mystery Coil' in target.db.sphere and 
            name != target.sd.sphere['Mystery Coil']):
            result = amount * 4
        else:
            result = amount * 3      
        return result
                
    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of a coil on a character sheet. Adds the coil if the
        character does not currently possess it. Removes the coil if the value is
        False.


        target: The character the coil is being set for
        value: The value the coil is being set to
        subentry: Dummy for overloading


        """
        name = self.db.longname
        if value > 0:
            if target.db.coils:
                target.db.coils[name] = value
                result = True
            else:
                target.db.coils = { name : value }
                result = True
            if target.db.sphere:
                if 'Mystery Coil' not in target.db.sphere:
                    target.db.sphere['Mystery Coil'] = name
            else:
                target.db.sphere = { 'Mystery Coil' : name }
        if value == 0:
            if target.db.coils and name in target.db.coils:
                del target.db.coils[name]
            result = True
        else:
            result = False
        return result
                
                