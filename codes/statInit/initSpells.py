from evennia import create_script

spell = create_script('typeclasses.scripts.spellScript',key = 'Adverse_Weather')
spell.db.longname = 'Adverse Weather'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage summons a major weather system as severe as a tornado, tsunami, monsoon, or hurricane. The weather effects take hold in minutes and dissipate immediately once the spell expires. This allows the mage to create Extreme Environments of nearly any kind up to Level 4, as per Control Weather (see above) but without the limitations. She does not have to call up disasters; she can make a rainstorm appear in a cloudless blue sky if she desires.'
spell.db.reference = 'M:tA p. 146'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Atonement')
spell.db.longname = 'Atonement'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 4'
spell.db.info = 'A powerful Witch can aid a hero who labors under a curse, but her remedies often demand strange rituals or arduous quests. This spell can dispel a supernatural effect enforced by the dictates of destiny, including Awakened spells, by Patterning Fate to provide a means by which the subject can escape his curse. While the subject remains under the effects of Atonement, she must complete a task determined by the caster.'
spell.db.reference = 'M:tA p. 137-138'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Call_Lightning')
spell.db.longname = 'Call Lightning'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 3'
spell.db.info = 'With a gesture the mage can conjure lightning down from a stormy sky to strike her foes. She must use this spell with an existing storm or one she sets into motion with "Control Weather" (see p. 143), since she cannot create lightning from nothing at this level.'
spell.db.reference = 'M:tA p. 144'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Chaos_Mastery')
spell.db.longname = 'Chaos Mastery'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage can Pattern Fate to manipulate complex probabilities within the spell\'s subject or area of effect. This spell allows the mage to dictate any physically possible outcome within the bounds of the spell\'s subject, no matter how unlikely.'
spell.db.reference = 'M:tA p. 138'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Cold_Snap')
spell.db.longname = 'Cold Snap'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage dissipates the heat in the spell\'s area of effect, causing frost and ice to form on the floor and exposed surfaces. For the Duration of the spell, all surfaces in the area are under the effects of the Ice Tilt (p. 321).'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Control_Electricity')
spell.db.longname = 'Control Electricity'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage may alter the flow of electricity as well as diminish its current. She cannot increase the current without some device capable of generating it, since she cannot create electricity from nothing. For example, the mage can direct the electricity in a building to single or multiple outlets, cut the power, or divide power going to one outlet to many other sources. This requires a method of conduction, like existing wiring or metal. She can also cause existing electrical currents to arc (such as striking a target near a wall outlet), or redirect it away from a particular device. Causing a short or using the electrical current to attack a target usually burns out the breakers or shorts out a device afterward, unless it\'s made to withstand the stresses of power fluctuations. Damage caused by this spell uses the electrical damage rules on p. 224. By directing the flow away from a subject, she subtracts the spell\'s Potency from the damage of an electrical source.'
spell.db.reference = 'M:tA p. 142'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Control_Fire')
spell.db.longname = 'Control Fire'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can exert control over a fire, fueling it to increase its size and intensity or depriving it of fuel to snuff it out. She can only control existing flames at this level, but can change a small campfire into a roaring inferno or bring even an out-of-control fire down to manageable levels.'
spell.db.reference = 'M:tA p. 142'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Control_Gravity')
spell.db.longname = 'Control Gravity'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can redirect the force of gravity in an area. She can alter the direction of its pull, causing affected objects to "fall" upwards or horizontally. She can\'t do more than change its direction at this level, but she can make it nearly impossible to approach a specific object or area without some means of overcoming gravity, like flight or climbing gear.'
spell.db.reference = 'M:tA p. 142'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Control_Heat')
spell.db.longname = 'Control Heat'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can now increase or decrease the temperature of an area. Each level of Potency allows a change of 1 level of Extreme Environment to produce heat or cold, counting a temperate room temperature as "zero." For example, with Potency 3, a mage could transform a Level 1 Extreme Environment based on cold into a Level 2 Environment based on heat.'
spell.db.reference = 'M:tA p. 142'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Control_Light')
spell.db.longname = 'Control Light'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can dim or intensify existing light the spell\'s area of effect, whether from an artificial or natural source. This can cause a 40-watt bulb to shine as brightly as a floodlight or make the sunlight on an overcast day like that of a clear summer morning. The magic modifies the light emitted by the source, and not the source or the emission itself, so this won\'t cause a bulb to burn itself out or increase the heat of sunlight without other spells. Each level of Potency in the spell doubles or halves the light\'s candescence.'
spell.db.reference = 'M:tA p. 142'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Control_Sound')
spell.db.longname = 'Control Sound'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'This spell allows a mage to amplify or weaken the volume of sound in the spell\'s area of effect. She can make a loudspeaker into a thunderous blast or a barely audible squeak. Each level of Potency doubles or halves the volume of sound in the targeted area, creating a zone of altered sound. For example, casting this spell on a podium at the front of the room affects the sounds of anyone standing at the podium. The mage can also influence the direction of existing sounds. She can focus sound waves from across the room to hear a whispered conversation, ensure her own voice does not reach anyone but her intended target, or cause noises to emanate from nearby locations instead of their original sources. The Scale factor determines the area she can affect.'
spell.db.reference = 'M:tA p. 142-143'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Control_Weather')
spell.db.longname = 'Control Weather'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can control existing weather patterns. She can force a light shower to become a thunderstorm, summon up fog on a clear morning, make a warm day into an unbearably hot one or conjure a cooling breeze. Drastic changes from existing weather require Reach, as noted below. The weather begins to change immediately upon casting the spell, with new systems taking shape within minutes. This spell allows the mage to change or create weather-based Extreme Environments up to Level 4, as well as cause a wide variety of environmental Tilts. Potency determines the maximum amount by which an Extreme Environment can change, up to a maximum of Level 4 (and a minimum of level 0). Listed below is an example set of Tilts possible for weather patterns, but it is by no means exhaustive. Note that without further spells, the mage is not immune to weather ilts she creates.'
spell.db.reference = 'M:tA p. 143'
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

