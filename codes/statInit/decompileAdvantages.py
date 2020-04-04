from evennia.utils.search import search_script_tag
from evennia import ScriptDB

advantages = ScriptDB.objects.typeclass_search('codes.stats.advantageScripts.advantageScript')
        
file = open('initAdvantages.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for advantage in advantages:
    name = advantage.db.longname.replace('\'','').replace(' ','_')
    file.write('advantage = create_script(\'typeclasses.scripts.advantageScript\',key = \'' + name + '\')\n')
    file.write('advantage.db.longname = \''+advantage.db.longname.replace('\'','\\\'')+'\'\n')
    file.write('advantage.db.category = \''+advantage.db.category+'\'\n')
    file.write('advantage.db.reference = \''+advantage.db.reference+'\'\n')
    file.write('advantage.db.info = \''+advantage.db.info.replace('\'','\\\'')+'\'\n')
    file.write('advantage.db.simple_gauge = '+str(advantage.db.simple_gauge)+'\n')
    file.write('\n')
file.write ('pass')
file.close()