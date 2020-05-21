from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

merits = ScriptDB.objects.typeclass_search('codes.stats.meritScripts.meritScript')
my_list = []
for item in merits:
    my_list.append([item.db.longname, item])
merits = sorted(my_list, key=itemgetter(0))

file = open('initMerits.py','w')
file.write('from evennia import create_script\n')
file.write('\nfrom codes import data\n')
file.write('\n')
for merit in merits:
    name = merit[1].db.longname.replace('\'','').replace(' ','_')
    file.write('stats = data.find(\'' + name + '\',statclass=\'Merit\')\n')
    file.write('if len(stats) == 0:\n')
    file.write('    merit = create_script(\'typeclasses.scripts.meritScript\',key = \'' + name + '\')\n')
    file.write('    merit.db.longname = \''+merit[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write('    merit.db.category = \''+merit[1].db.category+'\'\n')
    file.write('    merit.db.range = '+str(merit[1].db.range)+'\n')
    file.write('    merit.db.prereq = \''+merit[1].db.prereq.replace('\'','\\\'')+'\'\n')
    file.write('    merit.db.noteRestrictions = '+str(merit[1].db.noteRestrictions)+'\n')
    file.write('    merit.db.reference = \''+merit[1].db.reference+'\'\n')
    file.write('    merit.db.info = \''+merit[1].db.info.replace('\r\n','|/').replace('\'','\\\'')+'\'\n')
    file.write('    merit.db.cg_only = '+str(merit[1].db.cg_only)+'\n')
    file.write('    merit.db.restricted = '+str(merit[1].db.restricted)+'\n')
    file.write('\n')
file.write('pass')
file.close()
