from evennia import create_script

spell = create_script('typeclasses.scripts.spellScript',key = 'Corpse_Mask')
spell.db.longname = 'Corpse Mask'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage alters the appearance of a body to make it look different even under scrutiny. She can cast the spell on a corpse, modifying its wounds and apparent time and cause of death completely. She can make a charred corpse look as though it instead died of a heart attack, or a person who died in a car crash look as though he is the victim of a stab wound.'
spell.db.reference = 'M:tA p. 129'
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

spell = create_script('typeclasses.scripts.spellScript',key = 'Forensic_Gaze')
spell.db.longname = 'Forensic Gaze'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can determine the state of a corpse. She determines the exact method of its demise as well as exactly when it died. For each level of Potency, the mage reveals contributing factors to the cause of death. For example, a man found burned in a car might have died from asphyxiation, but might have gotten that way because he was unconscious due to a head wound from crashing his car into a tree while driving drunk.'
spell.db.reference = 'M:tA p. 128'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Ghost_Shield')
spell.db.longname = 'Ghost Shield'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The caster creates a shield that protects her subject from ghostly Numina, Influences, Manifestations, Death spells, and any death-related powers of other supernatural creatures. Any power attempting to pierce the shield provokes a Clash of Wills roll.'
spell.db.reference = 'M:tA p. 129'
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

spell = create_script('typeclasses.scripts.spellScript',key = 'Without_a_Trace')
spell.db.longname = 'Without a Trace'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'People constantly shed dead skin, hair, and other small evidences of themselves as they pass through the world. The mage conceals all physical evidence from casual observation. For the Duration of the spell, the subject leaves no fingerprints, footprints, traces of blood, or any other forensic type evidence of herself behind. Using Death Mage Sight to search for such signs provokes a Clash of Wills.'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

pass