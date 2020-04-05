from evennia.utils.search import search_script_tag
from evennia import ScriptDB

kiths = ScriptDB.objects.typeclass_search('codes.stats.kithScripts.kithScript')
        
file = open('initKiths.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for kith in kiths:
    name = kith.db.longname.replace('\'','').replace(' ','_')
    file.write('kith = create_script(\'typeclasses.scripts.kithScript\',key = \'' + name + '\')\n')
    file.write('kith.db.longname = \''+kith.db.longname.replace('\'','\\\'')+'\'\n')
    file.write('kith.db.reference = \''+kith.db.reference+'\'\n')
    file.write('kith.db.info = \''+kith.db.info.replace('\r\n','|/').replace('\'','\\\'')+'\'\n')
    file.write('kith.db.restricted = '+str(kith.db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()