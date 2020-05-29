from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

kiths = ScriptDB.objects.typeclass_search('codes.stats.kithScripts.KithScript')
my_list = []
for item in kiths:
    my_list.append([item.db.longname, item])
kiths = sorted(my_list, key=itemgetter(0))

file = open('initKiths.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for kith in kiths:
    name = kith[1].db.longname.replace('\'','').replace(' ','_')
    file.write('kith = create_script(\'typeclasses.scripts.KithScript\',key = \'' + name + '\')\n')
    file.write('kith.db.longname = \''+kith[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write('kith.db.reference = \''+kith[1].db.reference+'\'\n')
    file.write('kith.db.info = \''+kith[1].db.info.replace('\r\n','|/').replace('\'','\\\'')+'\'\n')
    file.write('kith.db.restricted = '+str(kith[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()
