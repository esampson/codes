from codes.stats.codesScript import codesScript
from codes.data import find

class giftScript(codesScript):
    
    def at_script_creation(self, longname='', category='', group='', rank='',
                           renown='', info='', reference='', restricted=False):
        """
        create_script('typeclasses.scripts.advantageScript'[,longname=<longname>]
            [,category=<category>][,group=<group>][,rank=<rank>][,renown=<renown>]
            [,info=<info>][,reference=<reference>][,restricted=<True/False>]

            longname: Name of gift
            category: Moon, Shadow, Wolf
            group: Crescent Moon, Dominance, Hunting
            rank: Only for Moon Gifts
            renown: Cunning, Glory, Honor, Purity, Wisdom
            info: Info for +info command
            reference: Page reference for +info command
            restricted: Whether gift is restricted
        """
        self.persistent = True  # will survive reload
        self.db.longname = longname
        self.db.category = category
        self.db.group = group
        self.db.rank = rank
        self.db.renown = renown
        self.db.info = info
        self.db.reference = reference
        self.db.restricted = restricted
        self.tags.add('stat_data')
        self.tags.add('gift_stat')
    
    def update(self, longname='', category='', group='', rank='', renown='',
                           info='', reference='', restricted=False):
        """
        update([longname=<longname>,][category=<category>,][group=<group>,]
            [rank=<rank>,][renown=<renown>,][info=<info>,]
            [reference=<reference>,][restricted=<True/False>]

            longname: Name of gift
            category: Moon, Shadow, Wolf
            group: Crescent Moon, Dominance, Hunting
            rank: Only for Moon Gifts
            renown: Cunning, Glory, Honor, Purity, Wisdom
            info: Info for +info command
            reference: Page reference for +info command
            restricted: Whether gift is restricted
        """
        self.db.longname = longname
        self.db.category = category
        self.db.group = group
        self.db.rank = rank
        self.db.renown = renown
        self.db.info = info
        self.db.reference = reference
        self.db.restricted = restricted
        
    def get(self, target, subentry=''):
        """
        get


        Determines if a character possesses a gift


        target: The character being checked
        subentry: To check for Seeming Blessings

        """
        if self.db.longname in target.db.gifts and subentry == '':
            result = True
        elif (self.db.longname in target.db.gifts and
              subentry.lower() in target.db.gifts[self.db.longname].lower()):
            result = True
        else:
            result = False
        return result
        
    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to purchase a gift.
        Should only return True or False.


        target: The character being checked
        value: Dummy for overloading
        subentry: Dummy for overloading
        
        
        """
        if target.template().lower() == 'werewolf':
            if self.db.category.lower() == 'moon':
                auspice = find(
                    target.get('Auspice',statclass='Sphere'),
                    statclass='Auspice')[0]
                auspice_gifts = auspice.db.auspice_gifts
                required_rank = self.db.rank
                auspice_renown = auspice.db.renown
                renown = target.get(auspice_renown,statclass='Renown')
                if self.db.group in auspice_gifts and int(required_rank) <= renown:
                    result = True
                else:
                    result = False
            else:
                result = False
        else:
            result = False
        return result
    
    def cost(self, target, value=True, subentry=''):
        """
        cost


        Determines the cost for a character to purchase a gift.


        target: The character being checked
        value: The level being checked.
        subentry: Seeming benefits


        """
        name = self.db.longname
        bonus = 0
        if self.db.group.lower() == 'regalia':
            if target.get(name, statclass='gift'):
                current_temp = (target.db.gifts[name].split(',') +
                                [target.get('Seeming', statclass='Sphere')])
                if subentry == '':
                    result = 0
                else:
                    new_temp = subentry.split(',')
                    current = set()
                    for entry in current_temp:
                        current.add(entry.strip())
                    new = set()
                    for entry in new_temp:
                        new.add(entry.strip())
                    result = len(new.difference(current))
            else:
                if self.db.subgroup.lower() == 'common':
                    result = 3
                else:
                    result = 4
                if self.db.category in target.get('Regalia', 
                                                  statclass='Sphere'):
                    result = result -1
                current_temp = ([target.get('Seeming', statclass='Sphere')] + 
                                [''])
                new_temp = subentry.split(',')
                current = set()
                for entry in current_temp:
                    current.add(entry.strip())
                new = set()
                for entry in new_temp:
                    new.add(entry.strip())
                if subentry != '':
                    result = result + len(new.difference(current))
        elif self.db.group.lower() == 'court':
            if target.get(name, statclass='gift'):
                result = 0
            else:
                if self.db.subgroup.lower() == 'common':
                    result = 3
                else:
                    result = 4
        else:
            if target.get(name, statclass='gift'):
                result = 0
            else:
                result = 2
        return result
                
    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of a gift on a character sheet. Adds the gift if the
        character does not currently possess it. Removes the gift if the value is
        False.


        target: The character the gift is being set for
        value: The value the gift is being set to
        subentry: Any Seeming Benefits being added to the gift


        """
        name = self.db.longname
        if  name not in target.db.gifts and value != False:
            current_temp = ([target.get('Seeming', statclass='Sphere')] +
                            [''])
            new_temp = subentry.split(',')
            current = set()
            for entry in current_temp:
                current.add(entry.strip())
            new = set()
            for entry in new_temp:
                new.add(entry.strip())
            new_entry = ''
            for entry in list(new.difference(current)):
                new_entry = new_entry + entry + ', '
            new_entry = new_entry[0:len(new_entry)-2]
            target.db.gifts[name] = new_entry
            result = True
        elif name in target.db.gifts and value == False:
            del target.db.gifts[name]
            result = True
        elif name in target.db.gifts and value == True:
            current_temp = ([target.get('Seeming', statclass='Sphere')] +
                            [''])
            new_temp = subentry.split(',')
            current = set()
            for entry in current_temp:
                current.add(entry.strip())
            new = set()
            for entry in new_temp:
                new.add(entry.strip())
            new_entry = ''
            for entry in list(new.difference(current)):
                new_entry = new_entry + entry + ', '
            new_entry = new_entry[0:len(new_entry)-2]
            target.db.gifts[name] = new_entry
            result = True
        else:
            result = False
        return result
                
                