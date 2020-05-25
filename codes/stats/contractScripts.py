from codes.stats.codesScript import CodesScript
from codes.data import find


class ContractScript(CodesScript):

    # noinspection PyAttributeOutsideInit
    def at_script_creation(self):
        self.persistent = True  # will survive reload
        self.db.longname = ''
        self.group = ''
        self.db.category = ''
        self.subgroup = ''
        self.db.reference = ''
        self.db.info = ''
        self.db.restricted = False
        self.tags.add('stat_data')
        self.tags.add('contract_stat')

    def update(self, longname='', group='', category='', subgroup='',
               restricted=False, reference='', info=''):
        self.db.longname = longname
        self.db.group = group
        self.db.category = category
        self.db.subgroup = subgroup
        self.db.restricted = restricted
        self.db.reference = reference
        self.db.info = info

    def get(self, target, subentry=''):
        """
        get


        Determines if a character possesses a contract


        target: The character being checked
        subentry: To check for Seeming Blessings

        """
        if self.db.longname in target.db.contracts and subentry == '':
            result = True
        elif (self.db.longname in target.db.contracts and
              subentry.lower() in
              target.db.contracts[self.db.longname].lower()):
            result = True
        else:
            result = False
        return result

    # noinspection PyUnusedLocal
    def meets_prereqs(self, target, value=0, subentry=''):
        """
        meets_prereqs


        Determines if a character meets the prerequisites to purchase a
        contract. Should only return True or False.


        target: The character being checked
        value: The level being checked.
        subentry: Seeming benefits


        """
        if target.template().lower() == 'changeling':
            if self.db.group.lower() == 'court':
                stat = []
                mantle = target.get('Mantle', subentry=self.db.category,
                                    statclass='Merit')
                goodwill = target.get('Court Goodwill',
                                      subentry=self.db.category,
                                      statclass='Merit')
                courts = {"spring": 0, "summer": 0, "autumn": 0, "winter": 0}
                contracts = list(target.db.contracts.keys())
                for contract in contracts:
                    stat = find(contract, statclass='contract')
                if len(contracts) > 0:
                    if stat[0].db.group.lower() == 'court':
                        court = stat[0].db.category.lower()
                        courts[court] = courts[court] + 1
                current_count = courts[self.db.category.lower()]
                if self.db.subgroup.lower() == 'common':
                    if current_count == 0:
                        result = True
                    elif mantle >= 1 or goodwill >= 3:
                        result = True
                    else:
                        result = False
                else:
                    if current_count == 0 and (mantle >= 3 or goodwill >= 4):
                        result = True
                    elif current_count >= 1 and (mantle >= 3 or goodwill == 5):
                        result = True
                    else:
                        result = False
            else:
                result = True
        else:
            result = False
        return result

    # noinspection DuplicatedCode,PyUnusedLocal
    def cost(self, target, value=True, subentry=''):
        """
        cost


        Determines the cost for a character to purchase a contract.


        target: The character being checked
        value: The level being checked.
        subentry: Seeming benefits


        """
        name = self.db.longname
        if self.db.group.lower() == 'regalia':
            if target.get(name, statclass='contract'):
                current_temp = (target.db.contracts[name].split(',') +
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
                    result = result - 1
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
            if target.get(name, statclass='contract'):
                result = 0
            else:
                if self.db.subgroup.lower() == 'common':
                    result = 3
                else:
                    result = 4
        else:
            if target.get(name, statclass='contract'):
                result = 0
            else:
                result = 2
        return result

    def set(self, target, value, subentry=''):
        """
        set


        Sets the value of a contract on a character sheet. Adds the
        contract if the character does not currently possess it. Removes
        the contract if the value is False.


        target: The character the contract is being set for
        value: The value the contract is being set to
        subentry: Any Seeming Benefits being added to the contract


        """
        name = self.db.longname
        # noinspection DuplicatedCode
        if name not in target.db.contracts and value is not False:
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
            new_entry = new_entry[0:len(new_entry) - 2]
            target.db.contracts[name] = new_entry
            result = True
        elif name in target.db.contracts and value is False:
            del target.db.contracts[name]
            result = True
        elif name in target.db.contracts and value is True:
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
            new_entry = new_entry[0:len(new_entry) - 2]
            target.db.contracts[name] = new_entry
            result = True
        else:
            result = False
        return result
