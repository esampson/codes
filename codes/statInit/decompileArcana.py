from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

arcana = ScriptDB.objects.typeclass_search('codes.stats.arcanaScripts.arcanaScript')
my_list = []
for item in arcana:
    my_list.append([item.db.longname, item])
arcana = sorted(my_list, key=itemgetter(0))
        
file = open('initArcana.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for arcanum in arcana:
    name = arcanum[1].db.longname.replace('\'','').replace(' ','_')
    file.write('arcanum = create_script(\'typeclasses.scripts.arcanaScript\',key = \'' + name + '\')\n')
    file.write('arcanum.db.longname = \''+arcanum[1].db.longname.replace('\'','\\\'') +'\'\n')
    file.write('arcanum.db.info = \''+arcanum[1].db.info.replace('\r\n','|/').replace('\'','\\\'') +'\'\n')
    file.write('arcanum.db.reference = \''+arcanum[1].db.reference+'\'\n')
    file.write('arcanum.db.restricted = '+str(arcanum[1].db.restricted)+'\n')
    file.write('\n')
file.write('pass')
file.close()