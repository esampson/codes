from evennia.utils.search import search_script_tag
from evennia import ScriptDB

from operator import itemgetter

spells = ScriptDB.objects.typeclass_search('codes.stats.spellScripts.spellScript')
my_list = []
for item in spells:
    my_list.append([item.db.longname, item])
spells = sorted(my_list, key=itemgetter(0))
        
file = open('initSpells.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for spell in spells:
    name = spell[1].db.longname.replace('\'','').replace(' ','_')
    file.write('spell = create_script(\'typeclasses.scripts.spellScript\',key = \'' + name + '\')\n')
    file.write('spell.db.longname = \''+spell[1].db.longname.replace('\'','\\\'') +'\'\n')
    file.write('spell.db.prereq = \''+spell[1].db.prereq.replace('\'','\\\'')+'\'\n')
    file.write('spell.db.info = \''+spell[1].db.info.replace('\r\n','|/').replace('\'','\\\'') +'\'\n')
    file.write('spell.db.reference = \''+spell[1].db.reference+'\'\n')
    file.write('spell.db.restricted = '+str(spell[1].db.restricted)+'\n')
    file.write('\n')
file.write('pass')
file.close()