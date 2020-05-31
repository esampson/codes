from evennia import create_script

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Banish')
rite.db.longname = 'Banish'
rite.db.type = 'Pack'
rite.db.rank = 1
rite.db.prereq = ''
rite.db.info = 'This rite invokes the pack\'s authority as guardian between the two worlds, casting intruders out from realms to which they do not belong.'
rite.db.reference = 'W:tF p. 142-143'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Bottle_Spirit')
rite.db.longname = 'Bottle Spirit'
rite.db.type = 'Wolf'
rite.db.rank = 2
rite.db.prereq = 'target.get(\'Tribe\',statclass=\'Sphere\').lower() == \'bone shadow\''
rite.db.info = 'Death Wolf taught her followers many occult secrets; this rite is a strange form of the laws of binding, a loophole that those in the know can exploit.'
rite.db.reference = 'W:tF p. 140'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Chain_Rage')
rite.db.longname = 'Chain Rage'
rite.db.type = 'Wolf'
rite.db.rank = 1
rite.db.prereq = ''
rite.db.info = 'This pact with spirits of rage forestalls fury, but only for a time. In the end, the chained beast must be free.'
rite.db.reference = 'W:tF p. 139-140'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Expel')
rite.db.longname = 'Expel'
rite.db.type = 'Pack'
rite.db.rank = 4
rite.db.prereq = ''
rite.db.info = 'This rite lays spiritual claim to a person or object with the pack\'s bond, forcing a possessing spirit out.'
rite.db.reference = 'W:tF p. 146'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Fetish')
rite.db.longname = 'Fetish'
rite.db.type = 'Wolf'
rite.db.rank = 4
rite.db.prereq = ''
rite.db.info = 'This rite binds a spirit into a sacred receptacle - a fetish. It\'s an ancient pact born from the symbolism of humankind\'s first artifice, and one that many spirits resent.'
rite.db.reference = 'W:tF p. 141'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Forge_Alliance')
rite.db.longname = 'Forge Alliance'
rite.db.type = 'Wolf'
rite.db.rank = 5
rite.db.prereq = ''
rite.db.info = 'Calling on the Firstborn, this rite replicates an ancient pact amongst those primeval wolf-spirits and burdens the Uratha with it instead.'
rite.db.reference = 'W:tF p. 142'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Great_Hunt')
rite.db.longname = 'Great Hunt'
rite.db.type = 'Pack'
rite.db.rank = 5
rite.db.prereq = ''
rite.db.info = 'Amongst the most potent of Pack Rites, the Great Hunt calls upon the Firstborn to empower lesser hunters that they might match the Uratha.'
rite.db.reference = 'W:tF p. 146'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Harness_the_Cycle')
rite.db.longname = 'Harness the Cycle'
rite.db.type = 'Pack'
rite.db.rank = 1
rite.db.prereq = ''
rite.db.info = 'The cycle of the changing seasons bears immense power. This rite compels spirits of the seasons to give up a tithe of the burgeoning Essence that they gorge themselves on as the world turns.'
rite.db.reference = 'W:tF p. 143'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Hidden_Path')
rite.db.longname = 'Hidden Path'
rite.db.type = 'Pack'
rite.db.rank = 4
rite.db.prereq = ''
rite.db.info = 'Calling upon the spirits of wolves and places to fulfill their side of an ancient pact, this rite sets hunters on a swift path to their prey - or to safety.'
rite.db.reference = 'W:tF p. 145-146'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Hunting_Ground')
rite.db.longname = 'Hunting Ground'
rite.db.type = 'Pack'
rite.db.rank = 2
rite.db.prereq = ''
rite.db.info = 'This rite invokes the old rights of Father Wolf to sanctify a claim of territory and ownership. The Shadow must bow before Urfarah even now.'
rite.db.reference = 'W:tF p. 143-144'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Kindle_Fury')
rite.db.longname = 'Kindle Fury'
rite.db.type = 'Wolf'
rite.db.rank = 3
rite.db.prereq = 'target.get(\'Tribe\',statclass=\'Sphere\').lower() == \'blood talon\''
rite.db.info = 'This rite draws on the ancient pact between Fenris-Urand the Blood Talons, granting the Suthar Anzuth the power of their patron.'
rite.db.reference = 'W:tF p. 140'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Messenger')
rite.db.longname = 'Messenger'
rite.db.type = 'Wolf'
rite.db.rank = 1
rite.db.prereq = ''
rite.db.info = 'A gift from Luna to the Moon\'s children, this rite is a staple of communication amongst the Tribes of the Moon. The Pure shun its use.'
rite.db.reference = 'W:tF p. 140'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Moons_Mad_Love')
rite.db.longname = 'Moon\'s Mad Love'
rite.db.type = 'Pack'
rite.db.rank = 2
rite.db.prereq = ''
rite.db.info = 'This rite is powerful and dangerous, drawing upon a pact with Luna herself to invest some of her presence into a human soul. The Pure mostly shun it.'
rite.db.reference = 'W:tF p. 144'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Raiment_of_the_Storm')
rite.db.longname = 'Raiment of the Storm'
rite.db.type = 'Pack'
rite.db.rank = 3
rite.db.prereq = ''
rite.db.info = 'Spirits of storm and rain respond to the call of this rite, empowering those who walk in their embrace.'
rite.db.reference = 'W:tF p. 145'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Sacred_Hunt')
rite.db.longname = 'Sacred Hunt'
rite.db.type = 'Wolf'
rite.db.rank = 2
rite.db.prereq = ''
rite.db.info = 'The Sacred Hunt, the Siskur-Dah, is the most holy of all rites. Many werewolves believe that it draws upon the laws of the hunt that the Wolf-Mother herself personified.'
rite.db.reference = 'W:tF p. 140'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Shadowbind')
rite.db.longname = 'Shadowbind'
rite.db.type = 'Wolf'
rite.db.rank = 3
rite.db.prereq = ''
rite.db.info = 'With this rite, the ritemaster seeks to bind a spirit in a weave of ancient law that it cannot easily pierce.'
rite.db.reference = 'W:tF p. 141'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Shadowcall')
rite.db.longname = 'Shadowcall'
rite.db.type = 'Pack'
rite.db.rank = 3
rite.db.prereq = ''
rite.db.info = 'This rite summons up a spirit through ancient laws that force it to heed the call.'
rite.db.reference = 'W:tF p. 145'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Supplication')
rite.db.longname = 'Supplication'
rite.db.type = 'Pack'
rite.db.rank = 3
rite.db.prereq = ''
rite.db.info = 'This rite is an invocation of balance, an exchange of respect in return for favor. Some Forsaken see it as groveling to the denizens of the Shadow, but many understand the wisdom in appeasing certain umia of the Hisil.'
rite.db.reference = 'W:tF p. 145'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Totemic_Empowerment')
rite.db.longname = 'Totemic Empowerment'
rite.db.type = 'Pack'
rite.db.rank = 1
rite.db.prereq = ''
rite.db.info = 'Drawing deep on the pack-bond\'s power, this rite turns a pack member into a vessel for the totem.'
rite.db.reference = 'W:tF p. 143'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Twilight_Purge')
rite.db.longname = 'Twilight Purge'
rite.db.type = 'Wolf'
rite.db.rank = 4
rite.db.prereq = ''
rite.db.info = 'Drawing on Shadow-laws of passage and dominance, this rite scours Twilight and snares those within it.'
rite.db.reference = 'W:tF p. 141-142'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Urfarahs_Bane')
rite.db.longname = 'Urfarah\'s Bane'
rite.db.type = 'Wolf'
rite.db.rank = 5
rite.db.prereq = ''
rite.db.info = 'Father Wolf\'s death at the hands of his offspring was an event of vast consequences, a moment that sundered the worlds. This rite is but an echo of that moment.'
rite.db.reference = 'W:tF p. 142'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Veil')
rite.db.longname = 'Veil'
rite.db.type = 'Wolf'
rite.db.rank = 5
rite.db.prereq = 'target.get(\'Tribe\',statclass=\'Sphere\').lower() == \'iron master\''
rite.db.info = 'This rite was born from the emergence of new spiritual laws as symbols of technology began to infest the Shadow of urban centers.'
rite.db.reference = 'W:tF p. 142'
rite.db.restricted = False

rite = create_script('typeclasses.scripts.WerewolfRiteScript',key = 'Wellspring')
rite.db.longname = 'Wellspring'
rite.db.type = 'Pack'
rite.db.rank = 2
rite.db.prereq = ''
rite.db.info = 'This rite invokes a pact between a pack and the spirit umia that reflect a locus\' resonance. In return, the locus becomes a wellspring that washes the Shadow with power.'
rite.db.reference = 'W:tF p. 144-145'
rite.db.restricted = False

pass
