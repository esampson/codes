from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

seemings = ScriptDB.objects.typeclass_search('codes.stats.seemingScripts.SeemingScript')
my_list = []
for item in seemings:
    my_list.append([item.db.longname, item])
seemings = sorted(my_list, key=itemgetter(0))

file = open('initSeemings.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for seeming in seemings:
    name = seeming[1].db.longname.replace('\'','').replace(' ','_')
    file.write('seeming = create_script(\'typeclasses.scripts.SeemingScript\',key = \'' + name + '\')\n')
    file.write('seeming.db.longname = \''+seeming[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write('seeming.db.favored_attributes = '+str(seeming[1].db.favored_attributes)+'\n')
    file.write('seeming.db.regalia = \''+seeming[1].db.regalia+'\'\n')
    file.write('seeming.db.reference = \''+seeming[1].db.reference+'\'\n')
    file.write('seeming.db.info = \''+seeming[1].db.info.replace('\r\n','|/').replace('\'','\\\'')+'\'\n')
    file.write('seeming.db.restricted = '+str(seeming[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()
