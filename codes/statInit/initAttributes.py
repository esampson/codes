from evennia import create_script

attribute = create_script('typeclasses.scripts.AttributeScript',key = 'Composure')
attribute.db.longname = 'Composure'
attribute.db.category = 'Social'
attribute.db.row = 'Resistance'
attribute.db.restricted = False

attribute = create_script('typeclasses.scripts.AttributeScript',key = 'Dexterity')
attribute.db.longname = 'Dexterity'
attribute.db.category = 'Physical'
attribute.db.row = 'Finese'
attribute.db.restricted = False

attribute = create_script('typeclasses.scripts.AttributeScript',key = 'Intelligence')
attribute.db.longname = 'Intelligence'
attribute.db.category = 'Mental'
attribute.db.row = 'Power'
attribute.db.restricted = False

attribute = create_script('typeclasses.scripts.AttributeScript',key = 'Manipulation')
attribute.db.longname = 'Manipulation'
attribute.db.category = 'Social'
attribute.db.row = 'Finese'
attribute.db.restricted = False

attribute = create_script('typeclasses.scripts.AttributeScript',key = 'Presence')
attribute.db.longname = 'Presence'
attribute.db.category = 'Social'
attribute.db.row = 'Power'
attribute.db.restricted = False

attribute = create_script('typeclasses.scripts.AttributeScript',key = 'Resolve')
attribute.db.longname = 'Resolve'
attribute.db.category = 'Mental'
attribute.db.row = 'Resistance'
attribute.db.restricted = False

attribute = create_script('typeclasses.scripts.AttributeScript',key = 'Stamina')
attribute.db.longname = 'Stamina'
attribute.db.category = 'Physical'
attribute.db.row = 'Resistance'
attribute.db.restricted = False

attribute = create_script('typeclasses.scripts.AttributeScript',key = 'Strength')
attribute.db.longname = 'Strength'
attribute.db.category = 'Physical'
attribute.db.row = 'Power'
attribute.db.restricted = False

attribute = create_script('typeclasses.scripts.AttributeScript',key = 'Wits')
attribute.db.longname = 'Wits'
attribute.db.category = 'Mental'
attribute.db.row = 'Finese'
attribute.db.restricted = False

pass
