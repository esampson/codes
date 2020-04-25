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
        subentry: Dummy for overloading
        """
        if target.db.gifts and self.db.longname in target.db.gifts:
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

            # Check auspice renown for rank of Moon Gift
            if self.db.category.lower() == 'moon':
                auspice = find(
                    target.get('Auspice',statclass='Sphere'),
                    statclass='Auspice')[0]
                auspice_gifts = auspice.db.auspice_gifts
                required_rank = self.db.rank
                auspice_renown = auspice.db.renown
                renown = target.get(auspice_renown,statclass='Renown')
                if (self.db.group in auspice_gifts and
                        int(required_rank) <= renown):
                    result = True
                else:
                    result = False

            # Check to see if target has any renown of the proper type
            else:
                gift_renown = self.db.renown
                renown = target.get(gift_renown,statclass='Renown')
                if renown >= 1:
                    result = True
                else:
                    result = False

        # Not a werewolf, no Gifts for you
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

        # Already have it
        if target.db.gifts and name in target.db.gifts:
            result = 0

        # Moon Gift which are free
        elif self.db.category.lower() == 'moon':
            result = 0

        # Wolf Gift
        elif self.db.category.lower() == 'wolf':
            result = 1

        # Shadow Gift and target has gifts to check
        elif target.db.gifts:

            # Is it unlocked
            group = self.db.group
            possess_facet = False
            for item in list(target.db.gifts.keys()):
                if find(item,statclass="Gift")[0].db.group == group:
                    possess_facet = True

            # Not unlocked
            if possess_facet == False:

                # Is it favored
                tribe = find(target.get('Tribe',statclass='Sphere'))[0]
                auspice = find(target.get('Auspice', statclass='Sphere'))[0]

                # Favored
                if (group in tribe.db.tribe_gifts or
                        group in auspice.db.auspice_gifts):
                    result = 3

                # Not favored
                else:
                    result = 5

            # Unlocked
            else:
                result = 2

        else:
            group = self.db.group

            # Is it favored
            tribe = find(target.get('Tribe', statclass='Sphere'))[0]
            auspice = find(target.get('Auspice', statclass='Sphere'))[0]

            # Favored
            if (group in tribe.db.tribe_gifts or
                    group in auspice.db.auspice_gifts):
                result = 3

            # Not favored
            else:
                result = 5

        return result
                
    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of a gift on a character sheet. Adds the gift if the
        character does not currently possess it. Removes the gift if the value is
        False.


        target: The character the gift is being set for
        value: The value the gift is being set to
        subentry: Dummy for overloading


        """
        name = self.db.longname

        # target.db.gifts doesn't exist
        if not target.db.gifts and value == True:
            target.db.gifts = {name : True}
            result = True
        elif not target.db.gifts and value == False:
            result = True

        # Not in target.db.gifts
        elif name not in target.db.gifts and value == True:
            target.db.gifts[name] = True
            result = True
        elif name not in target.db.gifts and value == False:
            result = True

        # In target.db.gifts
        elif name in target.db.gifts and value == True:
            result = True
        else:
            del target.db.gifts[name]
            result = True

        return result
                
                