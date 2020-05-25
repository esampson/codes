from evennia import create_script

clan = create_script('typeclasses.scripts.ClanScript',key = 'Daeva')
clan.db.longname = 'Daeva'
clan.db.favored_attributes = ['Dexterity', 'Manipulation']
clan.db.favored_disciplines = ['Celerity', 'Majesty', 'Vigor']
clan.db.reference = 'VtR p. 14-16'
clan.db.info = 'Nickname: Serpents|/|/Clan Bane (The Wanton Curse): You taste the romance in all things, but none so much as blood. Mortals are not just food. They are your obsession, and that fixation grows with every sip. Drink more than once, from any mortal, and you risk becoming emotionally dependent on your prey.'
clan.db.bloodline = False
clan.db.restricted = False

clan = create_script('typeclasses.scripts.ClanScript',key = 'Gangrel')
clan.db.longname = 'Gangrel'
clan.db.favored_attributes = ['Composure', 'Stamina']
clan.db.favored_disciplines = ['Animalism', 'Protean', 'Resilience']
clan.db.reference = 'VtR p. 17-19'
clan.db.info = 'Nickname: Savages|/|/Clan Bane (The Feral Curse): The Beast lethargically coils under the R-Complex of most Kindred. But you and the Beast are as thick as thieves. It rises and rips out of your skin to protect you from the bad, bad world. But it has a price. It\'s harder to resist the Beast\'s call, harder still to remember why you should even want to.'
clan.db.bloodline = False
clan.db.restricted = False

clan = create_script('typeclasses.scripts.ClanScript',key = 'Mekhet')
clan.db.longname = 'Mekhet'
clan.db.favored_attributes = ['Intelligence', 'Wits']
clan.db.favored_disciplines = ['Auspex', 'Celerity', 'Obfuscate']
clan.db.reference = 'VtR p. 20-22'
clan.db.info = 'Nickname: Shadows|/|/Clan Bane (The Tenebrous Curse): Whispering shades and forgotten lore lurk in your blood. Secrets and information distill down to a weird substance in your Vitae. Attuned to the otherworldly, vampire banes express themselves more quickly in you. Sunlight, fire, and the long slumber of torpor pull at your dead body with a stronger tide.'
clan.db.bloodline = False
clan.db.restricted = False

clan = create_script('typeclasses.scripts.ClanScript',key = 'Nosferatu')
clan.db.longname = 'Nosferatu'
clan.db.favored_attributes = ['Composure', 'Strength']
clan.db.favored_disciplines = ['Nightmare', 'Obfuscate', 'Vigor']
clan.db.reference = 'VtR p. 23-25'
clan.db.info = 'Nickname: Haunts|/|/Clan Bane (The Lonely Curse): You are an avatar of disgust. Dread and discomfort oozes from you, scabbing everything over in the putrid film of your rotting soul\'s exhaust. Your body is warped, or the world around you warps. This could manifest in ways grotesque or subtle. Fear and all its gibbering siblings come easy for you. Most other forms of social communion do not. Yours is a lonely Requiem.'
clan.db.bloodline = False
clan.db.restricted = False

clan = create_script('typeclasses.scripts.ClanScript',key = 'Ventrue')
clan.db.longname = 'Ventrue'
clan.db.favored_attributes = ['Presence', 'Resolve']
clan.db.favored_disciplines = ['Animalism', 'Dominate', 'Resilience']
clan.db.reference = 'VtR p. 26-28'
clan.db.info = 'Nickname: Lords|/|/Clan Bane (The Aloof Curse): Excellence breeds contempt. When people are puppets for your will and buildings are play pieces on a grand game board, it is hard not to become distant. It is so very easy for you to become detached from those people, places, and things that keep the Man secure in your breast.'
clan.db.bloodline = False
clan.db.restricted = False

pass
