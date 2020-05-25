from codes.stats.codesScript import CodesScript
from evennia.utils.search import search_script_tag
from codes.data import find

class spellScript(CodesScript):

    def at_script_creation(self):
            self.persistent = True  # will survive reload
            self.db.longname = ''
            self.db.prereq = ''
            self.db.reference = ''
            self.db.info = ''
            self.db.restricted = False
            self.tags.add('stat_data')
            self.tags.add('spell_stat')

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


        Determines if a character meets the prerequisites to cast a spell. Useful
        because it will still interface with +prove to show that a character has the
        ability to cast a given spell.


        target: The character being checked
        subentry: Dummy for overloading

        """
        if eval(self.db.prereq):
            result = True
        else:
            result = False
        return result

    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to cast a spell.
        Should only return True or False. Needed primarily for purchasing rotes and
        praxes and for overloading.


        target: The character being checked
        value: The level being checked.
        subentry: Seeming benefits


        """
        if eval(self.db.prereq):
            result = True
        else:
            result = False
        return result

    def cost(self, target, value=True, subentry=''):
        """
        cost


        Because mages do not actually buy spells this is a dummy function that exists
        purely for overloading


        target: The character being checked
        value: The level being checked.
        subentry: Dummy for overloading


        """
        result = 0
        return result

    def set(self, target, value, subentry=''):
        """
        set


        Because mages do not actually buy spells this is a dummy function that exists
        purely for overloading


        target: Dummy for overloading
        value: Dummy for overloading
        subentry: Dummy for overloading


        """
        result = False
        return result

