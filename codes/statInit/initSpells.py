from evennia import create_script

spell = create_script('typeclasses.scripts.SpellScript',key = 'Accelerate_Growth')
spell.db.longname = 'Accelerate Growth'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 4'
spell.db.info = 'With this spell a mage can greatly accelerate the growth of a living being. The subject\'s growth rate doubles for each level of Potency. At Potency 5, the subject grows 32 times faster than normal - a human infant would reach adulthood in a little over half a year, if the spell\'s Duration lasts long enough. When the spell expires, the subject returns to its actual age. The targets gain no life experience beyond that which they undergo during the spell\'s Duration, so a human child made into an adult by means of this spell will likely behave as a child unless other magic helps him learn quickly, and the mage or someone else sees fit to teach him. If the subject exceeds its natural lifespan, it dies of old age.'
spell.db.reference = 'M:tA p. 151'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Acceleration')
spell.db.longname = 'Acceleration'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage can greatly accelerate her subject\'s temporal motion. From the perspective of onlookers she becomes a blur as if moving in fast motion, acting with impossible speed. At high enough levels, mundane creatures simply cannot perceive her at all, save perhaps for hair raising on the neck or a gut feeling that something is not quite right.'
spell.db.reference = 'M:tA p. 188'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Adverse_Weather')
spell.db.longname = 'Adverse Weather'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage summons a major weather system as severe as a tornado, tsunami, monsoon, or hurricane. The weather effects take hold in minutes and dissipate immediately once the spell expires. This allows the mage to create Extreme Environments of nearly any kind up to Level 4, as per Control Weather (see above) but without the limitations. She does not have to call up disasters; she can make a rainstorm appear in a cloudless blue sky if she desires.'
spell.db.reference = 'M:tA p. 146'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Aegis')
spell.db.longname = 'Aegis'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 3'
spell.db.info = 'By adjusting the properties of matter, the mage may make silk shirts bullet-proof, or tear through bulky riot suits with her bare hands. The spell is cast upon a wearable object (giving living beings Armor is a function of Life). For each level of Potency, the player chooses one of the following effects:'
spell.db.reference = 'M:tA p. 156'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Aetheric_Winds')
spell.db.longname = 'Aetheric Winds'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage calls forth a bare fraction of the howling fury of the Aether, scouring her subject with shrieking winds. This is an attack spell, inflicting bashing damage equal to Potency.'
spell.db.reference = 'M:tA p. 168'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Alchemists_Touch')
spell.db.longname = 'Alchemist\'s Touch'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 2'
spell.db.info = 'Draped in the leaden shrouds of Stygia, the subject may handle even the most dangerous of substances without fear. When the spell is cast, the mage chooses a particular form of matter: The subject is largely immune to its deleterious effects. The material cannot inflict bashing damage on her at all, and she reduces the damage from lethal sources of harm by the spell\'s Potency. The spell has no effect on aggravated damage.'
spell.db.reference = 'M:tA p. 155'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Alter_Conductivity')
spell.db.longname = 'Alter Conductivity'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 3'
spell.db.info = 'With this spell, the mage alters a subject\'s base properties, changing the manner in which it conducts electricity. This spell can automatically shut down any electrical device whose power isn\'t great enough to inflict damage, or it can increase or decrease the amount of electricity that can flow through the object. For each level of Potency, the spell allows the object to conduct two points worth of electrical damage, or reduces electrical damage by two. The object must still be in contact with an appropriate source of electricity to deal this damage; even a Potency 6 spell won\'t let the power from a household wall outlet inflict more than four points of bashing damage (see Electricity on p. 224). Reducing electrical damage to zero also shuts electrical devices down - for example, completely snuffing a subway rail\'s conductivity shuts the trains down.'
spell.db.reference = 'M:tA p. 156'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Alter_Direction')
spell.db.longname = 'Alter Direction'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 4'
spell.db.info = '"Direction" is nothing more than a vector between two points. With this spell, the mage overwrites that concept, letting her define her path as anything she desires.'
spell.db.reference = 'M:tA p. 177'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Alter_Integrity')
spell.db.longname = 'Alter Integrity'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 3'
spell.db.info = 'By rotating an object\'s resonance into or out of alignment with Stygian truths, the mage can strengthen or weaken its material. Every level of Potency either increases or decreases the object\'s Durability by 1. This does not increase the object\'s Structure, but see below.'
spell.db.reference = 'M:tA p. 156-157'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Alter_Mental_Pattern')
spell.db.longname = 'Alter Mental Pattern'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can alter the subject\'s basic mental flow, changing her subconscious thoughts and surface emanations to reflect any mental or emotional state the mage wishes. The spell does not actually alter the subject\'s state of mind, but instead alters how she projects herself, shielding her from supernatural powers that would read her thoughts, or attempt to pierce her normal veil of lies and misdirection. Add the spell\'s Potency to relevant Subterfuge rolls.Supernatural powers that read the surface thoughts or emotions of the subject provoke a Clash of Wills.'
spell.db.reference = 'M:tA p. 160'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Amorality')
spell.db.longname = 'Amorality'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage severs her subject\'s ties to his guiding impulses, either completely removing his Virtue or his Vice. While without a Virtue, the subject is more prone to indulging his Vice and gains two points of Willpower whenever he would normally gain one. While without a Vice, the character acts in a manner completely consistent with his Virtue, and is incapable of actively engaging in activities that would constitute a breaking point or Act of Hubris. Witnessing heinous or horrifying deeds still causes breaking points for Sleeper characters.'
spell.db.reference = 'M:tA p. 164'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Analyze_Life')
spell.db.longname = 'Analyze Life'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 1'
spell.db.info = 'By observing a creature and casting this spell, the mage can discern details such as the species, age, sex, and overall health of a plant or animal, including humans. She may identify how many dots in Physical Attributes the subject has. Any illnesses or injuries, including Personal Tilts and Conditions, suffered by the creature become obvious to her sight. This spell identifies supernatural (but still living) creatures as unknown species, even if they take a human form, unless the mage has studied their kind before. Undead beings do not register to this spell.'
spell.db.reference = 'M:tA p. 148'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Animal_Minion')
spell.db.longname = 'Animal Minion'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 4'
spell.db.info = 'Rather than triggering instincts and directing an animal along a course it might normally take, an Adept can take full bodily control. She does so with raw domination, a puppetmaster commanding a marionette. While she can\'t force the creature to do something outside its physical capabilities, she can make it do anything of which its body is capable. This isn\'t full mind control and she doesn\'t have access to the creature\'s thoughts. The mage can force an human subject to talk, but can\'t prompt it to divulge specific information, or even anything intelligible (unless the mage herself demands that it speak certain words). Subjects often move differently from their usual gait in ways noticeable to those familiar with them.'
spell.db.reference = 'M:tA p. 151-152'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Annihilate_Matter')
spell.db.longname = 'Annihilate Matter'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage can destroy inert matter, reducing it to nothingness and utterly dissolving its atomic lattice. In effect, he makes it cease to be. Whereas objects destroyed by Nigredo and Albedo (see p. 157) shatter or crumble as appropriate, matter destroyed by this spell is annihilated; nothing remains of it.'
spell.db.reference = 'M:tA p. 158'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Annihilate_Spirit')
spell.db.longname = 'Annihilate Spirit'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The most fearsome spell in most shamans\' arsenal, this terrible magic utterly destroys a spirit. The target spirit may spend an Essence to roll Power + Finesse in a Clash of Wills, a last-ditch attempt to reassert its existence through its Influences. If the spell is successfully cast, the spirit is instantly and utterly destroyed - even if it still has Essence, it does not retreat into hibernation, it is simply gone. Short of archmastery, this spell cannot affect spirits of Rank 6 or higher.'
spell.db.reference = 'M:tA p. 184'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Apocalypse')
spell.db.longname = 'Apocalypse'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The subject of this spell has the scales of the Lie removed from his eyes. Anyone subject to this spell - mage, Sleeper, or other supernatural being - gains Mage Sight attuned to the Path of the caster. Along with this gift comes temporary immunity to the Quiescence curse. It does not, however, prepare the target for how to interpret the visions received under Mage Sight, and the uninitiated are likely to face breaking points due to the trauma of the Sight. While Awakened subjects may control the new Sight as though it were their own, focusing it and pushing it back to the Periphery like their own, other subjects gain Active Mage Sight and cannot shut the Sight off - it lasts until the spell\'s Duration expires, but still applies dice pool penalties and Willpower costs as per Mage Sight (see p. 90). If the subject runs out of Willpower points and the spell is still active, he gains the Blind Condition as the Supernal vision burns out his eyes. (At the Storyteller\'s discretion, this might be replaced with Deafened or a similar Condition if the subject experiences Mage Sight with other senses).'
spell.db.reference = 'M:tA p. 169-170'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'As_Above,_So_Below')
spell.db.longname = 'As Above, So Below'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 2'
spell.db.info = 'A mage\'s tools are sacred, her every word and deed a reflection of the Realms Above. By means of this spell, the mage imbues the tools of her Art with holy meaning, allowing her to draw down power with greater facility. For every level of Potency, she chooses a single Yantra (and it must be a specific example of a Yantra, not just a category: "the Crypt of the Mariner," not just "Environment"). Any spell cast that incorporates that Yantra gains the 9-Again effect on the spellcasting roll.'
spell.db.reference = 'M:tA p. 166-167'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Atonement')
spell.db.longname = 'Atonement'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 4'
spell.db.info = 'A powerful Witch can aid a hero who labors under a curse, but her remedies often demand strange rituals or arduous quests. This spell can dispel a supernatural effect enforced by the dictates of destiny, including Awakened spells, by Patterning Fate to provide a means by which the subject can escape his curse. While the subject remains under the effects of Atonement, she must complete a task determined by the caster.'
spell.db.reference = 'M:tA p. 137-138'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Augment_Mind')
spell.db.longname = 'Augment Mind'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage is capable of increasing the subject\'s mental or social capacity. The mage can increase one of either the subject\'s Mental or Social Attributes by one dot per level of Potency of the spell. This increase affects any Advantages or other traits derived from the Attribute\'s level. The spell cannot increase the subject\'s Attribute above her normal maximum allowed by her Gnosis. The benefits of this spell are not obvious to a casual observer, but those who know the subject may notice an increase in her intellect or charismatic nature.'
spell.db.reference = 'M:tA p. 161'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Ban')
spell.db.longname = 'Ban'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 3'
spell.db.info = 'In the quest for self-knowledge, it is sometimes useful to cut oneself off from the outer world so that one can understand that the world is contained within. By means of this spell, the mage inverts an area of space, such that nothing inside the space can get out and nothing outside the space can get in. Try to step in and you find yourself on the far side, carried in a single step. Try to get out and you\'re just stepping right back in again. Magic that manipulates space, like a teleportation power or the ability to step from one world to another, provokes a Clash of Wills to allow ingress or egress.'
spell.db.reference = 'M:tA p. 176'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Banishment')
spell.db.longname = 'Banishment'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 4'
spell.db.info = 'This spell strips a spirit of its ability to act in the world, reminding it of its place. This spell strips a number of Manifestation Conditions from the spirit (or its host) equal to the spell\'s Potency. The effect is Lasting, but the spirit may use its Influences and Manifestations to reestablish the Conditions as normal. This spell does not work on spirits above Rank 5.'
spell.db.reference = 'M:tA p. 182'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Befuddle')
spell.db.longname = 'Befuddle'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage lowers one of her subject\'s Mental or Social Attributes. Each level of Potency reduces one of the subject\'s Social or Mental Attributes by one dot, to a minimum of 1. Lowering Attributes also reduces any derived Advantages, such as Willpower or Initiative.'
spell.db.reference = 'M:tA p. 161'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Bind_Spirit')
spell.db.longname = 'Bind Spirit'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 4'
spell.db.info = 'What shows mastery more than a leash? With this spell, the mage may bind a spirit to the world, granting it a Manifestation Condition (see p. 258). The mage may grant a number of Conditions equal to the spell\'s Potency, and must create any prerequisite Conditions as well, if they aren\'t already present. The entity immediately enters the Manifestation of the mage\'s choice, and may not leave it while the spell remains in effect. This spell does not work on spirits above Rank 5.'
spell.db.reference = 'M:tA p. 183'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Birth_Spirit')
spell.db.longname = 'Birth Spirit'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 5'
spell.db.info = 'By means of this spell, the mage may coax dormant Essence into life, awakening it as a Rank 1 Spirit. This spirit is not under the mage\'s particular control, but most newborn spirits feel a kind of respect or gratitude toward their maker. Many mages then use Bolster Spirit and Shape Spirit to improve their ephemeral creation\'s capabilities.'
spell.db.reference = 'M:tA p. 184'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Blasphemy')
spell.db.longname = 'Blasphemy'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 5'
spell.db.info = 'By defining all truths, the Supernal includes the means of its own erasure. This spell severs the world\'s connection with the Supernal, creating a "dead zone" in which the energies'
spell.db.reference = 'M:tA p. 170'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Blink_of_an_Eye')
spell.db.longname = 'Blink of an Eye'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 5'
spell.db.info = 'By collapsing time around a subject, the mage allows her to accomplish in seconds what would take hours. This spell turns the next extended action taken by the subject into an instant action, absorbing rolls equal to Potency into a single turn. It does not affect ritual casting intervals for mages.'
spell.db.reference = 'M:tA p. 191'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Body_Control')
spell.db.longname = 'Body Control'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 2'
spell.db.info = 'With this spell a mage can control her subject\'s bodily functions to a degree that would make even the most inwardly-focused monks envious. She can do far more than slow heart rate; she can control her subject\'s metabolism, heighten reflexes, and consume less oxygen. For the spell\'s Duration, each level of Potency gives one rank in each of the following:'
spell.db.reference = 'M:tA p. 148-149'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Bolster_Spirit')
spell.db.longname = 'Bolster Spirit'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mouse who plucks the thorn is often more respected than the roaring lion. Each level of Potency of this spell heals a spirit of two boxes of bashing damage.'
spell.db.reference = 'M:tA p. 181'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Borrow_Threads')
spell.db.longname = 'Borrow Threads'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 2'
spell.db.info = 'By changing one\'s connection to others, one changes oneself. This spell allows the mage to transfer a number of sympathetic connections equal to the spell\'s Potency between herself and the subjects as determined by the spell\'s Scale. She can either steal links from her targets or give her own to others. If the mage transfers a link to someone who already has a connection to the same thing, the new connection overwrites the old one for the Duration of the spell. The mage has to be aware of a connection (either through magic or just knowing the subject) to manipulate it.'
spell.db.reference = 'M:tA p. 174'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Break_Boundary')
spell.db.longname = 'Break Boundary'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 2'
spell.db.info = 'To restrain a willworker is to try to ensnare someone in a lie he does not believe. This spell allows the mage to bypass a single obstacle restricting her subject\'s movement: a locked door, a pair of handcuffs, a barred window, etc. The subject "blinks" through the door, or her hands seem to pass right through the handcuffs, or similar effects.'
spell.db.reference = 'M:tA p. 174'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Bruise_Flesh')
spell.db.longname = 'Bruise Flesh'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 3'
spell.db.info = 'A mage can use Life magic to simply bruise and batter a living creature. This is an attack spell, inflicting bashing damage equal to the spell\'s Potency.'
spell.db.reference = 'M:tA p. 150'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Call_Lightning')
spell.db.longname = 'Call Lightning'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 3'
spell.db.info = 'With a gesture the mage can conjure lightning down from a stormy sky to strike her foes. She must use this spell with an existing storm or one she sets into motion with "Control Weather" (see p. 143), since she cannot create lightning from nothing at this level.'
spell.db.reference = 'M:tA p. 144'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Cap_the_Well')
spell.db.longname = 'Cap the Well'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 2'
spell.db.info = 'Any creature becomes more pliable when its food source is controlled. This spell wards a source of Essence, making it difficult for spirits to feed from it - but not harder to sense. Any attempt by a spirit to feed on the Essence (or a mage, werewolf, or other being to siphon the Essence) provokes a Clash of Wills.'
spell.db.reference = 'M:tA p. 180'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Celestial_Fire')
spell.db.longname = 'Celestial Fire'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage summons the Supernal fires of the Aether to smite her enemies. This is not base, Fallen flame, but rather the pure expression of Awakened will. This is an attack spell; its damage rating is equal to the spell\'s Potency, and it inflicts lethal damage. The spell affects Twilight entities.'
spell.db.reference = 'M:tA p. 170'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Channel_Essence')
spell.db.longname = 'Channel Essence'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 2'
spell.db.info = 'A wise master knows that sometimes she must reward rather than punish. This spell allows the mage to draw Essence into her Pattern from a Resonant Condition or channel Essence to a spirit or suitable receptacle. The mage may transfer an amount of Essence equal to the spell\'s Potency. However, she cannot channel more Essence per turn than her Gnosis-derived Mana per turn rate.'
spell.db.reference = 'M:tA p. 180-181'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Channel_Mana')
spell.db.longname = 'Channel Mana'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The flows of Supernal energy are the mage\'s to manipulate. This spell allows the mage to move a quantity of Mana equal to the spell\'s Potency between one or more vessels she can touch, including other mages, herself, Hallows, Artifacts, and others. She must, however, respect her Gnosis-derived Mana per turn limit.'
spell.db.reference = 'M:tA p. 168'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Chaos_Mastery')
spell.db.longname = 'Chaos Mastery'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage can Pattern Fate to manipulate complex probabilities within the spell\'s subject or area of effect. This spell allows the mage to dictate any physically possible outcome within the bounds of the spell\'s subject, no matter how unlikely.'
spell.db.reference = 'M:tA p. 138'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Choose_the_Thread')
spell.db.longname = 'Choose the Thread'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 2'
spell.db.info = 'Glimpsing the many potential futures of her subject, the mage selects the optimal course. The subject\'s player rolls twice for her next mundane dice roll, and the mage\'s player selects which dice roll takes effect.'
spell.db.reference = 'M:tA p. 187'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Chronos_Curse')
spell.db.longname = 'Chronos\' Curse'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage slows his subject\'s experience of time to a crawl. To the subject, everything seems to move at dazzling speeds, while she feels like she\'s caught in a dream, unable to run or punch or move properly. She can\'t even speak normally to others while affected - while from her perspective her words are clear enough, to everyone else they\'re a long, impossibly drawn-out sound.'
spell.db.reference = 'M:tA p. 189'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Cleanse_Pattern')
spell.db.longname = 'Cleanse Pattern'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The Forms making up a subject\'s Supernal Pattern are marked by the touch of magic. With this spell, a mage removes the tell-tale signs of Awakened interference. The spell removes the dramatic failure effect of a Focused Mage Sight Revelation (p. 92) from a subject. If the spell\'s subject bears a mage\'s Signature Nimbus, the spell removes it.'
spell.db.reference = 'M:tA p. 168'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Cleanse_the_Body')
spell.db.longname = 'Cleanse the Body'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can use this spell to help the subject\'s body fight the effects of any toxin in her system, or even purge them completely. Its magic allows her a bonus equal to Potency to her next roll to resist the toxin\'s effects.'
spell.db.reference = 'M:tA p. 148'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Clear_Thoughts')
spell.db.longname = 'Clear Thoughts'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage smoothes troubled thoughts and deadens emotions, making the subject think clearly. The spell suppresses one Mental Condition or Tilt per level of Potency for its Duration. While the spell is often used to treat mental illness, it may also be used against positive Conditions, suppressing elation and inspiration just as easily as despair and fugue. The spell may not affect Conditions created by Paradox, and those imposed by supernatural means provoke a Clash of Wills.'
spell.db.reference = 'M:tA p. 161-162'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Cloak_Nimbus')
spell.db.longname = 'Cloak Nimbus'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 2'
spell.db.info = 'This spell cloaks the subject\'s Nimbus from spells and effects that would read it, such as Supernal Vision or the ability of certain psychics to read emotional states in auras. Any such effect is subject to a Clash of Wills (see p. 117). Any effect that fails to pierce the veil registers the subject as an ordinary Sleeper. Spells cast while under the influence of this spell do not cause the caster\'s Immediate Nimbus (see p. 89) to flare unless she chooses to.'
spell.db.reference = 'M:tA p. 167'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Co-Location')
spell.db.longname = 'Co-Location'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 3'
spell.db.info = 'Where lesser spells merely distort the Lie that all things are separate, this spell attacks it directly. The mage smears the distance between a number of locations equal to the spell\'s Potency, causing them to overlap temporarily. The mage must employ the Sympathetic Range Attainment to overlap locations outside of her sensory range.'
spell.db.reference = 'M:tA p. 176'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Coaxing_the_Spirits')
spell.db.longname = 'Coaxing the Spirits'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Though most spirits are but slumbering motes that have no will or sapience, the mage may coax them to brief activity in accordance with their natures. She may compel the spirit (or its physical representation) to take a single instant action in accordance with its nature. A frightened animal might attack or flee, a car might start up, or a cliff face might start a small avalanche. The spell is Withstood by the Rank of the spirit coaxed or the Composure of a living representation, whichever is higher.'
spell.db.reference = 'M:tA p. 180'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Cold_Snap')
spell.db.longname = 'Cold Snap'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage dissipates the heat in the spell\'s area of effect, causing frost and ice to form on the floor and exposed surfaces. For the Duration of the spell, all surfaces in the area are under the effects of the Ice Tilt (p. 321).'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Collapse')
spell.db.longname = 'Collapse'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 4'
spell.db.info = 'While lesser magic can blur the distinction between locations, this spell can destroy them outright. The mage forces her subject to momentarily occupy the same space as another object, with catastrophic effects. This is an attack spell; its damage rating is equal to the spell\'s Potency, and it inflicts lethal damage. Collapsing multiple subjects into each other, thereby damaging them all, is an application of increased Subject Factor.'
spell.db.reference = 'M:tA p. 177'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Command_Spirit')
spell.db.longname = 'Command Spirit'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 2'
spell.db.info = 'Sometimes the gentle approach must give way to raw dominance. This spell allows the mage to command a spirit to undertake a number of actions equal to the spell\'s Potency. This compulsion only lasts as long as the spell\'s Duration, so the spirit might abandon an indefinite or extended action when the spell\'s Duration wears off. Commands that go against the spirit\'s self-interest (including abandoning a host or Fetter) provoke a Clash of Wills. This spell has no effect on spirits above Rank 5.'
spell.db.reference = 'M:tA p. 181'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Constant_Presence')
spell.db.longname = 'Constant Presence'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 2'
spell.db.info = 'Mages versed in Time know the tell-tale signs of disruption to the Patterns of time travelers, and not many Awakened are willing to trust that a traveler has honorable intentions. This spell preserves its subject against alterations to the timeline. Any alteration to history through the action of time travel provokes a Clash of Wills. If the mage wins, the subject is treated as though she were returning from a trip to the past herself when history settles, safeguarding her against being rewritten.'
spell.db.reference = 'M:tA p. 187'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Contagion')
spell.db.longname = 'Contagion'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 5'
spell.db.info = 'Life Masters can unleash horrific plagues on their foes. The mage can create minor sicknesses or life-threatening diseases. The Severity of the disease is equal to Potency. If the mage has something in which she can store the disease, she can create it within that equipment, or else she must target some form of carrier, depending on the disease\'s transmission methods (water, food, living hosts). It\'s contagious as soon as the mage creates it, requiring a reflexive Stamina + Resolve roll, modified by the Severity, to resist contracting it. Failure means the victim contracts the disease and suffers its normal effects.'
spell.db.reference = 'M:tA p. 153'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Control_Electricity')
spell.db.longname = 'Control Electricity'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage may alter the flow of electricity as well as diminish its current. She cannot increase the current without some device capable of generating it, since she cannot create electricity from nothing. For example, the mage can direct the electricity in a building to single or multiple outlets, cut the power, or divide power going to one outlet to many other sources. This requires a method of conduction, like existing wiring or metal. She can also cause existing electrical currents to arc (such as striking a target near a wall outlet), or redirect it away from a particular device. Causing a short or using the electrical current to attack a target usually burns out the breakers or shorts out a device afterward, unless it\'s made to withstand the stresses of power fluctuations. Damage caused by this spell uses the electrical damage rules on p. 224. By directing the flow away from a subject, she subtracts the spell\'s Potency from the damage of an electrical source.'
spell.db.reference = 'M:tA p. 142'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Control_Fire')
spell.db.longname = 'Control Fire'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can exert control over a fire, fueling it to increase its size and intensity or depriving it of fuel to snuff it out. She can only control existing flames at this level, but can change a small campfire into a roaring inferno or bring even an out-of-control fire down to manageable levels.'
spell.db.reference = 'M:tA p. 142'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Control_Gravity')
spell.db.longname = 'Control Gravity'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can redirect the force of gravity in an area. She can alter the direction of its pull, causing affected objects to "fall" upwards or horizontally. She can\'t do more than change its direction at this level, but she can make it nearly impossible to approach a specific object or area without some means of overcoming gravity, like flight or climbing gear.'
spell.db.reference = 'M:tA p. 142'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Control_Heat')
spell.db.longname = 'Control Heat'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can now increase or decrease the temperature of an area. Each level of Potency allows a change of 1 level of Extreme Environment to produce heat or cold, counting a temperate room temperature as "zero." For example, with Potency 3, a mage could transform a Level 1 Extreme Environment based on cold into a Level 2 Environment based on heat.'
spell.db.reference = 'M:tA p. 142'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Control_Instincts')
spell.db.longname = 'Control Instincts'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 2'
spell.db.info = 'For all their intellectual powers, humans are animals, too, and animals are governed by instincts. An Apprentice of Life can control these instinctual responses like a puppeteer pulling strings. In so doing she can make any animal or plant behave in any fashion natural to its type. She need not do so in the presence of circumstances that would provoke such behavior normally. A raging bear can be made to flee by manipulating its fight-or-flight response, a fish to leap, a rat to feast on something, or a snake made to secrete venom from its fangs, even in the absence of prey. A human may be made tired, hungry, or pumped with adrenaline. This spell works on any mundane life-form the mage can perceive. Humans with Supernatural Merits count as "mundane" enough for this spell to affect them.'
spell.db.reference = 'M:tA p. 149'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Control_Light')
spell.db.longname = 'Control Light'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can dim or intensify existing light the spell\'s area of effect, whether from an artificial or natural source. This can cause a 40-watt bulb to shine as brightly as a floodlight or make the sunlight on an overcast day like that of a clear summer morning. The magic modifies the light emitted by the source, and not the source or the emission itself, so this won\'t cause a bulb to burn itself out or increase the heat of sunlight without other spells. Each level of Potency in the spell doubles or halves the light\'s candescence.'
spell.db.reference = 'M:tA p. 142'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Control_Sound')
spell.db.longname = 'Control Sound'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'This spell allows a mage to amplify or weaken the volume of sound in the spell\'s area of effect. She can make a loudspeaker into a thunderous blast or a barely audible squeak. Each level of Potency doubles or halves the volume of sound in the targeted area, creating a zone of altered sound. For example, casting this spell on a podium at the front of the room affects the sounds of anyone standing at the podium. The mage can also influence the direction of existing sounds. She can focus sound waves from across the room to hear a whispered conversation, ensure her own voice does not reach anyone but her intended target, or cause noises to emanate from nearby locations instead of their original sources. The Scale factor determines the area she can affect.'
spell.db.reference = 'M:tA p. 142-143'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Control_Weather')
spell.db.longname = 'Control Weather'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can control existing weather patterns. She can force a light shower to become a thunderstorm, summon up fog on a clear morning, make a warm day into an unbearably hot one or conjure a cooling breeze. Drastic changes from existing weather require Reach, as noted below. The weather begins to change immediately upon casting the spell, with new systems taking shape within minutes. This spell allows the mage to change or create weather-based Extreme Environments up to Level 4, as well as cause a wide variety of environmental Tilts. Potency determines the maximum amount by which an Extreme Environment can change, up to a maximum of Level 4 (and a minimum of level 0). Listed below is an example set of Tilts possible for weather patterns, but it is by no means exhaustive. Note that without further spells, the mage is not immune to weather ilts she creates.'
spell.db.reference = 'M:tA p. 143'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Corpse_Mask')
spell.db.longname = 'Corpse Mask'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage alters the appearance of a body to make it look different even under scrutiny. She can cast the spell on a corpse, modifying its wounds and apparent time and cause of death completely. She can make a charred corpse look as though it instead died of a heart attack, or a person who died in a car crash look as though he is the victim of a stab wound.'
spell.db.reference = 'M:tA p. 129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Correspondence')
spell.db.longname = 'Correspondence'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 1'
spell.db.info = 'We are all of us defined by our connections, and through this spell a mage learns those definitions. For every level of Potency, the mage learns one of the subject\'s sympathetic links. The spell reveals the subject\'s oldest and strongest links first. She understands these connections in the same manner the subject thinks of them (e.g. "my childhood home," not "1414 Willowbrook Drive, Columbus, OH"). If the other half of the sympathetic link is within the mage\'s sensory range, she knows that and knows its exact location.'
spell.db.reference = 'M:tA p. 172-173'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Corridors_of_Time')
spell.db.longname = 'Corridors of Time'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 5'
spell.db.info = 'Where less-advanced Time mages can only undo actions leading directly up to the present, a Master may choose any moment in her subject\'s timeline and destroy everything after it, sending the subject\'s present self back in time to the moment of the mage\'s choosing. The subject arrives in the past at the specified time, inhabiting his own past body and is free to act, changing history by his actions, although the distortions to his timeline are visible under Active Time Mage Sight. He remains in the past for a time equal to Corridors of Time\'s Duration factor, or until he "catches up" to the present. Once in the present, the new timeline sets and any changes the subject made to history become Lasting.'
spell.db.reference = 'M:tA p. 191'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Craft_Fetish')
spell.db.longname = 'Craft Fetish'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 4'
spell.db.info = 'A vanquished foe can be a useful tool. This spell allows the mage to bind a hibernating spirit into a fetish, a kind of magical item. Fetishes work like an Imbued Items, save that a fetish is powered by Essence and, instead of holding a Supernal spell, it holds one of the bound spirit\'s Influences and, possibly, some of its Numina. Creating a fetish requires that the spell have one Potency per dot of Influence the object will possess, plus one Potency per Numen. A fetish doesn\'t have to host all of the spirit\'s abilities. Activating the powers within the fetish is an instant action and uses the spirit\'s dice pool.'
spell.db.reference = 'M:tA p. 183'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Craftsmans_Eye')
spell.db.longname = 'Craftsman\'s Eye'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Under the craftsman\'s eye, no tool is mysterious. By studying an object for one turn, the subject gains a complete understanding of the object\'s intended function. From a tool as simple as a hammer to an intricate puzzle box, the item\'s intended purpose is plain to see. If the object has no purpose (for example, a simple rock), the spell reveals that too. Likewise, if something prevents the object from fulfilling its purpose (for example, a car missing its spark plugs can\'t drive), the spell reveals the nature of the problem.'
spell.db.reference = 'M:tA p. 154'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Create_Anchor')
spell.db.longname = 'Create Anchor'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage applies a universally-applicable version of the Anchor Condition to a subject, usable by any ghosts. If the mage also has a ghost as an additional subject, that ghost becomes anchored to the new Anchor as well as its own.'
spell.db.reference = 'M:tA p. 133'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Create_Avernian_Gate')
spell.db.longname = 'Create Avernian Gate'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage rips open the material world to the Underworld, creating an Iris between the material world and the upper layers of the Underworld within the area of effect. Opening the gate causes the area to gain a Death Resonance and the Gateway Condition for the Duration of the spell.'
spell.db.reference = 'M:tA p. 133'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Create_Energy')
spell.db.longname = 'Create Energy'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage creates energy from othing within a subject or area of effect. She can create light (including sunlight), fire, radiation, sound, and electricity. Use the chart under Transform Energy above as an example of the levels she can create within the affected area. For fire, assume the heat is +1 for Potency 1-2, +2 for Potency 3-4 and +3 for Potency 5+. After creating the energy, she can modify it with Control spells. Creating radiation also creates an Extreme Environment hazardous to living beings.'
spell.db.reference = 'M:tA p. 146'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Create_Ghost')
spell.db.longname = 'Create Ghost'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage creates a ghost within Twilight. She can fashion the ghost as an echo of another person, either alive or dead, though the ghost is not the actual person. The ghost is created at Rank 1 and remains for the Duration of the spell as the mage\'s loyal servant, and she is able to direct it to take actions without the use of any additional spells.'
spell.db.reference = 'M:tA p. 133'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Create_Life')
spell.db.longname = 'Create Life'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 5'
spell.db.info = 'A Master of Life may create a new living organism of nearly any variety: plant, fungus, animal, even complex organisms like humans and cetaceans. The created being is mindless without the conjunctional use of the Mind Arcanum to give it intelligence, acting purely upon instinct. It will be a simple creature, even for its kind, but otherwise fully functional and even capable of procreation.'
spell.db.reference = 'M:tA p. 153'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Create_Locus')
spell.db.longname = 'Create Locus'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 5'
spell.db.info = 'By means of this spell, the mage creates a Locus at a location with the Resonant Condition. A Locus is a location in which the Shadow world is especially close. Spirits don\'t need the Reaching Manifestation Effect to use their powers across the Gauntlet at a Locus, attempts to cross over are at +2 dice, and spirits whose natures match the Locus\' Resonant Condition heal at twice the normal rate.'
spell.db.reference = 'M:tA p. 184-185'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Create_Sympathy')
spell.db.longname = 'Create Sympathy'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 5'
spell.db.info = 'To a Master of Space, powerful connections are forged as easily as snapping one\'s fingers. With this spell, the mage creates a new sympathetic connection on the subject. These new connections are Lasting, but can fade with time as described on p. 172.'
spell.db.reference = 'M:tA p. 178'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Create_Truth')
spell.db.longname = 'Create Truth'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The Awakened speaks, and the heavens reshape themselves. This spell overwrites the conditions of Fallen Reality within the area, creating a Hallow with a dot rating equal to the spell\'s Potency. This Hallow has Resonance appropriate to its location and to the caster\'s Path and Nimbus (see p. 242). The sudden emergence of such a mystically potent site causes massive ripples and aftershocks through the local network of ley lines, which almost certainly creates new Mysteries.'
spell.db.reference = 'M:tA p. 170-171'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Crucible')
spell.db.longname = 'Crucible'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 3'
spell.db.info = 'With this spell, an object takes on a glimmer of Supernal purity. If its primary purpose is as a tool, it grants 8-Again on a number of rolls equal to the spell\'s Potency. Valuable objects, such as gold or diamonds, become incredibly pure and beautiful. Add the spell\'s Potency to the object\'s Availability rating to determine its increased value. This spell cannot increase an object\'s Availability to more than twice its original rating.'
spell.db.reference = 'M:tA p. 157'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Cut_Threads')
spell.db.longname = 'Cut Threads'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 4'
spell.db.info = 'Isolation is the beginning of understanding. This spell destroys one of the subject\'s sympathetic links (additional connections can be severed by increasing the number of subjects with the Scale factor). This effect is Lasting, but normal interactions may restore the links in time, as described on p. 172.'
spell.db.reference = 'M:tA p. 177-178'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Damage_Ghost')
spell.db.longname = 'Damage Ghost'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage can cause pain to a ghost. She deals one bashing wound to the ghost\'s Corpus per Potency of the spell.'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Decay')
spell.db.longname = 'Decay'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage degrades a material object, causing it to age in a matter of moments. The object\'s Durability is lowered by -1 for each Potency of the spell\'s casting.'
spell.db.reference = 'M:tA p. 129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Deepen_Shadows')
spell.db.longname = 'Deepen Shadows'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can influence the shadows in the spell\'s area of effect, deepening darkness and making the area nearly completely pitch black. The area is affected by the Poor Light Environmental Tilt for the Duration of the spell.'
spell.db.reference = 'M:tA p. 128'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Degrading_the_Form')
spell.db.longname = 'Degrading the Form'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 3'
spell.db.info = 'Living things grow feeble when wracked with injury, disease, or genetic defect. This spell replicates those effects, crippling the subject\'s Physical Attributes. Each level of Potency reduces Strength, Dexterity, or Stamina by one, chosen when the spell is cast, to a minimum of 1.'
spell.db.reference = 'M:tA p. 150'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Deny_the_Reaper')
spell.db.longname = 'Deny the Reaper'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage is able to reverse the effects of entropy on her subject, even returning the dead back to life. The mage reverses the effects of decay, restoring the subject to its physical state of being from before up to one month per Potency of the spell. On a living subject, the spell can restore eyesight, the use of limbs, reversing irreparable damage, and restoring all bodily functions. On inanimate subjects the spell can restore time-ravaged photos, make old books pristine, or return old electronics to working order.'
spell.db.reference = 'M:tA p. 133'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Destroy_Tass')
spell.db.longname = 'Destroy Tass'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 4'
spell.db.info = 'At the mage\'s whim, constructs of Mana are swept away on the winds of Aether. A successful casting destroys the tass. The Mana held within it is not destroyed, but sublimates into the world and likely returns to the nearest Hallow.'
spell.db.reference = 'M:tA p. 170'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Detect_Substance')
spell.db.longname = 'Detect Substance'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage chooses a number of substances or objects that fall under Matter\'s purview equal to the spell\'s Potency. As long as this spell is active, the subject is automatically aware of the presence and location of the chosen substance within the area of effect. The chosen substance can be as broad or as specific as the mage likes ("ferrous metal," "stainless steel," "a knife," and "my hunting knife" are all valid options).'
spell.db.reference = 'M:tA p. 154'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Devouring_the_Slain')
spell.db.longname = 'Devouring the Slain'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage may pull the energy from his subject\'s suffering into himself. The mage chooses at the time of casting to either harvest Willpower or to scourge the subject\'s Pattern for Mana. The subject must have at least one Health box filled with either lethal or aggravated damage. For each level of Potency, the mage may take one point of Willpower (up to the subject\'s remaining Willpower points), or he may Scour the subject\'s Pattern for one point of Mana, dealing one lethal damage in the process, causing existing wounds to open and fester. Using this spell counts towards the limit of times per day a mage can gain Mana through Scouring.'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Discern_Composition')
spell.db.longname = 'Discern Composition'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The subject becomes aware of the precise composition of an object: its weight and density, as well as the precise elements that make it up.'
spell.db.reference = 'M:tA p. 154'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Dispel_Magic')
spell.db.longname = 'Dispel Magic'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 1'
spell.db.info = 'All Awakened magic contains the capacity to end, to allow the Fallen World\'s laws to reassert themselves. By Compelling these flaws in an extant spell, the mage may temporarily suppress it - or even destroy it entirely. This spell is not potent enough to dispel an archmage\'s spells, and only works against Awakened magic. In addition, the mage must include all Arcana involved in the casting of the subject spell at one dot.'
spell.db.reference = 'M:tA p. 165'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Display_of_Power')
spell.db.longname = 'Display of Power'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 3'
spell.db.info = 'Magic itself falls under the purview of Prime, even its most private functions. By using this spell, a mage stirs the Supernal World, making it respond to mages within the spell\'s area. Rather than being wholly internal, Imagos formed by mages within the spell\'s effect become visible in the Supernal World to all forms of Active Mage Sight, displayed as magical runes and flashes of symbols hovering around the mage. Mages use this spell as a teaching aid, forming Imagos to display to their students without actually casting. The spell has another role in mage society, though; it is the basis for the Duel Arcane (see p. 294), in which two rival mages display what they could do to one another.'
spell.db.reference = 'M:tA p. 168-169'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Divination')
spell.db.longname = 'Divination'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can look into her subject\'s most likely future. Without Reach, the mage can only see generalities: "Will I meet Anna again soon?" is a valid question, while "What time will the police arrive?" is too specific to return an answer. This spell can see far into the future, such as telling the mage that a young cashier might eventually become a state Governor, or that a child prodigy might become a superstar, but looking too far from the present increases the likelihood of the answer being superseded by the point the future becomes the present. The Storyteller must decide what the future holds, taking into account the nature of the story as well as cues from the mage\'s questions. The caster can ask one general question per level of Potency, receiving answers of "Yes," "No," or "Irrelevant."'
spell.db.reference = 'M:tA p. 186-187'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Divine_Intervention')
spell.db.longname = 'Divine Intervention'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage casts a powerful curse that either encourages the subject to achieve a goal specified by the mage when he casts this spell, or that thwarts the subject\'s every attempt to pursue such a goal. The subject must, however, be aware of the goal, and the mage cannot levy impossible tasks.'
spell.db.reference = 'M:tA p. 138'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Dream_Reaching')
spell.db.longname = 'Dream Reaching'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage may enter and share the dreams of a sleeping subject. The mage witnesses the dream, and can influence its direction, though she is not directly a part of the dream. Casting this spell on herself ensures the mage remembers her dreams.'
spell.db.reference = 'M:tA p. 160'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Earthquake')
spell.db.longname = 'Earthquake'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage unleashes an earthquake to crack the ground. This spell inflicts damage equal to its Potency to all structures within the affected area. Most modern buildings are built to endure earthquakes well and subtract their Durability from the damage as normal. Smaller or flimsier structures do not apply Durability to the damage at all. Living beings may make a Dexterity + Athletics roll to maintain their balance as the ground pitches and heaves beneath them. Failure means the character suffers bashing damage as she falls to the ground and is thrown about wildly, unless the fall sends her tumbling down stairs or over a ledge. Collapsing buildings can cause much more catastrophic damage or leave victims trapped under tons of debris.'
spell.db.reference = 'M:tA p. 147'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Ectoplasm')
spell.db.longname = 'Ectoplasm'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can create ectoplasm (see Ectoplasmic Shaping, above) from one of his own orifices, or the orifice of a corpse - normally the nose or mouth, but sometimes the tear ducts or ears. The mage can shape the ectoplasm into any shape he wishes. The ectoplasm retains its shape for the Duration of the spell.'
spell.db.reference = 'M:tA p. 129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Ectoplasmic_Shaping')
spell.db.longname = 'Ectoplasmic Shaping'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage may shape and mold an ectoplasmic manifestation, either conjured by another mage or from a Materialized ghost, though the person or ghost that controls the ectoplasm may Withstand the shaping. After a successful casting, the mage shapes the ectoplasm into any shape he desires. The ectoplasm remains in the new shape for the Duration of the spell. He can use it to craft a mirror that reflects ghosts and other structures in ghostly Twilight in a given area.'
spell.db.reference = 'M:tA p. 128'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Eidolon')
spell.db.longname = 'Eidolon'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 5'
spell.db.info = 'Where adepts of Prime can create platonic objects by forcing Mana into the pattern it wears within tass, a master can create the complex Prime patterns within living beings and the environment. When fuelled with Mana, this spell creates an obviously-magical construct much like Platonic Form, except that the construct is not limited to single physical objects. Eidolons may imitate fire, fog, and even entire environments, but most masters use it to create "living" constructs. Eidolons are still made of solidified Mana, and have Durability and Structure instead of Healt , and when mimicking environmental hazards do not inflict damage as they do (Eidolon fire does not burn, for example.) They follow the Potency rules for Platonic Form (p.169) but Potency may also be allocated to grant dots of the Retainer Merit.'
spell.db.reference = 'M:tA p. 171'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Electromagnetic_Pulse')
spell.db.longname = 'Electromagnetic Pulse'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage degrades electromagnetic energy within the spell\'s subject, wrecking electronic devices. The spell is capable of snuffing out mundane electrical devices, although some military-grade devices are shielded, requiring Potency equal to their level of hardening. Shorting out magical devices requires a Clash of Wills. When used against a living being, the damage to their nervous system acts as a direct damage spell, inflicting Potency in lethal damage.'
spell.db.reference = 'M:tA p. 145'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Emotional_Urging')
spell.db.longname = 'Emotional Urging'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can project an emotional state at her subject, instilling emotions that grease social wheels or create barriers between people. The mage chooses at casting to project a positive or negative emotion at her subject, which allows her to open or close one Door. Opening a Door usually occurs before an attempted Social maneuver, and the influence of the Door opening does not have to benefit the mage, but can benefit anyone dealing with the subject during the Duration of the spell. The mage may close Doors previously opened with the subject, making it harder for others to accomplish goals.'
spell.db.reference = 'M:tA p. 160'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Empty_Presence')
spell.db.longname = 'Empty Presence'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage destroys the subject\'s presence in the world, removing any evidence of her life or existence. Any attempts to see the subject through mundane means of detection or observation fail completely. Not only is she invisible to the naked eye, but evidence of her life is scrubbed. All Doors she may have opened during social interactions with others, either on herself or on the other person, are removed. All her Conditions, and all Conditions applying to her (except for Paradox Conditions), resolve without granting Beats. While invisible, the subject cannot make violent, overt actions without breaking the spell\'s illusion. Physically damaging or breaking objects, or attacking someone, causes the spell to end immediately.'
spell.db.reference = 'M:tA p. 133'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Enervation')
spell.db.longname = 'Enervation'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage causes her subject\'s muscles to stop working, breaking down connections between muscles, ligaments, and tendons. The spell imposes either the Leg Wrack Tilt or the Arm Wrack Tilt on the subject while the spell remains active.'
spell.db.reference = 'M:tA p. 132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Enhance_Skill')
spell.db.longname = 'Enhance Skill'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage is capable of temporarily increasing one of her subject\'s Skills. She can increase one Skill that the subject already has at least one rank in by one dot per level of Potency of the spell. The spell cannot increase the subject\'s Skill above the normal maximum.'
spell.db.reference = 'M:tA p. 162'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Environmental_Shield')
spell.db.longname = 'Environmental Shield'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can shield herself against harmful environmental conditions. This spell provides complete resistance to any Conditions or Tilts caused by environments, up to an Extreme Environment level of the spell\'s Potency. The spell only protects against indirect damage, like heat and cold and minor hazards like hail. The mage can still drown or be crushed by crashing waves. While the spell wouldn\'t protect her against lightning if something forced it to strike her, she wouldn\'t naturally attract the bolt. The spell requires a Clash of Wills to work against magical weather effects.'
spell.db.reference = 'M:tA p. 143'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Ephemeral_Enchantment')
spell.db.longname = 'Ephemeral Enchantment'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The symbol-forms of the Aether are real enough to cut through all layers of reality. This spell enchants the subject to be as solid to Twilight entities as to physical matter. This spell is equally effective against all forms of Twilight; the subject may interact with ghosts, spirits, angels, and stranger things with equal facility.'
spell.db.reference = 'M:tA p. 169'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Ephemeral_Shield')
spell.db.longname = 'Ephemeral Shield'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 2'
spell.db.info = 'To master the spirit world, one must show no vulnerability. This spell protects the subject against the Numina, Influences, and Manifestations of spirits, Spirit spells, and any spiritual powers of other supernatural creatures such as werewolves. Such attacks must succeed at a Clash of Wills to harm the subject.'
spell.db.reference = 'M:tA p. 181'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Eradicate_Energy')
spell.db.longname = 'Eradicate Energy'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 5'
spell.db.info = 'Rather than create energy, the mage snuffs out energies within a subject or area (see the chart "Transform Energy," above, for the Potency required by different levels of energy.) The destruction is spectacular, explosively scattering the affected energies into particles. If used on a creature, this spell is instantly fatal but Withstood by Stamina.'
spell.db.reference = 'M:tA p. 146'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Erode_Resonance')
spell.db.longname = 'Erode Resonance'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 3'
spell.db.info = 'Sometimes a healer must cut out diseased flesh so that the whole may heal. This spell removes the Open or Resonant condition on its target entirely. The effect is Lasting.'
spell.db.reference = 'M:tA p. 181-182'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Essence_Fountain')
spell.db.longname = 'Essence Fountain'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The shaman feeds her spiritual children. This spell generates a quantity of Essence equal to the spell\'s Potency within the subject\'s Pattern. The Essence has a Resonance of the mage\'s choosing, as long as she\'s encountered it before.'
spell.db.reference = 'M:tA p. 185'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Ex_Nihilo')
spell.db.longname = 'Ex Nihilo'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage creates an object out of nothing. The object may be any simple tool or relatively uncomplicated machine (a revolver qualifies, but an automatic handgun is too complex). The object\'s size is determined by the Scale factor. The spell\'s Potency may be allocated as the mage wishes between Durability or equipment bonus.'
spell.db.reference = 'M:tA p. 158-159'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Exceptional_Luck')
spell.db.longname = 'Exceptional Luck'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage blesses the subject\'s endeavors or curses them with misfortune. Whether good or bad, the subject\'s luck is truly exceptional. This spell bestows a boon or inflicts a hex on the subject (see p. 134). The subject may Withstand a hex with Composure'
spell.db.reference = 'M:tA p. 135'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Exorcism')
spell.db.longname = 'Exorcism'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 4'
spell.db.info = 'This spell rips a ghost\'s grip on the world away. This spell strips a number of Manifestation Conditions from the ghost (or its host) equal to the spell\'s Potency. The effect is Lasting, but the spirit may use its Influences and Manifestations to reestablish the Conditions as normal.'
spell.db.reference = 'M:tA p. 132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Exorcists_Eye')
spell.db.longname = 'Exorcist\'s Eye'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The first spell most Spirit mages learn, this spell allows the mage to perceive and speak with spirits in the physical world, whether they are roaming freely in Twilight, slumbering within an object (including discorporated spirits in hibernation), or possessing a living being. She can also sense any spirit-related Manifestation Conditions in the area. Finally, she can see the conduit of any spirit with the Reaching Manifestation, but cannot communicate across the Gauntlet.'
spell.db.reference = 'M:tA p. 180'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Fabricate_Fortune')
spell.db.longname = 'Fabricate Fortune'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 2'
spell.db.info = 'Sometimes a mage wishes to hide a child of destiny from those who would abuse her gift. Other times he wishes to convince observers that a subject has a fate that she does not. This spell conceals or falsifies fates and Destiny.'
spell.db.reference = 'M:tA p. 136'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Familiar')
spell.db.longname = 'Familiar'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage creates a Familiar bond between a spirit and a mage, who must both be subjects of the spell. The spirit may not be greater than Rank 2. The mage gains the Familiar Merit and the spirit the Familiar Manifestation Condition for the Duration of the spell. Both parties must be willing, and can end the bond whenever they wish.'
spell.db.reference = 'M:tA p. 183'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Find_the_Balance')
spell.db.longname = 'Find the Balance'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 2'
spell.db.info = 'Those initiated into the Stygian Mysteries know that understanding a tool is only the first step toward perfecting it. By subtly manipulating the density and purity of a tool, the mage improves its balance and heft. The tool grants its user the 9-Again quality for the Duration of the spell, so long as it\'s a tool that can benefit from balance or weight distribution.'
spell.db.reference = 'M:tA p. 155-156'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'First_Impressions')
spell.db.longname = 'First Impressions'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can dictate how a subject will react to a social interaction, making her more or less inclined to listen to an argument. The spell affects the next Social maneuvering attempt made against the subject, raising or lowering the first impression by levels equal to Potency.'
spell.db.reference = 'M:tA p. 160'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Fools_Rush_In')
spell.db.longname = 'Fools Rush In'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 2'
spell.db.info = 'According to old wisdom Fate favors children and fools, and this spell makes the old adage true. So long as the subject has little or no detailed knowledge about a situation before he enters it, the spell allows him to act with perfect grace and timing. A turn or two of studying the scene before acting is acceptable, but extensive reconnaissance or a detailed briefing does not permit the necessary degree of randomness this spell requires.'
spell.db.reference = 'M:tA p. 136'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Forensic_Gaze')
spell.db.longname = 'Forensic Gaze'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can determine the state of a corpse. She determines the exact method of its demise as well as exactly when it died. For each level of Potency, the mage reveals contributing factors to the cause of death. For example, a man found burned in a car might have died from asphyxiation, but might have gotten that way because he was unconscious due to a head wound from crashing his car into a tree while driving drunk.'
spell.db.reference = 'M:tA p. 128'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Forge_Destiny')
spell.db.longname = 'Forge Destiny'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 5'
spell.db.info = 'If a Master of Fate does not have a hero of destiny handy, he can simply make one. He has several means of accomplishing this at his disposal, and may apply one of the following effects:'
spell.db.reference = 'M:tA p. 139'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Forge_No_Chains')
spell.db.longname = 'Forge No Chains'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 5'
spell.db.info = 'To leave behind attachments is the truest sign of freedom. For the Duration of this spell, the subject leaves no sympathetic traces behind. She cannot forge sympathetic connections, and even blood, hair, and the like shed during the spell\'s Duration do not link back to her. Her Space spells leave no tell-tale ripples in the Tapestry. Any attempt to scrutinize her Space magic or previously-created sympathetic connections with Mage Sight (see p. 92) add the spell\'s Potency to the Mystery\'s Opacity.'
spell.db.reference = 'M:tA p. 178'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Forge_Purpose')
spell.db.longname = 'Forge Purpose'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage imparts a holy mission upon her subject. For the Duration of the spell, the subject gains one of the mage\'s Obsessions as his own. If the subject is a mage who already has the maximum number of Obsessions allowed by her Gnosis, this spell triggers a Clash of Wills. If the caster is successful, she replaces the subject\'s most recently acquired Obsession with her own.'
spell.db.reference = 'M:tA p. 171'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Gain_Skill')
spell.db.longname = 'Gain Skill'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage is capable of temporarily granting the subject a Skill, granting a number of dots in one Skill per level of Potency of the spell. The spell cannot increase the subject\'s Skill above the normal maximum.'
spell.db.reference = 'M:tA p. 163'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Geomancy')
spell.db.longname = 'Geomancy'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 3'
spell.db.info = 'By imposing her will upon the earth\'s natural flow of energy, the mage may redirect ley lines within the area of effect, reshaping Nodes and altering Resonance freely. She may move ley lines, and therefore the Nodes created where ley lines cross, "pinning" a line to a point within the area of effect of the spell. She may also change the Resonance Keyword of a Node to whatever she wishes.'
spell.db.reference = 'M:tA p. 169'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Ghost_Gate')
spell.db.longname = 'Ghost Gate'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage creates a two-dimensional plane that acts as a gateway, converting anything that moves through it into Twilight. While in Twilight, the person can interact with and see Death-attuned ephemeral objects and beings. Items can be carried through the gate, but doing so destroys their material forms, though they may be retrieved later with "Touch of the Grave."'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Ghost_Shield')
spell.db.longname = 'Ghost Shield'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The caster creates a shield that protects her subject from ghostly Numina, Influences, Manifestations, Death spells, and any death-related powers of other supernatural creatures. Any power attempting to pierce the shield provokes a Clash of Wills roll.'
spell.db.reference = 'M:tA p. 129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Ghost_Summons')
spell.db.longname = 'Ghost Summons'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage sends out a call to the nearest ghost within her sensory range. Alternately, she can summon ghosts she knows personally. She may send a general call and the nearest ghost will answer, or she can specify the type of ghost, such as a child or a female. The ghost cannot travel farther than allowed by its Anchor. The spell does not work on ghosts above Rank 5.'
spell.db.reference = 'M:tA p. 131'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Ghostwall')
spell.db.longname = 'Ghostwall'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 4'
spell.db.info = 'All Fallen Matter is merely a shadow of Supernal truth, and this spell reveals the truth of that axiom. The mage renders a volume of inert matter wholly or partly insubstantial, no more "real" than an illusion. Insubstantial objects remain where they were when transfigured (that is, they don\'t fall to the center of the Earth or fly off into space). Objects made insubstantial by this spell aren\'t in Twilight, they simply don\'t register as "real."'
spell.db.reference = 'M:tA p. 158'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Goetic_Summons')
spell.db.longname = 'Goetic Summons'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage sends out a call to the nearest Goetia within her sensory range. Conversely she can summon Goetia she knows personally. She may send a general call and the nearest Goetia will answer, or she can specify the type of entity by its Resonance. The spell does not work on Goetia above Rank 5.'
spell.db.reference = 'M:tA p. 162'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Golem')
spell.db.longname = 'Golem'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 4'
spell.db.info = 'This spell animates a statue or other object, allowing it to move and act almost as if it were alive. Each level of Potency effectively grants the mage a dot of the Retainer Merit. The Golem\'s "field" includes simple physical labor, combat, and other uncomplicated tasks.'
spell.db.reference = 'M:tA p. 158'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Gossamer_Touch')
spell.db.longname = 'Gossamer Touch'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 2'
spell.db.info = 'Sometimes the only way to command a spirit is with raw, brute force. This spell renders the subject\'s flesh solid to spirits in Twilight, allowing her to interact with them physically.'
spell.db.reference = 'M:tA p. 181'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Grave_Misfortune')
spell.db.longname = 'Grave Misfortune'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 3'
spell.db.info = 'This spell attracts misfortune to the subject or makes an already injurious situation considerably worse.'
spell.db.reference = 'M:tA p. 137'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Gravitic_Superiority')
spell.db.longname = 'Gravitic Superiority'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage may increase or decrease gravity. If increasing it, each level of Potency subtracts 3 Speed from all subjects, as well as penalizing jumping rolls, subtracting a distance equal to Potency from success rolled. If Potency exceeds the Strength of an animal caught in the area, the subject suffers -1 to all Physical dice pools for each point of difference. Flying creatures must succeed on a Strength + Athletics roll each turn or plummet downward at a Speed equal to the Potency.'
spell.db.reference = 'M:tA p. 144'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Green_Light/Red_Light')
spell.db.longname = 'Green Light/Red Light'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage may manipulate the subtle timings of events, smoothing or obstructing her subject\'s progress. Cast positively, the subject finds elevators and taxis arrive just as he needs them, stop lights turn green, and he arrives on time for meetings. Cast negatively, anything that can delay the subject will delay him.'
spell.db.reference = 'M:tA p. 187'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Gremlins')
spell.db.longname = 'Gremlins'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Just as the spirit of an object can be coaxed to help, it may also be coaxed to hinder. When a character fails a roll using this spell\'s subject as equipment, the spell converts the failure into a dramatic failure. The spell converts a number of failures equal to its Potency. If the object\'s user is a player\'s character, the player gains a Beat as normal.'
spell.db.reference = 'M:tA p. 180'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Ground-Eater')
spell.db.longname = 'Ground-Eater'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Space is more flexible than many believe. By subtly pinching or stretching the space around her subject, the mage allows her to cover far more ground with each step than is readily apparent. The mage adds the spell\'s Potency to the subject\'s Speed. Watching someone under the influence of this spell is alarming: It\'s hard for the eye to track her, as each step carries her farther than it should, and in every blink or momentary glance away she seems to leap farther than should be possible in such a short time.'
spell.db.reference = 'M:tA p. 173'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Hallow_Dance')
spell.db.longname = 'Hallow Dance'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The tides of Aether ebb and flow, awakening sacred places and sending them to sleep once more in the cycle of ages. This spell allows the mage to bend that cycle to her will. The mage may suppress an active Hallow or awaken a dormant one with this spell. Rousing a slumbering Hallow requires a Potency equal to the Hallow\'s rating, while damping a Hallow reduces its effective dot rating by one per point of Potency. If the Hallow is suppressed to zero dots or fewer, it falls dormant. See p. 241 for more information on Hallows.'
spell.db.reference = 'M:tA p. 170'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Hallucination')
spell.db.longname = 'Hallucination'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage creates false sensory input in her subject, tricking his senses and creating a hallucination. The mage creates a single illusion that seems completely real to her subject. She affects sound, smell, taste, and sight with the illusion, though she is unable to make the illusion tactile to the subject.'
spell.db.reference = 'M:tA p. 163-164'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Heightened_Senses')
spell.db.longname = 'Heightened Senses'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 1'
spell.db.info = 'While this spell cannot grant a mage new senses, it can heighten her existing ones, including touch. This is a popular spell among hedonistic mages as a result, as well as those who want to revitalize senses dulled by city life. A mage\'s strength lies in her preparation and knowledge, after all, and keen senses impart greater information about the world.'
spell.db.reference = 'M:tA p. 148'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Hidden_Hoard')
spell.db.longname = 'Hidden Hoard'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 2'
spell.db.info = 'This spell renders Matter difficult to detect. It isn\'t invisibility, precisely; rather, the spell veils the subject\'s connection to the Supernal truths, making it seem insignificant and beneath notice. Mundane attempts to detect the subject fail automatically. Spells and powers that would detect the veiled object are subject to a Clash of Wills.'
spell.db.reference = 'M:tA p. 156'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Honing_the_Form')
spell.db.longname = 'Honing the Form'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage may improve the subject\'s Physical Attributes. The spell increases Strength, Dexterity, or Stamina (chosen when the spell is cast) by its Potency. This increase affects any Advantages or other traits derived from the Attribute\'s level. The effects are subtle in appearance; the affected target doesn\'t grow or gain any obvious muscle mass, but observers can detect even subtle hints of changes to balance, strength, or stamina. The affected Attribute cannot be raised above the subject\'s maximum Attribute dots (5 for normal human beings).'
spell.db.reference = 'M:tA p. 150'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Howl_from_Beyond')
spell.db.longname = 'Howl from Beyond'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 3'
spell.db.info = 'With this spell the mage calls forth a torrent of Essence from the spirit world, which buffets her foes and leaves them drained in body and soul. This is an attack spell; its damage rating is equal to the spell\'s Potency, and it inflicts bashing damage. This spell can target physical beings or spirits in Twilight.'
spell.db.reference = 'M:tA p. 182'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Hung_Spell')
spell.db.longname = 'Hung Spell'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 2'
spell.db.info = 'With this spell, the mage captures pure expressions of magic - spells - at the moment they enter the Fallen World, suspending them before they take effect but preserving their Duration from decay. The subject must be a mage, who must deliberately build his Imago to take advantage of this spell\'s effect and pay one Mana when casting. Hung Spell may entrap up to its Potency in spells, which remain in their caster\'s spell control but do not take effect until Hung Spell is canceled or runs out of Duration. When Hung Spell ceases, the trapped spells immediately take effect and begin their own Durations.'
spell.db.reference = 'M:tA p. 187-188'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Imposter')
spell.db.longname = 'Imposter'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage confuses her subject\'s senses, making him believe she is someone else. She can invent an appearance, or mimic the exact look, sound, and smell of any individual she knows. Unless the mage has interacted extensively with the person she is impersonating, she must make a Manipulation + Subterfuge roll when she first begins interacting with her subject, and every minute she continues interacting with him. The spell cannot mimic specific Social Merits that grant dice bonuses to Social rolls.'
spell.db.reference = 'M:tA p. 162'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Incognito_Presence')
spell.db.longname = 'Incognito Presence'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage hides the subject\'s psychic presence, causing onlookers to ignore her. When people look at her, they want to avert their eyes, or barely notice her. People cannot remember seeing her when they are no longer looking her way. Beings using supernatural abilities to concentrate on her, including Active Mage Sight, provoke a Clash of Wills.'
spell.db.reference = 'M:tA p. 160'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Influence_Electricity')
spell.db.longname = 'Influence Electricity'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can operate or shut down electrical devices with magic. With this spell she can only cause existing devices to work as they normally would when powered on, or when the power is shut off. For example, she could "hotwire" a car without actually needing to touch any wires, turn lights off and on, and cause industrial machinery to power up or turn off. This spell does not give her further control over these devices, but does allow her to engage or shut down devices that might otherwise require passwords or electronic keys.'
spell.db.reference = 'M:tA p. 140'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Influence_Fire')
spell.db.longname = 'Influence Fire'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Legends of mages controlling fire begin with this spell, which allows a mage to guide the path of existing flames. This lets her cause flames to arc or stretch, command them to burn along a particular path (or prevent them from another), or even form particular fiery shapes. At this level the mage cannot increase the flames in size or intensity, though she could direct them into a source of fuel.'
spell.db.reference = 'M:tA p. 140-141'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Influence_Heat')
spell.db.longname = 'Influence Heat'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Initiates can guide the direction of existing forces. With this spell, the mage can control the flow of heat in the area. While she cannot increase or create heat, the mage can direct heat from a radiator across the room to her, or pull any ambient warmth shed by car engines, human bodies, or environmental sources. This can keep her warm in cold weather or cool in hot weather, preventing heat- or cold-related damage and Conditions caused by Extreme Environments up to Level 2 (see Extreme Environments, p. 224).'
spell.db.reference = 'M:tA p. 141'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Interconnections')
spell.db.longname = 'Interconnections'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 1'
spell.db.info = 'This spell reveals the marks of Fate on people, places, and things the mage observes (up to one subject per turn). In addition to allowing the mage to detect any sympathetic connections between the subjects, the mage can also identify those who have violated a magical oath, and the presence of spells with conditional Durations (see p. 192).'
spell.db.reference = 'M:tA p. 134-135'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Invisibility')
spell.db.longname = 'Invisibility'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'This spell can render its subject completely invisible, masking it from all forms of light. Even cameras cannot detect the object, no matter what type of filter or lenses they use. This spell does not mask the sounds an object makes, although when Combined with "Control Sound" (see above), the target can be made invisible and soundless.'
spell.db.reference = 'M:tA p. 143'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Invisible_Runes')
spell.db.longname = 'Invisible Runes'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The Awakened make use of signs others can\'t see. This spell draws a short message in High Speech, visible only to Mage Sight, onto its subject. Attempting to alter the marks by overwriting them provokes a Clash of Wills. Mages use these signs to mark their cabal\'s property and territory, or leave warnings for one another, as any form of Active Mage Sight reveals them.'
spell.db.reference = 'M:tA p. 167'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Invoke_Bane')
spell.db.longname = 'Invoke Bane'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The spirits know what causes them pain, and avoid it at all costs. This spell forces a spirit to avoid its Bane even more assiduously than normal. The spirit must spend a point of Willpower to even come within the area of influence of its Bane (described by the Area factor of the spell), and cannot touch it at all. If the spirit is already within the proscribed area and fails the roll, it must flee immediately. This spell does not affect spirits above Rank 5.'
spell.db.reference = 'M:tA p. 180'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Isolation')
spell.db.longname = 'Isolation'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Boundaries and barriers are a lie, but it is sometimes useful to lie. This spell subtly warps space and distance around the subject, making empty spaces seem larger and more foreboding. Crowds of people seem tightly packed together, an impenetrable wall of humanity.'
spell.db.reference = 'M:tA p. 173'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Kinetic_Blow')
spell.db.longname = 'Kinetic Blow'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage focuses the kinetic force of bludgeoning attacks to such a pinpoint that they cause damage like piercing weapons. This only works on the subject\'s unarmed attacks and not any held weapons, though body-hugging objects like gloves and shoes benefit from the spell\'s effect. Unarmed attacks (including those made in grapples) gain a weapon bonus equal to Potency, to a maximum of 5, and inflict lethal damage.'
spell.db.reference = 'M:tA p. 143-144'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Kinetic_Efficiency')
spell.db.longname = 'Kinetic Efficiency'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 1'
spell.db.info = 'With a simple spell, the mage can "nudge" kinetic forces, enhancing a subject\'s motion. This spell allows the subject to run a little faster, jump a little further, or lift a little more, not by altering forces but by maximizing the subject\'s kinetic energy use. This has the following benefits:'
spell.db.reference = 'M:tA p. 141'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Knit')
spell.db.longname = 'Knit'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage can heal her subject\'s body of injuries it would be capable of healing itself given time, and repair damage done by toxins or deprivation (though such damage will continue to accrue as normal unless prevented by other means). Each level of Potency heals two boxes of bashing damage.'
spell.db.reference = 'M:tA p. 150'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Know_Nature')
spell.db.longname = 'Know Nature'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 1'
spell.db.info = 'By observing her subject, the mage can determine his Virtue, Vice, and how many dots in Mental and Social Attributes he has.'
spell.db.reference = 'M:tA p. 159'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Know_Spirit')
spell.db.longname = 'Know Spirit'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 1'
spell.db.info = 'To command the spirits, one must first understand them. This spell allows the mage to glean a number of the following facts about a spirit equal to the Spell\'s Potency:'
spell.db.reference = 'M:tA p. 180'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Levitation')
spell.db.longname = 'Levitation'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The subject floats through the air using telekinetic force. Its air speed equals the spell\'s Potency. Subjects may use their Defense against attacks, if applicable. Unwilling subjects Withstand the spell with Stamina.'
spell.db.reference = 'M:tA p. 145'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Life-Force_Assault')
spell.db.longname = 'Life-Force Assault'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage attacks the very life energies that sustain a living Pattern. This involves rending that Pattern, causing horribly painful internal wounds and unspecific tissue damage. This is an attack spell, inflicting lethal damage equal to its Potency.'
spell.db.reference = 'M:tA p. 152'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Locate_Object')
spell.db.longname = 'Locate Object'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 1'
spell.db.info = 'All distance is an illusion. Once this truth is understood, all things are in the same place as the mage, and how can one lose track of herself? As long as the subject of this spell is within the Area of the spell, she knows its precise location. Short of concealing magic (which provokes a Clash of Wills), no attempt to hide the subject can fool her unerring senses.'
spell.db.reference = 'M:tA p. 173-174'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Lodestone')
spell.db.longname = 'Lodestone'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage chooses a substance or type of object. As long as the spell remains active, those objects within the spell\'s Area are drawn to the spell\'s subject: Dropped coins bounce toward her, water flows in her direction as long as she\'s standing downstream, and so on. Unless the object is capable of moving under its own power, this spell can only nudge the object when an external force is imparted on it: a ball might roll across the floor, but a heavy book won\'t fly off a table into the subject\'s hand. (It might, however, tip and fall off a shelf if it was precariously balanced to begin with.)'
spell.db.reference = 'M:tA p. 154-155'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Lucky_Number')
spell.db.longname = 'Lucky Number'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The probability of correctly guessing a phone number, a password, or lock combination on the first try is minute but not impossible. This spell allows the mage to do just that simply by entering data into an appropriate device (a password field, a telephone, a safe combination, etc.). In addition to any story benefits, the mage gains the Informed Condition on next relevant roll that benefits from knowledge gained through this spell.'
spell.db.reference = 'M:tA p. 136'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Lure_and_Repel')
spell.db.longname = 'Lure and Repel'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can create a magical lure or repellant for specific types of organisms. While the mage could in theory specify any type of organism, she is likely to be quickly overwhelmed by numbers. When casting this spell as a lure, a smart mage will specify only certain types of organisms (not microscopic ones, if she\'s smarter still) to draw to her. Plants and microorganisms have Resolve 0 for purposes of Withstanding the spell. Organisms drawn in are not necessarily friendly and will remain cautious or even hostile if it is within their nature to do so, but will not openly attack the subject unless cornered. People affected by the spell find the subject irresistible or repugnant, but can\'t pinpoint just what it is that provokes the reaction.'
spell.db.reference = 'M:tA p. 149'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Lying_Maps')
spell.db.longname = 'Lying Maps'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 2'
spell.db.info = 'To know how to get from here to there is to tacitly accept the Lie. By means of this spell, the mage twists the subject\'s sense of direction, making him certain that the best route from where he is to somewhere else is one the mage desires. She could, for instance, convince the subject that the road to a dangerous Verge is actually the way to his mother\'s house, or that the mage\'s sanctum is in another part of the city. If the subject actively, carefully navigates using a map or GPS or the like, the navigation roll is a single chance die, and even on a success it feels wrong. ("The map says left, but I swear it\'s right!")'
spell.db.reference = 'M:tA p. 174'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Machine_Invisibility')
spell.db.longname = 'Machine Invisibility'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 2'
spell.db.info = 'By means of this spell, the mage blinds the eyes and ears of inert matter to her subject\'s presence: cameras refuse to see her, microphones refuse to hear her voice, and so on. Supernatural objects (such as remote-viewing Artifacts or perhaps a ghost-haunted camera) provoke a Clash of Wills.'
spell.db.reference = 'M:tA p. 156'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Many_Faces')
spell.db.longname = 'Many Faces'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage may alter her subject\'s body in any way, within the confines of species and age. Rather than an illusion as with "Mutable Mask," the transformation caused by this spell is entirely physical and functional - subjects can be made fertile in their new forms, be granted radically altered weight and fitness, and have poor vision or other senses corrected. If the subject is missing organs or limbs, however, they remain gone in the new form, and injuries carry over from one form to the next. The mage may rearrange up to the spell\'s Potency in Physical Attribute dots, for example moving a dot of Strength to Stamina, but cannot change the total number of dots, bring any to 0, or raise them above the subject\'s limit.'
spell.db.reference = 'M:tA p. 150'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Memory_Hole')
spell.db.longname = 'Memory Hole'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage compartmentalizes the subject\'s thoughts, placing memories into areas that she cannot access or remember. The mage can compartmentalize one memory per Potency, making the subject forget them completely for the Duration of the spell.'
spell.db.reference = 'M:tA p. 160'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Mend')
spell.db.longname = 'Mend'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 4'
spell.db.info = 'Adepts of Life can heal even the most grievous wounds, rewriting the subject\'s body to seal injuries shut. Each level of Potency heals two lethal damage.'
spell.db.reference = 'M:tA p. 152'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Mental_Scan')
spell.db.longname = 'Mental Scan'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 1'
spell.db.info = 'By quickly scanning the very surface of a subject\'s thoughts, the mage is capable of discerning his mental and emotional state. For each level of Potency, the mage may ask the Storyteller a single question to gain information about the subject\'s mental or emotional state. This information comes as flashes of insight from the subject\'s thoughts, so the Storyteller should be sure to represent her answers as such.'
spell.db.reference = 'M:tA p. 159'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Mental_Shield')
spell.db.longname = 'Mental Shield'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage erects a mental shield that protects the subject from mental attack. The shield provokes a Clash of Wills against any Goetia Numina, Influences, or Manifestations targeting the subject, any Mind spells, and any other supernatural creature\'s mind-affecting abilities.'
spell.db.reference = 'M:tA p. 160-161'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Mind_Flay')
spell.db.longname = 'Mind Flay'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage pulls apart her subject\'s conscious and subconscious mind, dealing damage as she does so. The subject suffers one point of lethal damage for each level of Potency of the spell.'
spell.db.reference = 'M:tA p. 164'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Mind_Wipe')
spell.db.longname = 'Mind Wipe'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage removes a large portion of the subject\'s memories. The victim suffers from the Amnesia Condition for the Duration of the spell, unable to recall one month of time per level of Potency. The mage may specify which portion of the subject\'s life is forgotten.'
spell.db.reference = 'M:tA p. 165'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Miracle')
spell.db.longname = 'Miracle'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 5'
spell.db.info = 'This spell causes events to unfold according to the mage\'s dictates. The mage receives a number of Intercessions equal to Potency, which she may use as a reflexive action during the spell\'s Duration. Spending one Intercession can achieve the following, affecting a single subject within sensory range:'
spell.db.reference = 'M:tA p. 140'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Momentary_Flux')
spell.db.longname = 'Momentary Flux'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can sense whether a subject will prove beneficial or baneful in the most likely future. The mage can see whether the stranger crossing the street to approach her at night is as threatening as he seems, or whether he has come to offer advice, for example. The spell itself does not tell the mage exactly what will happen, only whether it will prove good or bad for her. The stranger may augur as a bad omen for her; this could be due to his malicious intent - or maybe he\'s running from some danger, or even carrying a cold.'
spell.db.reference = 'M:tA p. 187'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Monkeys_Paw')
spell.db.longname = 'Monkey\'s Paw'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage interacts with a lifeless object, bringing fortune to bear on it and making it a tool of destiny. The mage either blesses or curses the object.'
spell.db.reference = 'M:tA p. 137'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Mutable_Mask')
spell.db.longname = 'Mutable Mask'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage may alter her subject\'s apparent features, albeit only cosmetically and temporarily. She can change skin pigments, phenotypical features, apparent sex, or hair color and texture; add or subtract small fat deposits; or change the sound of the subject\'s voice. Distinguishing features like scars and moles can be added or removed. Even at its most extreme, the changes wrought by this spell still leave the subject somewhat resembling her original form. If someone were to compare the masked and regular appearances side by side, they might notice an almost familial resemblance (even if the two are of obviously different races), but the changes are enough to fool facial recognition devices, sketch artists, or even change the subject\'s scent enough to throw off tracking animals. Some biometric devices, such as fingerprint scanners, will still detect the difference. She cannot mimic specific people with this basic spell.'
spell.db.reference = 'M:tA p. 149'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Nightvision')
spell.db.longname = 'Nightvision'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Despite its name, the Nightvision spell enhances ambient light, fine-tunes the mage\'s sense for vibrations and thermal changes, and grants her the power to see into the infrared and ultraviolet spectra. She becomes able to intuitively feel as well as see forms of electromagnetic radiation, sound, and kinetic energies, allowing her to navigate without penalty in complete darkness. She can still see and make out details, even in the dark, although colors are somewhat muted. This spell has the side effect of making the caster much more vulnerable to light; while in effect, she suffers no penalties from dim or even no lighting, but suffers penalties from bright lights as she normally would from darkness. Bright lights and extremely loud sounds can disorient or even inflict the Blind Condition on her for the spell\'s Duration.'
spell.db.reference = 'M:tA p. 141'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Nigredo_and_Albedo')
spell.db.longname = 'Nigredo and Albedo'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 3'
spell.db.info = 'All matter contains within itself the Supernal Truth of its own perfection - or its annihilation. This spell allows the mage to repair or destroy objects, restoring lost Structure or inflicting damage equal to the spell\'s Potency.'
spell.db.reference = 'M:tA p. 157'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'No_Exit')
spell.db.longname = 'No Exit'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage creates a mental thought loop for her subject, trapping him within his own mind. For the Duration of the spell, the subject is unable to do anything but play through a single continuous loop in his mind. Thoughts cannot enter or exit the subject\'s mind, and he appears nearly catatonic to outside observers. Attempts to read the subject\'s mind or memories reveal the thought loop. Supernatural attempts to force new thoughts provoke a Clash of Wills.'
spell.db.reference = 'M:tA p. 164-165'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Oaths_Fulfilled')
spell.db.longname = 'Oaths Fulfilled'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 1'
spell.db.info = 'In folktales, witches always seem to know when their subjects fulfill (or violate) the terms of an agreement. This spell notifies the mage when a specified fate befalls its subject - whether the subject is the victim or the actor. This triggering event must be something the mage could perceive if he were present (e.g. the subject suffers an injury, goes to the restroom, breaks her word, speaks the mage\'s name, etc.).'
spell.db.reference = 'M:tA p. 135'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'One_Mind,_Two_Thoughts')
spell.db.longname = 'One Mind, Two Thoughts'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The subject may hold two individual and wholly distinct trains of thought at once, as long as neither is physically demanding. She can perform two separate Mental or Social extended tasks at the same time. Neither task can be a purely Physical task, but the subject can carry on a conversation while composing a sonnet, or write a poem while researching scientific discoveries. The subject is incapable of multitasking spells, as they are more than just an exercise of consciousness.'
spell.db.reference = 'M:tA p. 159-160'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Opener_of_the_Way')
spell.db.longname = 'Opener of the Way'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The shaman is not only intercessor, but also gatekeeper. This spell allows the mage to shift the Resonant Condition on the subject to the Open Condition, or vice versa.'
spell.db.reference = 'M:tA p. 181'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Pariah')
spell.db.longname = 'Pariah'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 5'
spell.db.info = 'One of the most terrifying curses in the arsenal of a Master of Fate, this spell turns the world against the victim.'
spell.db.reference = 'M:tA p. 139-140'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Perfect_Recall')
spell.db.longname = 'Perfect Recall'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The subject is able to recall things from her past with vivid detail. For each level of Potency of the spell, the subject can recall one memory with perfect accuracy. She can remember the exact size, smell, weight, and words written on a piece of paper. She can recall the exact details of a conversation, including bits that she wasn\'t consciously concentrating on, such as what kind of suit someone was wearing, or the smell of his cologne.'
spell.db.reference = 'M:tA p. 160'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Perfect_Sympathy')
spell.db.longname = 'Perfect Sympathy'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 3'
spell.db.info = 'To possess true Sympathy toward something is to be nearly indistinguishable from it. With this spell, the subject becomes so like those with whom she has sympathy that she finds it trivial to predict them. When the subject takes an action whose subject is one of her Strong sympathetic connections (e.g. social interaction, guessing what he\'ll do in a certain situation, etc.), she gains 8-Again on her roll.'
spell.db.reference = 'M:tA p. 176-177'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Perfect_Timing')
spell.db.longname = 'Perfect Timing'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage knows just the perfect time to act, whether it\'s with a kind (or condemning) word, a punch, or even simply slipping out a door at the right time. This spell does not directly alter time or affect others, but rather grants the subject a perfect temporal assessment of the situation. Others might describe her as "in the zone," mistaking her preternatural sense of timing for incredible focus.'
spell.db.reference = 'M:tA p. 187'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Pierce_Deception')
spell.db.longname = 'Pierce Deception'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Prime is the Arcanum of pure Truth, and no falsehood may stand before it. By means of this spell, the subject sees illusions, phantasms, and lies for what they are. The spell sees through mundane falsehoods the subject perceives automatically; magical illusion or deception automatically provokes a Clash of Wills.'
spell.db.reference = 'M:tA p. 165'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Piercing_Earth')
spell.db.longname = 'Piercing Earth'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 4'
spell.db.info = 'Much like Windstrike (see p. 157), this spell causes inanimate matter to lash out at the subject. But where Windstrike lashes out with air and water, this spell causes the Earth itself to rise up and crush the subject. This is an attack spell; its damage rating is equal to the spell\'s Potency, and it inflicts lethal damage.'
spell.db.reference = 'M:tA p. 158'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Place_of_Power')
spell.db.longname = 'Place of Power'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 3'
spell.db.info = 'Even the mightiest shaman needs a place to sleep safely, and a place to do her workings where the wall between worlds is thin. This spell allows the mage to either raise or lower the local Gauntlet Strength by an amount equal to the spell\'s Potency within the spell\'s Area.'
spell.db.reference = 'M:tA p. 182'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Platonic_Form')
spell.db.longname = 'Platonic Form'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage may pattern Mana into behaving as it does within tass, creating a magical object formed of pure Mana. The object must be a simple object or tool (swords and gemstones are allowable, guns and cars are not). It is obviously magical to onlookers, has a default Durability of 1 and consists of one point of Mana (which the mage must pay as part of the casting). Potency may be allocated to the following effects:'
spell.db.reference = 'M:tA p. 169'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Pocket_Dimension')
spell.db.longname = 'Pocket Dimension'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage creates a space outside of space, one ideally suited to serve as a sanctum - or a prison. Without the addition of other Arcana, this space is devoid of any identifiable features, dimensions, or boundaries. It has no Time, so anything within it is held in stasis, unaging (but also unhealing and never growing or improving). It has no Death or Spirit, so Twilight doesn\'t exist within it. It is, in essence, a space whose only definition is that it is a space. Someone within the dimension can walk forever in any direction, but when she turns back she finds herself only as far as the boundary of the spell\'s Area Factor.'
spell.db.reference = 'M:tA p. 178-179'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Possession')
spell.db.longname = 'Possession'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage can send her consciousness into the subject and take possession of his body. The mage takes control of the subject, imposing the Possessed Condition (see p. 261). While possessing the subject, the mage uses the rules for possession as an ephemeral entity, with the following changes. She may use any of her Mind spells on the subject to read his mind, and she may spend a point of Mana to use her own Mental and Social Attributes instead of the host\'s Attributes. She must always use her subject\'s Physical Attributes, but may spend a point of Mana to reduce the –3 penalty on Physical actions to 0. While possessing the subject, her body is comatose as with "Psychic Projection", below.'
spell.db.reference = 'M:tA p. 164'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Postcognition')
spell.db.longname = 'Postcognition'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can see into the past of a subject, witnessing events as though she were physically present to view them. By default, the caster may only view Unchanged subjects, but with Time ** she may view the more distant past, in which case the spell is Withstood by temporal sympathy.'
spell.db.reference = 'M:tA p. 187'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Present_as_Past')
spell.db.longname = 'Present as Past'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 4'
spell.db.info = 'Weaving between the many immediate potential futures, the mage can read the immediate futures of her subjects and react accordingly to thwart (or aid) their plans. In combat, while this spell is in effect, the player can require that every character affected by the spell declare his or her action at the start of every turn. The player need not declare her own action, but instead can choose to act freely at any point within the Initiative order. This trumps all other supernatural Initiative effects save for those created by the Time Arcanum, which requires a Clash of Wills.'
spell.db.reference = 'M:tA p. 190'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Prophecy')
spell.db.longname = 'Prophecy'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage causes the future to conform to her expectations, building a hypothetical scenario she can then examine for knowledge about how to alter the future drastically, whether to ensure or avert a specific event. This works like "Divination," p. 186, but the mage can ask specific questions and also gains answers about things that might come to pass, depending on variables like choice or outside chance. For example, she could ask whether calling her ex will lead to reconciliation if she makes the attempt, or whether killing a man might set his son down a road to revenge. She can ask one such question per level of Potency and receive a detailed answer that accounts for hypothetical events. Other mages using Divination on the same subject while Prophecy is in effect see the most likely outcome of the scenario set by this spell.'
spell.db.reference = 'M:tA p. 190'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Psychic_Assault')
spell.db.longname = 'Psychic Assault'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 3'
spell.db.info = 'A living mind is a delicate thing, easily broken. This spell forces the subject\'s brain into a dangerously overactive state, mimicking the effects of a stroke. The subject takes bashing damage equal to Potency.'
spell.db.reference = 'M:tA p. 162'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Psychic_Domination')
spell.db.longname = 'Psychic Domination'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage employs limited telepathic projections. She can send simple commands through thoughts and emotions to her subject through a mental link, but not full sentences or complex ideas. The ideas form urges and desires within the subject that he is compelled to act upon even against his will as long as the spell remains active. The commands must be simple, one-word orders - such as to sleep, eat, sit, or defend. The intention of the command is sent to the subject along with the thoughts and emotions.'
spell.db.reference = 'M:tA p. 161'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Psychic_Genesis')
spell.db.longname = 'Psychic Genesis'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage creates a consciousness as a self-aware intelligence with a Twilight presence. The consciousness gains traits as a Rank 1 Goetia. The consciousness remains for the Duration of the spell as the mage\'s loyal servant, and she is able to direct it to complete tasks without the use of any additional spells.'
spell.db.reference = 'M:tA p. 165'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Psychic_Projection')
spell.db.longname = 'Psychic Projection'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage can project the subject\'s consciousness into a state of Twilight or into another\'s dreams. The mental projection uses the rules for Dream Forms in Chapter Six (p. 249). It has no ephemeral body, but is instead an incorporeal, intangible mental image. While in Twilight, the subject cannot interact physically with her surroundings, and must use magic to affect anything. She is immune to physical attacks, but she is still susceptible to mind-affecting supernatural abilities. While mentally projected, her body lies in a comatose state, and she has no way of knowing its health or state without returning or the use of other magic. If her projection dies, she returns to her body with the Soul Shocked Condition.'
spell.db.reference = 'M:tA p. 164'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Psychic_Reprogramming')
spell.db.longname = 'Psychic Reprogramming'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage rewrites the subject\'s personality, changing the very essence of who she is. The mage may change one of the following aspects of the subject for each Potency of the spell: Virtue, Vice, Short-Term Aspiration, Long-Term Aspiration, Obsession, a non-Physical Persistent Condition, or may move one dot between two Social Skills, or between two Mental Skills.'
spell.db.reference = 'M:tA p. 164'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Purge_Illness')
spell.db.longname = 'Purge Illness'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 2'
spell.db.info = 'A mage with this spell can purge her subject\'s body of diseases. Compare Potency to the severity level of the infirmity (p. 223). If Potency is less than the illness\' rating, reduce it by the difference, and if greater, the spell eliminates the illness from the subject entirely.'
spell.db.reference = 'M:tA p. 149-150'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Quantum_Flux')
spell.db.longname = 'Quantum Flux'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage reads probability and compensates for deleterious factors, attracting small turns of good fortune to negate unfortunate obstacles that stand in her way. This negates penalties to any of the subject\'s actions equal to Potency for a number of actions during the Duration equal to Potency.'
spell.db.reference = 'M:tA p. 135'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Quarantine')
spell.db.longname = 'Quarantine'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 5'
spell.db.info = 'This spell excises a subject from Space altogether, removing all paths from it to the rest of the world and vice versa. For all intents and purposes, the subject simply ceases to exist and reality "fills in" to adjust. A Quarantined house doesn\'t leave behind an empty lot; rather, its two neighboring houses suddenly find themselves adjacent. A building with a Quarantined 12th floor appears to only have 11 stories - though the elevator has a "12" button, it doesn\'t do anything.'
spell.db.reference = 'M:tA p. 179'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Quicken_Corpse')
spell.db.longname = 'Quicken Corpse'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The caster can animate a corpse, creating a loyal zombie servant. A zombie has limited mental capacity, and can understand simple one- or two-word commands and nothing more. It is a mindless, soulless construct immune to fear, pain, exhaustion, intimidation, or coercion, and follows the creator\'s orders with no regard to self. The corpse\'s physical capabilities are impaired, making them slow and clumsy compared to a living person. The constructs are not suited for combat (and have no Defense), but count as Retainers worth dots equal to the spell\'s Potency with a "field" relating to the mage\'s commands. Zombies have as much Health as the living creature their corpse came from had, but suffer damage as though they are under the effects of Death Mage Armor. They do not fall unconscious through damage, or bleed when filled with lethal damage, and are only destroyed when their last Health box is filled with aggravated damage.'
spell.db.reference = 'M:tA p. 131'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Quicken_Ghost')
spell.db.longname = 'Quicken Ghost'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage bolsters a ghost, making low-Ranked ghosts more powerful and aware than they once were. Each level of Potency raises one of the ghost\'s three Attributes by one, not to exceed its Rank maximum. The mage can instead use the spell to heal a ghost\'s Corpus at a rate of one point per Potency of the spell.'
spell.db.reference = 'M:tA p. 131-132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Reaching')
spell.db.longname = 'Reaching'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The Spirit mage is a being of two worlds. With this spell, the mage may interact physically and magically with things on the far side of the Gauntlet, whichever realm she is in.'
spell.db.reference = 'M:tA p. 182'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Read_the_Depths')
spell.db.longname = 'Read the Depths'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage may telepathically enter her subject\'s subconscious. She may pull memories and ideas out of the subject\'s subconscious, instead of just reading surface thoughts (see "Telepathy").'
spell.db.reference = 'M:tA p. 162-163'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Reading_the_Outmost_Eddies')
spell.db.longname = 'Reading the Outmost Eddies'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 1'
spell.db.info = 'This spell bestows a small blessing or curse that attracts good or bad fortune to its subject. As long as the spell remains active the subject experiences an event within the next 24 hours, such as finding $20 or dropping his wallet in a puddle. The mage can exert limited control over the nature of the fortune (or misfortune), but ultimately fate decides the detail'
spell.db.reference = 'M:tA p. 135'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Receiver')
spell.db.longname = 'Receiver'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Casting this spell allows the mage to hear infrasound and ultrasound frequencies beyond what human ears can normally perceive. While active, she can hear sounds outside the normal frequency, from high-frequency (dog whistles, sonar) to low-frequency (the distant rumble of diesel engines, industrial sounds normally lost to humans in the noise). Apply the spell\'s Potency as a dice bonus to relevant dice pools, such as rolls to avoid ambush.'
spell.db.reference = 'M:tA p. 141'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Regeneration')
spell.db.longname = 'Regeneration'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 4'
spell.db.info = 'Life magic can regenerate lost organs, limbs, repair fire-scarred tissue, and restore function to dead tissues, provided the subject is still alive when the spell is cast. This spell can even cure brain damage, infertility, and birth defects. Potency determines the extent of the organs that may be regenerated. Affected body parts regenerate (growing from nothing if the limb or organ has been completely removed) at a rate of about one minute per level of Potency required.'
spell.db.reference = 'M:tA p. 152'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Remote_Control')
spell.db.longname = 'Remote Control'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 1'
spell.db.info = 'With the commanding power of Stygia, the subject can control any mechanical object, making it fulfill its function. She might flip a light switch, cause an industrial press to slam downward, or shift a car into gear. Anything that\'s within the bounds of a single instant action, and which the subject device is capable of performing, is fair game. Should the action require a Skill roll, treat the spell\'s Potency as its successes.'
spell.db.reference = 'M:tA p. 155'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Rend_Friction')
spell.db.longname = 'Rend Friction'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage alters the level of friction upon a target. She can increase it to the point where simple air friction shears the target to pieces, or lower it so much that an object can continue moving almost indefinitely.'
spell.db.reference = 'M:tA p. 145-146'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Rend_Lifespan')
spell.db.longname = 'Rend Lifespan'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage can cause parts of a target\'s body to age rapidly and others to regress in development. The effects are temporary but devastating, inflicting lethal damage equal to the spell\'s Potency. Targets killed by this spell often appear to have "died of old age," despite their apparent age. At the Storyteller\'s discretion, undead beings like vampires and ghosts may be immune to this spell.'
spell.db.reference = 'M:tA p. 190'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Revenant')
spell.db.longname = 'Revenant'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage may grant a ghost a Manifestation Condition (see p. 258). The mage may grant a number of Conditions equal to the spell\'s Potency, and must create any prerequisite Conditions as well, if they aren\'t already present. The entity immediately enters the Manifestation of the mage\'s choice, and may not leave it while the spell remains in effect. Mages often use this spell to allow ghosts to Possess their own corpses, creating undead beings called revenants.'
spell.db.reference = 'M:tA p. 132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Rewrite_History')
spell.db.longname = 'Rewrite History'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 4'
spell.db.info = 'Reaching back through time, the mage warps her subject\'s timeline, making her present self as though her life took a very different course. This spell allows the mage to rewrite a subject\'s history, choosing a point of divergence on his timeline and specifying changes from there. Without Temporal Sympathy, only recent decisions and changes can be rewritten, but as long as the subject is Unchanged at the point of divergence, the mage may make alterations as she wishes. With Temporal Sympathy, the spell is capable of changing every detail of a subject\'s history, though the false timeline created must still be possible.'
spell.db.reference = 'M:tA p. 190-191'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Rotting_Flesh')
spell.db.longname = 'Rotting Flesh'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage\'s touch rots away at her subject, causing his flesh and bones to wither and decay. Each level of Potency deals one point of bashing damage to the subject.'
spell.db.reference = 'M:tA p. 132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Rouse_Spirit')
spell.db.longname = 'Rouse Spirit'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 3'
spell.db.info = 'What slumbers can always be awoken. This spell can also rouse a hibernating spirit prematurely. The Potency required for this effect is the difference between the spirit\'s current Essence and its total Corpus. The spirit awakens immediately, with only its rightmost Corpus box cleared.'
spell.db.reference = 'M:tA p. 182'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Sacred_Geometry')
spell.db.longname = 'Sacred Geometry'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 1'
spell.db.info = 'While her senses are open to this spell, the subject can clearly perceive ley lines and nodes. Depending on the caster\'s Path and Nimbus, she might see them as beams of golden light meeting at shining Platonic solids, electric-blue rivers pooling into lakes, or strains of music building into a mighty symphony. If there are no ley lines or nodes within sensory range, the subject feels a tugging sensation toward the nearest ley or node.'
spell.db.reference = 'M:tA p. 166'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Salt_the_Earth')
spell.db.longname = 'Salt the Earth'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 5'
spell.db.info = 'This destructive spell rips the very life-force from an area or an individual, rendering it incapable of sustaining life. Plants, animals, and even fungi in the area die. The use of this spell even temporarily halts decomposition in an area based upon microbial breakdown of dead cells, as it kills all microscopic organisms as well. Finally, the spell prevents anything affected from becoming fertilized, though existing pregnancies stay if the organism survives. The spell creates an Extreme Environment effect equal to Potency.'
spell.db.reference = 'M:tA p. 153'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Scribe_Grimoire')
spell.db.longname = 'Scribe Grimoire'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 1'
spell.db.info = 'By means of this spell, the mage gives physical form to the mudras of a particular Rote, creating a Grimoire (see p. 101). This spell has two slightly different, albeit related, applications: The mage may either inscribe a Rote she knows, or she may copy a Rote from another Grimoire she has on hand.'
spell.db.reference = 'M:tA p. 166'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Scrying')
spell.db.longname = 'Scrying'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 2'
spell.db.info = 'By means of this spell, the mage parts the curtain of the Lie and reveals a distant location to her senses. She creates a "window" that allows her to perceive the subject, much like a television screen. When she casts the spell, she may choose whether the spell is one way, or whether people at the location can see back through the window.'
spell.db.reference = 'M:tA p. 174-175'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Secret_Door')
spell.db.longname = 'Secret Door'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 2'
spell.db.info = 'Doorways, roads, and portals represent a liminal point between two distinct locations - but if distance is an illusion, there can be no "distinct locations." This spell cloaks a door, intersection, or similar aperture between two locations, such that one\'s mundane perceptions simply slide ride past it. All magical attempts to uncover the door provoke a Clash of Wills.'
spell.db.reference = 'M:tA p. 175'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Secret_Room')
spell.db.longname = 'Secret Room'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 4'
spell.db.info = 'Volume is a product of dimension, and dimension is merely an expression of distance in three dimensions. This spell allows the mage to manipulate those axes, making a space much larger or smaller than should be possible. A cramped studio apartment can become a spacious loft, or a town square can be made the size of a closet. Subjects crushed by a shrinking space too small for them take lethal damage equal to the spell\'s Potency and are forcibly ejected from the space.'
spell.db.reference = 'M:tA p. 178'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Self-Repairing_Machine')
spell.db.longname = 'Self-Repairing Machine'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 5'
spell.db.info = 'This spell imbues an object with a small semblance of life - specifically, the ability to repair itself. As long as the spell lasts, the object heals (Potency) Structure every day.'
spell.db.reference = 'M:tA p. 159'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Serendipity')
spell.db.longname = 'Serendipity'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 1'
spell.db.info = 'This spell grants the mage a momentary glimpse of all the potential roads her destiny may follow to her desired destination, which allows the mage to identify the next step she must take to accomplish a stated objective. Upon casting, the mage receives a clear omen that suggests a course of action that will lead her closer to her goal. This seldom guarantees immediate success, especially if the task before her is complicated, but can provide an important breakthrough.'
spell.db.reference = 'M:tA p. 135'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Sever_Oaths')
spell.db.longname = 'Sever Oaths'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 4'
spell.db.info = 'To an Adept of Fate, all fetters on a being\'s free will are ultimately breakable, and oaths can be renegotiated. The mage may apply a number of the following effects equal to Potency'
spell.db.reference = 'M:tA p. 138-139'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Sever_Soul')
spell.db.longname = 'Sever Soul'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage rips the soul from a Sleeper, casting it into Twilight. While without a soul, the subject suffers from the Soulless Condition (p. 318). When the spell\'s Duration ends, the Sleeper\'s soul returns to him, unless otherwise prevented from escape, such as the case of being trapped in a soul jar or inside another body (see "Soul Jar" p. 129). If this spell is cast on a subject who is already under the effects of the Soulless Condition, he is stepped up to the Enervated Condition (p. 315) - though the mage does not gain immediate access to his soul, since it is already missing.'
spell.db.reference = 'M:tA p. 132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Sever_the_Awakened_Soul')
spell.db.longname = 'Sever the Awakened Soul'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The soul of a mage cannot be removed with Fraying alone; Awakened Gnosis holds it tight, requiring mastery to prise lose. This spell Unmakes the protective metaphysical layers of a mage\'s soul, ripping it free and placing it into a container. That container can either be a specially prepared vessel such as one created with "Soul Jar," or the caster can take the soul into her own body. While without a soul, the subject suffers from the Soulless Condition. If this spell is cast on a subject who is already under the effects of the Soulless Condition, he is stepped up to the Enervated Condition - though the mage does not gain immediate access to his soul, since it is already missing.'
spell.db.reference = 'M:tA p. 133-134'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Shadow_Crafting')
spell.db.longname = 'Shadow Crafting'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The caster can shape and harden shadows into solid, three-dimensional forms. The object gains a Durability of 2. If it is a weapon it gains a weapon rating of 2; if it is armor it gains an armor rating of 2; otherwise the object gains a +2 equipment bonus. Objects made of shadow retain a shadowy appearance and cast no shadow of their own.'
spell.db.reference = 'M:tA p. 132'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Shadow_Flesh')
spell.db.longname = 'Shadow Flesh'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage transforms the subject\'s body and all her personal possessions into a mass of moving and animated shadows. The mage may choose to make the subject a three-dimensional or a two-dimensional shadow. Three-dimensional shadows still have no apparent mass or substance, and cannot interact with physical objects. Two-dimensional shadows may move through cracks and crevices, though are still bound by the laws of gravity and must remain touching the floor, even if moving on walls.'
spell.db.reference = 'M:tA p. 132-133'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Shadow_Scream')
spell.db.longname = 'Shadow Scream'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage calls forth a writhing torrent of ephemera, raw Essence, and half-formed spirits, which tears into her foes with gleeful abandon. This is an attack spell; its damage rating is equal to the spell\'s Potency, and it inflicts lethal damage. This spell can target physical beings or spirits in Twilight.'
spell.db.reference = 'M:tA p. 183-184'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Shadow_Sculpting')
spell.db.longname = 'Shadow Sculpting'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can mold and shape the shadows in the area of effect. He can shape the shadows into any likeness of his choosing. The area must have shadows present for the mage to shape them.'
spell.db.reference = 'M:tA p. 128'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Shadow_Walk')
spell.db.longname = 'Shadow Walk'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 2'
spell.db.info = 'Sometimes the lords of shadow must walk unseen among their prey. This spell shrouds the subject from the notice of spirits and Spirit magic. Any supernatural effect that would detect her provokes a Clash of Wills.'
spell.db.reference = 'M:tA p. 181'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Shape_Ephemera')
spell.db.longname = 'Shape Ephemera'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The caster may reshape Death-attuned ephemera from one object into a new object entirely. This ephemera can be from a ghost or other entity in Twilight, but they have the ability to Withstand the spell, and being reshaped does not damage the entity\'s Corpus.'
spell.db.reference = 'M:tA p. 129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Shape_Spirit')
spell.db.longname = 'Shape Spirit'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 4'
spell.db.info = 'When no tool is ready to hand, the shaman shapes one from what is available. This spell allows the mage to reshape a spirit\'s fundamental nature. She may invoke a number of the following effects equal to the spell\'s Potency:'
spell.db.reference = 'M:tA p. 184'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Shapechanging')
spell.db.longname = 'Shapechanging'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage (or her subject) can fully take on the form of another creature. While the spell can greatly transform its subject\'s Size, changing into much larger forms is difficult. The Scale factor of the spell must cover the larger of the Size traits, before and after the transformation.'
spell.db.reference = 'M:tA p. 152-153'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Shaping')
spell.db.longname = 'Shaping'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 2'
spell.db.info = 'Liquids, gases, and amorphous solids are the mage\'s playthings with this spell. She can shape them into any form she desires, manipulating them in defiance of gravity, for as long as the spell lasts. This spell cannot change the state of matter (e.g. from solid to liquid), but substances that have been temporarily transformed into shapeable states by magic may be affected. Particularly intricate shapes may require a reflexive Wits + Crafts roll, at the Storyteller\'s discretion.'
spell.db.reference = 'M:tA p. 156'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Shared_Fate')
spell.db.longname = 'Shared Fate'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 3'
spell.db.info = 'Fate is an instrument of both justice and punishment. This spell braids the fates of two subjects together. Whatever befalls one subject affects the other.'
spell.db.reference = 'M:tA p. 137'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Shield_of_Chronos')
spell.db.longname = 'Shield of Chronos'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage shields a subject against temporal senses. While under the protection of this spell, any magic viewing the subject through time (whether looking at the shielded Duration from the future, or predicting the subject\'s future while in the present) provokes a Clash of Wills.'
spell.db.reference = 'M:tA p. 188'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Shifting_Sands')
spell.db.longname = 'Shifting Sands'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage may step back through time a short distance, undoing a few precious seconds. This spell sends the subject back through time a number of turns equal to Potency. The subject retains any injuries and Conditions gained in the undone turns, and spent Mana and Willpower do not return. Spells cast on her person in the undone time remain as long as she cast them. All other spells she may have cast or had cast on her in the intervening time are canceled. Until the subject catches up to the present, the distortion caused by this spell is visible under Active Time Mage Sight. Once she does so, any changes she made to history become Lasting.'
spell.db.reference = 'M:tA p. 189'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Shifting_the_Odds')
spell.db.longname = 'Shifting the Odds'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 2'
spell.db.info = 'An Apprentice of Fate always has access to what she needs at the moment. The mage focuses on locating a particular kind of person, place, or thing, and this spell directs her steps to it unerringly as soon as possible within the next 24 hours as long as the spell remains active. Casting the spell looking for a kind of person in a crowd or an item anywhere it could appear is usually enough to immediately succeed.'
spell.db.reference = 'M:tA p. 136'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Shrink_and_Grow')
spell.db.longname = 'Shrink and Grow'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 3'
spell.db.info = 'By means of this spell, the mage may bring an object\'s Supernal reflection closer to the world or push it farther away. This in turn causes the Supernal to cast a larger or smaller shadow into the Fallen World, effectively making the object grow or shrink. Each level of Potency either adds or subtracts one from the subject\'s Size. Size 0 objects can be shrunk down to roughly the size of a dime.'
spell.db.reference = 'M:tA p. 157'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Sleep_of_the_Just')
spell.db.longname = 'Sleep of the Just'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage controls the subject\'s sleep cycle, allowing her to remain awake without ill effects or asleep without being roused for the spell\'s Duration. The mage may also control what she dreams about, or create a lucid dreaming state where the subject has control. Anything attempting to enter or influence the dream state provokes a Clash of Wills.'
spell.db.reference = 'M:tA p. 162'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Slumber')
spell.db.longname = 'Slumber'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 2'
spell.db.info = 'A fool exhausts herself trying to kill what cannot die; better to send hostile spirits into a deep sleep. This spell reduces the frequency with which a spirit that is hibernating after being destroyed (see p. 257) regains Essence. Instead of regaining one point of Essence per day, it regains one point of Essence every (Potency) days; but the effect still ends when the spell\'s Duration expires.'
spell.db.reference = 'M:tA p. 181'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Social_Networking')
spell.db.longname = 'Social Networking'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage creates social networks where none existed before. For each level of Potency, the subject gains one dot in one of the following Merits: Allies, Contacts, or Status.'
spell.db.reference = 'M:tA p. 165'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Soul_Armor')
spell.db.longname = 'Soul Armor'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'This spell armors the subject\'s soul against all who would profane it. Any spell or effect that would remove, manipulate, or injure the subject\'s soul must first win a Clash of Wills.'
spell.db.reference = 'M:tA p. 129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Soul_Jar')
spell.db.longname = 'Soul Jar'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage creates a receptacle for a displaced soul. The soul jar can be anything designed to hold and seal a liquid, from a paint can to a water bottle. A soul placed into the soul jar cannot escape and is protected from outside attack. If the jar is opened or broken before the Duration of the spell ends, the soul is released.'
spell.db.reference = 'M:tA p. 129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Soul_Marks')
spell.db.longname = 'Soul Marks'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage can determine the health of a person\'s soul. She can determine one soul mark per Potency of the spell cast. She can discern the presence of Persistent Conditions, if the subject is Awakened, if the subject is a supernatural being, if the subject has created a soul stone (see "Soul Stones" p. 98), if the subject has had her soul tampered with, if the subject is Possessed, the presence of any Gnosis 5+ Legacy Attainments, if the subject has eaten or otherwise consumed another\'s soul, or if the subject is suffering from a Paradox Condition.'
spell.db.reference = 'M:tA p. 128'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Speak_with_Beasts')
spell.db.longname = 'Speak with Beasts'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The subject gains the ability to "speak" to any specimens of an animal specified by the mage during casting. She usually speaks to it by making noises similar to its own sounds, but this is not necessary; the subject can speak in her own language and the magic "translates" her words for her. This does not grant her any capability to control a creature, only to understand and be understood by it. Animals have limited ability to understand things that transpire around them, especially as pertains to humans, but the subject gains a bonus to any Animal Ken rolls made with that animal equal to the spell\'s Potency. A bird may not understand just why the people went into the house across the street last night, for example, but it could give a general estimate of their number and unusual features like being covered in tattoos ("skin patterns").'
spell.db.reference = 'M:tA p. 148'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Speak_with_the_Dead')
spell.db.longname = 'Speak with the Dead'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 1'
spell.db.info = 'The mage is able to sense and communicate with ghosts within Twilight. She can sense all ghosts within the area of effect, and is capable of communicating with them by simply talking, as long as the ghost is capable of understanding a language she speaks. She may sense Anchors within the area without using Death Mage Sight. She can concentrate on a single ghost within the area and determine its Rank, if it has an Anchor, and how many Anchors it has.'
spell.db.reference = 'M:tA p. 128-129'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Spirit_Manse')
spell.db.longname = 'Spirit Manse'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The master lives among her shadow brethren in a palace of her will. This spell carves out an extradimensional space in the Shadow, one of the fabled "Places That Aren\'t" that doesn\'t map to any location in the physical world. The Spirit Manse can take any form the mage desires, but its appearance is heavily colored by her Path and her Nimbus. As long as the spell\'s Duration lasts, the mage gains the Safe Place Merit at a rating equal to the spell\'s Potency.'
spell.db.reference = 'M:tA p. 185'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Spirit_Summons')
spell.db.longname = 'Spirit Summons'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage sends out a call to the nearest spirit within her sensory range. Conversely she can summon spirits she knows personally. She may send a general call and the nearest spirit will answer, or she can specify the type of spirit by Resonance. The spell does not work on spirits above Rank 5.'
spell.db.reference = 'M:tA p. 182'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'State_Change')
spell.db.longname = 'State Change'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage can transmute any inorganic material one "step" along the path from solid to liquid to gas. This magically-induced state change does not change the material\'s temperature: liquefied steel remains as cool to the touch as if it were solid, and vaporized ice is still freezing cold. Transforming a liquid or gas into a solid gives the new object a Durability equal to the spell\'s Potency; Structure is determined as Durability + Size.'
spell.db.reference = 'M:tA p. 157'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Stealing_Fire')
spell.db.longname = 'Stealing Fire'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 3'
spell.db.info = 'Prometheus brought fire from Olympus to the mortal realm. By means of this spell, the mage brings a tiny fragment of Supernal fire to the sleeping masses, if only for a time. The subject of this spell, who must be a Sleeper, temporarily becomes a Sleepwalker (see p. 303) with all that entails. Any breaking points due to witnessing magic and Quiescence effects the subject would normally suffer are held in abeyance until the spell\'s Duration expires, only to come crashing down all at once when the spell ends.'
spell.db.reference = 'M:tA p. 169'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Strings_of_Fate')
spell.db.longname = 'Strings of Fate'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The roads of destiny fork and converge, governing the probability of events. An adept of Fate can re-weave the strings of Fate on a subject, encouraging (if not ensuring) that a specified event will happen as long as the spell remains active.'
spell.db.reference = 'M:tA p. 138'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Superlative_Luck')
spell.db.longname = 'Superlative Luck'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage can ensure success at virtually any task he sets out to accomplish.'
spell.db.reference = 'M:tA p. 137'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Supernal_Dispellation')
spell.db.longname = 'Supernal Dispellation'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 4'
spell.db.info = 'Supernal truths can never truly be unmade, but with this spell the mage may cast them back across the Abyss, effectively erasing any spell she comes across. This spell is not potent enough to dispel archmages\' spells.'
spell.db.reference = 'M:tA p. 170'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Supernal_Veil')
spell.db.longname = 'Supernal Veil'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 2'
spell.db.info = 'Sometimes even the greatest magician must hide her light under a bushel. This spell wards its subject, which can be a spell, object, mage, supernatural creature, or any other active magical phenomenon, from detection. Passive abilities (such as Peripheral Mage Sight) automatically fail to detect the veiled phenomenon, while active attempts provoke a Clash of Wills.'
spell.db.reference = 'M:tA p. 168'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Supernal_Vision')
spell.db.longname = 'Supernal Vision'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 1'
spell.db.info = 'By opening her subject\'s third eye, the mage reveals her fellows as the wells of Supernal power they are. By studying a person, place, or location for one turn, the subject automatically knows whether it is connected to the Supernal (e.g. if a person is a mage, a Sleepwalker, a Proximus, or a Sleeper; if a place is a Demesne or Verge; if an object is Imbued, Enhanced, or an Artifact), and may ask a number of the following questions equal to the spell\'s Potency:'
spell.db.reference = 'M:tA p. 166'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Suppress_Aura')
spell.db.longname = 'Suppress Aura'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage suppresses the personal aura of her subject. The subject\'s Nimbus disappears and magical resonances around her are dampened, including the resonances of spells currently affecting her. She appears as a Sleeper to Mage Sight. She is harder to read in general, imposing a -2 penalty on Empathy checks, and supernatural attempts to discern her emotional or mental state. Magical attempts to see through the disguise provoke a Clash of Wills.'
spell.db.reference = 'M:tA p. 129-130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Suppress_Life')
spell.db.longname = 'Suppress Life'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can suppress the subject\'s life signs; the subject appears for all intents and purposes as though she is dead. All physical symptoms of death appear to set in and the soul appears absent from the body to magical senses.'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Swarm_of_Locusts')
spell.db.longname = 'Swarm of Locusts'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage creates chaotic conditions: rains of frogs, swarms of locusts, unscheduled total solar eclipses, and other similarly "Fortean" occurrences. This terrifying and obviously supernatural event wreaks havoc in the area, creating Environmental Tilts of the player\'s choosing.'
spell.db.reference = 'M:tA p. 140'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Sworn_Oaths')
spell.db.longname = 'Sworn Oaths'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage can witness a sworn oath and ensure that Fate itself enforces the subject\'s adherence to her vow. The subject makes a promise and states the consequences for herself if she violates the agreement. No one can be forced to take such an oath, although a subject may be placed under oath unwittingly if he voluntarily makes a vow and verbally agrees to a specified consequence, even if he doesn\'t realize the mage can enforce the oath supernaturally.'
spell.db.reference = 'M:tA p. 137'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Telekinesis')
spell.db.longname = 'Telekinesis'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage can conjure telekinetic force to lift or manipulate an object remotely. Apply the spell\'s Potency to one of the force\'s Strength (raw lifting/pushing power), Dexterity (fine manipulation), or Speed. The other two default to 1. Moving objects using Telekinesis requires concentration as an instant action each turn; if the mage fails to concentrate on moving the force, it simply hangs suspended, holding any objects it held before but no longer pushing or pulling (or manipulating objects, if used for that). The mage may then resume directing the telekinetic force until the spell\'s Duration expires.'
spell.db.reference = 'M:tA p. 144'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Telekinetic_Strike')
spell.db.longname = 'Telekinetic Strike'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage manipulates kinetic forces to crush subjects or form a "ball" of highly pressurized air and kinetic energy that she can hurl at foes. The spell inflicts bashing damage equal to its Potency.'
spell.db.reference = 'M:tA p. 145'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Telepathy')
spell.db.longname = 'Telepathy'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage synchronizes the surface thoughts of her subjects, making the surface thoughts of one play out in the mind of the others. Apply the spell\'s Potency as a bonus or penalty to relevant Skill rolls (such as Empathy or Subterfuge) between the subjects. Subjects who carefully think of a message may use the effect to communicate telepathically along the link; this may require a Composure + Empathy roll for subjects unused to the sensation.'
spell.db.reference = 'M:tA p. 161'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Teleportation')
spell.db.longname = 'Teleportation'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 4'
spell.db.info = 'By means of this spell, the mage transforms her subject\'s current location, effectively moving it from point to point without crossing the intervening space. She can, for example, summon a subject to her from anywhere in the world, banish someone to the outer reaches of Siberia, or teleport herself. By default, the subject\'s current location and destination must both be within sensory range, but the mage may employ the Sympathetic Range Attainment on one of them.'
spell.db.reference = 'M:tA p. 178'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Temporal_Pocket')
spell.db.longname = 'Temporal Pocket'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The mage grants her subject a gift of hours, Making extra time on her timeline. To the subject, the entire world appears to pause, frozen in time. After the subjective Duration factor of the spell, the subject rejoins the Fallen World\'s timeline and, to him, the universe immediately starts moving again.'
spell.db.reference = 'M:tA p. 191'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Temporal_Stutter')
spell.db.longname = 'Temporal Stutter'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 4'
spell.db.info = 'By redefining how a subject\'s Time Pattern interacts with the present, the mage throws that subject forward through time, awaiting the moment the present catches up to him. The subject completely vanishes from the Fallen World, and reappears unchanged when the spell\'s Duration ends. The subject experiences a momentary lurch in his perceptions, and then suddenly finds his surroundings changed by intervening events. The subject remains in the same location and retains momentum if he had been moving. If something now occupies the space the subject reappears in, apply the Knocked Down Tilt to whichever has the least Size.'
spell.db.reference = 'M:tA p. 191'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Temporal_Summoning')
spell.db.longname = 'Temporal Summoning'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 3'
spell.db.info = 'We are all the sum of our previous selves, and with this spell a mage can call those afterimages forth. Cast upon an object, area, or living being, this spell replaces its subject with an earlier version of itself, chosen by the caster. Without the Temporal Sympathy Attainment, only Unchanged pasts may be brought to the present, but this is still sufficient to remove most Conditions and heal injuries. By employing Temporal Sympathy, the mage can restore ancient ruins to their inhabited state, recapture her youth, or return her enemies to childhood. When the spell\'s Duration ends, the subject immediately returns to its present self. Injuries, Conditions, and other effects imposed on the subject while Temporal Summoning is in effect transfer to the present version of the subject when it returns. The spell does have limits, however; it cannot bring the dead back to life or undo transformation into supernatural beings, though it still changes the subject physically - a vampire returned to "childhood" becomes a vampiric child, and a corpse stripped of decades becomes a younger-looking corpse with no cause of death.'
spell.db.reference = 'M:tA p. 189-190'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Terrorize')
spell.db.longname = 'Terrorize'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The spell provokes an overwhelming sense of fear and dread in its subject, draining his strength and will to live. The subject suffers from the Insensate Tilt for the Duration of the spell, or until the Tilt is resolved (for instance, by being attacked).'
spell.db.reference = 'M:tA p. 164'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'The_Outward_and_Inward_Eye')
spell.db.longname = 'The Outward and Inward Eye'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 1'
spell.db.info = 'If all locations are one, it must follow that all directions are one as well. While this spell is active, the subject can see and hear in all directions and from all points within her sensory range simultaneously. She can see what\'s happening behind her, on the far side of a door, or beneath her feet. She cannot perceive things farther away than her normal perceptions might allow, nor can she see through darkness. In essence, it\'s as though everything happening around her were spread out on a flat plain, bereft of obstruction. This allows her to cast sensory-range spells on subjects she might not ordinarily be able to perceive.'
spell.db.reference = 'M:tA p. 174'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Thunderbolt')
spell.db.longname = 'Thunderbolt'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage channels ambient energies as a weapon, pouring them into her subject. This spell deals lethal damage equal to its Potency.'
spell.db.reference = 'M:tA p. 146'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Tipping_the_Hourglass')
spell.db.longname = 'Tipping the Hourglass'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can momentarily alter the flow of Time, causing it to speed up or slow down for a subject, but not drastically. While the spell might allow the subject extra time to dodge an oncoming car or slow an enemy\'s movements as though he were drunk, it won\'t let her go back in time to avoid the car or the angry assailant entirely. The caster may add or subtract Potency from the subject\'s Initiative. Subjects who have already acted in a turn before having this spell cast upon them do not act again on their new Initiative rating.'
spell.db.reference = 'M:tA p. 188'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Touch_of_the_Grave')
spell.db.longname = 'Touch of the Grave'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can physically interact with ghosts and other things in Death-attuned Twilight. She can "pull" items from Twilight, making them visible and solid; these items have a Durability of 1 and dissipate into ephemera if broken, or after the spell\'s Duration ends. Items pulled from Twilight function as their material counterparts bestowing the same equipment bonuses.'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Transform_Energy')
spell.db.longname = 'Transform Energy'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 4'
spell.db.info = 'All energy shares sympathy, born perhaps from the same cosmic source in the same instant. An Adept of Forces can use that sympathy to transform one energy type into another. The table below serves as a rough equivalency chart for different energy types. She can change a room full of light into heat, at once turning it into a pitch-black oven. She might also change the thunderous roar of a waterfall into electricity, far more efficient than any hydroelectric dam. The spell may affect energy of a level equal to Potency.'
spell.db.reference = 'M:tA p. 146'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Transform_Life')
spell.db.longname = 'Transform Life'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage can transform life by giving it features normally exhibited by other organisms. She can grant herself claws or gills, change a harmless herbivore into a venom-spitting killer, or impart limbs and air-breathing lungs to a shark, among other changes. She may grant one feature per level of Potency. A transformed target instinctively knows how to use its new aspects to the best of its ability. The magic is capable of affecting even microscopic organisms, if the mage can perceive them, but for obvious reasons most microbes cannot benefit from aspects like armor, limbs, or senses. The mage can grant viruses and bacteria increased Toxicity, or the ability to replicate or survive in environments that might otherwise kill them.'
spell.db.reference = 'M:tA p. 150-151'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Transmission')
spell.db.longname = 'Transmission'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can hijack existing signals and change the transmitted data or its destination. She can shorten or lengthen the transmission, and even change frequency, such as turning a wifi broadcast into a television signal. At this level, she must still work with a signal already present. Mimicking specific sounds or information requires a Skill roll or access to the data to be transmitted.'
spell.db.reference = 'M:tA p. 144'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Transubstantiation')
spell.db.longname = 'Transubstantiation'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage can transmute any inert matter into any other form of inert matter: lead into gold, water into wine, wood into chlorine gas, etc. The purity and quality of the transmuted matter is determined by the spell\'s Potency: treat Potency as an equipment bonus or equivalent Resource Merit dots for a single purchase, whichever is appropriate. Both the initial substance and the transubstantiated substance must be relatively pure: Wood can be transformed into gold, but not into gold chased with silver. (The Stygian Mysteries teach that "purity" is a perceptual concept - so, for example, even though "wine" and "steel" are made up of numerous compounds, they are concrete enough as concepts to be transmuted).'
spell.db.reference = 'M:tA p. 158'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Tune_In')
spell.db.longname = 'Tune In'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 1'
spell.db.info = 'A mage with this spell can listen to free-floating data transmissions, such as those broadcast by radios, cell phones, wireless modems, and more. The magic translates this electromagnetic noise into something she can understand, although it preserves the original transmission language. With this spell, the mage needs no receiver to listen or even see signals. Transmitting cables glow before her eyes with streams of data, while she might see a shimmer or even fleeting glimpses of images in the air. Satellite internet and TV programming, closed walkie-talkies, CB broadcasts, and radio transmissions all become open to her senses, as well as wireless communications.'
spell.db.reference = 'M:tA p. 141'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Turn_Momentum')
spell.db.longname = 'Turn Momentum'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 3'
spell.db.info = 'This spell allows the mage to redirect a target\'s momentum. Usually this forms a shield against projectiles, but it can be used on larger objects, as well. When a mage could use her Defense against an object, she may use this spell instead to redirect it as an instant action. If cast with a prolonged Duration, the mage may take a Dodge action each turn and use this spell instead of receiving the normal benefits for Dodging.'
spell.db.reference = 'M:tA p. 145'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Twilit_Body')
spell.db.longname = 'Twilit Body'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 4'
spell.db.info = 'To go unnoticed, the tiger must sometimes change her stripes. This spell causes the subject (and anything she\'s wearing or carrying, if applicable) to turn into Spirit-attuned ephemera, placing her in Twilight.'
spell.db.reference = 'M:tA p. 184'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Universal_Language')
spell.db.longname = 'Universal Language'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mind\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The spell\'s subject is capable of understanding and translating any language. This is true for the spoken word, written language, symbols, encoded signals, body language, hand symbols, and concepts that only exist as thought. She must be able to perceive the language to understand it (for example, using telepathy for thoughts in another\'s mind). This spell does not allow non-Awakened characters to understand High Speech.'
spell.db.reference = 'M:tA p. 163'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Veil_Sympathy')
spell.db.longname = 'Veil Sympathy'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 2'
spell.db.info = 'A magician\'s sympathetic connections allow her to reach out beyond herself, but they are also an avenue by which her enemies can attack her. This spell conceals one of the subject\'s sympathetic links, chosen by the mage from those she is aware of. Any attempt to uncover or use the link provokes a Clash of Wills.'
spell.db.reference = 'M:tA p. 175-176'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Veil_of_Moments')
spell.db.longname = 'Veil of Moments'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage can ward off the deleterious effects of advancing time on her subject. This spell cannot undo effects, but can create enough of a buffer between the subject and Time\'s endless march to buy what a mage needs most - time to think.'
spell.db.reference = 'M:tA p. 188'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Velocity_Control')
spell.db.longname = 'Velocity Control'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage can greatly increase or decrease an object\'s velocity. Its speed doubles or halves for each level of the spell\'s Potency. For example, a car traveling 50 MPH is increased to 200 MPH with Potency 2, or an incredible 800 MPH with Potency 4. Likewise, if the mage reduces its speed, the same car would slow to about 13 MPH at Potency 2, or about 4 MPH with Potency 4. The mage must be able to affect the target\'s entire Size to affect it with this spell; she cannot target only the front tire of an 18-wheeler with its trailer (Size 30) and bring it to a stop.'
spell.db.reference = 'M:tA p. 145'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Ward')
spell.db.longname = 'Ward'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 2'
spell.db.info = 'Space is mutable, until a magician wills otherwise. Cast on an area or individual subjects, this spell locks its subject down, preventing the space within from being manipulated. Magic that uses the sympathy of Warded subjects or attempts to warp Warded areas provokes a Clash of Wills. The mage is aware when one of her Wards is attacked.'
spell.db.reference = 'M:tA p. 176'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Warding_Gesture')
spell.db.longname = 'Warding Gesture'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Fate\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage creates a ward protecting the subject against supernatural effects that manipulate her fate - a geas, a supernatural compulsion to act against her will, or having her fate manipulated by Fate magic or similar supernatural effects. Each attempt to change the subject\'s destiny provokes a Clash of Wills with the mage. This spell has no effect on pre-existing alterations to the subject\'s destiny.'
spell.db.reference = 'M:tA p. 136-137'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Wards_and_Signs')
spell.db.longname = 'Wards and Signs'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 2'
spell.db.info = 'By cloaking her subject in Aetheric symbols of victory and indomitability, the mage shields the subject from the effects of hostile magic. When the subject is the target of a spell, that spell is Withstood with the Potency of Wards and Signs.'
spell.db.reference = 'M:tA p. 168'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Warp')
spell.db.longname = 'Warp'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The mage twists the space her subject occupies, torquing joints, bruising flesh, and tearing muscle. This is an attack spell; its damage rating is equal to the spell\'s Potency, and it inflicts bashing damage.'
spell.db.reference = 'M:tA p. 177'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Web_of_Life')
spell.db.longname = 'Web of Life'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Life\',statclass=\'Arcana\') >= 1'
spell.db.info = 'By tapping into the pulse of the living world, the mage becomes keenly aware of any living things nearby. She feels their presence by the weight they exert upon the Tapestry, a gravity of the life-force that connects all creatures to the same great cycle. Because the unfiltered sensing of all life might provide a sensory overload, most mages specify certain types of life to detect, such as "humans, insects, and birds" or "only dogs."'
spell.db.reference = 'M:tA p. 148'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Web-Weaver')
spell.db.longname = 'Web-Weaver'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Space\',statclass=\'Arcana\') >= 3'
spell.db.info = 'We all leave tiny, nigh-imperceptible webs of sympathy behind us wherever we go. With this spell, the mage may bolster such a web into a useful sympathetic link. Each level of Potency bolsters a single sympathetic connection by one "step," from Weak to Medium, Medium to Strong. The mage can step up a nonexistent connection to a Weak one, but only if the subject of the spell has been in contact with the desired focus within the last turn. For example, a person likely has no sympathetic connection to the soda cup from her lunch, but as long as it\'s in her hand, the mage can use the faint sympathy created by physical contact to make the cup a sympathetic connection.'
spell.db.reference = 'M:tA p. 177'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Weight_of_Years')
spell.db.longname = 'Weight of Years'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Time\',statclass=\'Arcana\') >= 3'
spell.db.info = 'Structures decay, bodies age. Toxins build up in muscles, and materials become brittle. The mage can inflict these processes by Perfecting the passage of time on her subject. This is an attack spell, inflicting its Potency in damage to objects and structures. This damage directly affects the object\'s Structure, and reduces its Durability by 1 for every 2 points of Structure lost. When used against living things, the spell deals bashing damage equal to Potency. At the Storyteller\'s discretion, immortal creatures like vampires might be immune to the damaging properties of this spell.'
spell.db.reference = 'M:tA p. 190'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Windstrike')
spell.db.longname = 'Windstrike'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 3'
spell.db.info = 'The very air (or other fluid matter) strikes out against the mage\'s enemies. The wind buffets and strikes like a fist, or water lashes out like a whip. This is an attack spell; its damage rating is equal to the spell\'s Potency, and it inflicts bashing damage.'
spell.db.reference = 'M:tA p. 157'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Withering')
spell.db.longname = 'Withering'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The mage causes the subject\'s body to wither and atrophy within moments, dealing one point of lethal damage per level of Potency of the spell.'
spell.db.reference = 'M:tA p. 133'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Without_a_Trace')
spell.db.longname = 'Without a Trace'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Death\',statclass=\'Arcana\') >= 2'
spell.db.info = 'People constantly shed dead skin, hair, and other small evidences of themselves as they pass through the world. The mage conceals all physical evidence from casual observation. For the Duration of the spell, the subject leaves no fingerprints, footprints, traces of blood, or any other forensic type evidence of herself behind. Using Death Mage Sight to search for such signs provokes a Clash of Wills.'
spell.db.reference = 'M:tA p. 130'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Wonderful_Machine')
spell.db.longname = 'Wonderful Machine'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Matter\',statclass=\'Arcana\') >= 3'
spell.db.info = 'This spell allows a mage to swiftly superimpose pieces of various objects into one another in such a way as to produce a desired result. With this spell, a mage could, for example, integrate a nail-gun and shotgun together to produce a weapon that fires a barrage of nails with each pull of the trigger.'
spell.db.reference = 'M:tA p. 157-158'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Word_of_Command')
spell.db.longname = 'Word of Command'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 1'
spell.db.info = 'Enchanted objects and long-lasting spells often have specific triggers or conditions that must be fulfilled before they will release their magic. With this spell, a mage can bypass those conditions, freeing the magic to do that which it would. The object or spell immediately activates, exactly as though it were triggered by whatever normally triggers the effect. If an activation roll is normally required, treat the spell\'s Potency as rolled successes.'
spell.db.reference = 'M:tA p. 166'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Word_of_Unmaking')
spell.db.longname = 'Word of Unmaking'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 5'
spell.db.info = 'The Aetheric storms scour and destroy as much as they revitalize. With this spell, the mage calls down the destructive power of the Supernal to destroy a magical item. Supernal Artifacts cannot be destroyed by this spell.'
spell.db.reference = 'M:tA p. 171'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Words_of_Truth')
spell.db.longname = 'Words of Truth'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Prime\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage speaks with tongues of fire, and the world listens. So long as the words the mage speaks are objectively true and the mage herself knows them to be true, all subjects of this spell can hear her and understand her clearly, regardless of distance, noise, or language barriers. Moreover, all subjects know, on a soul-deep level, that what the mage says is true. The spell only works on statements the mage knows to be true: She can\'t use it to confirm or reject theories. It also doesn\'t necessarily compel the targets to act on the information in any particular way, but ignoring or refuting this Supernal truth may be grounds for a breaking point. In a Social maneuvering action, this spell may remove one Door or improve the impression level by one step per point of Potency.'
spell.db.reference = 'M:tA p. 168'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'World_Walker')
spell.db.longname = 'World Walker'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Spirit\',statclass=\'Arcana\') >= 4'
spell.db.info = 'The shaman goes where she must to find wisdom and power. This spell allows the mage to bring a subject directly across the Gauntlet, either to or from the Shadow, without the need for a portal. If the subject is a spirit or ephemeral object, it appears in Twilight.'
spell.db.reference = 'M:tA p. 184'
spell.db.restricted = False

spell = create_script('typeclasses.scripts.SpellScript',key = 'Zoom_In')
spell.db.longname = 'Zoom In'
spell.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Forces\',statclass=\'Arcana\') >= 2'
spell.db.info = 'The mage focuses light entering her subject\'s senses, greatly magnifying vision. Without an Unveiling spell like "Nightvision" (p.141), the spell can only affect visible wavelengths. For example, a mage using this spell on herself could look closely at a bird circling high above, or zoom in to great detail to examine a layer of dust on an object, but she couldn\'t see things that would only appear under a blacklight.'
spell.db.reference = 'M:tA p. 144'
spell.db.restricted = False

pass
