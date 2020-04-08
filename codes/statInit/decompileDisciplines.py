from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

disciplines = ScriptDB.objects.typeclass_search('codes.stats.disciplineScripts.disciplineScript')
my_list = []
for item in disciplines:
    my_list.append([item.db.longname, item])
disciplines = sorted(my_list, key=itemgetter(0))
        
file = open('initDisciplines.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for discipline in disciplines:
    name = discipline[1].db.longname.replace('\'','').replace(' ','_')
    file.write('discipline = create_script(\'typeclasses.scripts.disciplineScript\',key = \'' + name + '\')\n')
    file.write('discipline.db.longname = \''+discipline[1].db.longname.replace('\'','\\\'') +'\'\n')
    file.write('discipline.db.prereq = \''+discipline[1].db.prereq.replace('\'','\\\'')+'\'\n')
    file.write('discipline.db.reference = \''+discipline[1].db.reference+'\'\n')
    file.write('discipline.db.info = \''+discipline[1].db.info.replace('\r\n','|/').replace('\'','\\\'') +'\'\n')
    file.write('discipline.db.restricted = '+str(discipline[1].db.restricted)+'\n')
    file.write('\n')
file.write('pass')
file.close()