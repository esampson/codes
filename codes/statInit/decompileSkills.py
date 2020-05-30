from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

skills = ScriptDB.objects.typeclass_search('codes.stats.skillScripts.SkillScript')
my_list = []
for item in skills:
    my_list.append([item.db.longname, item])
skills = sorted(my_list, key=itemgetter(0))

file = open('initSkills.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for skill in skills:
    name = skill[1].db.longname.replace('\'','').replace(' ','_')
    file.write('skill = create_script(\'typeclasses.scripts.SkillScript\',key = \'' + name + '\')\n')
    file.write('skill.db.longname = \''+skill[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write('skill.db.category = \''+skill[1].db.category+'\'\n')
    file.write('skill.db.restricted = '+str(skill[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()
