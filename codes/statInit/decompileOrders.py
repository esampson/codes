from evennia import ScriptDB

from operator import itemgetter

orders = ScriptDB.objects.typeclass_search(
    'codes.stats.orderScripts.orderScript')
my_list = []
for item in orders:
    my_list.append([item.db.longname, item])
orders = sorted(my_list, key=itemgetter(0))
        
file = open('initOrders.py','w')
file.write('from evennia import create_script\n')
file.write('\n')
for order in orders:
    name = order[1].db.longname.replace('\'','').replace(' ','_')
    file.write(
        'order = create_script(\'typeclasses.scripts.orderScript\','
        'key = \'' + name + '\')\n')
    file.write(
        'order.db.longname = \'' +
        order[1].db.longname.replace('\'','\\\'')+'\'\n')
    file.write(
        'order.db.rote_skills = ' + str(order[1].db.rote_skills) + '\n')
    file.write(
        'order.db.info = \'' +
        order[1].db.info.replace('\r\n', '|/').replace('\'', '\\\'') + '\'\n')
    file.write('order.db.reference = \''+order[1].db.reference+'\'\n')
    file.write('order.db.restricted = '+str(order[1].db.restricted)+'\n')
    file.write('\n')
file.write ('pass')
file.close()