from evennia import create_script

discipline = create_script('typeclasses.scripts.disciplineScript',key = 'Animalism')
discipline.db.longname = 'Animalism'
discipline.db.prereq = ''
discipline.db.reference = 'VtR p. 126-128'
discipline.db.info = 'A vampire’s Beast is not just a facet of her predatory nature, but a predator in and of itself — and it’s at the top of the food chain. A vampire can slip the leash of her Beast just a little to overpower weaker animals, forcing her will on them. Most Animalism powers affect predators and scavenging animals. In a city, the Kindred can call on feral cats and dogs, pigeons and crows, foxes, and more rats than anyone wants to think about. Rural vampires can summon bats, wolves, mountain lions, and even bears — any animal that feasts on the flesh of another.'
discipline.db.restricted = False

discipline = create_script('typeclasses.scripts.disciplineScript',key = 'Auspex')
discipline.db.longname = 'Auspex'
discipline.db.prereq = ''
discipline.db.reference = 'VtR p. 128-130'
discipline.db.info = 'Auspex turns the Beast’s predatory instincts loose on secrets, finding points of weakness and hidden gems that the vampire can exploit to his advantage. Auspex is an internal Discipline, revealing information to the Kindred through visions that range from the direct to the hallucinatory. Other vampires have no way to know when someone is using Auspex to discover their secrets, and for that reason many Mekhet feel the stares and whispered barbs of other vampires who worry what secrets the clan of Shadows will uncover next.'
discipline.db.restricted = False

discipline = create_script('typeclasses.scripts.disciplineScript',key = 'Celerity')
discipline.db.longname = 'Celerity'
discipline.db.prereq = ''
discipline.db.reference = 'VtR p. 130-131'
discipline.db.info = 'Unleashing her Beast, a vampire can cross vast distances in the blink of an eye, catch a thrown punch before her attacker has even moved a muscle, or snatch a gun barrel away from a man’s temple before he can pull the trigger. Celerity makes a vampire so fast that it’s as if she never has to move at all.'
discipline.db.restricted = False

discipline = create_script('typeclasses.scripts.disciplineScript',key = 'Cruac')
discipline.db.longname = 'Cruac'
discipline.db.prereq = 'target.get(\'Status\',subentry=\'Circle of the Crone\',statclass=\'Merit\') >= 1 or target.get(\'Cruac\',statclass=\'Discipline\') >= 1'
discipline.db.reference = 'VtR p. 150-153'
discipline.db.info = 'The Ritual Discipline taught by the Circle of the Crone, Crúac is an ancient, malevolent art — described by some opponents of the covenant as a literal infection of Vitae, a thing living within its practitioners. The power summoned by Crúac rites is the power of the Beast itself, paid in blood and forced to taint the world by invoking the primal gods of the Crone. Casting a rite is a fervent, consuming, ecstatic experience, and Acolytes often push the edge of frenzy when they perform their sorcery. Crúac is corrupting, wild, and pagan, degrading everything it touches with the corrosive aura of the Beast. It works its sorcery on flesh, wood, and stone, and is not concerned with the lofty thoughts and intellect of the Man.'
discipline.db.restricted = False

discipline = create_script('typeclasses.scripts.disciplineScript',key = 'Dominate')
discipline.db.longname = 'Dominate'
discipline.db.prereq = ''
discipline.db.reference = 'VtR p. 131-133'
discipline.db.info = 'The Beast demands obedience from lesser creatures. It slips into the Kindred’s voice, modulating his tone and his words to express absolute authority. It progresses from the simple barked commands of a drill sergeant to creating false memories of whatever the vampire desires — or letting her steal her victim’s body to walk in the sunlight once again.'
discipline.db.restricted = False

discipline = create_script('typeclasses.scripts.disciplineScript',key = 'Majesty')
discipline.db.longname = 'Majesty'
discipline.db.prereq = ''
discipline.db.reference = 'VtR p. 133-135'
discipline.db.info = 'Majesty draws on the Beast’s animal magnetism to amplify a vampire’s force of personality, making people like him and want to make him happy even though normally they wouldn’t give a shit about him. They like him and want to be around him just because it makes them feel good. Using Majesty isn’t like leaning forward and slipping a command behind a human’s eyes, it’s arranging the world so that people will kill — or die — for his attention.'
discipline.db.restricted = False