spell = create_script('typeclasses.scripts.spellScript',key = 'Create_Energy')
spell.db.longname = 'Create Energy'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage creates energy from othing within a subject or area of effect. She can create light (including sunlight), fire, radiation, sound, and electricity. Use the chart under Transform Energy above as an example of the levels she can create within the affected area. For fire, assume the heat is +1 for Potency 1-2, +2 for Potency 3-4 and +3 for Potency 5+. After creating the energy, she can modify it with Control spells. Creating radiation also creates an Extreme Environment hazardous to living beings.'
spell.db.reference = 'M:tA p. 146'
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

spell = create_script('typeclasses.scripts.spellScript',key = 'Divine_Intervention')
spell.db.longname = 'Divine Intervention'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage casts a powerful curse that either encourages the subject to achieve a goal specified by the mage when he casts this spell, or that thwarts the subject\'s every attempt to pursue such a goal. The subject must, however, be aware of the goal, and the mage cannot levy impossible tasks.'
spell.db.reference = 'M:tA p. 138'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Earthquake')
spell.db.longname = 'Earthquake'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage unleashes an earthquake to crack the ground. This spell inflicts damage equal to its Potency to all structures within the affected area. Most modern buildings are built to endure earthquakes well and subtract their Durability from the damage as normal. Smaller or flimsier structures do not apply Durability to the damage at all. Living beings may make a Dexterity + Athletics roll to maintain their balance as the ground pitches and heaves beneath them. Failure means the character suffers bashing damage as she falls to the ground and is thrown about wildly, unless the fall sends her tumbling down stairs or over a ledge. Collapsing buildings can cause much more catastrophic damage or leave victims trapped under tons of debris.'
spell.db.reference = 'M:tA p. 147'
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

spell = create_script('typeclasses.scripts.spellScript',key = 'Electromagnetic_Pulse')
spell.db.longname = 'Electromagnetic Pulse'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage degrades electromagnetic energy within the spell\'s subject, wrecking electronic devices. The spell is capable of snuffing out mundane electrical devices, although some military-grade devices are shielded, requiring Potency equal to their level of hardening. Shorting out magical devices requires a Clash of Wills. When used against a living being, the damage to their nervous system acts as a direct damage spell, inflicting Potency in lethal damage.'
spell.db.reference = 'M:tA p. 145'
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

