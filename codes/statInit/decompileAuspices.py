from evennia import ScriptDB

from operator import itemgetter

auspices = ScriptDB.objects.typeclass_search(
    'codes.stats.auspiceScripts.auspiceScript')
my_list = []
for item in auspices:
    my_list.append([item.db.longname, item])
auspices = sorted(my_list, key=itemgetter(0))

file = open('initAuspices.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for auspice in auspices:
    name = auspice[1].db.longname.replace('\'','').replace(' ','_')
    file.write(
        'auspice = create_script(\'typeclasses.scripts.AuspiceScript\','
        'key = \'' + name + '\')\n')
    file.write(
        'auspice.db.longname = \'' +
        auspice[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write(
        'auspice.db.auspice_skills = '+str(auspice[1].db.auspice_skills)+'\n')
    file.write('auspice.db.renown = \''+auspice[1].db.renown+'\'\n')
    file.write(
        'auspice.db.auspice_gifts = ' + str(auspice[1].db.auspice_gifts) + '\n')
    file.write(
        'auspice.db.info = \'' +
        auspice[1].db.info.replace('\r\n', '|/').replace('\'', '\\\'') + '\'\n')
    file.write('auspice.db.reference = \''+auspice[1].db.reference+'\'\n')
    file.write('auspice.db.restricted = '+str(auspice[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()
