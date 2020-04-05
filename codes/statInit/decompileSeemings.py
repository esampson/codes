from evennia.utils.search import search_script_tag
from evennia import ScriptDB

seemings = ScriptDB.objects.typeclass_search('codes.stats.seemingScripts.seemingScript')
        
file = open('initSeemings.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for seeming in seemings:
    name = seeming.db.longname.replace('\'','').replace(' ','_')
    file.write('seeming = create_script(\'typeclasses.scripts.seemingScript\',key = \'' + name + '\')\n')
    file.write('seeming.db.longname = \''+seeming.db.longname.replace('\'','\\\'')+'\'\n')
    file.write('seeming.db.bonus_attributes = '+str(seeming.db.bonus_attributes)+'\n')
    file.write('seeming.db.regalia = \''+seeming.db.regalia+'\'\n')
    file.write('seeming.db.reference = \''+seeming.db.reference+'\'\n')
    file.write('seeming.db.info = \''+seeming.db.info.replace('\r\n','|/').replace('\'','\\\'')+'\'\n')
    file.write('seeming.db.restricted = '+str(seeming.db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()