spell = create_script('typeclasses.scripts.spellScript',key = 'Environmental_Shield')
spell.db.longname = 'Environmental Shield'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can shield herself against harmful environmental conditions. This spell provides complete resistance to any Conditions or Tilts caused by environments, up to an Extreme Environment level of the spell\'s Potency. The spell only protects against indirect damage, like heat and cold and minor hazards like hail. The mage can still drown or be crushed by crashing waves. While the spell wouldn\'t protect her against lightning if something forced it to strike her, she wouldn\'t naturally attract the bolt. The spell requires a Clash of Wills to work against magical weather effects.'
spell.db.reference = 'M:tA p. 143'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Eradicate_Energy')
spell.db.longname = 'Eradicate Energy'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 5'
spell.db.info = 'Rather than create energy, the mage snuffs out energies within a subject or area (see the chart "Transform Energy," above, for the Potency required by different levels of energy.) The destruction is spectacular, explosively scattering the affected energies into particles. If used on a creature, this spell is instantly fatal but Withstood by Stamina.'
spell.db.reference = 'M:tA p. 146'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Exceptional_Luck')
spell.db.longname = 'Exceptional Luck'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage blesses the subject\'s endeavors or curses them with misfortune. Whether good or bad, the subject\'s luck is truly exceptional. This spell bestows a boon or inflicts a hex on the subject (see p. 134). The subject may Withstand a hex with Composure'
spell.db.reference = 'M:tA p. 135'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Exorcism')
spell.db.longname = 'Exorcism'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 4'
spell.db.info = 'This spell rips a ghost\'s grip on the world away. This spell strips a number of Manifestation Conditions from the ghost (or its host) equal to the spell\'s Potency. The effect is Lasting, but the spirit may use its Influences and Manifestations to reestablish the Conditions as normal.'
spell.db.reference = 'M:tA p. 132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Fabricate_Fortune')
spell.db.longname = 'Fabricate Fortune'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 2'
spell.db.info = 'Sometimes a mage wishes to hide a child of destiny from those who would abuse her gift. Other times he wishes to convince observers that a subject has a fate that she does not. This spell conceals or falsifies fates and Destiny.'
spell.db.reference = 'M:tA p. 136'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Fools_Rush_In')
spell.db.longname = 'Fools Rush In'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 2'
spell.db.info = 'According to old wisdom Fate favors children and fools, and this spell makes the old adage true. So long as the subject has little or no detailed knowledge about a situation before he enters it, the spell allows him to act with perfect grace and timing. A turn or two of studying the scene before acting is acceptable, but extensive reconnaissance or a detailed briefing does not permit the necessary degree of randomness this spell requires.'
spell.db.reference = 'M:tA p. 136'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Forensic_Gaze')
spell.db.longname = 'Forensic Gaze'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can determine the state of a corpse. She determines the exact method of its demise as well as exactly when it died. For each level of Potency, the mage reveals contributing factors to the cause of death. For example, a man found burned in a car might have died from asphyxiation, but might have gotten that way because he was unconscious due to a head wound from crashing his car into a tree while driving drunk.'
spell.db.reference = 'M:tA p. 128'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Forge_Destiny')
spell.db.longname = 'Forge Destiny'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 5'
spell.db.info = 'If a Master of Fate does not have a hero of destiny handy, he can simply make one. He has several means of accomplishing this at his disposal, and may apply one of the following effects:'
spell.db.reference = 'M:tA p. 139'
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

