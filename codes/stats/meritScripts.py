from codes.stats.codesScript import CodesScript


class MeritScript(CodesScript):

    # noinspection PyAttributeOutsideInit
    def at_script_creation(self):
        self.persistent = True  # will survive reload
        self.tags.add('stat_data')
        self.tags.add('merit_stat')

    # noinspection DuplicatedCode
    def update(self, longname='', category='', meritrange=None,
               noterestrictions='', prereq='', restricted=False,
               cg_only=False, reference='', info=''):
        self.db.longname = longname
        self.db.category = category
        self.db.range = meritrange
        self.db.noteRestrictions = noterestrictions
        self.db.prereq = prereq
        self.db.restricted = restricted
        self.db.cg_only = cg_only
        self.db.reference = reference
        self.db.info = info

    def get(self, target, subentry):
        """
        get


        Gets the value of a given merit from a target. Only returns a
        single value so subentry may be necessary in order to properly
        identify the merit if there are multiple merits on a character
        that begin with the same name.


        target: The character being checked
        subentry: Notes for merits. Mandatory in this case since a
            character may have a given merit multiple times with
            different notes.

        """
        r = []
        for merit in target.db.merits:
            if subentry == '' and self.db.longname == merit[0]:
                r.append(merit)
            elif (self.db.longname == merit[0] and
                  subentry.lower() == merit[2][0:len(subentry)].lower()):
                r.append(merit)
        if len(r) == 0:
            return 0
        elif len(r) > 1:
            return 'TOO_MANY_FOUND'
        else:
            return r[0][1]

    # noinspection PyUnusedLocal
    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to purchase a
        merit. Should only return True or False.


        target: The character being checked
        value: The level being checked.
        subentry: Notes for merits


        """
        if int(value) in self.db.range:
            if len(self.db.prereq) == 0:
                if (self.db.category.lower() == 'changeling' and
                        target.template().lower() != 'changeling'):
                    result = False
                elif (self.db.category.lower() == 'mage' and
                      target.template().lower() != 'mage'):
                    result = False
                elif (self.db.category.lower() == 'vampire' and
                      target.template().lower() != 'vampire'):
                    result = False
                elif (self.db.category.lower() == 'werewolf' and
                      target.template().lower() != 'werewolf'):
                    result = False
                elif (self.db.category.lower() == 'supernatural' and
                      target.template().lower() in ['changeling', 'mage',
                                                    'vampire', 'werewolf']):
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


        Determines the cost for a character to purchase or raise a
        merit.


        target: The character being checked
        value: The level being checked.
        subentry: Notes for merits


        """
        result = value - self.get(target, subentry)
        return result

    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of a merit on a character sheet. Adds the merit
        if the character does not currently possess it. Removes the
        merit if the value is 0.


        target: The character the merit is being set for
        value: The value the merit is being set to
        subentry: Notes for the merit


        """
        counter = 0
        count = -1
        meritlist = target.db.merits
        for item in meritlist:
            if (item[0].lower() == self.db.longname.lower()
                    and item[2].lower() == subentry.lower()):
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
