from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

devotions = ScriptDB.objects.typeclass_search('codes.stats.devotionScripts.DevotionScript')
my_list = []
for item in devotions:
    my_list.append([item.db.longname, item])
devotions = sorted(my_list, key=itemgetter(0))

file = open('initDevotions.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for devotion in devotions:
    name = devotion[1].db.longname.replace('\'','').replace(' ','_')
    file.write('devotion = create_script(\'typeclasses.scripts.DevotionScript\',key = \'' + name + '\')\n')
    file.write('devotion.db.longname = \''+devotion[1].db.longname.replace('\'','\\\'') +'\'\n')
    file.write('devotion.db.cost = '+str(devotion[1].db.cost) +'\n')
    file.write('devotion.db.prereq = \''+devotion[1].db.prereq.replace('\'','\\\'')+'\'\n')
    file.write('devotion.db.reference = \''+devotion[1].db.reference+'\'\n')
    file.write('devotion.db.info = \''+devotion[1].db.info.replace('\r\n','|/').replace('\'','\\\'') +'\'\n')
    file.write('devotion.db.restricted = '+str(devotion[1].db.restricted)+'\n')
    file.write('\n')
file.write('pass')
file.close()
