from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

rites = ScriptDB.objects.typeclass_search('codes.stats.thebanRitesScripts.ThebanRiteScript')
my_list = []
for item in rites:
    my_list.append([item.db.longname, item])
rites = sorted(my_list, key=itemgetter(0))

file = open('initTheban.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for item in rites:
    name = item[1].db.longname.replace('\'','').replace(' ','_')
    file.write('theban = create_script(\'typeclasses.scripts.ThebanRiteScript\',key = \'' + name + '\')\n')
    file.write('theban.db.longname = \''+item[1].db.longname.replace('\'','\\\'') +'\'\n')
    file.write('theban.db.rank = '+str(item[1].db.rank) +'\n')
    file.write('theban.db.prereq = \''+item[1].db.prereq.replace('\'','\\\'')+'\'\n')
    file.write('theban.db.reference = \''+item[1].db.reference+'\'\n')
    file.write('theban.db.info = \''+item[1].db.info.replace('\r\n','|/').replace('\'','\\\'') +'\'\n')
    file.write('theban.db.restricted = '+str(item[1].db.restricted)+'\n')
    file.write('\n')
file.write('pass')
file.close()
