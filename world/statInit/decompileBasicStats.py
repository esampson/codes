from evennia.utils.search import search_script_tag
from evennia import ScriptDB

basics = ScriptDB.objects.typeclass_search('world.stats.basicStatScripts.basicStatScript')
        
file = open('initBasicStats.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for basic in basics:
    name = basic.db.longname.replace('\'','').replace(' ','_')
    file.write('basic = create_script(\'typeclasses.scripts.basicStatScript\',key = \'' + name + '\')\n')
    file.write('basic.db.longname = \''+basic.db.longname.replace('\'','\\\'')+'\'\n')
    if basic.db.category:
        file.write('basic.db.category = \''+basic.db.category+'\'\n')
    if basic.db.reference:
        file.write('basic.db.reference = \''+basic.db.reference+'\'\n')
    if basic.db.info:
        file.write('basic.db.info = \''+basic.db.info.replace('\'','\\\'')+'\'\n')
    if basic.db.restricted:
        file.write('basic.db.restricted = '+str(basic.db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()