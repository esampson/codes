from typeclasses.scripts import Script

class meritScript(Script):
    
    def at_script_creation(self):
            self.persistent = True  # will survive reload
            self.tags.add('stat_data')
            self.tags.add('merit_stat')
                
    def update(self,longname='', category='',range=[], noteRestrictions='',
               prereq='',restricted=False,cost='',cg_only=False,reference='',
               info=''):
        self.db.longname = longname
        self.db.category = category
        self.db.range = range
        self.db.noteRestrictions = noteRestrictions
        self.db.prereq = prereq
        self.db.restricted = restricted
        self.db.cost = cost
        self.db.cg_only = cg_only
        self.db.reference = reference
        self.db.info = info
    
    def get(self, target, subentry):
        """
        get


        Gets the value of a given merit from a target. Only returns a single value so 
        subentry may be neccessary in order to properly identify the merit if there
        are multiple merits on a character that begin with the same name.


        target: The character being checked
        subentry: Notes for merits,

        """
        r = []
        for merit in target.db.merits:
            t = False
            if subentry == '' and self.db.longname == merit[0]:
                r.append(merit)
            elif (self.db.longname == merit[0] and 
                  subentry.lower() == merit[2][0:len(subentry)].lower()):
                r.append(merit)
        if len(r) == 0:
            return 0
        elif len(r) > 1:
            return TOO_MANY_FOUND
        else:
            return r[0][1]
        
    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to purchase a merit. Should
        only return True or False.


        target: The character being checked
        value: The level being checked.
        subentry: Notes for merits


        """
        if int(value) in self.db.range:
            if len(self.db.prereq) == 0:
                if (self.db.category.lower() == 'changeling' and 
                    target.template().lower() != 'changeling'):
                    result = False
                elif (self.db.category.lower() == 'supernatural' and 
                    target.template().lower() == 'changeling'):
                    result = False 
                else:   
                    result = True
            else:
                if eval(self.db.prereq):
                    result = True
                else:
                    result = False
        else:
            result = False
        return result
    
    def cost(self, target, value, subentry=''):
        """
        cost


        Determines the cost for a character to purchase or raise a merit.


        target: The character being checked
        value: The level being checked.
        subentry: Notes for merits


        """
        if len(self.db.cost) == 0:
            result = value - self.get(target, subentry)
        else:
            result = exec(self.db.cost)
        return result
    
    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of a merit on a character sheet. Adds the merit if the character
        does not currently possess it. Removes the merit if the value is 0.


        target: The character the merit is being set for
        value: The value the merit is being set to
        subentry: Notes for the merit


        """
        counter = 0
        count = -1
        list = target.db.merits
        for item in list:
            if (item[0].lower() == self.db.longname.lower() and item[2].lower() == subentry.lower()):
                count = counter
            counter = counter + 1
        if count == -1 and value != 0:
            target.db.merits.append([self.db.longname, value, subentry])
            result = True
        elif count != -1 and value == 0:
            del target.db.merits[count]
            result = True
        elif count != -1 and value != 0:
            target.db.merits[count] = [self.db.longname, value, subentry]
            result = True
        else:
            result = False
        return result
                
    
    
    