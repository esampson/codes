from evennia import create_script

kith = create_script('typeclasses.scripts.KithScript',key = 'Artist')
kith.db.longname = 'Artist'
kith.db.reference = 'CtL p. 51-52'
kith.db.info = 'Kith Blessing: Choose either Crafts or Expression. When the Artist uses a Specialty for art with that Skill, achieving three successes counts as an exceptional success.|/|/Tools of the Trade: A good Artist is never without her tools. She can spend a point of Glamour for her player to gain bonus dice equal to her Wyrd, to a maximum of +5, on a Crafts or Expression roll with one of her Specialties pertaining to creating art. All the necessary implements of her craft manifest around her for a scene.'
kith.db.restricted = False

kith = create_script('typeclasses.scripts.KithScript',key = 'Bright_One')
kith.db.longname = 'Bright One'
kith.db.reference = 'CtL p. 52'
kith.db.info = 'Kith Blessing: When the Bright One uses Socialize to be the center of attention, achieving three successes counts as an exceptional success.|/|/Flare: A Bright One always has a visible glow, even in the darkest of rooms, though the Mask normally prevents mortals from seeing it. She can spend a point of Glamour to turn this glow up to a dazzling brilliance that blinds her enemies for one turn; the Mask does not obscure this light. Each turn the Bright One uses this blessing, each enemy that can see her takes a point of bashing damage and rolls at a −2 on all Physical and Mental actions that turn.'
kith.db.restricted = False

kith = create_script('typeclasses.scripts.KithScript',key = 'Chatelaine')
kith.db.longname = 'Chatelaine'
kith.db.reference = 'CtL p. 52-53'
kith.db.info = 'Kith Blessing; When the Chatelaine uses Empathy to determine a target\'s immediate desires, achieving three successes counts as an exceptional success.|/|/Will That Be All?: Spend a point of Glamour to activate this blessing for the scene. With a successful Manipulation + Socialize roll, a Chatelaine may use the Social Merits of one other character in the scene as though they were her own. When the effect ends, characters act as though the target had used the Merits himself.'
kith.db.restricted = False

kith = create_script('typeclasses.scripts.KithScript',key = 'Gristlegrinder')
kith.db.longname = 'Gristlegrinder'
kith.db.reference = 'CtL p. 53'
kith.db.info = 'Kith Blessing: When the Gristlegrinder uses Brawl to grapple someone with intent to eat them, achieving three successes counts as an exceptional success.|/|/To Serve Man: A Gristlegrinder can make bite attacks that deal lethal damage, without needing to grapple a foe first. If she holds something or grapples someone of a smaller Size than herself, she can swallow it (or them) whole. She spends a point of Glamour and her jaw expands to the necessary size. With a successful Stamina + Survival roll, she gets the target down with minimal effort. A Gristlegrinder\'s digestive system deals two points of lethal damage per turn. If the target is poisoned or toxic, the Gristlegrinder takes damage as normal (p. 189), unless she has a Merit, token, or other means to negate it. Targets attacking the changeling from inside her must deal at least five points of lethal damage with a single attack to break out, but she can\'t apply her Defense or armor against such attacks.'
kith.db.restricted = False

kith = create_script('typeclasses.scripts.KithScript',key = 'Helldiver')
kith.db.longname = 'Helldiver'
kith.db.reference = 'CtL p. 54'
kith.db.info = 'Kith Blessing: When the Helldiver uses Larceny in the Hedge, Arcadia, or another unearthly realm, achieving three success counts as an exceptional success.|/|/Dive: Spend a Glamour point to make a Dexterity + Occult roll. On a success, the Helldiver begins to fade into an incorporeal, invisible form. It takes a number of turns equal to (10 − her current Clarity), to a minimum of one full turn, to completely fade. While fading, the Helldiver cannot take any non-reflexive actions or interact with objects or people, and attacks with a non-magical component pass harmlessly through her. Once she completely fades, she acts like a dematerialized Hedge ghost (p. 249), unable to physically interact with anything except other immaterial beings and objects, such as Hedge ghosts, other Helldivers, changelings using the Whispers of Morning Contract (p. 143), the unquiet dead, and spirits of all stripes. She can see and interact with all of these, no matter their current state. If she can find a gate to another realm, such as the deathly Underworld or mysterious Shadow, she may slip through with a point of Glamour as though it were a Hedgeway (p. 109). If ephemeral beings are normally material in another realm, she becomes so as well. She can spend as much time as she likes Diving, but she still requires basic necessities, such as food and sleep.|/|/To end this effect, spend another Glamour point and make another Dexterity + Occult roll. If successful, the changeling fades back into the world at the same rate she faded out. Should a Helldiver gain the Comatose Condition (p. 334) while Diving, she immediately vanishes from wherever she is to reappear inside her Bastion, as though she had passed through the Gate of Horn to be physically present in her dreams.'
kith.db.restricted = False

