from evennia import create_script

spell = create_script('typeclasses.scripts.spellScript',key = 'Cold_Snap')
spell.db.longname = 'Cold Snap'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage dissipates the heat in the spell\'s area of effect, causing frost and ice to form on the floor and exposed surfaces. For the Duration of the spell, all surfaces in the area are under the effects of the Ice Tilt (p. 321).'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Corpse_Mask')
spell.db.longname = 'Corpse Mask'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage alters the appearance of a body to make it look different even under scrutiny. She can cast the spell on a corpse, modifying its wounds and apparent time and cause of death completely. She can make a charred corpse look as though it instead died of a heart attack, or a person who died in a car crash look as though he is the victim of a stab wound.'
spell.db.reference = 'M:tA p. 129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Create_Anchor')
spell.db.longname = 'Create Anchor'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage applies a universally-applicable version of the Anchor Condition to a subject, usable by any ghosts. If the mage also has a ghost as an additional subject, that ghost becomes anchored to the new Anchor as well as its own.'
spell.db.reference = 'M:tA p. 133'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Create_Avernian_Gate')
spell.db.longname = 'Create Avernian Gate'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage rips open the material world to the Underworld, creating an Iris between the material world and the upper layers of the Underworld within the area of effect. Opening the gate causes the area to gain a Death Resonance and the Gateway Condition for the Duration of the spell.'
spell.db.reference = 'M:tA p. 133'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Create_Ghost')
spell.db.longname = 'Create Ghost'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage creates a ghost within Twilight. She can fashion the ghost as an echo of another person, either alive or dead, though the ghost is not the actual person. The ghost is created at Rank 1 and remains for the Duration of the spell as the mage\'s loyal servant, and she is able to direct it to take actions without the use of any additional spells.'
spell.db.reference = 'M:tA p. 133'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Damage_Ghost')
spell.db.longname = 'Damage Ghost'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage can cause pain to a ghost. She deals one bashing wound to the ghost\'s Corpus per Potency of the spell.'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Decay')
spell.db.longname = 'Decay'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage degrades a material object, causing it to age in a matter of moments. The object\'s Durability is lowered by -1 for each Potency of the spell\'s casting.'
spell.db.reference = 'M:tA p. 129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Deepen_Shadows')
spell.db.longname = 'Deepen Shadows'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can influence the shadows in the spell\'s area of effect, deepening darkness and making the area nearly completely pitch black. The area is affected by the Poor Light Environmental Tilt for the Duration of the spell.'
spell.db.reference = 'M:tA p. 128'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Deny_the_Reaper')
spell.db.longname = 'Deny the Reaper'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage is able to reverse the effects of entropy on her subject, even returning the dead back to life. The mage reverses the effects of decay, restoring the subject to its physical state of being from before up to one month per Potency of the spell. On a living subject, the spell can restore eyesight, the use of limbs, reversing irreparable damage, and restoring all bodily functions. On inanimate subjects the spell can restore time-ravaged photos, make old books pristine, or return old electronics to working order.'
spell.db.reference = 'M:tA p. 133'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Devouring_the_Slain')
spell.db.longname = 'Devouring the Slain'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage may pull the energy from his subject\'s suffering into himself. The mage chooses at the time of casting to either harvest Willpower or to scourge the subject\'s Pattern for Mana. The subject must have at least one Health box filled with either lethal or aggravated damage. For each level of Potency, the mage may take one point of Willpower (up to the subject\'s remaining Willpower points), or he may Scour the subject\'s Pattern for one point of Mana, dealing one lethal damage in the process, causing existing wounds to open and fester. Using this spell counts towards the limit of times per day a mage can gain Mana through Scouring.'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Ectoplasm')
spell.db.longname = 'Ectoplasm'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can create ectoplasm (see Ectoplasmic Shaping, above) from one of his own orifices, or the orifice of a corpse - normally the nose or mouth, but sometimes the tear ducts or ears. The mage can shape the ectoplasm into any shape he wishes. The ectoplasm retains its shape for the Duration of the spell.'
spell.db.reference = 'M:tA p. 129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Ectoplasmic_Shaping')
spell.db.longname = 'Ectoplasmic Shaping'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage may shape and mold an ectoplasmic manifestation, either conjured by another mage or from a Materialized ghost, though the person or ghost that controls the ectoplasm may Withstand the shaping. After a successful casting, the mage shapes the ectoplasm into any shape he desires. The ectoplasm remains in the new shape for the Duration of the spell. He can use it to craft a mirror that reflects ghosts and other structures in ghostly Twilight in a given area.'
spell.db.reference = 'M:tA p. 128'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Empty_Presence')
spell.db.longname = 'Empty Presence'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage destroys the subject\'s presence in the world, removing any evidence of her life or existence. Any attempts to see the subject through mundane means of detection or observation fail completely. Not only is she invisible to the naked eye, but evidence of her life is scrubbed. All Doors she may have opened during social interactions with others, either on herself or on the other person, are removed. All her Conditions, and all Conditions applying to her (except for Paradox Conditions), resolve without granting Beats. While invisible, the subject cannot make violent, overt actions without breaking the spell\'s illusion. Physically damaging or breaking objects, or attacking someone, causes the spell to end immediately.'
spell.db.reference = 'M:tA p. 133'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Enervation')
spell.db.longname = 'Enervation'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage causes her subject\'s muscles to stop working, breaking down connections between muscles, ligaments, and tendons. The spell imposes either the Leg Wrack Tilt or the Arm Wrack Tilt on the subject while the spell remains active.'
spell.db.reference = 'M:tA p. 132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Exorcism')
spell.db.longname = 'Exorcism'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 4'
spell.db.info = 'This spell rips a ghost\'s grip on the world away. This spell strips a number of Manifestation Conditions from the ghost (or its host) equal to the spell\'s Potency. The effect is Lasting, but the spirit may use its Influences and Manifestations to reestablish the Conditions as normal.'
spell.db.reference = 'M:tA p. 132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Forensic_Gaze')
spell.db.longname = 'Forensic Gaze'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can determine the state of a corpse. She determines the exact method of its demise as well as exactly when it died. For each level of Potency, the mage reveals contributing factors to the cause of death. For example, a man found burned in a car might have died from asphyxiation, but might have gotten that way because he was unconscious due to a head wound from crashing his car into a tree while driving drunk.'
spell.db.reference = 'M:tA p. 128'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Ghost_Gate')
spell.db.longname = 'Ghost Gate'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage creates a two-dimensional plane that acts as a gateway, converting anything that moves through it into Twilight. While in Twilight, the person can interact with and see Death-attuned ephemeral objects and beings. Items can be carried through the gate, but doing so destroys their material forms, though they may be retrieved later with "Touch of the Grave."'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Ghost_Shield')
spell.db.longname = 'Ghost Shield'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The caster creates a shield that protects her subject from ghostly Numina, Influences, Manifestations, Death spells, and any death-related powers of other supernatural creatures. Any power attempting to pierce the shield provokes a Clash of Wills roll.'
spell.db.reference = 'M:tA p. 129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Ghost_Summons')
spell.db.longname = 'Ghost Summons'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage sends out a call to the nearest ghost within her sensory range. Alternately, she can summon ghosts she knows personally. She may send a general call and the nearest ghost will answer, or she can specify the type of ghost, such as a child or a female. The ghost cannot travel farther than allowed by its Anchor. The spell does not work on ghosts above Rank 5.'
spell.db.reference = 'M:tA p. 131'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Quicken_Corpse')
spell.db.longname = 'Quicken Corpse'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The caster can animate a corpse, creating a loyal zombie servant. A zombie has limited mental capacity, and can understand simple one- or two-word commands and nothing more. It is a mindless, soulless construct immune to fear, pain, exhaustion, intimidation, or coercion, and follows the creator\'s orders with no regard to self. The corpse\'s physical capabilities are impaired, making them slow and clumsy compared to a living person. The constructs are not suited for combat (and have no Defense), but count as Retainers worth dots equal to the spell\'s Potency with a "field" relating to the mage\'s commands. Zombies have as much Health as the living creature their corpse came from had, but suffer damage as though they are under the effects of Death Mage Armor. They do not fall unconscious through damage, or bleed when filled with lethal damage, and are only destroyed when their last Health box is filled with aggravated damage.'
spell.db.reference = 'M:tA p. 131'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Quicken_Ghost')
spell.db.longname = 'Quicken Ghost'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage bolsters a ghost, making low-Ranked ghosts more powerful and aware than they once were. Each level of Potency raises one of the ghost\'s three Attributes by one, not to exceed its Rank maximum. The mage can instead use the spell to heal a ghost\'s Corpus at a rate of one point per Potency of the spell.'
spell.db.reference = 'M:tA p. 131-132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Revenant')
spell.db.longname = 'Revenant'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage may grant a ghost a Manifestation Condition (see p. 258). The mage may grant a number of Conditions equal to the spell\'s Potency, and must create any prerequisite Conditions as well, if they aren\'t already present. The entity immediately enters the Manifestation of the mage\'s choice, and may not leave it while the spell remains in effect. Mages often use this spell to allow ghosts to Possess their own corpses, creating undead beings called revenants.'
spell.db.reference = 'M:tA p. 132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Rotting_Flesh')
spell.db.longname = 'Rotting Flesh'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage\'s touch rots away at her subject, causing his flesh and bones to wither and decay. Each level of Potency deals one point of bashing damage to the subject.'
spell.db.reference = 'M:tA p. 132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Sever_Soul')
spell.db.longname = 'Sever Soul'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage rips the soul from a Sleeper, casting it into Twilight. While without a soul, the subject suffers from the Soulless Condition (p. 318). When the spell\'s Duration ends, the Sleeper\'s soul returns to him, unless otherwise prevented from escape, such as the case of being trapped in a soul jar or inside another body (see "Soul Jar" p. 129). If this spell is cast on a subject who is already under the effects of the Soulless Condition, he is stepped up to the Enervated Condition (p. 315) - though the mage does not gain immediate access to his soul, since it is already missing.'
spell.db.reference = 'M:tA p. 132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Sever_the_Awakened_Soul')
spell.db.longname = 'Sever the Awakened Soul'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The soul of a mage cannot be removed with Fraying alone; Awakened Gnosis holds it tight, requiring mastery to prise lose. This spell Unmakes the protective metaphysical layers of a mage\'s soul, ripping it free and placing it into a container. That container can either be a specially prepared vessel such as one created with "Soul Jar," or the caster can take the soul into her own body. While without a soul, the subject suffers from the Soulless Condition. If this spell is cast on a subject who is already under the effects of the Soulless Condition, he is stepped up to the Enervated Condition - though the mage does not gain immediate access to his soul, since it is already missing.'
spell.db.reference = 'M:tA p. 133-134'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Shadow_Crafting')
spell.db.longname = 'Shadow Crafting'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The caster can shape and harden shadows into solid, three-dimensional forms. The object gains a Durability of 2. If it is a weapon it gains a weapon rating of 2; if it is armor it gains an armor rating of 2; otherwise the object gains a +2 equipment bonus. Objects made of shadow retain a shadowy appearance and cast no shadow of their own.'
spell.db.reference = 'M:tA p. 132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Shadow_Flesh')
spell.db.longname = 'Shadow Flesh'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage transforms the subject\'s body and all her personal possessions into a mass of moving and animated shadows. The mage may choose to make the subject a three-dimensional or a two-dimensional shadow. Three-dimensional shadows still have no apparent mass or substance, and cannot interact with physical objects. Two-dimensional shadows may move through cracks and crevices, though are still bound by the laws of gravity and must remain touching the floor, even if moving on walls.'
spell.db.reference = 'M:tA p. 132-133'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Shadow_Sculpting')
spell.db.longname = 'Shadow Sculpting'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can mold and shape the shadows in the area of effect. He can shape the shadows into any likeness of his choosing. The area must have shadows present for the mage to shape them.'
spell.db.reference = 'M:tA p. 128'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Shape_Ephemera')
spell.db.longname = 'Shape Ephemera'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The caster may reshape Death-attuned ephemera from one object into a new object entirely. This ephemera can be from a ghost or other entity in Twilight, but they have the ability to Withstand the spell, and being reshaped does not damage the entity\'s Corpus.'
spell.db.reference = 'M:tA p. 129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Soul_Armor')
spell.db.longname = 'Soul Armor'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'This spell armors the subject\'s soul against all who would profane it. Any spell or effect that would remove, manipulate, or injure the subject\'s soul must first win a Clash of Wills.'
spell.db.reference = 'M:tA p. 129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Soul_Jar')
spell.db.longname = 'Soul Jar'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage creates a receptacle for a displaced soul. The soul jar can be anything designed to hold and seal a liquid, from a paint can to a water bottle. A soul placed into the soul jar cannot escape and is protected from outside attack. If the jar is opened or broken before the Duration of the spell ends, the soul is released.'
spell.db.reference = 'M:tA p. 129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Soul_Marks')
spell.db.longname = 'Soul Marks'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can determine the health of a person\'s soul. She can determine one soul mark per Potency of the spell cast. She can discern the presence of Persistent Conditions, if the subject is Awakened, if the subject is a supernatural being, if the subject has created a soul stone (see "Soul Stones" p. 98), if the subject has had her soul tampered with, if the subject is Possessed, the presence of any Gnosis 5+ Legacy Attainments, if the subject has eaten or otherwise consumed another\'s soul, or if the subject is suffering from a Paradox Condition.'
spell.db.reference = 'M:tA p. 128'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Speak_with_the_Dead')
spell.db.longname = 'Speak with the Dead'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage is able to sense and communicate with ghosts within Twilight. She can sense all ghosts within the area of effect, and is capable of communicating with them by simply talking, as long as the ghost is capable of understanding a language she speaks. She may sense Anchors within the area without using Death Mage Sight. She can concentrate on a single ghost within the area and determine its Rank, if it has an Anchor, and how many Anchors it has.'
spell.db.reference = 'M:tA p. 128-129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Suppress_Aura')
spell.db.longname = 'Suppress Aura'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage suppresses the personal aura of her subject. The subject\'s Nimbus disappears and magical resonances around her are dampened, including the resonances of spells currently affecting her. She appears as a Sleeper to Mage Sight. She is harder to read in general, imposing a -2 penalty on Empathy checks, and supernatural attempts to discern her emotional or mental state. Magical attempts to see through the disguise provoke a Clash of Wills.'
spell.db.reference = 'M:tA p. 129-130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Suppress_Life')
spell.db.longname = 'Suppress Life'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can suppress the subject\'s life signs; the subject appears for all intents and purposes as though she is dead. All physical symptoms of death appear to set in and the soul appears absent from the body to magical senses.'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Touch_of_the_Grave')
spell.db.longname = 'Touch of the Grave'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can physically interact with ghosts and other things in Death-attuned Twilight. She can "pull" items from Twilight, making them visible and solid; these items have a Durability of 1 and dissipate into ephemera if broken, or after the spell\'s Duration ends. Items pulled from Twilight function as their material counterparts bestowing the same equipment bonuses.'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Withering')
spell.db.longname = 'Withering'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage causes the subject\'s body to wither and atrophy within moments, dealing one point of lethal damage per level of Potency of the spell.'
spell.db.reference = 'M:tA p. 133'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Without_a_Trace')
spell.db.longname = 'Without a Trace'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'People constantly shed dead skin, hair, and other small evidences of themselves as they pass through the world. The mage conceals all physical evidence from casual observation. For the Duration of the spell, the subject leaves no fingerprints, footprints, traces of blood, or any other forensic type evidence of herself behind. Using Death Mage Sight to search for such signs provokes a Clash of Wills.'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

pass