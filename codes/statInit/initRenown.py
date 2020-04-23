from evennia import create_script

renown = create_script('typeclasses.scripts.renownScript',key = 'Cunning')
renown.db.longname = 'Cunning'
renown.db.reference = 'W:tF p. 99'
renown.db.info = 'Uratha hunt things greater than they are. They can\'t always win through brute force or superior numbers. Sometimes, raw creativity and clever planning win the day. Cunning, Renown of the Irraka and the Iron Masters, governs these behaviors.'
renown.db.restricted = False

renown = create_script('typeclasses.scripts.renownScript',key = 'Glory')
renown.db.longname = 'Glory'
renown.db.reference = 'W:tF p. 99'
renown.db.info = 'Uratha stand strong, and fight until their muscles tear apart. They boil with epic fury, storm into battle, and remain in the fray in spite of overwhelming threats. Glory, Renown of the Cahalith and the Blood Talons, reflects these behaviors.'
renown.db.restricted = False

renown = create_script('typeclasses.scripts.renownScript',key = 'Honor')
renown.db.longname = 'Honor'
renown.db.reference = 'W:tF p. 100'
renown.db.info = 'The Forsaken fight not because they must, but because it\'s right. A werewolf could eschew her ancestral duties, and find a place to hide away from her role. An honorable Uratha grabs that role and owns it proudly, standing as a judge and shepherd. Honor, Renown of the Elodoth and the Storm Lords, rewards these behaviors.'
renown.db.restricted = False

renown = create_script('typeclasses.scripts.renownScript',key = 'Purity')
renown.db.longname = 'Purity'
renown.db.reference = 'W:tF p. 100'
renown.db.info = 'The Forsaken represent Father Wolf, Luna, and the Firstborn in everything they do. Uratha espousing Purity adhere strictly to the Oath of the Moon, to the exclusion of other concerns. They put their ancestral duty before friendships, work, love, and even territory. Purity, Renown of the Rahu and the Hunters in Darkness, governs such behaviors.'
renown.db.restricted = False

renown = create_script('typeclasses.scripts.renownScript',key = 'Wisdom')
renown.db.longname = 'Wisdom'
renown.db.reference = 'W:tF p. 100'
renown.db.info = 'The Uratha favor Wisdom as a counterpoint to their savage fury. Sometimes, it\'s better to take a holistic approach to a problem, even when the blood of the wolf rears its violent head. After all, Uratha are beings half of spirit, and have esoteric answers to many questions. Wisdom, Renown of the Ithaeur and the Bone Shadows, governs this.'
renown.db.restricted = False

pass