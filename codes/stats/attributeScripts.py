from typeclasses.scripts import Script

class attributeScript(Script):
    
    def at_script_creation(self):
            self.persistent = True  # will survive reload
            self.tags.add('stat_data')
            self.tags.add('attribute_stat')
                
    def update(self,longname='', category='', row='', restricted=False,cost=''):
        self.db.longname = longname
        self.db.category = category
        self.db.row = row
        self.db.restricted = restricted
    
    def get(self, target, subentry=''):
        """
        get


        Gets the value of a given attribute from a target. 


        target: The character being checked
        subentry: Dummy for overloading,

        """
        attributes = target.db.attributes
        name = self.db.longname
        if name in attributes:
            result = attributes[name]
        else:
            result = 0
        return result
        
    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to purchase an attribute. Should
        only return True or False.


        target: The character being checked
        value: The level being checked.
        subentry: Dummy for overloading


        """
        power = target.db.power
        key = list(power.keys())
        power_value = power[key[0]]
        if power_value < 6:
            max = 5
        else:
            max = power_value
        if value > max:
            result = False
        else:
            result = True
        return result
    
    def cost(self, target, value, subentry=''):
        """
        cost


        Determines the cost for a character to raise an attribute.


        target: The character being checked
        value: The level being checked.
        subentry: Dummy for overloading


        """
        result = (value - self.get(target, subentry)) * 4
        return result
    
    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of an attribute on a character sheet. Adds the attribute if the
        character does not currently possess it.


        target: The character the attribute is being set for
        value: The value the attribute is being set to
        subentry: Dummy for overloading


        """
        attributes = target.db.attributes
        name = self.db.longname
        target.db.attributes[name] = value
        return True
                
    
    
    