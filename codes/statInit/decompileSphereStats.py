from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

spheres = ScriptDB.objects.typeclass_search('codes.stats.sphereStatScripts.sphereStatScript')
my_list = []
for item in spheres:
    my_list.append([item.db.longname, item])
spheres = sorted(my_list, key=itemgetter(0))
        
file = open('initSphereStats.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for sphere in spheres:
    name = sphere[1].db.longname.replace('\'','').replace(' ','_')
    file.write('sphere = create_script(\'typeclasses.scripts.sphereStatScript\',key = \'' + name + '\')\n')
    file.write('sphere.db.longname = \''+sphere[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write('sphere.db.category = \''+sphere[1].db.category+'\'\n')
    file.write('sphere.db.reference = \''+sphere[1].db.reference+'\'\n')
    file.write('sphere.db.info = \''+sphere[1].db.info.replace('\'','\\\'')+'\'\n')
    file.write('sphere.db.restricted = '+str(sphere[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()