from evennia import ScriptDB

from operator import itemgetter

tribes = ScriptDB.objects.typeclass_search(
    'codes.stats.tribesScripts.tribeScript')
my_list = []
for item in tribes:
    my_list.append([item.db.longname, item])
tribes = sorted(my_list, key=itemgetter(0))
        
file = open('initTribes.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for tribe in tribes:
    name = tribe[1].db.longname.replace('\'','').replace(' ','_')
    file.write(
        'tribe = create_script(\'typeclasses.scripts.tribeScript\','
        'key = \'' + name + '\')\n')
    file.write(
        'tribe.db.longname = \'' +
        tribe[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write('tribe.db.renown = \''+tribe[1].db.renown+'\'\n')
    file.write(
        'tribe.db.tribe_gifts = ' + str(tribe[1].db.tribe_gifts) + '\n')
    file.write(
        'tribe.db.info = \'' +
        tribe[1].db.info.replace('\r\n', '|/').replace('\'', '\\\'') + '\'\n')
    file.write('tribe.db.reference = \''+tribe[1].db.reference+'\'\n')
    file.write('tribe.db.restricted = '+str(tribe[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()