spell = create_script('typeclasses.scripts.spellScript',key = 'Grave_Misfortune')
spell.db.longname = 'Grave Misfortune'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 3'
spell.db.info = 'This spell attracts misfortune to the subject or makes an already injurious situation considerably worse.'
spell.db.reference = 'M:tA p. 137'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Gravitic_Superiority')
spell.db.longname = 'Gravitic Superiority'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage may increase or decrease gravity. If increasing it, each level of Potency subtracts 3 Speed from all subjects, as well as penalizing jumping rolls, subtracting a distance equal to Potency from success rolled. If Potency exceeds the Strength of an animal caught in the area, the subject suffers -1 to all Physical dice pools for each point of difference. Flying creatures must succeed on a Strength + Athletics roll each turn or plummet downward at a Speed equal to the Potency.'
spell.db.reference = 'M:tA p. 144'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Influence_Electricity')
spell.db.longname = 'Influence Electricity'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can operate or shut down electrical devices with magic. With this spell she can only cause existing devices to work as they normally would when powered on, or when the power is shut off. For example, she could "hotwire" a car without actually needing to touch any wires, turn lights off and on, and cause industrial machinery to power up or turn off. This spell does not give her further control over these devices, but does allow her to engage or shut down devices that might otherwise require passwords or electronic keys.'
spell.db.reference = 'M:tA p. 140'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Influence_Fire')
spell.db.longname = 'Influence Fire'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Legends of mages controlling fire begin with this spell, which allows a mage to guide the path of existing flames. This lets her cause flames to arc or stretch, command them to burn along a particular path (or prevent them from another), or even form particular fiery shapes. At this level the mage cannot increase the flames in size or intensity, though she could direct them into a source of fuel.'
spell.db.reference = 'M:tA p. 140-141'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Influence_Heat')
spell.db.longname = 'Influence Heat'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Initiates can guide the direction of existing forces. With this spell, the mage can control the flow of heat in the area. While she cannot increase or create heat, the mage can direct heat from a radiator across the room to her, or pull any ambient warmth shed by car engines, human bodies, or environmental sources. This can keep her warm in cold weather or cool in hot weather, preventing heat- or cold-related damage and Conditions caused by Extreme Environments up to Level 2 (see Extreme Environments, p. 224).'
spell.db.reference = 'M:tA p. 141'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Interconnections')
spell.db.longname = 'Interconnections'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 1'
spell.db.info = 'This spell reveals the marks of Fate on people, places, and things the mage observes (up to one subject per turn). In addition to allowing the mage to detect any sympathetic connections between the subjects, the mage can also identify those who have violated a magical oath, and the presence of spells with conditional Durations (see p. 192).'
spell.db.reference = 'M:tA p. 134-135'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Invisibility')
spell.db.longname = 'Invisibility'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'This spell can render its subject completely invisible, masking it from all forms of light. Even cameras cannot detect the object, no matter what type of filter or lenses they use. This spell does not mask the sounds an object makes, although when Combined with "Control Sound" (see above), the target can be made invisible and soundless.'
spell.db.reference = 'M:tA p. 143'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Kinetic_Blow')
spell.db.longname = 'Kinetic Blow'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage focuses the kinetic force of bludgeoning attacks to such a pinpoint that they cause damage like piercing weapons. This only works on the subject\'s unarmed attacks and not any held weapons, though body-hugging objects like gloves and shoes benefit from the spell\'s effect. Unarmed attacks (including those made in grapples) gain a weapon bonus equal to Potency, to a maximum of 5, and inflict lethal damage.'
spell.db.reference = 'M:tA p. 143-144'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Kinetic_Efficiency')
spell.db.longname = 'Kinetic Efficiency'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 1'
spell.db.info = 'With a simple spell, the mage can "nudge" kinetic forces, enhancing a subject\'s motion. This spell allows the subject to run a little faster, jump a little further, or lift a little more, not by altering forces but by maximizing the subject\'s kinetic energy use. This has the following benefits:'
spell.db.reference = 'M:tA p. 141'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Levitation')
spell.db.longname = 'Levitation'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The subject floats through the air using telekinetic force. Its air speed equals the spell\'s Potency. Subjects may use their Defense against attacks, if applicable. Unwilling subjects Withstand the spell with Stamina.'
spell.db.reference = 'M:tA p. 145'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Lucky_Number')
spell.db.longname = 'Lucky Number'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The probability of correctly guessing a phone number, a password, or lock combination on the first try is minute but not impossible. This spell allows the mage to do just that simply by entering data into an appropriate device (a password field, a telephone, a safe combination, etc.). In addition to any story benefits, the mage gains the Informed Condition on next relevant roll that benefits from knowledge gained through this spell.'
spell.db.reference = 'M:tA p. 136'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Miracle')
spell.db.longname = 'Miracle'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 5'
spell.db.info = 'This spell causes events to unfold according to the mage\'s dictates. The mage receives a number of Intercessions equal to Potency, which she may use as a reflexive action during the spell\'s Duration. Spending one Intercession can achieve the following, affecting a single subject within sensory range:'
spell.db.reference = 'M:tA p. 140'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Monkeys_Paw')
spell.db.longname = 'Monkey\'s Paw'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage interacts with a lifeless object, bringing fortune to bear on it and making it a tool of destiny. The mage either blesses or curses the object.'
spell.db.reference = 'M:tA p. 137'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Nightvision')
spell.db.longname = 'Nightvision'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Despite its name, the Nightvision spell enhances ambient light, fine-tunes the mage\'s sense for vibrations and thermal changes, and grants her the power to see into the infrared and ultraviolet spectra. She becomes able to intuitively feel as well as see forms of electromagnetic radiation, sound, and kinetic energies, allowing her to navigate without penalty in complete darkness. She can still see and make out details, even in the dark, although colors are somewhat muted. This spell has the side effect of making the caster much more vulnerable to light; while in effect, she suffers no penalties from dim or even no lighting, but suffers penalties from bright lights as she normally would from darkness. Bright lights and extremely loud sounds can disorient or even inflict the Blind Condition on her for the spell\'s Duration.'
spell.db.reference = 'M:tA p. 141'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Oaths_Fulfilled')
spell.db.longname = 'Oaths Fulfilled'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 1'
spell.db.info = 'In folktales, witches always seem to know when their subjects fulfill (or violate) the terms of an agreement. This spell notifies the mage when a specified fate befalls its subject - whether the subject is the victim or the actor. This triggering event must be something the mage could perceive if he were present (e.g. the subject suffers an injury, goes to the restroom, breaks her word, speaks the mage\'s name, etc.).'
spell.db.reference = 'M:tA p. 135'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Pariah')
spell.db.longname = 'Pariah'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 5'
spell.db.info = 'One of the most terrifying curses in the arsenal of a Master of Fate, this spell turns the world against the victim.'
spell.db.reference = 'M:tA p. 139-140'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Quantum_Flux')
spell.db.longname = 'Quantum Flux'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage reads probability and compensates for deleterious factors, attracting small turns of good fortune to negate unfortunate obstacles that stand in her way. This negates penalties to any of the subject\'s actions equal to Potency for a number of actions during the Duration equal to Potency.'
spell.db.reference = 'M:tA p. 135'
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

