from evennia import create_script

power = create_script('typeclasses.scripts.powerStatScript',key = 'Wyrd')
power.db.longname = 'Wyrd'
power.db.category = 'Changeling'
power.db.reference = ''
power.db.info = ''
power.db.restricted = True

power = create_script('typeclasses.scripts.powerStatScript',key = 'Blood_Potency')
power.db.longname = 'Blood Potency'
power.db.category = 'Vampire'
power.db.reference = ''
power.db.info = ''
power.db.restricted = True

pass