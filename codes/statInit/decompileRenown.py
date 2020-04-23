from evennia import ScriptDB

from operator import itemgetter

attributes = ScriptDB.objects.typeclass_search('codes.stats.renownScripts.renownScript')
my_list = []
for item in attributes:
    my_list.append([item.db.longname, item])
attributes = sorted(my_list, key=itemgetter(0))
        
file = open('initRenown.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for attribute in attributes:
    name = attribute[1].db.longname.replace('\'','').replace(' ','_')
    file.write('attribute = create_script(\'typeclasses.scripts.attributeScript\',key = \'' + name + '\')\n')
    file.write('attribute.db.longname = \''+attribute[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write('attribute.db.restricted = '+str(attribute[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()