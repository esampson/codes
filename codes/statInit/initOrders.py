from evennia import create_script

order = create_script('typeclasses.scripts.OrderScript',key = 'Adamantine_Arrow')
order.db.longname = 'Adamantine Arrow'
order.db.rote_skills = ['Athletics', 'Intimidation', 'Medicine']
order.db.info = 'Every Order practices offensive and defensive occult techniques, but the Adamantine Arrow internalizes the metaphor of eternal war as principle. More than that, they seek to serve as soldiers and generals in this war, fighting to maintain their magic. Arrows are the guardians and wardens of the Pentacle, warriors of the Diamond, fighting against stagnation and complacency. They typically hold a majority of non-leadership roles in Consilia and Convocations (and no few Assemblies), as community-oriented duties find fulfillment within their philosophy. Above all else, their magic calls for dedication: striving for a chosen goal against meaningful opposition.'
order.db.reference = 'M:tA p. 36-38'
order.db.restricted = False

order = create_script('typeclasses.scripts.OrderScript',key = 'Free_Council')
order.db.longname = 'Free Council'
order.db.rote_skills = ['Crafts', 'Persuasion', 'Science']
order.db.info = 'Upheaval and innovation lead to occult Wisdom: This is the basis of the Council of Free Assemblies, an Order comprised of modern idealists and ancient rebels united by a shared love of humanity and the belief that the traditions of the Fallen World hold a place equal to the Supernal. Geniuses, rebels, malcontents - all have places within Assemblies, fostering a flourishing idealism tempered by practical iconoclasm. Larger and more varied than all other Orders, Libertine sancta ring with competing voices of anarchists, free-market capitalists, and doctrinaire demagogues. Ancient Legacies and formerly-Nameless societies that predate the Diamond share a table with cutting-edge technomancers, bound by the Libertine Creed and a vision of the future.'
order.db.reference = 'M:tA p. 49-51'
order.db.restricted = False

order = create_script('typeclasses.scripts.OrderScript',key = 'Guardians_of_the_Veil')
order.db.longname = 'Guardians of the Veil'
order.db.rote_skills = ['Investigation', 'Stealth', 'Subterfuge']
order.db.info = 'The Guardians of the Veil defend the Awakened from strife and treachery by employing those tools themselves, serving the Pentacle as recruiters and espionage agents keeping watch for threats from without and within. They plot to maintain the Labyrinth, a world-spanning society of conspiracy cells and contradictory mystery cults secretly under Guardian control, designed to weed out the weak, distract the unworthy, and attract those close to Awakeing. A newly Awakened mage attempting to understand what\'s happening around him will likely stumble across the Labyrinth; in fact, the system works so well that Guardians actually detect the majority of Awakenings and pass suitable solitaries to other Orders. By contrast, the Order also spends a great deal of resources attempting to ensure those with traits they find objectionable become lost in the Labyrinth, losing the chance to Awaken. Together, the Order works tirelessly to keep magic secret - and in secrecy, safe.'
order.db.reference = 'M:tA p. 39-42'
order.db.restricted = False

order = create_script('typeclasses.scripts.OrderScript',key = 'Mysterium')
order.db.longname = 'Mysterium'
order.db.rote_skills = ['Investigation', 'Occult', 'Survival']
order.db.info = 'Mystagogues battle against Pancryptia, the tendency of sorcery to actively hide itself amidst the cultural detritus of the Fallen World. They work to foster academia, instilling the intellectual discipline and rigor needed for the Awakened to sift through the Fallen World for pearls of Supernal wisdom. The World is Fallen and damaged, but Mystagogues scrutinize with singular focus. Two open secrets propel their questioning natures: One, that magic itself is alive and active in the world; and two, that anything living can be healed.'
order.db.reference = 'M:tA p. 43-45'
order.db.restricted = False

order = create_script('typeclasses.scripts.OrderScript',key = 'Seers_of_the_Throne')
order.db.longname = 'Seers of the Throne'
order.db.rote_skills = ['Investigation', 'Occult', 'Persuasion']
order.db.info = 'From a position of wealth and power in the Fallen World, the Seers of the Throne interpret the will of the Exarchs. In the kingdom of the blind, the Seers are kings. The third great sect of the Awakened opposes the Diamond and the Free Council out of religious obligation - one of many commandments from their faceless, never-seen masters in the Supernal Realms.'
order.db.reference = 'M:tA p. 52-55'
order.db.restricted = False

order = create_script('typeclasses.scripts.OrderScript',key = 'Silver_Ladder')
order.db.longname = 'Silver Ladder'
order.db.rote_skills = ['Expression', 'Persuasion', 'Subterfuge']
order.db.info = 'The Silver Ladder is invested in the Diamond and Pentacle as a whole, not just the goals of their Order - beyond their status as creators and definers of Awakened society, the Ladder requires them to advise other mages on the best path to freeing humanity from the Lie. The Enemy seeks to keep humanity in chains, turning their slaves towards keeping the Sleeping rabble ignorant and Quiescent. The Order defies those efforts by dreaming big, spreading the flame of Awakening and sundering the chains of the Lie. They create Cryptopolies, mystery cults that encourage Sleepers towards enlightened behavior, continually working to counter the Seers\' influence over humanity. More than any other Order, they seek out and shelter families of Proximi in the hopes of fostering an enlightened class of human.'
order.db.reference = 'M:tA p. 46-48'
order.db.restricted = False

pass
