from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

gifts = ScriptDB.objects.typeclass_search('codes.stats.giftsScripts.giftScript')
my_list = []
for item in gifts:
    my_list.append([item.db.longname, item])
gifts = sorted(my_list, key=itemgetter(0))
        
file = open('initGifts.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for gift in gifts:
    name = gift[1].db.longname.replace('\'','').replace(' ','_')
    file.write('gift = create_script(\'typeclasses.scripts.giftScript\',key = \'' + name + '\')\n')
    file.write('gift.db.longname = \''+gift[1].db.longname.replace('\'','\\\'') +'\'\n')
    file.write('gift.db.category = \''+gift[1].db.category+'\'\n')
    file.write('gift.db.group = \''+gift[1].db.group+'\'\n')
    file.write('gift.db.rank = \''+gift[1].db.rank+'\'\n')
    file.write('gift.db.renown = \'' + gift[1].db.renown + '\'\n')
    file.write('gift.db.reference = \''+gift[1].db.reference+'\'\n')
    file.write('gift.db.info = \''+gift[1].db.info.replace('\r\n','|/').replace('\'','\\\'') +'\'\n')
    file.write('gift.db.restricted = '+str(gift[1].db.restricted)+'\n')
    file.write('\n')
file.write('pass')
file.close()