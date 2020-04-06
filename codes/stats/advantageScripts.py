from codes.stats.codesScript import codesScript

class advantageScript(codesScript):
    
    def at_script_creation(self):
            self.persistent = True  # will survive reload
            self.tags.add('stat_data')
            self.tags.add('advantage_stat')
                
    def update(self,longname='', category='',info='',reference='',simple_gauge=False):
        self.db.longname = longname
        self.db.category = category
        self.db.reference = reference
        self.db.info = info
        self.db.simple_gauge = simple_gauge
    
    def get(self, target, subentry=''):
        """
        get


        Gets the value of a given advantage from a target. 


        target: The character being checked
        subentry: [Temporary, Permanent, Bashing, Lethal, Aggravated, Bar]

        """
        advantages = target.db.advantages
        name = self.db.longname
        if self.db.simple_gauge and (subentry.lower() not in ['permanent', 'perm'] and subentry != ''):
            if subentry.lower() in ['temporary', 'temp']:
                if name in target.db.advantages:
                    result = target.db.advantages[name]
            elif subentry.lower() == 'bar':
                result_1 = ''
                max = self.get(target, subentry='Permanent')
                current = target.db.advantages[name]
                for box in range(max):
                    result_1 = result_1 +'['
                    if box <= max - current - 1:
                        result_1 = result_1 + 'X'
                    else:
                        result_1 = result_1 + ' '
                    result_1 = result_1 + ']'
                result = result_1
            else:
                result = False
        if name == 'Size':
            result = 5
            if target.get('Giant',statclass='Merit') == 3:
                result = result + 1
            if target.get('Small-Framed',statclass='Merit') == 2:
                result = result -1
        elif name == 'Speed':
            result = 5 + target.strength() + target.dexterity()
            result = result + target.get('Fleet of Foot',statclass='Merit')
            if target.get('Seeming',statclass='Sphere') == 'Beast':
                result = result + 3
        elif name == 'Defense':
            if target.wits() > target.dexterity():
                result = target.dexterity()
            else:
                result = target.wits()
            result = result + target.athletics()
        elif name == 'Initiative':
            result = target.dexterity() + target.composure()
            result = result + target.get('Fast Reflexes',statclass='Merit')
            if target.get('Seeming',statclass='Sphere') == 'Beast':
                result = result + 3
        elif name == 'Clarity':
            if subentry.lower() in ['permanent', 'perm'] or subentry == '':
                result = target.wits() + target.composure()
                result = result + target.get('Icons',statclass='Sphere')
        elif name == 'Integrity':
            result = target.db.advantages['Integrity']
        elif name == 'Willpower':
            if subentry.lower() in ['permanent', 'perm'] or subentry == '':
                result = target.resolve() + target.composure()
        elif name == 'Health':
            if subentry.lower() in ['permanent', 'perm'] or subentry == '':
                result = target.stamina() + target.get('Size',statclass='Advantage')
            elif subentry.lower() in ['bashing', 'bash']:
                if 'Health' in target.db.advantages:
                    result = target.db.advantages['Health'][0]
            elif subentry.lower() in ['lethal']:
                if 'Health' in target.db.advantages:
                    result = target.db.advantages['Health'][1]
            elif subentry.lower() in ['aggravated', 'agg']:
                if 'Health' in target.db.advantages:
                    result = target.db.advantages['Health'][2]
            elif subentry.lower() == 'bar':
                result = '['
                bash = target.db.advantages['Health'][0]
                lethal = target.db.advantages['Health'][1]
                agg = target.db.advantages['Health'][2]
                for box in range(self.get(target, subentry='Permanent')):
                    if box <= agg - 1:
                        result = result + '*'
                    elif box <= lethal + agg - 1:
                        result = result + 'X'
                    elif box <= bash + lethal + agg - 1:
                        result = result + '\\'
                    else:
                        result = result + ' '
                result = result + ']'
            else:
                result = False
        elif name == 'Glamour':
            if subentry.lower() in ['permanent', 'perm'] or subentry == '':
                pools = [10,11,12,13,15,20,25,30,50,75]
                result = pools[target.get('Wyrd',statclass='Power')-1]
            elif subentry.lower() in ['temporary', 'temp']:
                if 'Clarity' in target.db.advantages:
                    result = target.db.advantages['Glamour']
            else:
                result = False
        else:
            result = False
        return result
        
    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Dummy function for overloading


        """
        result = False
        return result
    
    def cost(self, target, value, subentry=''):
        """
        cost


        Dummy function for overloading


        """
        return False
    
    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of an advantage on a character sheet. Adds the advantage if the
        character does not currently possess it. Primarily for modifying pools. It
        should be noted that with pools what is actually being tracked are losses, not
        totals, so 0 means a character's pool is at full value.


        target: The character the advantage is being set for
        value: The value the advantage is being set to
        subentry: [Temporary, Permanent, Bashing, Lethal, Aggravated]


        """
        name = self.db.longname
        if name == 'Willpower':
            if subentry.lower() in ['permanent', 'perm']:
                result = False
            elif subentry.lower() in ['temporary', 'temp'] or subentry == '':
                target.db.advantages['Willpower'] = target.resolve() + target.composure() - value
                result = True
        elif name == 'Clarity':
            if subentry.lower() in ['permanent', 'perm']:
                result = False
            elif subentry.lower() in ['temporary', 'temp'] or subentry == '':
                target.db.advantages['Clarity'] = target.wits() + target.composure() - value
                result = True
        elif name == 'Integrity':
            target.db.advantages['Integrity'] = value
            result = True
        elif name == 'Glamour':
            if subentry.lower() in ['permanent', 'perm']:
                result = False
            elif subentry.lower() in ['temporary', 'temp'] or subentry == '':
                pools = [10,11,12,13,15,20,25,30,50,75]
                pool = pools[target.get('Wyrd',statclass='Power')-1]
                target.db.advantages['Glamour'] = pool - value
                result = True
        elif name == 'Health':
            if subentry.lower() in ['permanent', 'perm'] or subentry == '':
                result = False
            elif subentry.lower() in ['bashing', 'bash']:
                target.db.advantages['Health'][0] = value
                result = True
            elif subentry.lower() in ['lethal']:
                target.db.advantages['Health'][1] = value
                result = True
            elif subentry.lower() in ['aggravated', 'agg']:
                target.db.advantages['Health'][2] = value
                result = True
            else:
                result = False
        else:
            result = False
        return result
                
    
    
    