from evennia.utils.search import search_script_tag
from evennia import ScriptDB

skills = ScriptDB.objects.typeclass_search('world.stats.skillScripts.skillScript')
        
file = open('initSkills.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for skill in skills:
    name = skill.db.longname.replace('\'','').replace(' ','_')
    file.write('skill = create_script(\'typeclasses.scripts.skillScript\',key = \'' + name + '\')\n')
    file.write('skill.db.longname = \''+skill.db.longname.replace('\'','\\\'')+'\'\n')
    file.write('skill.db.category = \''+skill.db.category+'\'\n')
    file.write('skill.db.restricted = '+str(skill.db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()