from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

covenants = ScriptDB.objects.typeclass_search('codes.stats.covenantScripts.covenantScript')
my_list = []
for item in covenants:
    my_list.append([item.db.longname, item])
covenants = sorted(my_list, key=itemgetter(0))
        
file = open('initCovenants.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for covenant in covenants:
    name = covenant[1].db.longname.replace('\'','').replace(' ','_')
    file.write('covenant = create_script(\'typeclasses.scripts.covenantScript\',key = \'' + name + '\')\n')
    file.write('covenant.db.longname = \''+covenant[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write('covenant.db.reference = \''+covenant[1].db.reference+'\'\n')
    file.write('covenant.db.info = \''+covenant[1].db.info.replace('\r\n','|/').replace('\'','\\\'')+'\'\n')
    file.write('covenant.db.restricted = '+str(covenant[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()