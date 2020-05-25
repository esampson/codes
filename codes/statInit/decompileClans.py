from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

clans = ScriptDB.objects.typeclass_search('codes.stats.clanScripts.clanScript')
my_list = []
for item in clans:
    my_list.append([item.db.longname, item])
clans = sorted(my_list, key=itemgetter(0))

file = open('initClans.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for clan in clans:
    name = clan[1].db.longname.replace('\'','').replace(' ','_')
    file.write('clan = create_script(\'typeclasses.scripts.ClanScript\',key = \'' + name + '\')\n')
    file.write('clan.db.longname = \''+clan[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write('clan.db.favored_attributes = '+str(clan[1].db.favored_attributes)+'\n')
    file.write('clan.db.favored_disciplines = '+str(clan[1].db.favored_disciplines)+'\n')
    file.write('clan.db.reference = \''+clan[1].db.reference+'\'\n')
    file.write('clan.db.info = \''+clan[1].db.info.replace('\r\n','|/').replace('\'','\\\'')+'\'\n')
    file.write('clan.db.bloodline = '+str(clan[1].db.bloodline)+'\n')
    file.write('clan.db.restricted = '+str(clan[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()