spell = create_script('typeclasses.scripts.spellScript',key = 'Reading_the_Outmost_Eddies')
spell.db.longname = 'Reading the Outmost Eddies'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 1'
spell.db.info = 'This spell bestows a small blessing or curse that attracts good or bad fortune to its subject. As long as the spell remains active the subject experiences an event within the next 24 hours, such as finding $20 or dropping his wallet in a puddle. The mage can exert limited control over the nature of the fortune (or misfortune), but ultimately fate decides the detail'
spell.db.reference = 'M:tA p. 135'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Receiver')
spell.db.longname = 'Receiver'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Casting this spell allows the mage to hear infrasound and ultrasound frequencies beyond what human ears can normally perceive. While active, she can hear sounds outside the normal frequency, from high-frequency (dog whistles, sonar) to low-frequency (the distant rumble of diesel engines, industrial sounds normally lost to humans in the noise). Apply the spell\'s Potency as a dice bonus to relevant dice pools, such as rolls to avoid ambush.'
spell.db.reference = 'M:tA p. 141'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Rend_Friction')
spell.db.longname = 'Rend Friction'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage alters the level of friction upon a target. She can increase it to the point where simple air friction shears the target to pieces, or lower it so much that an object can continue moving almost indefinitely.'
spell.db.reference = 'M:tA p. 145-146'
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

