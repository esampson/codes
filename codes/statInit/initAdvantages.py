from evennia import create_script

advantage = create_script('typeclasses.scripts.advantageScript',key = 'Health')
advantage.db.longname = 'Health'
advantage.db.category = 'Standard'
advantage.db.reference = ''
advantage.db.info = ''
advantage.db.simple_gauge = False

advantage = create_script('typeclasses.scripts.advantageScript',key = 'Initiative')
advantage.db.longname = 'Initiative'
advantage.db.category = 'Standard'
advantage.db.reference = ''
advantage.db.info = ''
advantage.db.simple_gauge = False

advantage = create_script('typeclasses.scripts.advantageScript',key = 'Willpower')
advantage.db.longname = 'Willpower'
advantage.db.category = 'Standard'
advantage.db.reference = ''
advantage.db.info = ''
advantage.db.simple_gauge = True

advantage = create_script('typeclasses.scripts.advantageScript',key = 'Clarity')
advantage.db.longname = 'Clarity'
advantage.db.category = 'Changeling'
advantage.db.reference = ''
advantage.db.info = ''
advantage.db.simple_gauge = True

advantage = create_script('typeclasses.scripts.advantageScript',key = 'Glamour')
advantage.db.longname = 'Glamour'
advantage.db.category = 'Changeling'
advantage.db.reference = ''
advantage.db.info = ''
advantage.db.simple_gauge = False

advantage = create_script('typeclasses.scripts.advantageScript',key = 'Integrity')
advantage.db.longname = 'Integrity'
advantage.db.category = 'Mortal'
advantage.db.reference = ''
advantage.db.info = ''
advantage.db.simple_gauge = False

advantage = create_script('typeclasses.scripts.advantageScript',key = 'Size')
advantage.db.longname = 'Size'
advantage.db.category = 'Standard'
advantage.db.reference = ''
advantage.db.info = ''
advantage.db.simple_gauge = False

advantage = create_script('typeclasses.scripts.advantageScript',key = 'Speed')
advantage.db.longname = 'Speed'
advantage.db.category = 'Standard'
advantage.db.reference = ''
advantage.db.info = ''
advantage.db.simple_gauge = False

advantage = create_script('typeclasses.scripts.advantageScript',key = 'Defense')
advantage.db.longname = 'Defense'
advantage.db.category = 'Standard'
advantage.db.reference = ''
advantage.db.info = ''
advantage.db.simple_gauge = False

pass