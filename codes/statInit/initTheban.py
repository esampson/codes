from evennia import create_script

theban = create_script('typeclasses.scripts.thebanRiteScript',key = 'Blandishment_of_Sin')
theban.db.longname = 'Blandishment of Sin'
theban.db.rank = 1
theban.db.prereq = ''
theban.db.reference = 'VtR p. 153'
theban.db.info = 'The ritualist names a victim, who must be within one mile of the ritual. The next time any bashing damage is inflicted on the victim, it is upgraded to lethal. The ritual upgrades all damage from one single attack, and ends at sunrise if the victim is not injured that night. A four-dot version of this miracle, requiring 8 successes, upgrades damage from lethal to aggravated.'
theban.db.restricted = False

theban = create_script('typeclasses.scripts.thebanRiteScript',key = 'Blood_Scourge')
theban.db.longname = 'Blood Scourge'
theban.db.rank = 1
theban.db.prereq = ''
theban.db.reference = 'VtR p. 153'
theban.db.info = 'The ritualist transforms a portion of his blood into a weapon. At any point until sunrise, he may create a stinging whip of Vitae (a 2L weapon). The whip crumbles to dust at the end of the scene in which it is used, or when the ritual’s effect ends with the sunrise.'
theban.db.restricted = False

theban = create_script('typeclasses.scripts.thebanRiteScript',key = 'Curse_of_Babel')
theban.db.longname = 'Curse of Babel'
theban.db.rank = 2
theban.db.prereq = ''
theban.db.reference = 'VtR p. 153'
theban.db.info = 'The victim of this ritual, who must be within one mile of the ritual, is rendered unable to speak or write until the next sunrise.'
theban.db.restricted = False

theban = create_script('typeclasses.scripts.thebanRiteScript',key = 'Gift_of_Lazarus')
theban.db.longname = 'Gift of Lazarus'
theban.db.rank = 4
theban.db.prereq = ''
theban.db.reference = 'VtR p. 154'
theban.db.info = 'The ritualist raises a servant by animating a human corpse. The servant has no Willpower, but retains all skills the person had when alive. For every day the servant was dead prior to this ritual being used, reduce an Attribute by one. The ritualist may command the servant herself or tell it to accept orders from another. If its rightmost Health box is filled with aggravated damage or a full lunar month passes, the ritual ends and the servant is destroyed.'
theban.db.restricted = False

theban = create_script('typeclasses.scripts.thebanRiteScript',key = 'Liars_Plague')
theban.db.longname = 'Liar\'s Plague'
theban.db.rank = 2
theban.db.prereq = ''
theban.db.reference = 'VtR p. 153'
theban.db.info = 'The ritualist curses his victim, who must be present for the ritual, to not tell any falsehoods. If the victim lies over the course of the next scene, beetles swarm from his mouth.'
theban.db.restricted = False

theban = create_script('typeclasses.scripts.thebanRiteScript',key = 'Malediction_of_Despair')
theban.db.longname = 'Malediction of Despair'
theban.db.rank = 3
theban.db.prereq = ''
theban.db.reference = 'VtR p. 154'
theban.db.info = 'The ritualist curses her victim, who must be within one mile of the ritual, with regard to a specific action. The next time the victim engages in that action, he suffers a –5 dice penalty. This occurs only once. The effect of the ritual ends if not used after a lunar month.'
theban.db.restricted = False

theban = create_script('typeclasses.scripts.thebanRiteScript',key = 'Stigmata')
theban.db.longname = 'Stigmata'
theban.db.rank = 4
theban.db.prereq = ''
theban.db.reference = 'VtR p. 154'
theban.db.info = 'The ritualist curses his victim - who must be present for the ritual - with the wounds of Christ. The Stigmata last for the ritual’s Potency in turns. Mortal victims suffer one point of lethal damage per turn from blood loss. Vampires and ghouls lose one Vitae per turn. If a vampire runs out of Vitae through this ritual, he begins to take lethal damage instead, provoking a frenzy.'
theban.db.restricted = False

theban = create_script('typeclasses.scripts.thebanRiteScript',key = 'Transubstatiation')
theban.db.longname = 'Transubstatiation'
theban.db.rank = 5
theban.db.prereq = ''
theban.db.reference = 'VtR p. 154'
theban.db.info = 'The ritualist transforms one substance to another - water into wine, lead into gold, a human into stone, or a wolf into a cat. The object, creature, or person to be transformed must be present for the ritual. The ritual cannot affect anything larger than the ritualist, cannot create intelligence and does not harm the things it transforms, although damage or injury sustained by the transformed subject remains when the ritual wears off. All transformations are undone at the next sunrise.'
theban.db.restricted = False

theban = create_script('typeclasses.scripts.thebanRiteScript',key = 'Vitae_Reliquary')
theban.db.longname = 'Vitae Reliquary'
theban.db.rank = 1
theban.db.prereq = ''
theban.db.reference = 'VtR p. 153'
theban.db.info = 'The ritualist infuses an object with up to the ritual’s Potency in Vitae. The Vitae stored is mystically transferred from the ritualist’s body, and can be retrieved by any vampire, Strix, or ghoul who touches the object. The Vitae still causes Vinculum  and blood addiction in anyone drinking it. After one lunar month, the ritual ends and the object crumbles to dust.'
theban.db.restricted = False

pass