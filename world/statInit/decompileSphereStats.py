from evennia.utils.search import search_script_tag
from evennia import ScriptDB

spheres = ScriptDB.objects.typeclass_search('world.stats.sphereStatScripts.sphereStatScript')
        
file = open('initSphereStats.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for sphere in spheres:
    name = sphere.db.longname.replace('\'','').replace(' ','_')
    file.write('sphere = create_script(\'typeclasses.scripts.sphereStatScript\',key = \'' + name + '\')\n')
    file.write('sphere.db.longname = \''+sphere.db.longname.replace('\'','\\\'')+'\'\n')
    file.write('sphere.db.category = \''+sphere.db.category+'\'\n')
    file.write('sphere.db.reference = \''+sphere.db.reference+'\'\n')
    file.write('sphere.db.info = \''+sphere.db.info.replace('\'','\\\'')+'\'\n')
    file.write('sphere.db.restricted = '+str(sphere.db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()