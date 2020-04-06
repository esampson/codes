from evennia.utils.search import search_script_tag
from evennia import search_script

import textwrap


def find(iString, statclass = ''):
    """
    findE


    Returns a list of data scripts which begin with iString. If statclass is
    specified the list is restricted to those whose type begins with statclass.

    """
    
    d = search_script_tag('dictionary_data')[0]
    if not hasattr(d, 'dictionary'):
        d.at_server_reload()
    matches = []
    if iString.lower() in d.dictionary:
        stats = d.dictionary[iString.lower()]
        for stat in stats:
            typeclass = stat[1][0:len(statclass)].lower()
            if statclass == '':
                matches.append(search_script('#'+str(stat[2]))[0])
            elif typeclass == statclass.lower():
                matches.append(search_script('#'+str(stat[2]))[0])
    return matches

def get(target, entry, subentry='', statclass=''):
    """
    get


    Gets the value of a given stat from a target. Only returns a single value so
    statclass may be neccessary in order to properly identify the stat if there
    are multiple stats that begin with the same name.


    target: The character being checked
    entry: The stat being looked for
    subentry: Notes for merits, for gauge stats, valid values are permanent, 
        temporary, bashing, lethal, and aggravated.
    statclass: Category of stat

    """
    if len(entry.split(':'))  == 2:
        if entry.split(':')[1] == '*':
            result = 0
            for specialty in target.db.specialties:
                if specialty.split(':')[0].lower() == entry.split(':')[0].lower():
                    result = 1
        else:
            if entry in target.db.specialties:
                result = 1
            else:
                result = 0
    else:
        stat_list = find(entry, statclass=statclass)
        if len(stat_list) == 0:
            raise Exception('StatError: ' + entry + 'NOT FOUND')
        elif len(stat_list) > 1:
            raise Exception('StatError: ' + 'TOO MANY FOUND FOR '+ entry)
        else:
            stat = stat_list[0]
            result = stat.get(target,subentry=subentry)            
    return result
    
def meets_prereqs(target, entry, value=0, subentry='', statclass=''):
    """
    meets_prereqs


    Determines if a character meets the prerequisites to purchase a stat. Should
    only return True or False.


    target: The character being checked
    entry: The stat being looked for
    value: The level being checked.
    subentry: Notes for merits, for gauge stats, valid values are permanent, 
        temporary, bashing, lethal, and aggravated.
    search_type: Category of stat


    """
    stat_list = find(entry, statclass)
    if len(stat_list) == 0:
        raise Exception('StatError: ' + entry + 'NOT FOUND')
    elif len(stat_list) > 1:
        raise Exception('StatError: ' + 'TOO MANY FOUND FOR '+ entry)
    else:
        stat = stat_list[0]
        result = stat.meets_prereqs(target, value=value, subentry=subentry)
        return result
    
def cost(target, entry, value, subentry='', statclass=''):
    """
    cost


    Determines the cost for a character to raise a stat


    target: The character being checked
    entry: The stat being looked for
    value: The level being checked.
    subentry: Notes for merits, for gauge stats, valid values are permanent, 
        temporary, bashing, lethal, and aggravated.
    statclass: Force the category of stat


    """
    stat_list = find(entry, statclass)
    if len(stat_list) == 0:
        raise Exception('StatError: ' + entry + 'NOT FOUND')
    elif len(stat_list) > 1:
        raise Exception('StatError: ' + 'TOO MANY FOUND FOR '+ entry)
    else:
        stat = stat_list[0]
        result = stat.cost(target, value=value, subentry=subentry)         
        return result
    
def set(target, entry, value, subentry='', statclass=''):
    """
    set


    Sets the value of a stat on a character sheet. Adds the stat if the character
    does not currently possess it. Removes the stat if the value is 0 for stats
    such as merits or False for stats such as contracts.


    target: The character the stat is being set for
    entry: The name of the stat being set.
    value: The value the stat is being set to.
    subentry: Secondary information for the stat
    statclass: Force the category of the stat
    

        """
    if len(entry.split(':')) == 2:     #routing to handle specialties
        if value == False:
            target.db.specialties.remove(entry)
            result = True
        elif value == True:
            target.db.specialties.append(entry)
            result = True
        else:
            result = False
    else:
        stat_list = find(entry, statclass)
        if len(stat_list) == 0:
            raise Exception('StatError: ' + entry + 'NOT FOUND')
        elif len(stat_list) > 1:
            raise Exception('StatError: ' + 'TOO MANY FOUND FOR '+ entry)
        else:
            stat = stat_list[0]
            result = stat.set(target, value=value, subentry=subentry)
    return result
    
