from evennia import create_script

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Body_of_Will')
devotion.db.longname = 'Body of Will'
devotion.db.cost = 2
devotion.db.prereq = 'target.get(\'Resilience\',statclass=\'Discipline\') >= 3 and target.get(\'Vigor\',statclass=\'Discipline\') >= 1'
devotion.db.reference = 'VtR p. 142'
devotion.db.info = 'Kindred trained in this Devotion can push through pain, and find strength in pain and injury. On the outside, it looks like masochism; crippling blows empower and invigorate the vampire. But this Devotion transfers the energy of a wounding attack into the fuel for the vampire’s Vigor.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Chain_of_Command')
devotion.db.longname = 'Chain of Command'
devotion.db.cost = 2
devotion.db.prereq = 'target.get(\'Dominate\',statclass=\'Discipline\') >= 3 and target.get(\'Vigor\',statclass=\'Discipline\') >= 1'
devotion.db.reference = 'VtR p. 142'
devotion.db.info = 'Dominate masters can implant suggestions and commands into their victims. With this Devotion, the vampire can force more of her own will into her victim, imparting a single use of her own Dominate for the victim to use later. She must clearly explain on whom he must use the gift, and how. She can give a general description, such as "the first person you see wearing red." Or, she can be very specific: "Tell this to Gregor at 11:45 P.M. sharp."'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Cloak_the_Gathering')
devotion.db.longname = 'Cloak the Gathering'
devotion.db.cost = 2
devotion.db.prereq = 'target.get(\'Obfuscate\',statclass=\'Discipline\') >= 5'
devotion.db.reference = 'VtR p. 142'
devotion.db.info = 'The vampire slips from the mind as easily as easily as blood dripping from an open wound, though rather than picking off his victims, he can make a whole group vanish at once. He might obscure his comrades — or pluck a group of unwilling victims from the minds of onlookers, leaving them scared and isolated.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Conditioning')
devotion.db.longname = 'Conditioning'
devotion.db.cost = 2
devotion.db.prereq = 'target.get(\'Dominate\',statclass=\'Discipline\') >= 4'
devotion.db.reference = 'VtR p. 143'
devotion.db.info = 'Over a period of weeks, the vampire pushes on her victim’s will, forcing him to repeat the same tasks over and over until he cannot resist her voice. She slowly builds up control over her victim to the point where he can barely manifest his own thoughts or feelings. Instead he’s an empty shell, waiting for his mistress’ next command.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Cross-Contamination')
devotion.db.longname = 'Cross-Contamination'
devotion.db.cost = 1
devotion.db.prereq = 'target.get(\'Majesty\',statclass=\'Discipline\') >= 1 and target.get(\'Nightmare\',statclass=\'Discipline\') >= 1'
devotion.db.reference = 'VtR p. 143'
devotion.db.info = 'Majesty awes its victims; Nightmare unnerves them. This Devotion blends the two effects, creating a confusing aura where those affected rapidly shift between fear and elation.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Cult_of_Personality')
devotion.db.longname = 'Cult of Personality'
devotion.db.cost = 4
devotion.db.prereq = 'target.get(\'Majesty\',statclass=\'Discipline\') >= 4 and target.get(\'Vigor\',statclass=\'Discipline\') >= 3'
devotion.db.reference = 'VtR p. 143'
devotion.db.info = 'Under normal circumstances, Loyalty inflicts a deep, overbearing sense of obedience on a single victim. With this Devotion, the vampire broadcasts her charm and overwhelms all in her presence. All but the strongest fall in line and worship her.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Enchantment')
devotion.db.longname = 'Enchantment'
devotion.db.cost = 2
devotion.db.prereq = 'target.get(\'Majesty\',statclass=\'Discipline\') >= 4 and target.get(\'Obfuscate\',statclass=\'Discipline\') >= 2'
devotion.db.reference = 'VtR p. 143'
devotion.db.info = 'Majesty is a gift that draws attention and bends feelings toward the vampire. With this Devotion, and a bit of Obfuscate, the vampire can deflect those feelings to another person, or to a place or thing.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Enfeebling_Aura')
devotion.db.longname = 'Enfeebling Aura'
devotion.db.cost = 3
devotion.db.prereq = 'target.get(\'Majesty\',statclass=\'Discipline\') >= 1 and target.get(\'Resilience\',statclass=\'Discipline\') >= 1'
devotion.db.reference = 'VtR p. 143-144'
devotion.db.info = 'Many Daeva masters of Celerity and Vigor claim that Majesty means nothing when you’re staring down a skull-crushing fist. This Devotion seeks to disprove that notion. It brings forth the vampire’s supernatural presence not to awe a crowd, but to cow and enfeeble a victim. While it won’t completely stop an assailant, it will even the playing field in a tussle.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Force_of_Nature')
devotion.db.longname = 'Force of Nature'
devotion.db.cost = 5
devotion.db.prereq = 'target.get(\'Protean\',statclass=\'Discipline\') >= 4 and target.get(\'Resilience\',statclass=\'Discipline\') >= 4 and target.get(\'Vigor\',statclass=\'Discipline\') >= 2'
devotion.db.reference = 'VtR p. 144'
devotion.db.info = 'Most of Protean’s gifts change the vampire subtly, or in small ways, in accordance with nature. Unnatural Aspect takes that a step further, moving into eldritch territory with a single mutation. When the vampire activates Force of Nature, her body becomes a mess of rapid change. She grows and loses limbs in the blink of an eye. Her skin becomes rock solid, then gelatinous within moments. She’s truly protean; she changes the way water flows. However, she needs the strength of Resilience to protect her form from collapsing in upon itself.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Foul_Grave')
devotion.db.longname = 'Foul Grave'
devotion.db.cost = 1
devotion.db.prereq = 'target.get(\'Protean\',statclass=\'Discipline\') >= 1 and target.get(\'Nightmare\',statclass=\'Discipline\') >= 1'
devotion.db.reference = 'VtR p. 144'
devotion.db.info = 'Usually, when interred in an Unmarked Grave, the vampire rests passively, barely aware of his surroundings, let alone able to influence them. With this Devotion, he can project his predatory aura on those near his resting place. Some vampires use this ability to divert pursuers or even as a stalling tactic when confronted by a mob of attackers.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Gargoyles_Vigilance')
devotion.db.longname = 'Gargoyle\'s Vigilance'
devotion.db.cost = 1
devotion.db.prereq = 'target.get(\'Auspex\',statclass=\'Discipline\') >= 1 and target.get(\'Resilience\',statclass=\'Discipline\') >= 2'
devotion.db.reference = 'VtR p. 144'
devotion.db.info = 'This Devotion grants a patient and vigilant vampire the ability to oversee her haven with immense clarity. She becomes completely aware of every single inch, and can respond at a moment’s notice. When she moves against a trespasser, nothing can stop her. Her Resilience affords her senses a stoic patience, so she can divide her attention throughout her resting place.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Gargoyles_Vigilance_-_Advanced')
devotion.db.longname = 'Gargoyle\'s Vigilance - Advanced'
devotion.db.cost = 4
devotion.db.prereq = 'target.get(\'Auspex\',statclass=\'Discipline\') >= 1 and target.get(\'Resilience\',statclass=\'Discipline\') >= 2 and target.get(\'Protean\',statclass=\'Discipline\') >= 5'
devotion.db.reference = 'VtR p. 144'
devotion.db.info = 'This Devotion grants a patient and vigilant vampire the ability to oversee her haven with immense clarity. She becomes completely aware of every single inch, and can respond at a moment’s notice. When she moves against a trespasser, nothing can stop her. Her Resilience affords her senses a stoic patience, so she can divide her attention throughout her resting place.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Hint_of_Fear')
devotion.db.longname = 'Hint of Fear'
devotion.db.cost = 2
devotion.db.prereq = 'target.get(\'Celerity\',statclass=\'Discipline\') >= 2 and target.get(\'Nightmare\',statclass=\'Discipline\') >= 2'
devotion.db.reference = 'VtR p. 144-145'
devotion.db.info = 'Usually, using Face of the Beast takes extended eye contact, and none could confuse it for anything but an attempt to invoke pure terror. With a subtle application of Celerity, this Devotion allows the vampire to use a rapid, unnoticeable look to bring the Face of the Beast to bear. If the vampire doesn’t designate himself as the source of the fear, onlookers will be none the wiser.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Juggernauts_Gait')
devotion.db.longname = 'Juggernaut\'s Gait'
devotion.db.cost = 4
devotion.db.prereq = 'target.get(\'Resilience\',statclass=\'Discipline\') >= 5 and target.get(\'Vigor\',statclass=\'Discipline\') >= 3'
devotion.db.reference = 'VtR p. 145'
devotion.db.info = 'With this rare Devotion, an elder Kindred can temporarily render herself completely immune to harm. Her blood flows rapidly from her flesh, and coats her body to defend her. Even the strongest Kindred cannot maintain this ability for more than a few seconds at a time, but for those moments, they’re veritable gods of blood.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Quicken_Sight')
devotion.db.longname = 'Quicken Sight'
devotion.db.cost = 1
devotion.db.prereq = 'target.get(\'Auspex\',statclass=\'Discipline\') >= 1 and target.get(\'Celerity\',statclass=\'Discipline\') >= 1'
devotion.db.reference = 'VtR p. 145'
devotion.db.info = 'When activated, Quicken Sight lasts for a turn. The vampire can examine the details on fast-moving items, and respond to things outside the normal human spectrum. She can read multiple pages of text in three seconds. She can apply her Defense to ranged attacks, and can benefit from aiming instantly.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Reasons_Salon')
devotion.db.longname = 'Reason\'s Salon'
devotion.db.cost = 3
devotion.db.prereq = 'target.get(\'Animalism\',statclass=\'Discipline\') >= 4 and target.get(\'Resilience\',statclass=\'Discipline\') >= 2'
devotion.db.reference = 'VtR p. 146'
devotion.db.info = 'Animalism can draw bestial behavior out of a person, but with this Devotion, it can also suppress those behaviors. By spreading his Vitae about a building or gathering place, the vampire can keep Kindred from losing control and unleashing their Beasts for a short time. For this reason, it’s not uncommon to see a Gangrel Master of Elysium.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Riot')
devotion.db.longname = 'Riot'
devotion.db.cost = 5
devotion.db.prereq = 'target.get(\'Animalism\',statclass=\'Discipline\') >= 4 and target.get(\'Majesty\',statclass=\'Discipline\') >= 5'
devotion.db.reference = 'VtR p. 146'
devotion.db.info = 'Feral Infection gives an Animalism user the power to move a small group of people to bestial rampages. Coupled with the pinnacle ability of Majesty, an elder can cause a large group of people to explode into complete bedlam, where they hurt each other, destroy property, and resort to other violent, antisocial behaviors. This Devotion brings the full weight of the vampire’s predatory aura to bear on her surroundings.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Shared_Sight')
devotion.db.longname = 'Shared Sight'
devotion.db.cost = 2
devotion.db.prereq = 'target.get(\'Auspex\',statclass=\'Discipline\') >= 4 and target.get(\'Dominate\',statclass=\'Discipline\') >= 1'
devotion.db.reference = 'VtR p. 146'
devotion.db.info = 'While employing Dominate’s trance, a practitioner of this Devotion can extend to her subject some of her second sight. It’s a limited, less effective version of her Auspex, but it opens an otherwise uninitiated mind.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Shatter_the_Shroud')
devotion.db.longname = 'Shatter the Shroud'
devotion.db.cost = 2
devotion.db.prereq = 'target.get(\'Auspex\',statclass=\'Discipline\') >= 2 and target.get(\'Vigor\',statclass=\'Discipline\') >= 1'
devotion.db.reference = 'VtR p. 146'
devotion.db.info = 'With Auspex, Kindred can see through the shrouds of Obfuscate and other Discipline effects (and supernatural powers) that others use in attempts to hide. This Devotion extends that ability with force, shattering those gifts and exposing their users for the world to see.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Stalwart_Servant')
devotion.db.longname = 'Stalwart Servant'
devotion.db.cost = 2
devotion.db.prereq = 'target.get(\'Dominate\',statclass=\'Discipline\') >= 3 and target.get(\'Resilience\',statclass=\'Discipline\') >= 1'
devotion.db.reference = 'VtR p. 146'
devotion.db.info = 'This Devotion enables the Kindred to impart some of her preternatural toughness through her blood, making for stronger servants and bodyguards. The subject drinks of the Kindred’s Vitae, with normal ghouling, addiction, and blood bond effects, and then receives a hint of the vampire’s Resilience.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Subsume_the_Lesser_Beast')
devotion.db.longname = 'Subsume the Lesser Beast'
devotion.db.cost = 3
devotion.db.prereq = 'target.get(\'Animalism\',statclass=\'Discipline\') >= 4 and target.get(\'Dominate\',statclass=\'Discipline\') >= 2'
devotion.db.reference = 'VtR p. 147'
devotion.db.info = 'The vampire locks eyes with an animal and forces her mind into its body. She can only command a predator, a parasite, a carrion-eater, or a plague-bearer; she cannot affect a mere prey animal. She completely subsumes the animal’s consciousness, piloting it like a meat puppet. Her body falls into a state of torpor while she controls the beast.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Summoning')
devotion.db.longname = 'Summoning'
devotion.db.cost = 2
devotion.db.prereq = 'target.get(\'Dominate\',statclass=\'Discipline\') >= 4 or target.get(\'Majesty\',statclass=\'Discipline\') >= 4'
devotion.db.reference = 'VtR p. 147'
devotion.db.info = 'The vampire reaches out to someone whom he knows, anywhere in the world, and calls her to his side. Somehow, the victim knows that the vampire wants her to be with him, and she will go to be by his side come hell or high water. Summoning isn’t instant — it can’t account for natural disasters — but the victim will happily empty her bank accounts and steal from friends or family to make the trip. She knows who has called her and where to find him, but the urge to meet him is an emotional compulsion rather than a supernatural command, and she won’t put herself in unnecessary danger to make the journey — a vampire is still self-aware enough to seek shelter for the day even though he has been summoned. At the time of summoning, the vampire can impress upon his victim the need to bring something with her — weapons to defend her master from a nemesis, or a sacrifice for some strange Blood Sorcery.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Suns_Brutal_Dreamscape')
devotion.db.longname = 'Sun\'s Brutal Dreamscape'
devotion.db.cost = 4
devotion.db.prereq = 'target.get(\'Nightmare\',statclass=\'Discipline\') >= 5 and target.get(\'Resilience\',statclass=\'Discipline\') >= 2'
devotion.db.reference = 'VtR p. 148'
devotion.db.info = 'Nothing frightens Kindred worse than the vengeful rays of the sun or the heat of the fire. Most Kindred can manage short bursts in the daylight, but most avoid it whenever possible. This Devotion curses a sleeping victim to suffer all the burns the vampire experiences from the sun, and curses him with horrifying dreams of the sun’s purifying touch. These terrifying daymares leave the victim waking terrified and charred.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'The_Wish')
devotion.db.longname = 'The Wish'
devotion.db.cost = 2
devotion.db.prereq = 'target.get(\'Celerity\',statclass=\'Discipline\') >= 2 and target.get(\'Majesty\',statclass=\'Discipline\') >= 4 and target.get(\'Vigor\',statclass=\'Discipline\') >=2'
devotion.db.reference = 'VtR p. 148-149'
devotion.db.info = '"For three nights, you’ll be fast, you’ll be strong, you’ll be beautiful, and you’ll stand above the flock. After that, you’re mine. Do you understand?" This classic Daeva Devotion is a common fixture of the Serpent’s Embrace. The vampire finds someone she wishes to exalt, then makes him an offer for temporary supremacy. He gets a taste of power, and wants more. At the end of the deal, the victim becomes irrevocably attached to the vampire. It requires a great deal of Vitae to enact, but creates a loyal supplicant.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Touch_of_Deprivation')
devotion.db.longname = 'Touch of Deprivation'
devotion.db.cost = 3
devotion.db.prereq = 'target.get(\'Obfuscate\',statclass=\'Discipline\') >= 4 and target.get(\'Dominate\',statclass=\'Discipline\') >= 2'
devotion.db.reference = 'VtR p. 148'
devotion.db.info = 'With this Devotion, the vampire can deny a victim her senses with only a touch. He chooses a single sense when activating the Devotion, and that sense becomes temporarily useless. Often, this Devotion serves to blind enemies or deafen a victim at a critical time.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Undying_Familiar')
devotion.db.longname = 'Undying Familiar'
devotion.db.cost = 1
devotion.db.prereq = 'target.get(\'Animalism\',statclass=\'Discipline\') >= 2 and target.get(\'Resilience\',statclass=\'Discipline\') >= 2'
devotion.db.reference = 'VtR p. 148'
devotion.db.info = 'Raise the Familiar awakens a dead animal to serve its Kindred master. However, the animal must be dead for that ability to take effect. This Devotion cuts out the middle man, and awakens a living, ghouled animal at its time of death.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Vermin_Flood')
devotion.db.longname = 'Vermin Flood'
devotion.db.cost = 4
devotion.db.prereq = 'target.get(\'Animalism\',statclass=\'Discipline\') >= 3 and target.get(\'Celerity\',statclass=\'Discipline\') >= 2 and target.get(\'Vigor\',statclass=\'Discipline\') >=2'
devotion.db.reference = 'VtR p. 149'
devotion.db.info = 'This Devotion takes the groundwork laid by Summon the Hunt, and increases it exponentially. Vermin Flood calls every small animal in the neighborhood to swarm en masse and pick apart every little thing in the chosen area. Not only do they feed on living things, but they wipe the space clean. While effective as an assault against groups, it sees some use in cleaning up crime scenes. Unlike Summon the Hunt, this Devotion never appears to be a coincidental event. The Vermin Flood is a plague of biblical proportions. While it tends to stretch the Masquerade, it also causes disbelief in onlookers. Those in the swarm do not survive to tell the tale.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Wet_Dream')
devotion.db.longname = 'Wet Dream'
devotion.db.cost = 2
devotion.db.prereq = 'target.get(\'Majesty\',statclass=\'Discipline\') >= 2 and target.get(\'Nightmare\',statclass=\'Discipline\') >= 2'
devotion.db.reference = 'VtR p. 148'
devotion.db.info = 'This Devotion blends the more subconscious effects of Majesty and Nightmare to plague the victim’s sleep. His dreams leave him both feeling dirty, and wanting more.'
devotion.db.restricted = False

devotion = create_script('typeclasses.scripts.devotionScript',key = 'Wraiths_Presence')
devotion.db.longname = 'Wraith\'s Presence'
devotion.db.cost = 2
devotion.db.prereq = 'target.get(\'Obfuscate\',statclass=\'Discipline\') >= 3 and target.get(\'Nightmare\',statclass=\'Discipline\') >= 1'
devotion.db.reference = 'VtR p. 149'
devotion.db.info = 'With this Devotion, the vampire can make herself or something else vanish from the mind’s eye, but appear elsewhere. This diversion can distract a pursuer, or make someone rush after a false lead.'
devotion.db.restricted = False

pass