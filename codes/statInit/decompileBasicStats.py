from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

basics = ScriptDB.objects.typeclass_search('codes.stats.basicStatScripts.basicStatScript')
my_list = []
for item in basics:
    my_list.append([item.db.longname, item])
basics = sorted(my_list, key=itemgetter(0))

file = open('initBasicStats.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for basic in basics:
    name = basic[1].db.longname.replace('\'','').replace(' ','_')
    file.write('basic = create_script(\'typeclasses.scripts.BasicStatScript\',key = \'' + name + '\')\n')
    file.write('basic.db.longname = \''+basic[1].db.longname.replace('\'','\\\'')+'\'\n')
    if basic[1].db.category:
        file.write('basic.db.category = \''+basic[1].db.category+'\'\n')
    if basic[1].db.reference:
        file.write('basic.db.reference = \''+basic[1].db.reference+'\'\n')
    if basic[1].db.info:
        file.write('basic.db.info = \''+basic[1].db.info.replace('\'','\\\'')+'\'\n')
    if basic[1].db.restricted:
        file.write('basic.db.restricted = '+str(basic[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()