discipline = create_script('typeclasses.scripts.disciplineScript',key = 'Nightmare')
discipline.db.longname = 'Nightmare'
discipline.db.prereq = ''
discipline.db.reference = 'VtR p. 135-137'
discipline.db.info = 'The Beast doesn’t need fear. Fear is rational, understandable — a reaction to a presented stimulus. Any idiot can make people fear him. Nightmare indulges the Beast’s desire to cause abject terror. It starts slowly at first: Just for a second, you see a human face in the path of a circular saw. Your keyboard feels unaccountably warm and fleshy, but when you look down it’s fine. Walking down the street the shadows fall at the wrong angles. You bump into someone, an old friend from your childhood, and all you can do is run and scream. You fall into the arms of your wife, shaking and sobbing, but she’s holding you too tight and she smells wrong. Your daughter comes up behind you and sinks her teeth into your thigh. You scream in pain and bolt out of the door. Looking back, you see your daughter’s face.|/|/Only then does the real terror begin.'
discipline.db.restricted = False

discipline = create_script('typeclasses.scripts.disciplineScript',key = 'Obfuscate')
discipline.db.longname = 'Obfuscate'
discipline.db.prereq = ''
discipline.db.reference = 'VtR p. 137-139'
discipline.db.info = 'The Beast is a hidden killer. It lurks just below the surface, unnoticed by its prey until it’s too late. Just another man in the street, no different from anyone else. Just another woman passing by. Why can’t you remember what they looked like? One of them turns, and you can’t quite see his face, but he’s walking towards you. Another second and he’s grabbed you. His teeth sink into your neck and all you can think is "why won’t anyone do anything? Why won’t they help me?"|/|/Obfuscate is the reason you’ll never be sure that you’re alone again.'
discipline.db.restricted = False

discipline = create_script('typeclasses.scripts.disciplineScript',key = 'Protean')
discipline.db.longname = 'Protean'
discipline.db.prereq = ''
discipline.db.reference = 'VtR p. 139-141'
discipline.db.info = 'Every vampire is one bad day away from giving in to the Beast. Some keep the creature leashed within, holding it back and only letting it out to prey on the weak. Others indulge their Beasts, reveling in the descent from an undead thing yearning for its grave to a force of savage power. A vampire who attains the pinnacle of Protean becomes a formless creature, nothing more than smoke and hunger.'
discipline.db.restricted = False

discipline = create_script('typeclasses.scripts.disciplineScript',key = 'Resilience')
discipline.db.longname = 'Resilience'
discipline.db.prereq = ''
discipline.db.reference = 'VtR p. 141'
discipline.db.info = 'The Kindred are walking corpses, free of the frailties of a mortal form. Their bodies are capable of great endurance, but Resilience harnesses the Beast to take that endurance beyond "great" and into "impossible." With Resilience a vampire could continue to act even when his body has been reduced to little more than bone and tendon.'
discipline.db.restricted = False

discipline = create_script('typeclasses.scripts.disciplineScript',key = 'Theban_Sorcery')
discipline.db.longname = 'Theban Sorcery'
discipline.db.prereq = 'target.get(\'Status\',subentry=\'Lancea et Sanctum\',statclass=\'Merit\') >= 1'
discipline.db.reference = 'VtR p. 150-153'
discipline.db.info = 'The Ritual Discipline of the Lancea et Sanctum, Theban Sorcery was discovered early in the covenant’s history. According to the writings of St. Daniel, one of the earliest members of the covenant, he was led by an angel naming itself "Amoniel" to a cavern deep beneath Thebes in Egypt. The cavern walls were covered in inscribed incantations and diagrams. These formed the basis of Theban Sorcery, which Daniel faithfully recorded and passed on to his fellow Kindred. Theban Sorcery is stern, deliberate, and judgmental — the product of a harsh, uncompromising faith — and the power it calls down feels the same way. Some ritualists characterize the power of miracles as transmitting the touch of God’s Curse (as opposed to the Beast) onto the subject. Sanctified miracles provide divinations, reveal wrong-doers and punish those who trespass against the church’s laws. Performing a Theban miracle is an act of concentrated faith, mentally exhausting and not done in haste. Every miracle requires a physical sacrament, a symbolic item that crumbles to dust as though it were a slain elder when the ritual reaches a crescendo.'
discipline.db.restricted = False

discipline = create_script('typeclasses.scripts.disciplineScript',key = 'Vigor')
discipline.db.longname = 'Vigor'
discipline.db.prereq = ''
discipline.db.reference = 'VtR p. 141-142'
discipline.db.info = 'While all Kindred possess the power to bolster their might in short bursts, Vigor allows some vampires to kick like a freight train or rend steel with their bare hands. The Beast tunes every bone, tendon and muscle fiber to its highest performance, allowing the night’s most fearsome predator to strut through the jungle of his choosing without fear of lesser, weaker creatures.'
discipline.db.restricted = False

pass