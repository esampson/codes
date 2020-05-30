from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

rites = ScriptDB.objects.typeclass_search('codes.stats.scalesScripts.ScaleScript')
my_list = []
for item in rites:
    my_list.append([item.db.longname, item])
rites = sorted(my_list, key=itemgetter(0))

file = open('initScales.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for item in rites:
    name = item[1].db.longname.replace('\'','').replace(' ','_')
    file.write('scale = create_script(\'typeclasses.scripts.ScaleScript\',key = \'' + name + '\')\n')
    file.write('scale.db.longname = \''+item[1].db.longname.replace('\'','\\\'') +'\'\n')
    file.write('scale.db.mystery = \''+item[1].db.mystery.replace('\'','\\\'') +'\'\n')
    file.write('scale.db.rank = '+str(item[1].db.rank) +'\n')
    file.write('scale.db.prereq = \''+item[1].db.prereq.replace('\'','\\\'')+'\'\n')
    file.write('scale.db.reference = \''+item[1].db.reference+'\'\n')
    file.write('scale.db.info = \''+item[1].db.info.replace('\r\n','|/').replace('\'','\\\'') +'\'\n')
    file.write('scale.db.restricted = '+str(item[1].db.restricted)+'\n')
    file.write('\n')
file.write('pass')
file.close()
