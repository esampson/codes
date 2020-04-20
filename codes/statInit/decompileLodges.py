from evennia import ScriptDB

from operator import itemgetter

lodges = ScriptDB.objects.typeclass_search(
    'codes.stats.lodgesScripts.lodgeScript')
my_list = []
for item in lodges:
    my_list.append([item.db.longname, item])
lodges = sorted(my_list, key=itemgetter(0))
        
file = open('initLodges.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for lodge in lodges:
    name = lodge[1].db.longname.replace('\'','').replace(' ','_')
    file.write(
        'lodge = create_script(\'typeclasses.scripts.lodgeScript\','
        'key = \'' + name + '\')\n')
    file.write(
        'lodge.db.longname = \'' +
        lodge[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write(
        'lodge.db.info = \'' +
        lodge[1].db.info.replace('\r\n', '|/').replace('\'', '\\\'') + '\'\n')
    file.write('lodge.db.reference = \''+lodge[1].db.reference+'\'\n')
    file.write('lodge.db.restricted = '+str(lodge[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()