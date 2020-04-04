from evennia.utils.search import search_script_tag
from evennia import ScriptDB

powers = ScriptDB.objects.typeclass_search('codes.stats.powerStatScripts.powerStatScript')
        
file = open('initPowerStats.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for power in powers:
    name = power.db.longname.replace('\'','').replace(' ','_')
    file.write('power = create_script(\'typeclasses.scripts.powerStatScript\',key = \'' + name + '\')\n')
    file.write('power.db.longname = \''+power.db.longname.replace('\'','\\\'')+'\'\n')
    file.write('power.db.category = \''+power.db.category+'\'\n')
    file.write('power.db.reference = \''+power.db.reference+'\'\n')
    file.write('power.db.info = \''+power.db.info.replace('\'','\\\'')+'\'\n')
    file.write('power.db.restricted = '+str(power.db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()