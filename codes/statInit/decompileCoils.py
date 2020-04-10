from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

coils = ScriptDB.objects.typeclass_search('codes.stats.coilScripts.coilScript')
my_list = []
for item in coils:
    my_list.append([item.db.longname, item])
coils = sorted(my_list, key=itemgetter(0))
        
file = open('initCoils.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for coil in coils:
    name = coil[1].db.longname.replace('\'','').replace(' ','_')
    file.write('coil = create_script(\'typeclasses.scripts.coilScript\',key = \'' + name + '\')\n')
    file.write('coil.db.longname = \''+coil[1].db.longname.replace('\'','\\\'') +'\'\n')
    file.write('coil.db.prereq = \''+coil[1].db.prereq.replace('\'','\\\'')+'\'\n')
    file.write('coil.db.reference = \''+coil[1].db.reference+'\'\n')
    file.write('coil.db.info = \''+coil[1].db.info.replace('\r\n','|/').replace('\'','\\\'') +'\'\n')
    file.write('coil.db.restricted = '+str(coil[1].db.restricted)+'\n')
    file.write('\n')
file.write('pass')
file.close()