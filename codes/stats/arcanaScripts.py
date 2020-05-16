from codes.stats.codesScript import codesScript
from evennia.utils.search import search_script_tag
from codes.data import find

restrict_level = False

sphere_limits = [[3,2], [3,3], [4,3], [4,4], [5,4], [5,5], [5,5], [5,5], [5,5],
                 [5,5]]

class arcanaScript(codesScript):

    def at_script_creation(self):
            self.persistent = True  # will survive reload
            self.db.longname = ''
            self.db.info = ''
            self.db.reference = ''
            self.db.restricted = False
            self.tags.add('stat_data')
            self.tags.add('arcana_stat')

    def update(self,longname='', info='', reference='',
               restricted=False):
                self.db.longname = longname
                self.db.info = info
                self.db.reference = reference
                self.db.restricted = restricted

    def get(self, target, subentry=''):
        """
        get


        Returns the value of an arcanum on a character.


        target: The character being checked
        subentry: Dummy for overloading

        """
        if target.db.arcana:
            if self.db.longname in target.db.arcana:
                result = target.db.arcana[self.db.longname]
            else:
                result = 0
        else:
            result = 0
        return result

    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to purchase an arcanum.
        Should only return True or False.


        target: The character being checked
        value: The level being checked.
        subentry: Seeming benefits


        """
        name = self.db.longname
        highest = 0
        for item in list(target.db.arcana.keys()):
            if target.db.arcana[item] > highest:
                highest = target.db.arcana[item]
        highest_max = sphere_limits[target.get('Gnosis',statclass='Power')+1][0]
        other_max = sphere_limits[target.get('Gnosis',
                                             statclass='Power') + 1][1]
        if target.template().lower() == 'mage':
            order = find(target.get('Order', statclass='Sphere'),
                         statclass='Order')[0]
            if name == order.db.inferior and value > 2 and restrict_level:
                result = False
            elif name != order.db.inferior and value > 4 and restrict_level:
                result = False
            elif value > highest_max:
                result = False
            elif value > other_max and highest == highest_max:
                result = False
            else:
                result = True
        return result

    def cost(self, target, value=True, subentry=''):
        """
        cost


        Determines the cost for a character to purchase an arcanum.


        target: The character being checked
        value: The level being checked.
        subentry: Dummy for overloading


        """
        name = self.db.longname
        current = self.get(target)
        path = find(target.get('Path',statclass='Sphere'),
                     statclass='Path')[0]
        if name == path.db.inferior_arcana and value > 2:
            result = 5 * (value - current)
        elif name != path.db.inferior_arcana and value > 4:
            result = 5 * (value - current)
        else:
            result = 4 * (value - current)
        return result

    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of an arcanum on a character sheet. Adds the arcanum if the
        character does not currently possess it. Removes the arcanum if the value is
        False.


        target: The character the arcanum is being set for
        value: The value the arcanum is being set to
        subentry: Dummy for overloading


        """
        name = self.db.longname
        if target.db.arcana:
            if name not in target.db.arcana and value != 0:
                target.db.arcana[name] = value
                result = True
            elif name in target.db.arcana and value == 0:
                del target.db.arcana[name]
                result = True
            elif name in target.db.arcana and value > 0:
                target.db.arcana[name] = value
                result = True
            else:
                result = False
        else:
            if value != 0:
                target.db.arcana = {name : value}
                result = True
            else:
                result = False
        return result

