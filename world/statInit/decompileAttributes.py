from evennia.utils.search import search_script_tag
from evennia import ScriptDB

attributes = ScriptDB.objects.typeclass_search('world.stats.attributeScripts.attributeScript')
        
file = open('initAttributes.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for attribute in attributes:
    name = attribute.db.longname.replace('\'','').replace(' ','_')
    file.write('attribute = create_script(\'typeclasses.scripts.attributeScript\',key = \'' + name + '\')\n')
    file.write('attribute.db.longname = \''+attribute.db.longname.replace('\'','\\\'')+'\'\n')
    file.write('attribute.db.category = \''+attribute.db.category+'\'\n')
    file.write('attribute.db.row = \''+attribute.db.row+'\'\n')
    file.write('attribute.db.restricted = '+str(attribute.db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()