from evennia import ScriptDB

from operator import itemgetter

paths = ScriptDB.objects.typeclass_search(
    'codes.stats.pathScripts.PathScript')
my_list = []
for item in paths:
    my_list.append([item.db.longname, item])
paths = sorted(my_list, key=itemgetter(0))

file = open('initPaths.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for path in paths:
    name = path[1].db.longname.replace('\'','').replace(' ','_')
    file.write(
        'path = create_script(\'typeclasses.scripts.PathScript\','
        'key = \'' + name + '\')\n')
    file.write(
        'path.db.longname = \'' +
        path[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write(
        'path.db.ruling_arcana = ' + str(path[1].db.ruling_arcana) + '\n')
    file.write('path.db.inferior_arcana = \''+path[1].db.inferior_arcana+'\'\n')

    file.write(
        'path.db.info = \'' +
        path[1].db.info.replace('\r\n', '|/').replace('\'', '\\\'') + '\'\n')
    file.write('path.db.reference = \''+path[1].db.reference+'\'\n')
    file.write('path.db.restricted = '+str(path[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()