spell = create_script('typeclasses.scripts.spellScript',key = 'Serendipity')
spell.db.longname = 'Serendipity'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 1'
spell.db.info = 'This spell grants the mage a momentary glimpse of all the potential roads her destiny may follow to her desired destination, which allows the mage to identify the next step she must take to accomplish a stated objective. Upon casting, the mage receives a clear omen that suggests a course of action that will lead her closer to her goal. This seldom guarantees immediate success, especially if the task before her is complicated, but can provide an important breakthrough.'
spell.db.reference = 'M:tA p. 135'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Sever_Oaths')
spell.db.longname = 'Sever Oaths'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 4'
spell.db.info = 'To an Adept of Fate, all fetters on a being\'s free will are ultimately breakable, and oaths can be renegotiated. The mage may apply a number of the following effects equal to Potency'
spell.db.reference = 'M:tA p. 138-139'
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

spell = create_script('typeclasses.scripts.spellScript',key = 'Shared_Fate')
spell.db.longname = 'Shared Fate'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 3'
spell.db.info = 'Fate is an instrument of both justice and punishment. This spell braids the fates of two subjects together. Whatever befalls one subject affects the other.'
spell.db.reference = 'M:tA p. 137'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Shifting_the_Odds')
spell.db.longname = 'Shifting the Odds'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 2'
spell.db.info = 'An Apprentice of Fate always has access to what she needs at the moment. The mage focuses on locating a particular kind of person, place, or thing, and this spell directs her steps to it unerringly as soon as possible within the next 24 hours as long as the spell remains active. Casting the spell looking for a kind of person in a crowd or an item anywhere it could appear is usually enough to immediately succeed.'
spell.db.reference = 'M:tA p. 136'
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

spell = create_script('typeclasses.scripts.spellScript',key = 'Strings_of_Fate')
spell.db.longname = 'Strings of Fate'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The roads of destiny fork and converge, governing the probability of events. An adept of Fate can re-weave the strings of Fate on a subject, encouraging (if not ensuring) that a specified event will happen as long as the spell remains active.'
spell.db.reference = 'M:tA p. 138'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Superlative_Luck')
spell.db.longname = 'Superlative Luck'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage can ensure success at virtually any task he sets out to accomplish.'
spell.db.reference = 'M:tA p. 137'
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

