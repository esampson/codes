from evennia import create_script

seeming = create_script('typeclasses.scripts.seemingScript',key = 'Beast')
seeming.db.longname = 'Beast'
seeming.db.favored_attributes = ['Resolve', 'Stamina', 'Composure']
seeming.db.regalia = 'Steed'
seeming.db.reference = 'CtL p. 22-23'
seeming.db.info = 'Nicknames: Coursers, Grims, the Savage|/|/Blessing: Your character gains +3 to Initiative rolls and Speed, and may choose to deal lethal damage with unarmed attacks. It costs a point of Glamour per three consecutive turns to enjoy this benefit if he has the Shaken or Spooked Condition, or another Condition that imposes fear.|/|/Curse: In addition to your character’s other breaking points, he risks Clarity damage with a dice pool equal to half his Wyrd (rounded up) whenever acting without thinking causes significant harm or complications for someone else.'
seeming.db.restricted = False

seeming = create_script('typeclasses.scripts.seemingScript',key = 'Darkling')
seeming.db.longname = 'Darkling'
seeming.db.favored_attributes = ['Wits', 'Dexterity', 'Manipulation']
seeming.db.regalia = 'Mirror'
seeming.db.reference = 'CtL p. 24-25'
seeming.db.info = 'Nicknames: the Bewitched, Mountebanks, Wisps|/|/Blessing: If you spend a point of Willpower, your character may touch something insubstantial and become part of it for three consecutive turns, transubstantiating into smoke, shadow, a sunbeam - whatever’s handy. This ability costs a point of Glamour if anyone is looking directly at her at the time.|/|/Curse: In addition to your character’s other breaking points, she risks Clarity damage with a dice pool equal to half her Wyrd (rounded up) whenever a secret or important piece of information she knows turns out to be false.'
seeming.db.restricted = False

seeming = create_script('typeclasses.scripts.seemingScript',key = 'Elemental')
seeming.db.longname = 'Elemental'
seeming.db.favored_attributes = ['Resolve', 'Stamina', 'Composure']
seeming.db.regalia = 'Sword'
seeming.db.reference = 'CtL p. 26-27'
seeming.db.info = 'Nicknames: Sprites, Torrents, the Unbound|/|/Blessing: As long as your character touches or is surrounded by his element, he may use it to take mundane actions at a distance of up to three yards (meters) away; these actions use his usual traits. This includes unarmed attacks, but not attacks with weapons. This ability costs a point of Glamour per action if he has fewer than half his maximum Willpower points remaining.|/|/Curse: In addition to your character’s other breaking points, he risks Clarity damage with a dice pool equal to half his Wyrd (rounded up) whenever someone browbeats, coerces, or forces him to act against his will.'
seeming.db.restricted = False

seeming = create_script('typeclasses.scripts.seemingScript',key = 'Fairest')
seeming.db.longname = 'Fairest'
seeming.db.favored_attributes = ['Intelligence', 'Strength', 'Presence']
seeming.db.regalia = 'Crown'
seeming.db.reference = 'CtL p. 28-29'
seeming.db.info = 'Nicknames: Muses, the Sovereign, Unicorns|/|/Blessing: You may spend Willpower points on another character’s behalf for purposes of the usual three-die bonus or +2 Resistance trait increase. You may still only spend one Willpower point per action. This ability costs a point of Glamour if any Condition is in play that would cause contention or mistrust between the characters, such as Leveraged or Notoriety.|/|/Curse: In addition to your character’s other breaking points, she risks Clarity damage with a dice pool equal to half her Wyrd (rounded up) whenever her action - or inaction - leads directly to misfortune for her allies.'
seeming.db.restricted = False

seeming = create_script('typeclasses.scripts.seemingScript',key = 'Ogre')
seeming.db.longname = 'Ogre'
seeming.db.favored_attributes = ['Intelligence', 'Strength', 'Presence']
seeming.db.regalia = 'Shield'
seeming.db.reference = 'CtL p. 30-31'
seeming.db.info = 'Nicknames: Bruisers, Gargoyles, the Terrible|/|/Blessing: Whenever your character deals any damage to another, you may impose the Beaten Down Tilt, which lasts for three turns. This ability costs a point of Glamour if the Ogre makes the attack on his own behalf and not someone else’s.|/|/Curse: In addition to your character’s other breaking points, he risks Clarity damage with a dice pool equal to half his Wyrd (rounded up) whenever someone he doesn’t consider an enemy flees or cowers from him.'
seeming.db.restricted = False

seeming = create_script('typeclasses.scripts.seemingScript',key = 'Wizened')
seeming.db.longname = 'Wizened'
seeming.db.favored_attributes = ['Wits', 'Dexterity', 'Manipulation']
seeming.db.regalia = 'Jewels'
seeming.db.reference = 'CtL p. 32-33'
seeming.db.info = 'Nicknames: Domovye (singular: Domovoi), Hatters, the Shrewd|/|/Blessing: Your charater can take a Build Equipment action (p. 196) to transform one kind of material into another, as long as she has the appropriate tools to work with what she has. For instance, she could spin straw into gold with a spinning wheel, or forge steel into diamond with an anvil and hammer. This counts as a five-die bonus for purposes of determining the required successes. This ability costs a point of Glamour per action if she’s jury-rigging, but in this case she can improvise her tools as well; she might spin straw into gold by running it around a ceiling fan, or forge steel into diamond by running over it with a car.|/|/Curse: In addition to your character’s other breaking points, she risks Clarity damage with a dice pool equal to half her Wyrd (rounded up) whenever an unpleasant surprise takes her offguard.'
seeming.db.restricted = False

pass