from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

advantages = ScriptDB.objects.typeclass_search('codes.stats.advantageScripts.advantageScript')
my_list = []
for item in advantages:
    my_list.append([item.db.longname, item])
advantages = sorted(my_list, key=itemgetter(0))
        
file = open('initAdvantages.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for advantage in advantages:
    name = advantage[1].db.longname.replace('\'','').replace(' ','_')
    file.write('advantage = create_script(\'typeclasses.scripts.advantageScript\',key = \'' + name + '\')\n')
    file.write('advantage.db.longname = \''+advantage[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write('advantage.db.category = \''+advantage[1].db.category+'\'\n')
    file.write('advantage.db.reference = \''+advantage[1].db.reference+'\'\n')
    file.write('advantage.db.info = \''+advantage[1].db.info.replace('\'','\\\'')+'\'\n')
    file.write('advantage.db.simple_gauge = '+str(advantage[1].db.simple_gauge)+'\n')
    file.write('\n')
file.write ('pass')
file.close()