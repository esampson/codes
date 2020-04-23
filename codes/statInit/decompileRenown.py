from evennia import ScriptDB

from operator import itemgetter

renowns = ScriptDB.objects.typeclass_search('codes.stats.renownScripts.renownScript')
my_list = []
for item in renowns:
    my_list.append([item.db.longname, item])
renowns = sorted(my_list, key=itemgetter(0))
        
file = open('initRenown.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for renown in renowns:
    name = renown[1].db.longname.replace('\'','').replace(' ','_')
    file.write('renown = create_script(\'typeclasses.scripts.renownScript\',key = \'' + name + '\')\n')
    file.write('renown.db.longname = \''+renown[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write('renown.db.reference = \'' + renown[1].db.reference + '\'\n')
    file.write('renown.db.info = \'' + renown[1].db.info.replace('\r\n', '|/').replace('\'', '\\\'') + '\'\n')
    file.write('renown.db.restricted = '+str(renown[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()