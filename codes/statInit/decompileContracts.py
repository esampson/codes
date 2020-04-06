from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

contracts = ScriptDB.objects.typeclass_search('codes.stats.contractScripts.contractScript')
my_list = []
for item in contracts:
    my_list.append([item.db.longname, item])
contracts = sorted(my_list, key=itemgetter(0))
        
file = open('initContracts.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for contract in contracts:
    name = contract[1].db.longname.replace('\'','').replace(' ','_')
    file.write('contract = create_script(\'typeclasses.scripts.contractScript\',key = \'' + name + '\')\n')
    file.write('contract.db.longname = \''+contract[1].db.longname.replace('\'','\\\'') +'\'\n')
    file.write('contract.db.category = \''+contract[1].db.category+'\'\n')
    file.write('contract.db.group = \''+contract[1].db.group+'\'\n')
    file.write('contract.db.subgroup = \''+contract[1].db.subgroup+'\'\n')
    file.write('contract.db.reference = \''+contract[1].db.reference+'\'\n')
    file.write('contract.db.info = \''+contract[1].db.info.replace('\r\n','|/').replace('\'','\\\'') +'\'\n')
    file.write('contract.db.restricted = '+str(contract[1].db.restricted)+'\n')
    file.write('\n')
file.write('pass')
file.close()