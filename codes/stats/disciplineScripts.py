from codes.stats.codesScript import CodesScript
from evennia.utils.search import search_script_tag


class DisciplineScript(CodesScript):

    # noinspection PyAttributeOutsideInit
    def at_script_creation(self):
        self.persistent = True  # will survive reload
        self.db.longname = ''
        self.db.prereq = ''
        self.db.reference = ''
        self.db.info = ''
        self.db.restricted = False
        self.tags.add('stat_data')
        self.tags.add('discipline_stat')

    def update(self, longname='', prereq='',
               restricted=False, reference='', info=''):
        self.db.longname = longname
        self.db.prereq = prereq
        self.db.restricted = restricted
        self.db.reference = reference
        self.db.info = info

    # noinspection PyUnusedLocal
    def get(self, target, subentry=''):
        """
        get


        Returns the value of a discipline on a character.


        target: The character being checked
        subentry: Dummy for overloading

        """
        if target.db.disciplines:
            if self.db.longname in target.db.disciplines:
                result = target.db.disciplines[self.db.longname]
            else:
                result = 0
        else:
            result = 0
        return result

    # noinspection PyUnusedLocal
    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to purchase a
        discipline. Should only return True or False.


        target: The character being checked
        value: The level being checked.
        subentry: Seeming benefits


        """
        if len(self.db.prereq) == 0:
            if target.template().lower() == 'vampire':
                result = True
            else:
                result = False
        else:
            if eval(self.db.prereq):
                result = True
            else:
                result = False
        return result

    # noinspection PyUnusedLocal
    def cost(self, target, value=True, subentry=''):
        """
        cost


        Determines the cost for a character to purchase a discipline.


        target: The character being checked
        value: The level being checked.
        subentry: Dummy for overloading


        """
        name = self.db.longname
        if target.db.disciplines:
            if name in target.db.disciplines:
                current = target.db.disciplines[name]
            else:
                current = 0
        else:
            current = 0
        amount = value - current
        clan = False
        clans = search_script_tag('clan_stat')
        for item in clans:
            if 'Clan' in target.db.sphere:
                if item.db.longname == target.db.sphere['Clan']:
                    clan = item
        if clan is not False:
            if self.db.longname in clan.db.favored_disciplines:
                result = amount * 3
            else:
                result = amount * 4
        else:
            raise Exception('Character has no clan')
        return result

    # noinspection DuplicatedCode,PyUnusedLocal
    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of a discipline on a character sheet. Adds the
        discipline if the character does not currently possess it.
        Removes the discipline if the value is False.


        target: The character the discipline is being set for
        value: The value the discipline is being set to
        subentry: Dummy for overloading


        """
        name = self.db.longname
        if target.db.disciplines:
            if name not in target.db.disciplines and value != 0:
                target.db.disciplines[name] = value
                result = True
            elif name in target.db.disciplines and value == 0:
                del target.db.disciplines[name]
                result = True
            elif name in target.db.disciplines and value > 0:
                target.db.disciplines[name] = value
                result = True
            else:
                result = False
        else:
            if value != 0:
                target.db.disciplines = {name: value}
                result = True
            else:
                result = False
        return result

