from evennia import create_script

cruac = create_script('typeclasses.scripts.CruacRiteScript',key = 'Blood_Blight')
cruac.db.longname = 'Blood Blight'
cruac.db.rank = 4
cruac.db.prereq = ''
cruac.db.reference = 'VtR. p. 153'
cruac.db.info = 'The ritualist mystically destroys his victim\'s blood. Mortal victims suffer the ritual\'s Potency in lethal damage. Kindred, Strix, and ghoul victims lose the ritual\'s Potency in Vitae. This will usually provoke a frenzy check in Kindred.'
cruac.db.restricted = False

cruac = create_script('typeclasses.scripts.CruacRiteScript',key = 'Blood_Price')
cruac.db.longname = 'Blood Price'
cruac.db.rank = 4
cruac.db.prereq = ''
cruac.db.reference = 'VtR. p. 153'
cruac.db.info = 'The ritualist claims blood consumed by his ritual\'s subject. The subject must be a vampire or ghoul present for the casting. Every time the subject drinks blood, Vitae up to and equal to the ritual\'s Potency is gained by the ritualist instead of by the subject. If the subject drinks more than the ritual steals, she gains the balance. The effect of the ritual ends at the next sunrise.'
cruac.db.restricted = False

cruac = create_script('typeclasses.scripts.CruacRiteScript',key = 'Cheval')
cruac.db.longname = 'Cheval'
cruac.db.rank = 2
cruac.db.prereq = ''
cruac.db.reference = 'VtR. p. 152'
cruac.db.info = 'The subject of this ritual must be present at the casting, being physically touched by the ritualist. For the rest of the night, the ritualist may see and hear what the subject does, no matter how far away she is.'
cruac.db.restricted = False

cruac = create_script('typeclasses.scripts.CruacRiteScript',key = 'Deflection_of_Wooden_Doom')
cruac.db.longname = 'Deflection of Wooden Doom'
cruac.db.rank = 3
cruac.db.prereq = ''
cruac.db.reference = 'VtR. p. 153'
cruac.db.info = 'The ritualist wards himself from having his heart impaled. All attempts to stake the ritualist fail until the next sunrise.'
cruac.db.restricted = False

cruac = create_script('typeclasses.scripts.CruacRiteScript',key = 'Feeding_the_Crone')
cruac.db.longname = 'Feeding the Crone'
cruac.db.rank = 4
cruac.db.prereq = ''
cruac.db.reference = 'VtR. p. 153'
cruac.db.info = 'The ritualist transforms her fangs into a maw of wicked, flesh-tearing teeth. She gains no Vitae from feeding as long as the ritual remains in effect, but her bite does +2 aggravated damage. The effect of the ritual fades at the next sunrise, or if she uses one Vitae to cancel it early, transforming her features back to normal.'
cruac.db.restricted = False

cruac = create_script('typeclasses.scripts.CruacRiteScript',key = 'Pangs_of_Proserpina')
cruac.db.longname = 'Pangs of Proserpina'
cruac.db.rank = 1
cruac.db.prereq = ''
cruac.db.reference = 'VtR. p. 152'
cruac.db.info = 'The victim suffers feelings of intense hunger, provoking frenzy in Kindred. The victim may be up to a mile away from the ritual during casting, and is starving for the purposes of the roll to resist frenzy, regardless of how much blood she has consumed.'
cruac.db.restricted = False

cruac = create_script('typeclasses.scripts.CruacRiteScript',key = 'Rigor_Mortis')
cruac.db.longname = 'Rigor Mortis'
cruac.db.rank = 1
cruac.db.prereq = ''
cruac.db.reference = 'VtR. p. 152'
cruac.db.info = 'The victim, who must be a vampire within a mile of the ritual, suffers the loss of the reanimating power of Vitae. His next physical action is penalized by a -3 die penalty.'
cruac.db.restricted = False

cruac = create_script('typeclasses.scripts.CruacRiteScript',key = 'The_Hydras_Vitae')
cruac.db.longname = 'The Hydra\'s Vitae'
cruac.db.rank = 2
cruac.db.prereq = ''
cruac.db.reference = 'VtR. p. 152'
cruac.db.info = 'The ritualist lays a curse on his own blood, transforming it into poison. Vampires and Strix drinking from the ritualist suffer one point of lethal damage per Vitae taken and gain no nourishment from it. Mortals and ghouls drinking from the ritualist suffer two points of lethal damage. Blood is only venomous as long as it\'s in the ritualist\'s system, and the effect ends at the next sunrise.'
cruac.db.restricted = False

cruac = create_script('typeclasses.scripts.CruacRiteScript',key = 'Touch_of_the_Morrigan')
cruac.db.longname = 'Touch of the Morrigan'
cruac.db.rank = 3
cruac.db.prereq = ''
cruac.db.reference = 'VtR. p. 153'
cruac.db.info = 'The ritualist pours the consuming, tearing force of his Beast into his hands. He may attempt to strike an opponent with his open palm (Touching a Target requires a Dexterity + Brawl roll in combat). The first time he does so, the victim suffers the ritual\'s Potency in lethal wounds. The ritual ends when it is first used, or at the next sunrise, whichever is sooner.'
cruac.db.restricted = False

cruac = create_script('typeclasses.scripts.CruacRiteScript',key = 'Willful_Vitae')
cruac.db.longname = 'Willful Vitae'
cruac.db.rank = 4
cruac.db.prereq = ''
cruac.db.reference = 'VtR. p. 153'
cruac.db.info = 'The ritualist makes herself immune to Vinculum and blood addiction for the remainder of the night. The ritual does not counteract any addiction or Vinculum that the ritualist already has.'
cruac.db.restricted = False

pass