spell = create_script('typeclasses.scripts.spellScript',key = 'Swarm_of_Locusts')
spell.db.longname = 'Swarm of Locusts'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage creates chaotic conditions: rains of frogs, swarms of locusts, unscheduled total solar eclipses, and other similarly "Fortean" occurrences. This terrifying and obviously supernatural event wreaks havoc in the area, creating Environmental Tilts of the player\'s choosing.'
spell.db.reference = 'M:tA p. 140'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Sworn_Oaths')
spell.db.longname = 'Sworn Oaths'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage can witness a sworn oath and ensure that Fate itself enforces the subject\'s adherence to her vow. The subject makes a promise and states the consequences for herself if she violates the agreement. No one can be forced to take such an oath, although a subject may be placed under oath unwittingly if he voluntarily makes a vow and verbally agrees to a specified consequence, even if he doesn\'t realize the mage can enforce the oath supernaturally.'
spell.db.reference = 'M:tA p. 137'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Telekinesis')
spell.db.longname = 'Telekinesis'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage can conjure telekinetic force to lift or manipulate an object remotely. Apply the spell\'s Potency to one of the force\'s Strength (raw lifting/pushing power), Dexterity (fine manipulation), or Speed. The other two default to 1. Moving objects using Telekinesis requires concentration as an instant action each turn; if the mage fails to concentrate on moving the force, it simply hangs suspended, holding any objects it held before but no longer pushing or pulling (or manipulating objects, if used for that). The mage may then resume directing the telekinetic force until the spell\'s Duration expires.'
spell.db.reference = 'M:tA p. 144'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Telekinetic_Strike')
spell.db.longname = 'Telekinetic Strike'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage manipulates kinetic forces to crush subjects or form a "ball" of highly pressurized air and kinetic energy that she can hurl at foes. The spell inflicts bashing damage equal to its Potency.'
spell.db.reference = 'M:tA p. 145'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Thunderbolt')
spell.db.longname = 'Thunderbolt'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage channels ambient energies as a weapon, pouring them into her subject. This spell deals lethal damage equal to its Potency.'
spell.db.reference = 'M:tA p. 146'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Touch_of_the_Grave')
spell.db.longname = 'Touch of the Grave'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can physically interact with ghosts and other things in Death-attuned Twilight. She can "pull" items from Twilight, making them visible and solid; these items have a Durability of 1 and dissipate into ephemera if broken, or after the spell\'s Duration ends. Items pulled from Twilight function as their material counterparts bestowing the same equipment bonuses.'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Transform_Energy')
spell.db.longname = 'Transform Energy'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 4'
spell.db.info = 'All energy shares sympathy, born perhaps from the same cosmic source in the same instant. An Adept of Forces can use that sympathy to transform one energy type into another. The table below serves as a rough equivalency chart for different energy types. She can change a room full of light into heat, at once turning it into a pitch-black oven. She might also change the thunderous roar of a waterfall into electricity, far more efficient than any hydroelectric dam. The spell may affect energy of a level equal to Potency.'
spell.db.reference = 'M:tA p. 146'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Transmission')
spell.db.longname = 'Transmission'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can hijack existing signals and change the transmitted data or its destination. She can shorten or lengthen the transmission, and even change frequency, such as turning a wifi broadcast into a television signal. At this level, she must still work with a signal already present. Mimicking specific sounds or information requires a Skill roll or access to the data to be transmitted.'
spell.db.reference = 'M:tA p. 144'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Tune_In')
spell.db.longname = 'Tune In'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 1'
spell.db.info = 'A mage with this spell can listen to free-floating data transmissions, such as those broadcast by radios, cell phones, wireless modems, and more. The magic translates this electromagnetic noise into something she can understand, although it preserves the original transmission language. With this spell, the mage needs no receiver to listen or even see signals. Transmitting cables glow before her eyes with streams of data, while she might see a shimmer or even fleeting glimpses of images in the air. Satellite internet and TV programming, closed walkie-talkies, CB broadcasts, and radio transmissions all become open to her senses, as well as wireless communications.'
spell.db.reference = 'M:tA p. 141'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Turn_Momentum')
spell.db.longname = 'Turn Momentum'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 3'
spell.db.info = 'This spell allows the mage to redirect a target\'s momentum. Usually this forms a shield against projectiles, but it can be used on larger objects, as well. When a mage could use her Defense against an object, she may use this spell instead to redirect it as an instant action. If cast with a prolonged Duration, the mage may take a Dodge action each turn and use this spell instead of receiving the normal benefits for Dodging.'
spell.db.reference = 'M:tA p. 145'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Velocity_Control')
spell.db.longname = 'Velocity Control'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage can greatly increase or decrease an object\'s velocity. Its speed doubles or halves for each level of the spell\'s Potency. For example, a car traveling 50 MPH is increased to 200 MPH with Potency 2, or an incredible 800 MPH with Potency 4. Likewise, if the mage reduces its speed, the same car would slow to about 13 MPH at Potency 2, or about 4 MPH with Potency 4. The mage must be able to affect the target\'s entire Size to affect it with this spell; she cannot target only the front tire of an 18-wheeler with its trailer (Size 30) and bring it to a stop.'
spell.db.reference = 'M:tA p. 145'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.spellScript',key = 'Warding_Gesture')
spell.db.longname = 'Warding Gesture'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage creates a ward protecting the subject against supernatural effects that manipulate her fate - a geas, a supernatural compulsion to act against her will, or having her fate manipulated by Fate magic or similar supernatural effects. Each attempt to change the subject\'s destiny provokes a Clash of Wills with the mage. This spell has no effect on pre-existing alterations to the subject\'s destiny.'
spell.db.reference = 'M:tA p. 136-137'
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

spell = create_script('typeclasses.scripts.spellScript',key = 'Zoom_In')
spell.db.longname = 'Zoom In'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage focuses light entering her subject\'s senses, greatly magnifying vision. Without an Unveiling spell like "Nightvision" (p.141), the spell can only affect visible wavelengths. For example, a mage using this spell on herself could look closely at a bird circling high above, or zoom in to great detail to examine a layer of dust on an object, but she couldn\'t see things that would only appear under a blacklight.'
spell.db.reference = 'M:tA p. 144'
spell.db.restricted = False

pass