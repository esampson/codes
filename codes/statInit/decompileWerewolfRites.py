
from evennia import ScriptDB

from operator import itemgetter

rites = ScriptDB.objects.typeclass_search('codes.stats.werewolfRitesScripts.WerewolfRiteScript')
my_list = []
for item in rites:
    my_list.append([item.db.longname, item])
rites = sorted(my_list, key=itemgetter(0))

file = open('initWerewolfRites.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for rite in rites:
    name = rite[1].db.longname.replace('\'','').replace(' ','_')
    file.write('rite = create_script(\'typeclasses.scripts.WerewolfRiteScript\',key = \'' + name + '\')\n')
    file.write('rite.db.longname = \''+rite[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write('rite.db.type = \''+rite[1].db.type+'\'\n')
    file.write('rite.db.rank = '+str(rite[1].db.rank)+'\n')
    file.write('rite.db.prereq = \''+rite[1].db.prereq.replace('\'','\\\'')+'\'\n')
    file.write('rite.db.info = \''+rite[1].db.info.replace('\r\n','|/').replace('\'','\\\'')+'\'\n')
    file.write('rite.db.reference = \''+rite[1].db.reference+'\'\n')
    file.write('rite.db.restricted = '+str(rite[1].db.restricted)+'\n')
    file.write('\n')
file.write('pass')
file.close()
