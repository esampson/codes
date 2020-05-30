from evennia import create_script

power = create_script('typeclasses.scripts.PowerStatScript',key = 'Blood_Potency')
power.db.longname = 'Blood Potency'
power.db.category = 'Vampire'
power.db.reference = ''
power.db.info = ''
power.db.restricted = True

power = create_script('typeclasses.scripts.PowerStatScript',key = 'Gnosis')
power.db.longname = 'Gnosis'
power.db.category = 'Mage'
power.db.reference = ''
power.db.info = ''
power.db.restricted = False

power = create_script('typeclasses.scripts.PowerStatScript',key = 'Primal_Urge')
power.db.longname = 'Primal Urge'
power.db.category = 'Werewolf'
power.db.reference = ''
power.db.info = ''
power.db.restricted = False

power = create_script('typeclasses.scripts.PowerStatScript',key = 'Wyrd')
power.db.longname = 'Wyrd'
power.db.category = 'Changeling'
power.db.reference = ''
power.db.info = ''
power.db.restricted = True

pass
