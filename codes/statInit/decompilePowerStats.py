from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

powers = ScriptDB.objects.typeclass_search('codes.stats.powerStatScripts.powerStatScript')
my_list = []
for item in powers:
    my_list.append([item.db.longname, item])
powers = sorted(my_list, key=itemgetter(0))

file = open('initPowerStats.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for power in powers:
    name = power[1].db.longname.replace('\'','').replace(' ','_')
    file.write('power = create_script(\'typeclasses.scripts.powerStatScript\',key = \'' + name + '\')\n')
    file.write('power.db.longname = \''+power[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write('power.db.category = \''+power[1].db.category+'\'\n')
    file.write('power.db.reference = \''+power[1].db.reference+'\'\n')
    file.write('power.db.info = \''+power[1].db.info.replace('\'','\\\'')+'\'\n')
    file.write('power.db.restricted = '+str(power[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()