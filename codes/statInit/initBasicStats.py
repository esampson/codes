from evennia import create_script

basic = create_script('typeclasses.scripts.BasicStatScript',key = 'Concept')
basic.db.longname = 'Concept'

basic = create_script('typeclasses.scripts.BasicStatScript',key = 'Sphere')
basic.db.longname = 'Sphere'

pass
