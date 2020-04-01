from evennia.utils.search import search_script_tag
from evennia import ScriptDB

contracts = ScriptDB.objects.typeclass_search('world.stats.contractScripts.contractScript')
        
file = open('initContracts.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for contract in contracts:
    name = contract.db.longname.replace('\'','').replace(' ','_')
    file.write('contract = create_script(\'typeclasses.scripts.contractScript\',key = \'' + name + '\')\n')
    file.write('contract.db.longname = \''+contract.db.longname.replace('\'','\\\'') +'\'\n')
    file.write('contract.db.category = \''+contract.db.category+'\'\n')
    file.write('contract.db.group = \''+contract.db.group+'\'\n')
    file.write('contract.db.subgroup = \''+contract.db.subgroup+'\'\n')
    file.write('contract.db.reference = \''+contract.db.reference+'\'\n')
    file.write('contract.db.info = \''+contract.db.info.replace('\r\n','|/').replace('\'','\\\'') +'\'\n')
    file.write('contract.db.restricted = '+str(contract.db.restricted)+'\n')
    file.write('\n')
file.write('pass')
file.close()