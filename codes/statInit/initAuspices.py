from evennia import create_script

auspice = create_script('typeclasses.scripts.auspiceScript',key = 'Cahalith')
auspice.db.longname = 'Cahalith'
auspice.db.auspice_skills = ['Crafts', 'Expression', 'Persuasion']
auspice.db.renown = 'Glory'
auspice.db.auspice_gifts = ['Gibbous Moon', 'Inspiration', 'Knowledge']
auspice.db.info = 'The Cahalith is the storyteller, the lore-keeper, and the prophet. She is the living history of her pack and her tribe, and in a larger sense, her People. But the Cahalith is not some lonely wise woman, dispensing wisdom to pilgrims in a hermit\'s retreat. She leads the howling charge, she screams her anguish and rage to the fattening moon and entreats her packmates to do likewise.'
auspice.db.reference = 'W:tF p. 16-19'
auspice.db.restricted = False

auspice = create_script('typeclasses.scripts.auspiceScript',key = 'Elodoth')
auspice.db.longname = 'Elodoth'
auspice.db.auspice_skills = ['Empathy', 'Investigation', 'Politics']
auspice.db.renown = 'Honor'
auspice.db.auspice_gifts = ['Half Moon', 'Insight', 'Warding']
auspice.db.info = 'The half moon keeps as much hidden as it illuminates. Half-moons are not as enigmatic as their Ithaeur compatriots, but then, they wouldn\'t be - most of the crescent moon is obscured. An Elodoth can be gregarious, charming, or clever - or he can be taciturn, secretive, and paranoid. The Elodoth is all in equal measure, and that is what terrifies other werewolves.'
auspice.db.reference = 'W:tF p. 20-23'
auspice.db.restricted = False

auspice = create_script('typeclasses.scripts.auspiceScript',key = 'Irraka')
auspice.db.longname = 'Irraka'
auspice.db.auspice_skills = ['Larceny', 'Stealth', 'Subterfuge']
auspice.db.renown = 'Cunning'
auspice.db.auspice_gifts = ['New Moon', 'Evasion', 'Stealth']
auspice.db.info = 'The new moon is the moon of secrets, ambushes, and hunting unseen. The werewolf chosen under the new moon, the Irraka, is the wolf that does not howl while hunting. She listens for her packmates, but she trusts them to know that she will not answer. She strikes, tearing out her prey\'s throat so it cannot scream, breaking its leg so it cannot run, or pushing it down a bluff so it is far from help. If she can strike the killing blow, she will, but the Stalker is more interested in making sure that the killing blow is inevitable. When hunting with a pack, she often chooses not to claim this honor herself. The Irraka is proud of her role as the one to cripple the prey. The righteous Rahu or the boisterous Cahalith might be the one to take the prey\'s throat at the end of the hunt, but it was the Irraka who snapped its femur or disemboweled it so it couldn\'t run.'
auspice.db.reference = 'W:tF p. 24-26'
auspice.db.restricted = False

auspice = create_script('typeclasses.scripts.auspiceScript',key = 'Ithaeur')
auspice.db.longname = 'Ithaeur'
auspice.db.auspice_skills = ['Animal Ken', 'Medicine', 'Occult']
auspice.db.renown = 'Wisdom'
auspice.db.auspice_gifts = ['Crescent Moon', 'Elemental', 'Shaping']
auspice.db.info = 'Of all the auspices, the Ithaeur undergoes the most drastic change between human life and his new existence as Uratha. Before, even if he believed in spirits, he didn\'t see them on a regular basis. Now they are everywhere. Everything has a spirit, and every spirit is hungry.'
auspice.db.reference = 'W:tF p. 27-29'
auspice.db.restricted = False

auspice = create_script('typeclasses.scripts.auspiceScript',key = 'Rahu')
auspice.db.longname = 'Rahu'
auspice.db.auspice_skills = ['Brawl', 'Intimidation', 'Survival']
auspice.db.renown = 'Purity'
auspice.db.auspice_gifts = ['Full Moon', 'Dominance', 'Strength']
auspice.db.info = 'All werewolves are hunters, but the Rahu is a Warrior. Where other auspices are experts in the best ways to conduct the hunt, the Rahu is the expert on ending it. She charges into battle, weapons or fangs at the ready, and does not retreat until either she or the quarry is dead. If her pack has done its job, the quarry is wounded, terrified, harried, and ready to die. If not...then the Rahu has a harder fight ahead of her. She does not shy from the fight, even so.'
auspice.db.reference = 'W:tF p. 30-32'
auspice.db.restricted = False

pass