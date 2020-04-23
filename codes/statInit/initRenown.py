from evennia import create_script

attribute = create_script('typeclasses.scripts.attributeScript',key = 'Cunning')
attribute.db.longname = 'Cunning'
attribute.db.restricted = None

attribute = create_script('typeclasses.scripts.attributeScript',key = 'Glory')
attribute.db.longname = 'Glory'
attribute.db.restricted = None

attribute = create_script('typeclasses.scripts.attributeScript',key = 'Honor')
attribute.db.longname = 'Honor'
attribute.db.restricted = None

attribute = create_script('typeclasses.scripts.attributeScript',key = 'Purity')
attribute.db.longname = 'Purity'
attribute.db.restricted = None

attribute = create_script('typeclasses.scripts.attributeScript',key = 'Wisdom')
attribute.db.longname = 'Wisdom'
attribute.db.restricted = None

pass