from codes.stats.codesScript import CodesScript


class SkillScript(CodesScript):

    # noinspection PyAttributeOutsideInit
    def at_script_creation(self):
        self.persistent = True  # will survive reload
        self.tags.add('stat_data')
        self.tags.add('skill_stat')

    def update(self, longname='', category='', restricted=False):
        self.db.longname = longname
        self.db.category = category
        self.db.restricted = restricted

    # noinspection PyUnusedLocal
    def get(self, target, subentry=''):
        """
        get


        Gets the value of a given skill from a target.


        target: The character being checked
        subentry: Dummy for overloading,

        """
        skills = target.db.skills
        name = self.db.longname
        if name in skills:
            result = skills[name]
        else:
            result = 0
        return result

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to purchase a
        skill. Should only return True or False.


        target: The character being checked
        value: The level being checked.
        subentry: Dummy for overloading


        """
        power = target.db.power
        key = list(power.keys())
        power_value = power[key[0]]
        if power_value < 6:
            skill_max = 5
        else:
            skill_max = power_value
        if value > skill_max:
            result = False
        else:
            result = True
        return result

    def cost(self, target, value, subentry=''):
        """
        cost


        Determines the cost for a character to raise a skill.


        target: The character being checked
        value: The level being checked.
        subentry: Dummy for overloading


        """
        result = (value - self.get(target, subentry)) * 2
        return result

    # noinspection PyUnusedLocal
    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of a skill on a character sheet. Adds the skill
        if the character does not currently possess it.


        target: The character the skill is being set for
        value: The value the skill is being set to
        subentry: Dummy for overloading


        """
        name = self.db.longname
        target.db.skills[name] = value
        return True