kith = create_script('typeclasses.scripts.KithScript',key = 'Hunterheart')
kith.db.longname = 'Hunterheart'
kith.db.reference = 'CtL p. 54-55'
kith.db.info = 'Kith Blessing: Choose either Investigation or Survival. When the Hunterheart uses the chosen Skill to track down creatures from Faerie, achieving three successes counts as an exceptional success.|/|/Pounce: If the target can see the Hunterheart\'s eyes, the changeling may spend a point of Glamour to lock the target in place or cause him to flee in terror. The Hunterheart\'s player rolls Presence + Wyrd as an instant action, contested by the target\'s Composure + Supernatural Tolerance. The target gains the Insensate Tilt (p. 330) or the Frightened Condition (p. 339) if the Hunterheart is successful, chosen by the target\'s player. If the changeling attacks the frozen or fleeing target, her unarmed attacks deal lethal damage.'
kith.db.restricted = False

kith = create_script('typeclasses.scripts.KithScript',key = 'Leechfinger')
kith.db.longname = 'Leechfinger'
kith.db.reference = 'CtL p. 55'
kith.db.info = 'Kith Blessing: When the Leechfinger uses Medicine to determine the health of a potential target, achieving three successes counts as an exceptional success.|/|/Sap The Vital Spark: If the Leechfinger maintains physical contact with a target for a full turn, she may spend a point of Glamour to inflict a point of bashing damage. This heals the Leechfinger, either downgrading one aggravated wound to lethal, one lethal to bashing, or one bashing to fully healed. As long as the Leechfinger maintains contact, she can spend a point of Glamour each turn to continue the effect. If the target is a changeling, the Leechfinger inflicts two points of damage per Glamour instead, and thus heals or downgrades two points of damage per turn.'
kith.db.restricted = False

kith = create_script('typeclasses.scripts.KithScript',key = 'Mirrorskin')
kith.db.longname = 'Mirrorskin'
kith.db.reference = 'CtL p. 55-56'
kith.db.info = 'Kith Blessing: When the Mirrorskin uses Stealth while in disguise, achieving three successes counts as an exceptional success.|/|/Mercurial Visage: A Mirrorskin may mold and shape her appearance like putty, making an entirely new Mask out of composite pieces of people she\'s met or seen in photos. Spend a point of Glamour and make a reflexive Wits + Subterfuge + Wyrd roll, with no penalties for lacking equipment. For an extra point of Glamour, the changeling can build a new composite mien as well. Supernatural abilities that would pierce her deception prompt a Clash of Wills (p. 126). This effect lasts indefinitely, but the changeling must use it again even to return to her own natural appearance.'
kith.db.restricted = False

kith = create_script('typeclasses.scripts.KithScript',key = 'Nightsinger')
kith.db.longname = 'Nightsinger'
kith.db.reference = 'CtL p. 56-57'
kith.db.info = 'Kith Blessing: When the Nightsinger uses Expression to sing or compose a piece of music, achieving three successes counts as an exceptional success.|/|/Siren Song: Spend a point of Glamour and roll Presence + Expression + Wyrd as an instant action, contested with Composure + Supernatural Tolerance by anyone who hears the Nightsinger\'s unearthly song. Anyone who fails gains the Swooned Condition (p. 345) and is rooted to the spot for as long as the Nightsinger continues to sing; the changeling can take a victim\'s hand and lead him along with her, but otherwise he can\'t move, although he can still apply his Defense against attacks. Jarring him out of it requires an opposing power (prompting a Clash of Wills), dealing him at least as much damage as his Stamina rating, or making it impossible for him to hear the song anymore.'
kith.db.restricted = False

kith = create_script('typeclasses.scripts.KithScript',key = 'Notary')
kith.db.longname = 'Notary'
kith.db.reference = 'CtL p. 57'
kith.db.info = 'Kith Blessing: When the Notary uses Politics to negotiate, read, or interpret a fae pledge, achieving three successes counts as an exceptional success.|/|/Abatement: Once per chapter, a Notary can completely negate the need for Glamour in a pledge as long as she is involved in its creation, without a roll. Thereafter, the Notary can perfectly recite the pledge as long as it lasts.'
kith.db.restricted = False

kith = create_script('typeclasses.scripts.KithScript',key = 'Playmate')
kith.db.longname = 'Playmate'
kith.db.reference = 'CtL p. 57-58'
kith.db.info = 'Kith Blessing: When the Playmate uses Persuasion to make someone like her or her friends, achieving three successes counts as an exceptional success.|/|/Coeur Loyal: A Playmate may touch a wounded character and spend a point of Glamour to heal any number of bashing or lethal damage points as an instant action. She takes the same amount of mild Clarity damage as bashing damage healed, and the same amount of severe Clarity damage as lethal damage healed; apply the mild damage first. She can\'t heal more damage than she has room to take more Clarity damage. It is entirely possible for a Playmate to lose herself completely while healing others.'
kith.db.restricted = False

kith = create_script('typeclasses.scripts.KithScript',key = 'Snowskin')
kith.db.longname = 'Snowskin'
kith.db.reference = 'CtL p. 58-59'
kith.db.info = 'Kith Blessing: When the Snowskin attempts to use Subterfuge to hide her feelings from others, achieving three successes counts as an exceptional success.|/|/Heart of Ice: A Snowskin\'s derision is more vicious than a howling blizzard. When she attempts to shut someone down in front of an audience, spend a point of Glamour and roll Presence + Intimidation + Wyrd, contested by the target\'s Composure + Supernatural Tolerance. If the Snowskin succeeds, her target gains the Shaken Condition (p. 344) and suffers a −2 on all Social rolls involving other changelings until the Condition resolves, as her contempt freezes him out of society.'
kith.db.restricted = False

pass
