from evennia.utils.search import search_script_tag
from evennia import ScriptDB

merits = ScriptDB.objects.typeclass_search('codes.stats.meritScripts.meritScript')
        
file = open('initMerits.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for merit in merits:
    name = merit.db.longname.replace('\'','').replace(' ','_')
    file.write('merit = create_script(\'typeclasses.scripts.meritScript\',key = \'' + name + '\')\n')
    file.write('merit.db.longname = \''+merit.db.longname.replace('\'','\\\'')+'\'\n')
    file.write('merit.db.category = \''+merit.db.category+'\'\n')
    file.write('merit.db.range = '+str(merit.db.range)+'\n')
    file.write('merit.db.prereq = \''+merit.db.prereq.replace('\'','\\\'')+'\'\n')
    file.write('merit.db.noteRestrictions = '+str(merit.db.noteRestrictions)+'\n')
    file.write('merit.db.cost = \''+merit.db.cost+'\'\n')
    file.write('merit.db.reference = \''+merit.db.reference+'\'\n')
    file.write('merit.db.info = \''+merit.db.info.replace('\r\n','|/').replace('\'','\\\'')+'\'\n')
    file.write('merit.db.cg_only = '+str(merit.db.cg_only)+'\n')
    file.write('merit.db.restricted = '+str(merit.db.restricted)+'\n')
    file.write('\n')
file.write('pass')
file.close()