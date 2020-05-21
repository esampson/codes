from evennia import create_script

from codes import data

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Acute_Senses')
    merit.db.longname = 'Acute Senses'
    merit.db.category = 'Changeling and Vampire'
    merit.db.range = [1]
    merit.db.prereq = '(target.template().lower() == \'changeling\' and (target.wits() >= 3 or target.composure() >= 3)) or target.template().lower() == \'vampire\''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 111, VtR p. 109'
    merit.db.info = 'The changeling\'s senses are especially acute, even by the standards of high Clarity. Her sight, hearing, and sense of smell operate at twice the distance and accuracy of mortal senses. She can\'t see in pitch darkness (for that, she needs Contract magic), but she can see much more clearly than humans can.|/|/Add the character\'s Wyrd rating as dice to any perception-based rolls. This bonus supersedes the one normally granted by maximum Clarity. Also, add the bonus to any rolls made to remember or identify details.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Adamant_Hand')
    merit.db.longname = 'Adamant Hand'
    merit.db.category = 'Mage'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Status\',statclass=\'Merit\',subentry=\'Adamantine Arrow\') >= 1 and target.get(subentry,statclass=\'Skill\') >= 3'
    merit.db.noteRestrictions = ['Athletics', 'Brawl', 'Weaponry']
    merit.db.reference = 'M:tA p. 99'
    merit.db.info = 'Your character has studied extensively in the Adamantine Arrow martial arts. This allows her to use combat techniques as Yantras for instant spells. When taking this Merit, choose Athletics, Weaponry, or Brawl, which your character must have three or more dots in. This Merit allows use of that Skill in combat as a reflexive Order tool Yantra, adding dice to a spell cast on subsequent turns, or to a spell cast reflexively in the same turn as the combat action. You may purchase this Merit multiple times to reflect the other styles.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Aggressive_Driving')
    merit.db.longname = 'Aggressive Driving'
    merit.db.category = 'Physical'
    merit.db.range = [1, 2, 3, 4]
    merit.db.prereq = 'target.resolve() >= 3 and target.get(\'Fast Reflexes\',statclass=\'Merit\') >= 3 and target.drive() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 55'
    merit.db.info = 'Any vehicle can become a weapon when your character is behind the wheel. From the earliest days of bootleggers these maneuvers have passed between police and criminals as a means to evade or stop other vehicles, even at high speeds.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Air_of_Menace')
    merit.db.longname = 'Air of Menace'
    merit.db.category = 'General'
    merit.db.range = [2]
    merit.db.prereq = 'target.intimidation() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 41'
    merit.db.info = 'Your character has survived dozens of fights, and each one has taken its toll. He carries scars, features that have healed crookedly, and an attitude that unsettles others. The character gains +2 dice to rolls that use fear and menace to force compliance, such as with Intimidation rolls. Opponents less menacing than the character also think twice before provoking him. Opponents with Intimidation dots fewer than the character\'s must spend a point of Willpower to initiate combat against him.|/|/Drawback: Though many people try to overcome their prejudices, appearance still drives many human opinions. In social maneuvers, the character\'s first impression is downgraded one step for people who do not know him, and even for those who do, he must overcome an additional Door.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Allies')
    merit.db.longname = 'Allies'
    merit.db.category = 'Social'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 49-50'
    merit.db.info = 'Allies help your character. They might be friends, employees, associates, or people your character has blackmailed. Each instance of this Merit represents one type of ally. This could be an organization, a society, a clique, or an individual. Examples include the police, a secret society, criminal organizations, unions, local politicians, or the academic community. Each purchase has its own rating. Your character might have Allies (Masons) **, Allies (Carter Crime Family) ***, and Allies (Catholic Church) *.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Altar')
    merit.db.longname = 'Altar'
    merit.db.category = 'Vampire'
    merit.db.range = [3]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\',subentry=\'Circle of the Crone\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 109'
    merit.db.info = 'Your character is attuned to a mystical, bloody altar. She may have crafted it herself, or a covenmate may have designed it. In the presence of the altar, Acolytes may use the teamwork rules (see p. 173) when using Crúac rituals. However, double the time necessary to make the roll, and determine the time per roll by the lowest Crúac dots of the collective group. This allows vampires uninitiated in the secrets of Crúac to participate in rituals. Characters do not need dots in Crúac to act as supporting performers with the Altar Merit, but double the time between rolls if any participants have no Crúac dots whatsoever.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Alternate_Identity')
    merit.db.longname = 'Alternate Identity'
    merit.db.category = 'Social'
    merit.db.range = [1, 2, 4]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 50'
    merit.db.info = 'Your character has established an alternate identity. The level of this Merit determines the amount of scrutiny it holds up to. At one dot, the identity is superficial and unofficial. For example, your character uses an alias with a simple costume and adopts an accent. She hasn\'t established the necessary paperwork to even approach a bureaucratic background check, let alone pass one. At two dots, she\'s supported her identity with paperwork and identification. It\'s not liable to stand up to extensive research, but it\'ll turn away private investigators and internet hobbyists. At three dots, the identity can pass a thorough inspection. The identity has been deeply entrenched in relevant databases, with subtle flourishes and details to make it seem real, even to trained professionals.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Ambidextrous')
    merit.db.longname = 'Ambidextrous'
    merit.db.category = 'Physical'
    merit.db.range = [3]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = ''
    merit.db.info = 'Your character does not suffer the -2 penalty for using his off hand in combat or to perform other actions.'
    merit.db.cg_only = True
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Anchored')
    merit.db.longname = 'Anchored'
    merit.db.category = 'Werewolf'
    merit.db.range = [1, 2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'W:tF p. 105'
    merit.db.info = 'Your character has a stronger association with one of her Touchstones than the other. Choose one of her Touchstones when purchasing this Merit. When calling upon that Touchstone to resist a breaking point, take +3 bonus dice. With the two-dot version of the Merit, take +4 dice.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Anointed')
    merit.db.longname = 'Anointed'
    merit.db.category = 'Vampire'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\',subentry=\'Lancea et Sanctum\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 109-110'
    merit.db.info = 'Not all Sanctified are members of the clergy. Most are lay members. Those anointed under the damnation of Longinus wield his word like a firebrand. Once per chapter, roll Presence + Expression when preaching to a crowd. A small clique of listeners levies a -1 die penalty, a small crowd a -2, and a large crowd a -3. Listeners gain the Raptured Condition (see p. 305).'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Anonymity')
    merit.db.longname = 'Anonymity'
    merit.db.category = 'Social'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.get(entry=\'fame\') == 0'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 50'
    merit.db.info = 'Your character lives off the grid. This means purchases must be made with cash or falsified credit cards. She eschews identification. She avoids any official authoritative influence in her affairs. Any attempts to find her by paper trail suffer a -1 penalty per dot purchased in this Merit.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Arcadian_Metabolism')
    merit.db.longname = 'Arcadian Metabolism'
    merit.db.category = 'Changeling'
    merit.db.range = [2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 111'
    merit.db.info = 'Your character is particularly well-suited to time in Arcadia and the Hedge. Maybe he was abducted at an early age and knows more of Arcadia than Earth, or he glutted himself on rare goblin fruit for the entirety of his captivity.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Area_of_Expertise')
    merit.db.longname = 'Area of Expertise'
    merit.db.category = 'Mental'
    merit.db.range = [1]
    merit.db.prereq = 'target.resolve() >= 2 and subentry in target.db.specialties'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 44'
    merit.db.info = 'Your character is uncommonly specialized in one area. Choose a Specialty to assign to this Merit. Forgo the +1 bonus afforded by a Specialty, in exchange for a +2.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Armed_Defense')
    merit.db.longname = 'Armed Defense'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.dexterity >= 3 and target.weaponry >= 2 and target.get(\'Defensive Combat\', \'Weaponry\') == 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 60-61'
    merit.db.info = 'You\'re able to use a weapon to stop people who are trying to kill you. Often deployed by police officers using riot shields or telescoping batons, it\'s just as effective while using a chair leg.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Armed_Restraint')
    merit.db.longname = 'Armed Restraint'
    merit.db.category = 'Fighting'
    merit.db.range = [2]
    merit.db.prereq = 'target.get(\'Staff Fighting\',statclass=\'Merit\') >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 53'
    merit.db.info = 'Your character knows how to use a pole with a hook or noose on the end of it to restrain animal and human targets. Using a suitable weapon, such as a catch pole or shepherd\'s crook, your character can grapple and immediately apply the Hold maneuver on success. During subsequent turns her opponent\'s grapple rolls are penalized by the weapon\'s damage rating.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Artifact')
    merit.db.longname = 'Artifact'
    merit.db.category = 'Mage'
    merit.db.range = [3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'M:tA p. 99-100'
    merit.db.info = 'Your character possesses an Artifact, an item from the Supernal World which is both a physical symbol of magic and a unique item independently empowered to create sorcerous effects. These items possess their own Mana stores, and have their own effective Gnosis and Arcana with which to generate effects. They can cast these effects when harnessed by an Awakened owner who has researched (or divined through Prime) the manner in which the item works. In general, this takes successes on an extended research action equal to twice the Artifact\'s Merit dots.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Astral_Adept')
    merit.db.longname = 'Astral Adept'
    merit.db.category = 'Mage'
    merit.db.range = [3]
    merit.db.prereq = 'target.template().lower() == \'mage\' or target.template().lower() == \'sleepwalker\''
    merit.db.noteRestrictions = []
    merit.db.reference = 'M:tA p. 100'
    merit.db.info = 'Your character is deeply in tune with her own soul, and may enter the Astral Realms without a place of power. In addition to the access methods listed on p. 249, your character may perform a ceremony to attune herself to the astral, then spend a Willpower point to allow her to meditate into the realms. Decide what form your ceremony takes when buying this Merit; many mages use a Legacy Oblation, while Sleepwalkers might require special drugs, exercises, or chants.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Atrocious')
    merit.db.longname = 'Atrocious'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and not (target.get(\'Cutthroat\',statclass=\'Merit\') >= 1) and not (target.get(\'Enticing\',statclass=\'Merit\') >= 1)'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 110'
    merit.db.info = 'Your character\'s monstrous Beast dominates her personality. Her threats always ring true. Her very gaze inspires anger and fear. Any rolls to invoke the monstrous Beast gain the 8-again quality.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Attache')
    merit.db.longname = 'Attache'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\',subentry=\'Invictus\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 110'
    merit.db.info = 'Normally, Retainers (see p. 123) serve a couple of functions, represented by dice pools. They don\'t normally allow a character to access other things represented by Social Merits. However, Invictus vampires with this Merit have Retainers of a more thoroughly loyal breed. Each Retainer gains any combination of the following Merit dots equal to the vampire\'s Invictus Status: Contacts, Resources, or Safe Place.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Aura_Reading')
    merit.db.longname = 'Aura Reading'
    merit.db.category = 'Supernatural'
    merit.db.range = [3]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 56'
    merit.db.info = 'Your character has the psychic ability to perceive auras, the ephemeral halos of energy that surround all living things. This allows her to perceive a subject\'s emotional state, and potentially any supernatural nature. The colors of an aura show a person\'s general disposition, and the ebbs, flows, tone, and other oddities reveal other influences. Note that your character may not know what she\'s looking at when seeing something odd in an aura. For example, she may not know that a pale aura means she\'s seeing a vampire, unless she\'s confirmed other vampiric auras in the past.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Automatic_Writing')
    merit.db.longname = 'Automatic Writing'
    merit.db.category = 'Supernatural'
    merit.db.range = [2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 56-57'
    merit.db.info = 'Your character can enter a trance of sorts, in which she\'s temporarily overtaken by a spirit or ghost, and compelled to write mysterious things.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Automotive_Genius')
    merit.db.longname = 'Automotive Genius'
    merit.db.category = 'Physical'
    merit.db.range = [1]
    merit.db.prereq = 'target.crafts() >= 3 and target.drive() >=1 and target.science() >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 47'
    merit.db.info = 'Your character knows how to fine-tune a vehicle to utter extremes. When determining how many modifications she can add to a vehicle (see p. 98), triple her Crafts dots instead of doubling them. So, a character with Crafts **** could support 12 combined modifications on a vehicle instead of eight. Additionally, any relevant Crafts Specialties add one more potential modification to the total.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Avoidance')
    merit.db.longname = 'Avoidance'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4]
    merit.db.prereq = 'target.manipulation() >= 3 and target.athletics() >= 2 and target.stealth() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 46'
    merit.db.info = 'Your character\'s only goal in a fight is not to get hurt. She tries to create situations where opponents hurt themselves or target her big mean friends instead. There is no formal training for this Style; it\'s a mixture of ingenuity and a person\'s innate desire to avoid pain.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Barfly')
    merit.db.longname = 'Barfly'
    merit.db.category = 'Social'
    merit.db.range = [2]
    merit.db.prereq = 'target.socialize() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 50'
    merit.db.info = 'Your character is a natural in the bar environment, and can procure an open invitation wherever he wishes. Whereas most characters would require rolls to blend into social functions they don\'t belong in, he doesn\'t; he belongs. Rolls to identify him as an outsider suffer his Socialize as a penalty.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Berserker')
    merit.db.longname = 'Berserker'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.strength() >= 3 and target.get(\'Iron Stamina\',statclass=\'Merit\') >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 46-47'
    merit.db.info = 'Your character enters a controlled madness in combat. Whether a believer in the throes of ecstatic fervor or a warrior emulating the Norse berserks, this Style is not about technique but about achieving the right state of mind.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Between_the_Ticks')
    merit.db.longname = 'Between the Ticks'
    merit.db.category = 'Mage'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'mage\' and target.wits() >= 3 and target.get(\'Time\',statclass=\'Arcana\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'M:tA p. 100'
    merit.db.info = 'Your character has perceived the depths of Time, and thus can act with the utmost precision, performing an action perfectly for ideal timing, or ideal efficiency. With this Merit, once per scene you can subtract -1 from your character\'s Initiative for the turn to add a die to her action for the turn, or subtract a die from her action to add +1 to her Initiative.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Biokinesis')
    merit.db.longname = 'Biokinesis'
    merit.db.category = 'Supernatural'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 56-57'
    merit.db.info = 'Your character has the ability to psychically alter his biological makeup. By spending a Willpower point and concentrating for a full minute, he can shift his Physical Attributes, moving dots from one to another. He can shift one dot in an Attribute per dot in this Merit. This shift lasts for one hour. This can shift an Attribute no higher than five dots.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Blood_Affinity')
    merit.db.longname = 'Blood Affinity'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Harmony\',statclass=\'Advantage\') >= 3 and target.get(\'Harmony\',statclass=\'Advantage\') <= 8'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 105'
    merit.db.info = 'Choose Blood or Bone when choosing this Merit at the two-dot version. The five-dot version encompasses both Blood and Bone. Once per chapter, when taking an action that would replenish all Willpower from the chosen Blood or Bone trait, you can apply the rote quality to the roll (see p. 162).'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Blood_and_Bone_Affinity')
    merit.db.longname = 'Blood and Bone Affinity'
    merit.db.category = 'Werewolf'
    merit.db.range = [5]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Harmony\',statclass=\'Advantage\') >= 3 and target.get(\'Harmony\',statclass=\'Advantage\') <= 8'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 105'
    merit.db.info = 'Choose Blood or Bone when choosing this Merit at the two-dot version. The five-dot version encompasses both Blood and Bone. Once per chapter, when taking an action that would replenish all Willpower from the chosen Blood or Bone trait, you can apply the rote quality to the roll (see p. 162).'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Bloodhound')
    merit.db.longname = 'Bloodhound'
    merit.db.category = 'Vampire'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.wits() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 110'
    merit.db.info = 'Your character can discern the intricacies of blood by smelling it, as if he had tasted it. When using his Kindred senses to detect blood, to track by blood, or to pick out the details of blood, he only needs to smell a blood source.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Body_as_Weapon')
    merit.db.longname = 'Body as Weapon'
    merit.db.category = 'General'
    merit.db.range = [2]
    merit.db.prereq = 'target.stamina() >= 3 and target.brawl() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 41'
    merit.db.info = 'Your character has honed her body to be a hardened weapon. She has trained long, punishing hours to inure herself to the pain of the cracked knuckles, broken hands, and crushed toes that come with hitting others with her body. She can hit harder and more often without flinching. Your character\'s unarmed strikes still cause bashing damage normally, but they add one point of bashing damage on a successful hit.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Bone_Affinity')
    merit.db.longname = 'Bone Affinity'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Harmony\',statclass=\'Advantage\') >= 3 and target.get(\'Harmony\',statclass=\'Advantage\') <= 8'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 105'
    merit.db.info = 'Choose Blood or Bone when choosing this Merit at the two-dot version. The five-dot version encompasses both Blood and Bone. Once per chapter, when taking an action that would replenish all Willpower from the chosen Blood or Bone trait, you can apply the rote quality to the roll (see p. 162).'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Boot_Party')
    merit.db.longname = 'Boot Party'
    merit.db.category = 'Fighting'
    merit.db.range = [2]
    merit.db.prereq = 'target.brawl() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 53'
    merit.db.info = 'Your character understands the effectiveness of grinding her heel into a delicate part of a downed opponent\'s anatomy. When attacking an opponent in the prone position, she may make an unarmed attack at a -3 penalty in addition to normal modifiers. Any damage inflicted is lethal.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Bowmanship')
    merit.db.longname = 'Bowmanship'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4]
    merit.db.prereq = 'target.dexterity() >= 3 and target.firearms() >=2 and target.get(\'Trained Observer\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 47'
    merit.db.info = 'Your character is a patient hunter with a bow. She fires precision shots across long distances to take out targets that had no idea she was even there. This Style focuses on a character\'s ability to aim by judging distance and trajectory. It uses a dice pool of Dexterity + Firearms for its attacks.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Boxing')
    merit.db.longname = 'Boxing'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.strength() >= 2 and target.dexterity() >= 2 and target.stamina() >= 2 and target.brawl() >= 2 and target.athletics() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 47-48'
    merit.db.info = 'Trading blows with the hands dates back to Classical times, and probably earlier - some biologists believe our hands have been optimized to deliver blows. There are hundreds of folk styles of boxing, from West Africa\'s Dambe to the Filipino method known as Suntukan or Panantukan. This style concentrates on the modern combat sport, which combines European methods with innovations developed by trainers or borrowed from other cultures. Your character is trained in modern boxing, or a similar traditional style.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Brownies_Boon')
    merit.db.longname = 'Brownie\'s Boon'
    merit.db.category = 'Changeling'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 111'
    merit.db.info = 'Like the shoemaker\'s elves, your character completes tasks with a casual disregard for time. Reduce the interval for any mundane extended action roll she makes while no one watches her by half. The character may spend a Glamour to halve the interval again, working at four times her normal speed for that roll. Exceptional success on an individual roll can decrease the time it takes to complete that roll to an eighth of the usual interval, if the player chooses the time reduction benefit.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Cabal_Theme')
    merit.db.longname = 'Cabal Theme'
    merit.db.category = 'Mage'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'M:tA p. 100'
    merit.db.info = 'Your character is part of a deeply themed cabal. All members of the cabal are counted as having one dot higher in the Shadow Name Merit for purposes of persona Yantras, even if they do not possess the Merit at all, or if it would take Shadow Name above three dots.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Cacophony_Savvy')
    merit.db.longname = 'Cacophony Savvy'
    merit.db.category = 'Vampire'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\',subentry=\'City\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 110'
    merit.db.info = 'You have your finger on the pulse of the Kindred underground. You\'re adept with the codes and cants that allow Kindred culture to flourish despite the Masquerade. Each level of Cacophony Savvy builds on the previous. This Merit assumes the character can read and deliver Cacophony messages.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Call_Out')
    merit.db.longname = 'Call Out'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower == \'werewolf\' and target.get(\'Honor\',statclass=\'Renown\') >=2 and target.intimidation() >= 2 and target.composure() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p.108'
    merit.db.info = 'Your character fights with honor and dignity. When he calls out his opponent, it must abide by his challenge. When he uses an instant action to call out a potential combatant, that opponent suffers your character\'s Honor as a penalty to attack anyone else. If the opponent does attack someone else, you can add your character\'s Honor to any attacks against him.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Carthian_Pull')
    merit.db.longname = 'Carthian Pull'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\',subentry=\'Carthian\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 110'
    merit.db.info = 'Carthians know people. Being the covenant arguably most in touch with humanity, they tend to have the most numerous connections. Membership in the Movement can mean leveraging those connections. Each month, you can access a number of dots of the Allies, Contacts, Haven, and Herd Merits equal to your Carthian Status.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Chain_Weapons')
    merit.db.longname = 'Chain Weapons'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2]
    merit.db.prereq = 'target.strength() >= 3 and target.dexterity() >= 3 and target.athletics() >= 2 and target.weaponry() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 48'
    merit.db.info = 'Your character knows how to use a length of chain as a weapon. These maneuvers require at least a yard\'s (or meter\'s) worth of chain and can be any design from a martial artist\'s chain whip to one ripped off the sprocket of a motorcycle. The Style is taught among traditional Chinese weapon styles but is also favored among everyday street gangs.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Cheap_Shot')
    merit.db.longname = 'Cheap Shot'
    merit.db.category = 'Fighting'
    merit.db.range = [2]
    merit.db.prereq = 'target.get(\'Street Fighting\') >= 3 and target.subterfuge() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 61'
    merit.db.info = 'Your character is a master at the bait and switch. She can look off in an odd direction and prompt her opponent to do the same, or she might step on his toes to distract him. She fights dirty. Make a Dexterity + Subterfuge roll as a reflexive action. The opponent\'s player contests with Wits + Composure. If you score more successes, the opponent loses his Defense for the next turn. Each time a character uses this maneuver in a scene, it levies a cumulative -2 penalty to further uses since the opposition gets used to the tricks.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Choke_Hold')
    merit.db.longname = 'Choke Hold'
    merit.db.category = 'Fighting'
    merit.db.range = [2]
    merit.db.prereq = 'target.brawl() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 61'
    merit.db.info = 'If you can get your hands on someone, they\'re putty in your hands. When grappling, your character can use the Choke move'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Clairvoyance')
    merit.db.longname = 'Clairvoyance'
    merit.db.category = 'Supernatural'
    merit.db.range = [3]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 57'
    merit.db.info = 'Your character can project her senses to another location. She sees, hears, smells, and otherwise experiences the other place as if she were there. This ability requires a point of Willpower to activate, successful meditation, and a Wits + Occult roll.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Claws_of_the_Unholy')
    merit.db.longname = 'Claws of the Unholy'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Protean\',statclass=\'Discipline\') >= 4'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 110-111'
    merit.db.info = 'A Gangrel\'s claws are deadly and bestial; yours are downright unnatural. The vampire allows the Beast out of its cage and lets it punish all those around her. When wielding claws borne of Unnatural Aspect while in frenzy, this Merit takes effect. The weapon modifier for the claws becomes +0 aggravated. These claws ignore all armor not generated by Resilience.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Clinch_Strike')
    merit.db.longname = 'Clinch Strike'
    merit.db.category = 'Fighting'
    merit.db.range = [1]
    merit.db.prereq = 'target.brawl() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 53'
    merit.db.info = 'Most people will instinctively grab anyone they want to hit, but your character has trained to hit hard and accurately from a clinch position, using short punches, elbows, and knees. She inflicts standard Brawl damage when initiating a grapple instead of sacrificing the opportunity to damage someone in order to grab.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Cloak_of_Leaves')
    merit.db.longname = 'Cloak of Leaves'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.template().lower() == \'changeling\' and target.get(\'Mantle\',\'Autumn\') >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 111'
    merit.db.info = 'Your character has learned to embrace his worries and fears, and use them as a shield against the supernatural. Anyone using a supernatural ability to cause damage or inflict physical Tilts upon the character suffers a penalty equal to his dots in this Merit. Supernatural abilities include Contracts, kith blessings, vampire Disciplines, mage spells, and any other innate ability used by a supernatural creature.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Close_Family')
    merit.db.longname = 'Close Family'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 111'
    merit.db.info = 'Your character feels blood sympathy more keenly than most of her kind. Add +1 to all blood sympathy bonuses, and apply the 8-again quality to all blood sympathy rolls. As well, treat all relations as one step closer for the purposes of sympathy distances.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Close_Quarters_Combat')
    merit.db.longname = 'Close Quarters Combat'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.wits() >= 3 and target.athletics() >= 2 and target.brawl >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 61'
    merit.db.info = 'Your character knows that hitting someone in the face is an easy way to break the little bones in his hand. To that end, he\'s perfected the art of using the environment to hurt people.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Closed_Book')
    merit.db.longname = 'Closed Book'
    merit.db.category = 'Social'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.manipulation() >= 3 and target.resolve() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 50'
    merit.db.info = 'Your character is particularly tough to crack. When a character uses Social Maneuvering (see p. 81) against her, add her dots in this Merit as additional Doors. In other Social actions to uncover her true feelings, motives, and position, add her Merit dots to any contested rolls for her.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Code_of_Honor')
    merit.db.longname = 'Code of Honor'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Harmony\',statclass=\'Advantage\') >= 8'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 105'
    merit.db.info = 'Your character has established and held onto a code of human behavior. Maybe she follows a knightly tradition, or maybe she was part of a generational secret society before her Change. When purchasing this Merit, choose a Virtue (p. 158) that reflects her Code of Honor. In addition to the advantages of a Virtue, such as Willpower replenishment, she gets +3 dice to any Stamina, Resolve, or Composure roll to uphold the integrity of her code.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Cohesive_Unit')
    merit.db.longname = 'Cohesive Unit'
    merit.db.category = 'General'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.presence() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 42'
    merit.db.info = 'Your character is a natural leader who brings out the best from those he works with. At one dot, team members add +2 dice to teamwork actions dedicated to helping the team (see Chronicles of Darkness Rulebook, p. 72). At two dots the team gains access to a pool of dice equal to the character\'s Presence each scene, which they can draw upon for actions where they work towards their established purpose. At three dots, all team members can reroll a failed result once per scene. In each case, the benefits last until depleted, or until the team reaches or deviates from its agreed goal or disbands. The character with this Merit can\'t access any of the benefits he encourages in others.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Cold_Hearted')
    merit.db.longname = 'Cold Hearted'
    merit.db.category = 'Changeling'
    merit.db.range = [3]
    merit.db.prereq = 'target.template().lower() == \'changeling\' and target.get(\'Mantle\',\'Winter\') >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 111-112'
    merit.db.info = 'Your character has taken her pain, and the pain of others, and crafted them into a barrier against further suffering. She may spend a Willpower to ignore the effects of a single Clarity Condition once per scene. She still has the Condition and doesn\'t heal any Clarity damage, but she does not suffer the ill effects of the Condition. If her actions during the scene would resolve the Condition, it resolves normally.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Combat_Archery')
    merit.db.longname = 'Combat Archery'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.strength() >= 3 and target.athletics() >= 2 and target.get(\'Quick Draw\', subentry=\'Bow\', statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 48'
    merit.db.info = 'Your character uses a bow for rapid draws that riddle opponents with arrows. She knows how to move across the battlefield while firing from any angle. This Style is about trick shots and using archery in the thick of a fight. It uses a dice pool of Dexterity + Athletics for its attacks.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Common_Sense')
    merit.db.longname = 'Common Sense'
    merit.db.category = 'Mental'
    merit.db.range = [3]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 44'
    merit.db.info = 'Your character has an exceptionally sound and rational mind. With a moment\'s thought, she can weigh potential courses of action and outcomes.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Contacts')
    merit.db.longname = 'Contacts'
    merit.db.category = 'Social'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 50'
    merit.db.info = 'Contacts provide your character with information. Each dot in this Merit represents a sphere or organization with which the character can garner information. For example, a character with Contacts *** might have Bloggers, Drug Dealers, and Financial Speculators for connections. Contacts do not provide services, only information. This may be face-to-face, via email, by telephone, or even by seance in some strange instances.|/|/Garnering information via Contacts requires a Manipulation + Social Skill roll, depending on the method the character uses, and the relationship between the characters. The Storyteller should give a bonus or penalty, dependent on how relevant the information is to that particular Contact, whether accessing the information is dangerous, and if the character has maintained good relations or done favors for the Contact. These modifiers should range from -3 to +3 in most cases. If successful, the Contact provides the information.|/|/One use of a Contact is to dig dirt on another character. A Contact can find another character\'s Social Merits, and any relevant Conditions (Embarrassing Secret is a prime example.)|/|/A character can have more than five Contacts, but the Merit\'s rating is limited to five, for the purposes of Allies blocking.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Controlled_Burn')
    merit.db.longname = 'Controlled Burn'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.resolve() >= 3 and target.composure() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 105'
    merit.db.info = 'Your character suffers from a dampened form of Wasu-Im, the first stage of Death Rage. When she goes into Wasu-Im, she shifts to Hishu or Urhan form, not Dalu or Urshul. If she succeeds in getting a turn of lucidity (see p. 102), she can spend a point of Willpower to shrug the Rage off entirely.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Court_Goodwill')
    merit.db.longname = 'Court Goodwill'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['Spring', 'Summer', 'Autumn', 'Winter']
    merit.db.reference = 'CtL p. 112'
    merit.db.info = 'Court Goodwill represents a changeling\'s influence and respect in a court that isn\'t his own. It allows him to have serious ties to as many courts as he likes, in addition to the one he has sworn magical allegiance to. This isn\'t to say Court Goodwill is a purely social construct. This Merit covers both the mundane networking required of being part of a large social group and the fickle favor of whatever plays patron to a court. In this way, a changeling of the White Rose Court can use the benefits of the Red Rose Court\'s Mantle, the Red Rose Courtier can be privy to the Blue Rose Court\'s magic, and so on.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Covert_Operative')
    merit.db.longname = 'Covert Operative'
    merit.db.category = 'Fighting'
    merit.db.range = [1]
    merit.db.prereq = 'target.wits() >= 3 and target.dexterity() >= 3 and target.stealth() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 53-54'
    merit.db.info = 'Your character is trained in getting the jump on her opponents. She creeps up on unsuspecting enemies from the shadows and neutralizes them before anyone realizes anything\'s happening. When your character ambushes an opponent, the victim loses the 10-again quality on his roll to notice the attack. Even if he successfully notices your character, your character acts at +3 Initiative in the first turn.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Crack_Driver')
    merit.db.longname = 'Crack Driver'
    merit.db.category = 'Physical'
    merit.db.range = [2, 3]
    merit.db.prereq = 'target.drive() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 47'
    merit.db.info = 'Your character\'s an ace at the wheel, and nothing shakes his concentration. So long as he\'s not taking any actions other than driving (and keeping the car safe), add his Composure to any rolls to Drive. Any rolls to disable his vehicle suffer a penalty equal to his Composure as well. With the three-dot version, once per turn he may take a Drive action reflexively.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Creative_Tactician')
    merit.db.longname = 'Creative Tactician'
    merit.db.category = 'Werewolf'
    merit.db.range = [3]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Purity\',statclass=\'Renown\') >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 105-106'
    merit.db.info = 'Your character has an intuitive mind for strategy. Any time she acts as the tactician or organizer in a teamwork action (see p. 162), the participants ignore circumstantial penalties up to her Purity dots. As well, once per chapter, the primary actor can gain a Beat if he follows your character\'s strategic guidance. Your character does not have to be the primary actor to use this Merit.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Cursed')
    merit.db.longname = 'Cursed'
    merit.db.category = 'Supernatural'
    merit.db.range = [2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 57'
    merit.db.info = 'Your character has run afoul of fate. Somewhere, somehow, he\'s been cursed. Most importantly, he\'s aware of the curse. When taking this Merit, define the limitations of the curse. Usually, it\'s expressed in the form of a single statement, such as, "On the eve of your twenty-seventh birthday, you will feast upon your doom." It\'s important to work out the details with the Storyteller. The curse must take effect within the scope of the planned chronicle.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Cutthroat')
    merit.db.longname = 'Cutthroat'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and not (target.get(\'Atrocious\',statclass=\'Merit\') >= 1) and not (target.get(\'Enticing\',statclass=\'Merit\') >= 1)'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 111'
    merit.db.info = 'Your character\'s competitive Beast flows in her every action. Her smug bearing forces a desire to dominate or submit. Any rolls to invoke the competitive Beast gain the 8-again quality.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Danger_Sense')
    merit.db.longname = 'Danger Sense'
    merit.db.category = 'Mental'
    merit.db.range = [2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 44'
    merit.db.info = 'You gain a +2 modifier on reflexive Wits + Composure rolls for your character to detect an impending ambush.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Dedicated_Locus')
    merit.db.longname = 'Dedicated Locus'
    merit.db.category = 'Werewolf'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Safe Place\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'W:tF p. 106'
    merit.db.info = 'The pack has a locus on its territory that\'s attuned to their totem\'s resonance. While most packs protect a locus, a Dedicated Locus represents one they\'ve invested deeply into, which provides significant and highly quickened Essence. The locus\' rating is equal to the dots in this merit. Additionally, the pack can use the filtered, focused Essence faster than other Essence. Collectively, pack members with this Merit can spend a number of points of Essence equal to the Merit cost in a day, above and beyond their normal per-turn limits.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Defender')
    merit.db.longname = 'Defender'
    merit.db.category = 'General'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 42'
    merit.db.info = 'Your character is filled with a burning fury when her friends or family are threatened. For each dot of this Merit, the character gains a Willpower point to spend on actions related to defending or protecting these loved ones. This also applies to actions taken preemptively to prevent clear threats to her charges, and to acts of retribution against an offender if her loved ones are hurt. These bonus Willpower points do not count towards the character\'s normal Willpower dots, and replenish each chapter.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Defensive_Combat')
    merit.db.longname = 'Defensive Combat'
    merit.db.category = 'Fighting'
    merit.db.range = [1]
    merit.db.prereq = 'subentry in target.db.specialties'
    merit.db.noteRestrictions = ['Brawl', 'Weaponry']
    merit.db.reference = 'CoD p. 61'
    merit.db.info = 'Your character is trained in avoiding damage in combat. Use her Brawl or Weaponry to calculate Defense, rather than Athletics. Your character can learn both versions of this Merit, allowing you to use any of the three Skills to calculate Defense. However, you cannot use Weaponry to calculate Defense unless she actually has a weapon in her hand.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Defensive_Dreamscaping')
    merit.db.longname = 'Defensive Dreamscaping'
    merit.db.category = 'Changeling'
    merit.db.range = [2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 112'
    merit.db.info = 'Your character is adept at manipulating the dream in a hand-to-hand fight. A gust of wind carries her out of the way of an attack, an eidolon leaps in front of a bullet for her, or her opponent\'s blade dulls when it strikes. Add half her Wyrd (rounded down) to her Defense in dreams.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Demolisher')
    merit.db.longname = 'Demolisher'
    merit.db.category = 'Physical'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.strength() >= 3 or target.intelligence() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 47'
    merit.db.info = 'Your character has an innate feel for the weak points in objects. When damaging an object, she ignores one point of the object\'s Durability per dot with this Merit.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Destiny')
    merit.db.longname = 'Destiny'
    merit.db.category = 'Mage'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'M:tA p. 100-101'
    merit.db.info = 'Your character\'s thread stands out in the skein of Fate. Like the hero of an epic she is destined for great triumphs, but she also has a Doom that hangs over her head and threatens to turn her tale into a tragedy.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Direction_Sense')
    merit.db.longname = 'Direction Sense'
    merit.db.category = 'Mental'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 44'
    merit.db.info = 'Your character has an innate sense of direction, and is always aware of her location in space. She always knows which direction she faces, and never suffers penalties to navigate or find her way.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Distinguished_Palate')
    merit.db.longname = 'Distinguished Palate'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 111'
    merit.db.info = 'Your character can discern the subtle nuances in blood and Vitae. Consider any Taste of Blood roll (see p. 91) an exceptional success with only a single success.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Diviner')
    merit.db.longname = 'Diviner'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.template().lower() == \'changeling\' and target.composure() >= 3 and target.wits() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 112'
    merit.db.info = 'Your character can dig within his dreams for prophetic answers to primordial truths, as all humanity is and has always been connected through its dreams via the Dreaming Roads. He must enter a dream state, through either the Gate of Ivory or Horn, into his own Bastion. Then, he may ask the Storyteller a yes or no question about something he wishes to divine from his dreams. She must answer accurately, but can use "maybe" if the answer is truly neither yes nor no. Depending on the answer, you may ask additional, related questions, up to your Merit dots. You can ask that many total questions per chapter.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Double_Jointed')
    merit.db.longname = 'Double Jointed'
    merit.db.category = 'Physical'
    merit.db.range = [2]
    merit.db.prereq = 'target.dexterity() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 47'
    merit.db.info = 'Your character might have been a contortionist, or spent time practicing yoga. She can dislodge joints when need be. She automatically escapes from any mundane bonds without a roll. When grappled, subtract her Dexterity from any rolls to overpower her, as long as she\'s not taking any aggressive actions.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Dream')
    merit.db.longname = 'Dream'
    merit.db.category = 'Mage'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.template().lower() == \'mage\' and target.composure() >= 3 and target.wits() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'M:tA p. 101'
    merit.db.info = 'Once per chapter, your character can dig within her dreams for prophetic answers to primordial truths. She may enter her own dreams without a meditation roll when she sleeps, and if she has a basic understanding of something she wishes to divine from her dreams, you may use this Merit. Your character must sleep or meditate for at least four hours. Then, ask the Storyteller a yes or no question about the topic at hand. He must answer accurately, but can use "maybe" if the answer is truly neither yes nor no. Depending on the answer, you may ask additional questions, until you have asked questions equal to your Dream Merit dots.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Dream_Visions')
    merit.db.longname = 'Dream Visions'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Clan\',statclass=\'Sphere\').lower() == \'mekhet\''
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 111'
    merit.db.info = 'Your character\'s Mekhet blood touches on a level of universal interconnectedness that her mind cannot truly grasp. However, sometimes it gives her fleeting glimpses of insight and intuition. During the day, she dreams of what\'s to come in vague symbols. Once per night, when she meets someone new or visits a new place, make a Blood Potency roll. If successful, ask one question to the Storyteller or the character\'s player. The question must fit with a yes/no/maybe answer. The answer reflects the last day\'s dreams.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Dream_Warrior')
    merit.db.longname = 'Dream Warrior'
    merit.db.category = 'Changeling'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower() == \'changeling\' and target.get(\'Wyrd\') >= 2 and (target.presence() >= 3 or target.manipulation() >= 3 or target.composure() >= 3) and (target.get(\'Weaponry:*\') or target.get(\'Brawl:*\'))'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 112'
    merit.db.info = 'Your character\'s extensive training in oneiromancy allows her to benefit from the flexibility of the dream. By blending dreamscaping and martial techniques, strikes land faster as the dream bends to aid her blows. Whenever you allocate any successes generated with a Brawl or Weaponry attack (depending on which Specialty you have) to a subtle oneiromantic shift, gain one bonus success to spend on that shift as long as you spend it to impact the fight in some direct way. If you have a Specialty in both Skills, you gain these benefits on both types of attack.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Dreamweaver')
    merit.db.longname = 'Dreamweaver'
    merit.db.category = 'Changeling'
    merit.db.range = [3]
    merit.db.prereq = 'target.template().lower() == \'changeling\' and target.get(\'Wyrd\') >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 112'
    merit.db.info = 'Your character\'s extensive training in oneiromancy allows her to benefit from the flexibility of the dream. By blending dreamscaping and martial techniques, strikes land faster as the dream bends to aid her blows. Whenever you allocate any successes generated with a Brawl or Weaponry attack (depending on which Specialty you have) to a subtle oneiromantic shift, gain one bonus success to spend on that shift as long as you spend it to impact the fight in some direct way. If you have a Specialty in both Skills, you gain these benefits on both types of attack.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Drone_Control')
    merit.db.longname = 'Drone Control'
    merit.db.category = 'Mental'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.intelligence() >= 3 and target.computer() >= 3 and target.drive() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 55-56'
    merit.db.info = 'Your character knows how to operate weapon systems via remote. Though more impersonal than a knife or a gun, armed drones are quickly becoming a mainstay of the modern battlefield and increasingly sophisticated in the consumer market. These maneuvers work independently of the sophistication of the actual device. An RC car with a mounted pistol and a Wi-Fi receiver works just as well as a state-of-the-art military drone for the purposes of using this Style.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Dull_Beacon')
    merit.db.longname = 'Dull Beacon'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 113'
    merit.db.info = 'Your character\'s Mask is far less obtrusive when she drops it. Reduce her Wyrd by her Dull Beacon dots when determining the distance at which she alerts fae creatures and opens Hedge gateways when dropping her Mask (p. 83). If this would effectively reduce her to Wyrd 0, she no longer opens gates or alerts fae creatures at all until her Wyrd increases.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Dynasty_Membership')
    merit.db.longname = 'Dynasty Membership'
    merit.db.category = 'Vampire'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.template().lower == \'vampire\' and (target.get(\'Status\',subentry=target.get(\'Clan\',statclass=\'Sphere\'),statclass=\'Merit\') >= 1 or target.get(\'Status\',subentry=\'Clan\',statclass=\'Merit\') >= 1)'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 112'
    merit.db.info = 'Your character claims membership to a long-standing dynasty of Kindred. Her clan and city know her family\'s exploits, and they often precede her. Each level of this Merit builds on the earlier abilities.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Efficient_Killer')
    merit.db.longname = 'Efficient Killer'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower == \'werewolf\' and target.get(\'Purity\',statclass=\'Renown\') >= 2 and target.brawl() >= 3 and target.medicine >= 2 and target.strength() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p.108'
    merit.db.info = 'Your character is a master of immediate, merciful killing. She knows exactly where to clamp down to end a life in one swift blow. When in Gauru form, any time an opponent is completely denied her Defense - for example, if she\'s sacrificed it for an all-out attack, during a successful ambush, or when activating certain Merits - you can use Efficient Killer. Sacrifice your Defense for the turn, and you can deal a Killing Blow (see p. 168).'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Egregore')
    merit.db.longname = 'Egregore'
    merit.db.category = 'Mage'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Status\',statclass=\'Merit\',subentry=\'Mysterium\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'M:tA p. 101'
    merit.db.info = 'This Merit reflects a deeper inclusion into Mysterium secrets than the Mysterium Status Merit normally grants. Mystery Initiation opens the doors to the communal experience of living magic the Mysterium calls the egregore. Access to the egregore opens certain techniques for use within Mysterium rituals.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Eidetic_Memory')
    merit.db.longname = 'Eidetic Memory'
    merit.db.category = 'Mental'
    merit.db.range = [2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 44'
    merit.db.info = 'Your character recalls events and details with pinpoint accuracy. You do not have to make rolls for your character to remember past experiences. When making Intelligence + Composure (or relevant Skill) rolls to recall minute facts from swaths of information, take a +2 bonus.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Elemental_Warrior')
    merit.db.longname = 'Elemental Warrior'
    merit.db.category = 'Changeling'
    merit.db.range = ['1', '2', '3', '4', '5']
    merit.db.prereq = 'target.template().lower() == \'changeling\' and (target.dexterity() >= 3 or target.wits() >= 3) and (target.brawl() >= 2 or target.firearms() >= 2  or target.weaponry() >= 2) and (target.get(\'Elemental Weapon\', statclass=\'Contract\') or target.get(\'Primal Glory\', statclass=\'Contract\') or target.get(\'Seeming\', statclass=\'Sphere\').lower() == \'elemental\')'
    merit.db.noteRestrictions = ["'*'"]
    merit.db.reference = 'CtL p. 113'
    merit.db.info = 'Choose one physical element when you purchase this Merit, such as wind, flame, or wood. Your character commands it in battle; all of the following effects apply only to the chosen element.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Embodiment_of_the_Firstborn')
    merit.db.longname = 'Embodiment of the Firstborn'
    merit.db.category = 'Werewolf'
    merit.db.range = [5]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Tribe\',statclass=\'Sphere\').lower() != \'ghost wolves\''
    merit.db.noteRestrictions = ['Intelligence', 'Wits', 'Composure', 'Strength', 'Dexterity', 'Stamina', 'Presence', 'Manipulation', 'Resolve']
    merit.db.reference = 'W:tF p. 106'
    merit.db.info = 'Your character is the perfect likeness of one of Father Wolf\'s brood. She looks the part so very closely that she shakes the souls of her onlookers. Choose an Attribute that reflects her relationship to the Firstborn. She gains a dot in that Attribute, and that Attribute can go one above the normal maximum - normally six dots, unless she has an advanced level of Primal Urge. She can draw on her bearing to cow her opponents. When the player spends a point of Willpower, anyone who tries to attack the character that turn gains the Shaken Condition.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Empath')
    merit.db.longname = 'Empath'
    merit.db.category = 'General'
    merit.db.range = [2]
    merit.db.prereq = 'target.empathy() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 42'
    merit.db.info = 'Your character has seen pain, and can identify it instantly. With a single Wits + Empathy roll, you can identify any mental Conditions from which a character suffers, and his Integrity. A character trying to hide this can contest with Manipulation + Subterfuge, but may roll no more dice than his Integrity or other relevant trait. If he does not have Integrity, you get an idea of his general, abstract state and internal conflicts. For example, a vampire has Humanity instead of Integrity. Your character might know that the'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Enchanting_Performance')
    merit.db.longname = 'Enchanting Performance'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.template().lower() == \'changeling\' and target.presence() >= 3 and target.expression() >=3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 113'
    merit.db.info = 'A character with Enchanting Performance can touch upon whatever font makes all things fae so captivating. She brings a little of that magical obsession from beyond the Hedge and puts it to use. Whether she does so for cruelty or kindness depends on the changeling.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Encyclopedic_Knowledge')
    merit.db.longname = 'Encyclopedic Knowledge'
    merit.db.category = 'Mental'
    merit.db.range = [2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 44'
    merit.db.info = 'Choose a Skill. Due to an immersion in academia, pop culture, or a hobby obsession, your character has collected limitless factoids about the topic, even if she has no dots in the Skill.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Enhanced_Item')
    merit.db.longname = 'Enhanced Item'
    merit.db.category = 'Mage'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'M:tA p. 101'
    merit.db.info = 'Your character owns an item enhanced by indefinite Duration spells, which permanently modify the item\'s properties.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Enticing')
    merit.db.longname = 'Enticing'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and not (target.get(\'Atrocious\',statclass=\'Merit\') >= 1) and not (target.get(\'Cutthroat\',statclass=\'Merit\') >= 1)'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 112'
    merit.db.info = 'Your character\'s seductive Beast oozes with ease and confidence. Her smoky looks tantalize the imagination. Every movement of her hands makes promises. Any rolls to invoke the seductive Beast gain the 8-again quality.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Eye_for_the_Strange')
    merit.db.longname = 'Eye for the Strange'
    merit.db.category = 'Mental'
    merit.db.range = [2]
    merit.db.prereq = 'target.resolve() >= 2 and target.occult >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 44'
    merit.db.info = 'While your character does not necessarily possess a breadth of knowledge about the supernatural, she knows the otherworldly when she sees it. By perusing evidence, she can determine whether something comes from natural or supernatural origins. Roll Intelligence + Composure. With a success, the Storyteller must tell you if the scene has a supernatural cause, and provide one piece of found information that confirms the answer. With an exceptional success, she must give you a bit of supernatural folklore that suggests what type of creature caused the problem. If the problem was mundane, an exceptional success gives an ongoing +2 to all rolls to investigate the event, due to her redoubled certainty in its natural causation.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Fae_Mount')
    merit.db.longname = 'Fae Mount'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 113-114'
    merit.db.info = 'Your character has befriended a creature of the Hedge to serve as his steed. Through a special song or gesture, the mount comes to its master anywhere in the Hedge, except to the Hollow of a changeling who prohibits it.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Faerie_Favor')
    merit.db.longname = 'Faerie Favor'
    merit.db.category = 'Changeling'
    merit.db.range = [3]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 114'
    merit.db.info = 'The Gentry\'s promises bind them to a greater degree than those of the Lost do, and your character possesses such a promise. She is entitled to a favor from one of the True Fae. She may have gained this favor through anything from knowing a clever riddle to a dark deed done at the cost of another changeling\'s freedom. However she earned it, she has a bauble, song, or phrase that represents the favor, and when she breaks, sings, or utters it, the True Fae appears.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Fair_Harvest')
    merit.db.longname = 'Fair Harvest'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CtL p. 114-115'
    merit.db.info = 'Your character favors a particular flavor of Glamour. Choose a specific emotion when taking this Merit. With one dot, any rolls to harvest that emotion (p. 103) enjoy the 8-again quality. Rolls to harvest any other emotion do not benefit from the 10-again quality. At two dots, harvesting the favored emotion instead enjoys the rote quality, and you subtract one success from rolls to harvest other emotions in addition to the loss of 10-again.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Falconry')
    merit.db.longname = 'Falconry'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4]
    merit.db.prereq = 'target.wits() >= 3 and  target.animal_ken() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 48-49'
    merit.db.info = 'Your bird performs incredible feats at your command. You purchase this Merit for your character, who may apply it to any bird she shares the Bonded Condition with after a reasonable amount of time training together. Used for both hunting and sport, this practice has roots going back into antiquity and among numerous cultures. While not as widespread now as in the past, finding a trainer for this style is still relatively easy. Unless otherwise noted, these Merits constitute actions the bird takes independently, with only a simple, one-word or gesture command. Thus, your character does not have to dedicate an action to make them happen. Additionally, possession of this Merit allows your character to spend Willpower to benefit the bird\'s actions in her presence.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Fame')
    merit.db.longname = 'Fame'
    merit.db.category = 'Social'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.get(entry=\'anonymity\') == 0'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 50'
    merit.db.info = 'Your character is recognized within a certain sphere, for a certain skill, or because of some past action or stroke of luck. This can mean favors and attention, it can also mean negative attention and scrutiny. When choosing the Merit, define what your character is known for. As a rule of thumb, one dot means local recognition, or reputation within a confined subculture. Two dots means regional recognition by a wide swath of people. Three dots means worldwide recognition to anyone that might have been exposed to the source of the fame. Each dot adds a die to any Social rolls among those who are impressed by your character\'s celebrity.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Familiar')
    merit.db.longname = 'Familiar'
    merit.db.category = 'Mage'
    merit.db.range = [2, 4]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'M:tA p. 101'
    merit.db.info = 'Your character has been bonded to a Familiar, an ephemeral entity (a ghost, spirit, or Goetia) that has agreed to partner her in exchange for safety from bleeding Essence. Design your familiar with the rules for ephemeral entities in Chapter Six; it may be wholly in Twilight or Fettered to an item or animal. Two dots in this Merit indicate a Rank 1 entity. Four dots indicate a Rank 2 entity.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Fast_Reflexes')
    merit.db.longname = 'Fast Reflexes'
    merit.db.category = 'Mental'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.wits() >= 3 or target.dexterity() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 44'
    merit.db.info = '+1 Initiative per dot'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Fast_Spells')
    merit.db.longname = 'Fast Spells'
    merit.db.category = 'Mage'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'mage\' and target.firearms() >= 2 and target.get(\'Time\',statclass=\'Arcana\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'M:tA p. 101'
    merit.db.info = 'Your character\'s Aimed spells streak out with the speed of bullets. Subjects may not apply their Defense against your Aimed Spell rolls unless they use a Supernatural power that allows them to use Defense against firearms.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Fast-Talking')
    merit.db.longname = 'Fast-Talking'
    merit.db.category = 'Social'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.manipulation() >= 3 and target.subterfuge () >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 50-51'
    merit.db.info = 'Your character talks circles around listeners. He speaks a mile a minute, and often leaves his targets reeling, but nodding in agreement.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Favored_Form')
    merit.db.longname = 'Favored Form'
    merit.db.category = 'Werewolf'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Primal Urge\',statclass=\'Power\') >= (value + 1)'
    merit.db.noteRestrictions = ['Dalu', 'Gauru', 'Urshul', 'Urhan']
    merit.db.reference = 'W:tF p. 106'
    merit.db.info = 'Your character favors one of her four forms aside from Hishu, and when she takes that form, it\'s larger, stronger, and faster than most Uratha. With each dot in this Merit, he gains a specific, additional advantage in that form. Attribute increases from this Merit apply to derived traits.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Feeding_Grounds')
    merit.db.longname = 'Feeding Grounds'
    merit.db.category = 'Vampire'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'VtR p. 112'
    merit.db.info = 'Your character has fertile feeding grounds, whether officially granted or not. Dots in this Merit represent the ease of hunting in that territory. Add the dot rating to any hunting rolls, and to starting Vitae rolls (see p. 95). In addition, add the dot rating to any predatory aura conflicts on her territory.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Fighting_Finesse')
    merit.db.longname = 'Fighting Finesse'
    merit.db.category = 'Fighting'
    merit.db.range = [2]
    merit.db.prereq = 'target.dexterity() >= 3 and (subentry.split(\':\')[0].lower() == \'brawl\' or note.split(\':\')[0].lower() == \'weaponry\') and subentry in target.db.specialties'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 61'
    merit.db.info = 'Choose a Specialty in Weaponry or Brawl when you purchase this Merit. Your character\'s extensive training in that particular weapon or style has allowed them to benefit more from their alacrity and agility than their strength. You may substitute your character\'s Dexterity for her Strength when making rolls with that Specialty.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Firebrand')
    merit.db.longname = 'Firebrand'
    merit.db.category = 'Changeling'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'changeling\' and target.get(\'mantle\',\'summer\') >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 115'
    merit.db.info = 'Your character has the spirit of Summer within him, and channels that wrath into others. Once per scene, when your character goads someone into a fight, he regains a single Willpower point.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Firefight')
    merit.db.longname = 'Firefight'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.composure() >= 3 and target.dexterity() >= 3 and target.athletics() >= 2 and target.firearms() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 61-62'
    merit.db.info = 'Your character is comfortable with a gun. She\'s been trained in stressful situations, and knows how to keep herself from being shot, while still shooting at her opponents. This Style is about moving, strafing, and taking shots when you get them. It\'s not a series of precision techniques; it\'s for using a gun practically in a real-world situation.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Fixer')
    merit.db.longname = 'Fixer'
    merit.db.category = 'Social'
    merit.db.range = [2]
    merit.db.prereq = 'target.get(entry = \'contacts\') >= 2 and target.wits() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 51'
    merit.db.info = 'Your character is people that knows people. She can not only get in touch with the right people to do a job, but she can get them at the best possible prices. When hiring a service (see p. 100), reduce the Availability score of the service by one dot.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Flanking')
    merit.db.longname = 'Flanking'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower == \'werewolf\' and target.get(\'Cunning\',statclass=\'Renown\') >= 2 and target.wits() >= 3 and target.stealth() >= 2 and target.brawl() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p.108'
    merit.db.info = 'Your character can support another character by poking at an enemy\'s flanks. She grabs, bites, or otherwise restrains an opponent, setting it up for an opportune strike from a packmate. Any time your character makes a successful attack you can choose to apply successes as a penalty to the victim\'s Initiative and Defense for the turn instead of causing damage.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Fleet_of_Foot')
    merit.db.longname = 'Fleet of Foot'
    merit.db.category = 'Physical'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.athletics() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 47'
    merit.db.info = 'Your character is remarkably quick, and runs far faster than his frame suggests. He gains +1 Speed per dot, and anyone pursuing him suffers a -1 per dot to any foot chase rolls.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Fortified_Form')
    merit.db.longname = 'Fortified Form'
    merit.db.category = 'Werewolf'
    merit.db.range = [3, 4, 5]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.stamina() >= 3 and target.survival() >= 2'
    merit.db.noteRestrictions = ['Dalu', 'Gauru', 'Urshul', 'Urhan']
    merit.db.reference = 'W:tF p. 106'
    merit.db.info = 'Your character has one form that\'s particularly durable compared to her others. Choose a form other than Hishu when purchasing this Merit. That form has tougher hide, thicker fur, and stronger bones. At the three-dot version, this offers 1/0 armor in that form. The four dot offers 1/1 armor. The five dot offers 2/2 armor.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Friends_in_High_Places')
    merit.db.longname = 'Friends in High Places'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\',subentry=\'Invictus\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 112'
    merit.db.info = 'The Invictus have their fingers in a lot of pies...but any one vampire only has so many fingers. So the vampires of the First Estate do not just leverage their personal connections - they leverage each other\'s. An Invictus member can always do a little horse trading.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Gentrified_Bearing')
    merit.db.longname = 'Gentrified Bearing'
    merit.db.category = 'Changeling'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'changeling\' and target.get(\'wyrd\') >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 115'
    merit.db.info = 'Your character was molded in the image of her Keeper, stole some essential spark of its fire, or learned to emulate its otherness. Regardless of how she obtained this mixed blessing, hobgoblins tend to mistake her for a True Fae - if only for a moment.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Giant')
    merit.db.longname = 'Giant'
    merit.db.category = 'Physical'
    merit.db.range = [3]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 47'
    merit.db.info = 'Your character is massive. She\'s well over six feet tall, and crowds part when she approaches. She\'s Size 6, and gains +1 Health.'
    merit.db.cg_only = True
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Glamour_Fasting')
    merit.db.longname = 'Glamour Fasting'
    merit.db.category = 'Changeling'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 115'
    merit.db.info = 'Your character can endure without Glamour longer than others. As long as he has Willpower remaining, he doesn\'t suffer from deprivation when he drops to Glamour 0 (or below his Wyrd, for high-Wyrd changelings) until one full chapter has passed since he last had any Glamour.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Goblin_Bounty')
    merit.db.longname = 'Goblin Bounty'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 115'
    merit.db.info = 'The Lost has access to a regular bounty of goblin fruit and oddments. She may personally cultivate them, or scavenge them from a secret place in the Hedge that only she knows about. She has access to three times her dots in this Merit of common goblin fruits and oddments per chapter. Depending on her Wyrd, she may not be able to carry them with her all at once, but the rest are stored somewhere safe and do not require a special scene to access.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Good_Time_Management')
    merit.db.longname = 'Good Time Management'
    merit.db.category = 'Mental'
    merit.db.range = [1]
    merit.db.prereq = 'target.academics() >= 2 or target.science() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 44'
    merit.db.info = 'Your character has vast experience managing complex tasks, keeping schedules, and meeting deadlines. When taking an extended action, halve the time required between rolls.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Grappling')
    merit.db.longname = 'Grappling'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.stamina() >= 3 and target.strength() >= 2 and target.athletics() >= 2 and target.brawl() >= 2'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 62 and HL p. 49'
    merit.db.info = 'Your character has trained in wrestling, or one of many grappling martial arts.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Greyhound')
    merit.db.longname = 'Greyhound'
    merit.db.category = 'Physical'
    merit.db.range = [1]
    merit.db.prereq = 'target.athletics() >= 3 and target.wits() >= 3 and target.stamina() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 48'
    merit.db.info = 'Your character works best when chasing or being chased; the hunt is in his blood. When in a chase (see p. 84), you receive the effects of an exceptional success on three successes instead of five.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Grimoire')
    merit.db.longname = 'Grimoire'
    merit.db.category = 'Mage'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'M:tA p. 101'
    merit.db.info = 'Your character has discovered a Grimoire. If she is capable of casting the spells described, she may use the Grimoire to learn those rotes with Experiences, or cast following the Grimoire\'s instructions to gain the rote quality (see p. 214).'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Ground_Fighter')
    merit.db.longname = 'Ground Fighter'
    merit.db.category = 'Fighting'
    merit.db.range = [3]
    merit.db.prereq = 'target.wits() >= 3 and target.dexterity() >= 3 and target.brawl() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 54'
    merit.db.info = 'Your character knows how to fight from her back. Many mixed martial arts styles emphasize being able to fight from the ground. Brawl and weaponry attacks do not gain the +2 bonus to attack your character when prone. She can perform the Stand Up maneuver.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Ground_and_Pound')
    merit.db.longname = 'Ground and Pound'
    merit.db.category = 'Fighting'
    merit.db.range = [2]
    merit.db.prereq = 'target.brawl() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 54'
    merit.db.info = 'Your character skillfully uses gravity to drop a fist, elbow, knee, or other strike on a prone opponent. When using Brawl to strike or inflict the Damage grappling maneuver on a prone opponent, you may declare your character uses this maneuver. You gain the rote benefit (re-roll failed dice) to your attack, but automatically fall prone; and if grappled, your opponent automatically breaks free.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Grounded')
    merit.db.longname = 'Grounded'
    merit.db.category = 'Changeling'
    merit.db.range = [3]
    merit.db.prereq = 'target.template().lower == \'changeling\' and target.get(\'Mantle\',subentry=\'Spring\',statclass=\'Merit\') >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 115'
    merit.db.info = 'Your character\'s connection to the Spring Court makes him sure of himself and his perceptions. Even when he is at his weakest and most vulnerable, the verdant life of Spring protects him. He has an armor rating of 1 against all Clarity attacks that deal mild damage.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Hallow')
    merit.db.longname = 'Hallow'
    merit.db.category = 'Mage'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'M:tA p. 101'
    merit.db.info = 'Your character has secured a Hallow, a nexus of magical energies that seeps Mana into the world. A Hallow produces one Mana per dot in the Merit per day. When choosing this Merit, determine how the Hallow leaks Mana into the world. Mana that is not harvested congeals quickly into tass. Left to its devices, the Hallow can store three times its dot rating in tass before it becomes "dormant" and stops producing Mana until all of the tass is harvested. As with Sanctum and Safe Place, a Hallow can be shared between a cabal.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Hardy')
    merit.db.longname = 'Hardy'
    merit.db.category = 'Physical'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.stamina() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 47'
    merit.db.info = 'Your character\'s body goes further than it rightfully should. Add the dots in this Merit to any rolls to resist disease, poison, deprivation, unconsciousness, or suffocation.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Haven')
    merit.db.longname = 'Haven'
    merit.db.category = 'Vampire'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Safe Place\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'VtR p. 112'
    merit.db.info = 'A good haven is not only safe from the sun, but also familiar and comforting. The dot rating reflects your character\'s affinity for his home and its defenses against the sun\'s intrusion. A low rating might mean an unreliable apartment with boarded windows. A high rating may mean an ancestral home with no windows and an extensive system of vaults.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Headbutt')
    merit.db.longname = 'Headbutt'
    merit.db.category = 'Fighting'
    merit.db.range = [1]
    merit.db.prereq = 'target.brawl() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 54'
    merit.db.info = 'Your character has found few arguments she can\'t end by ramming her skull into a softer part of the human anatomy. This Merit allows for a new grappling maneuver.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Hearing_Whispers')
    merit.db.longname = 'Hearing Whispers'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Tribe\',statclass=\'Sphere\').lower() == \'bone shadows\''
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 106'
    merit.db.info = 'Your Bone Shadow sees the deep, dark, and embarrassing in people. With a turn of scrutiny, she can identify the subject\'s Persistent Conditions. If your character suspects additional weaknesses, she can identify them with a Wits + Skill roll. Each weakness requires a separate roll, and at least a turn of scrutiny; the Storyteller determines the Skill by the weakness your character suspects. Having no dots in a Skill qualifies as a weakness for this purpose, as well as does anything else the Storyteller deems fit. This can\'t identify a spirit\'s ban.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Heavy_Weapons')
    merit.db.longname = 'Heavy Weapons'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.stamina() >= 3 and target.strength() >= 3 and target.athletics() >=2 and target.weaponry() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 62'
    merit.db.info = 'Your character is trained with heavy weapons which require strength, wide range, and follow through more than direct speed and accuracy. This Style may be used with a two-handed weapon such as a claymore, chainsaw, pike, or an uprooted street sign.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Hedge_Brawler')
    merit.db.longname = 'Hedge Brawler'
    merit.db.category = 'Changeling'
    merit.db.range = [2]
    merit.db.prereq = 'target.template.lower() == \'changeling\' and (target.brawl() >= 2 or target.firearms() >= 2 or target.weaponry() >= 2)'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 115'
    merit.db.info = 'Your character is adept at fighting within the Hedge. You may take a dice penalty on a violent action designated for Hedgespinning between −1 and −3 to gain that number of extra successes if the action is successful. You can only use these successes for shaping Hedge details; this can\'t turn a normal success into an exceptional one.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Hedge_Duelist')
    merit.db.longname = 'Hedge Duelist'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = '(target.template().lower() == \'changeling\') and (target.presence() >= 2 or target.manipulation() >=  2) and (target.brawl() >=2 or target.weaponry() >= 2) and (target.animal_ken() >= 2 or target.empathy() >= 2 or target.expression() >= 2 or target.intimidation() >= 2 or target.persuasion() >= 2 or target.socialize() >= 2 or target.streetwise() >= 2 or target.subterfuge() >= 2)'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 115'
    merit.db.info = 'Your character is a skilled fae duelist, capable of turning the Hedge into a weapon. Each duelist adopts a different style. A capricious sword dancer might taunt and tease the Hedge into action, while a king of beasts calls Glamour phantoms and Hedge fiends to aid him, and a druidic sorcerer communes with the Hedge, its voice guiding his movements. This Merit\'s effects only work in the Hedge proper.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Hedge_Sense')
    merit.db.longname = 'Hedge Sense'
    merit.db.category = 'Changeling'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 115'
    merit.db.info = 'The character is especially skilled at finding her way in the Hedge. Gain a two-die bonus to all rolls to navigate the Hedge, and to find Icons, food, shelter, or goblin fruit there.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Herd')
    merit.db.longname = 'Herd'
    merit.db.category = 'Vampire'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 112'
    merit.db.info = 'Your character cultivates cliques of mortals willing and eager for the Kiss. Each week, you can draw on a number of Vitae equal to twice the Merit\'s dot rating. This requires no roll, only a quick interlude. Taking more than that amount requires normal hunting rolls.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'High_Speech')
    merit.db.longname = 'High Speech'
    merit.db.category = 'Mage'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'M:tA p. 102'
    merit.db.info = 'The character can use High Speech as a Yantra in spellcasting'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Hob_Kin')
    merit.db.longname = 'Hob Kin'
    merit.db.category = 'Changeling'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 115-116'
    merit.db.info = 'Your character has established a kind of kinship with hobgoblins. It may be a matter of resemblance to a True Fae they fear, or something about his kith that encourages this behavior, but they show him a respect generally unheard of by the Lost. It isn\'t much like the respect of friends or peers, but they treat him less ruthlessly than'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Hobbyist_Clique')
    merit.db.longname = 'Hobbyist Clique'
    merit.db.category = 'Social'
    merit.db.range = [2]
    merit.db.prereq = 'target.get(subentry, \'Skill\') >= 2'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 51'
    merit.db.info = 'Your character is part of a group of hobbyists that specialize in one area, represented by a Skill. It may be a book club, a coven, a political party, or any group brought together by a common interest. When the group\'s support is available, you benefit from the 9-again quality on rolls involving the group\'s chosen Skill. As well, the clique offers two additional dice on any extended actions involving that Skill.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Holistic_Awareness')
    merit.db.longname = 'Holistic Awareness'
    merit.db.category = 'Mental'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 44-45'
    merit.db.info = 'Your character is skilled at non-traditional healing methods. While scientific minds might scoff, he can provide basic medical care with natural means. He knows what herbs can stem an infection, and what minerals will stave off a minor sickness. Unless your patient suffers wound penalties from lethal or aggravated wounds, you do not need traditional medical equipment to stabilize and treat injuries. With access to woodlands, a greenhouse, or other source of diverse flora, a Wits + Survival roll allows your character to gather all necessary supplies.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Hollow')
    merit.db.longname = 'Hollow'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CtL p. 116-117'
    merit.db.info = 'While Safe Place (p. 125) represents a mundane-but-secure lair outside the Hedge, Hollow is your character\'s secret, private bit of real estate inside the Hedge. It may be something as simple as a closet door that opens into a quiet, hollowed-out tree, or as elaborate as a knock that opens any unlocked door into a lavish, gothic mansion. These locations are as varied as the Hedge itself.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Honey_Trap')
    merit.db.longname = 'Honey Trap'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 112'
    merit.db.info = 'Your character\'s blood not only bonds, but it invigorates. When a vampire tastes your character\'s Vitae, she regains a point of Willpower. If this results in a new bond, or steps up an existing bond, she also takes a Beat.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'I_Know_a_Guy')
    merit.db.longname = 'I Know a Guy'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\',subentry=\'Carthian\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 115'
    merit.db.info = 'When Carthians make Allies (see p. 118), their covenant acts as a sort of support network that bolsters the efficiency of those allies. Once per story, a Carthian may access temporary Retainer dots equal to their Allies. These Retainers act in the Carthian\'s interest, just like any other Retainers. (Since Allies gained with Carthian Pull don\'t really belong to the character as a Merit, they don\'t count for purposes of I Know A Guy.)'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Imbued_Item')
    merit.db.longname = 'Imbued Item'
    merit.db.category = 'Mage'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'M:tA p. 102'
    merit.db.info = 'An Imbued Item is an item storing a spell that does not have an indefinite duration, and Mana with which to cast that spell. When creating an Imbued Item for your game, choose a spell. The item contains that spell, and a user (even a Sleeper) may trigger the spell if she knows the method of triggering. The method is usually a simple word or gesture, but the creator can make it as complex as he wishes. The spell always requires at least one point of Mana; if the spell would require Mana, use that amount. If it would normally not require Mana, it requires one point. When a user triggers the spell, the player rolls to cast it with a dice pool of the spell\'s Arcanum rating plus the user\'s Gnosis (if Awakened).'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Impartial_Mediator')
    merit.db.longname = 'Impartial Mediator'
    merit.db.category = 'Werewolf'
    merit.db.range = [3]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Honor\',statclass=\'Renown\') >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 106-107'
    merit.db.info = 'Your character can cut to the heart of an argument. She can intervene between arguing parties to cut to the truth - or favor one side over another with nobody doubting her impartiality. When she steps into an argument or debate and spends time listening to both sides, roll Presence + Persuasion + Honor versus the highest Resolve + Honor on each side. If you score more successes than one side\'s contested roll, that side accepts your interpretation of the truth.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Improvised_Weaponry')
    merit.db.longname = 'Improvised Weaponry'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.wits() >= 3 and target.weaponry >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 62-63'
    merit.db.info = 'Most people don\'t walk around armed. While someone pulling a knife or a gun can cool a hostile situation down, it can also cause things to boil over - an argument that wouldn\'t be more than harsh words suddenly ends up with three people in the morgue. If your character is on the receiving end of someone pulling a knife, it helps to have something in his hand as well.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Indomitable')
    merit.db.longname = 'Indomitable'
    merit.db.category = 'Mental'
    merit.db.range = [2]
    merit.db.prereq = 'target.resolve() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 45'
    merit.db.info = 'Your character possesses an iron will. The powers of the supernatural have little bearing on her behavior. She can stand up to a vampire\'s mind control, a witch\'s charms, or a ghost\'s gifts of fright. Any time a supernatural creature uses a power to influence your character\'s thoughts or emotions, add two dice to the dice pool to contest it. If the roll is resisted, instead subtract two dice from the monster\'s dice pool. Note that this only affects mental influence and manipulation from a supernatural origin. A vampire with a remarkable Manipulation + Persuasion score is just as likely to convince your character to do something using mundane tricks.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Infamous_Mentor')
    merit.db.longname = 'Infamous Mentor'
    merit.db.category = 'Mage'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.template().lower() == \'mage\' and target.get(\'Mentor\',statclass=\'Merit\') >= value'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'M:tA p. 102'
    merit.db.info = 'Your character\'s Mentor is of particularly strong repute. This may be negative or positive. When taking this Merit, determine the Mentor\'s Order and Consilium Status. They should be close to the Mentor dot rating. As well, choose Social Merits equal to twice the Infamous Mentor dots. Your character can access these Merits and Status, so long as she\'s willing to name-drop her Mentor and live with the consequences.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Inspiring')
    merit.db.longname = 'Inspiring'
    merit.db.category = 'Social'
    merit.db.range = [3]
    merit.db.prereq = 'target.presence() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 51'
    merit.db.info = 'Your character\'s passion inspires those around her to greatness. With a few words, she can redouble a group\'s confidence or move them to action.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Instinctive_Defense')
    merit.db.longname = 'Instinctive Defense'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower == \'werewolf\' and target.get(\'Primal Urge\',statclass=\'Power\') >= 2 and target.athletics() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p.108'
    merit.db.info = 'Your character\'s instincts protect her when in her canine forms. In Urhan and Urshul, use the higher of your character\'s Wits and Dexterity when figuring her Defense, instead of the lower.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Interdisciplinary_Specialty')
    merit.db.longname = 'Interdisciplinary Specialty'
    merit.db.category = 'Mental'
    merit.db.range = [1]
    merit.db.prereq = 'target.get(subentry.split(\':\')[0], search_type = \'Skill\') >= 3 and subentry in target.db.specialties'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 45'
    merit.db.info = 'Choose a Specialty that your character possesses when you purchase this Merit. You can apply the +1 from that Specialty on any Skill with at least one dot, provided it\'s justifiable within the scope of the fiction. For example, a doctor with a Medicine Specialty in Anatomy may be able to use it when targeting a specific body part with Weaponry, but could not with a general strike.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Invested')
    merit.db.longname = 'Invested'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\',subentry=\'Invictus\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 112'
    merit.db.info = 'In the Invictus, you get out what you put in. Through doing favors and making herself noticed, your character has gotten back plenty. Divide dots equal to your Invictus status in the Herd, Mentor, Resources, and Retainers Merits. You may distribute them as you like. These dots can be added to existing Merit dots, or added upon later. If she loses dots of Status, the dots granted by this Merit go away as well.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Investigative_Aide')
    merit.db.longname = 'Investigative Aide'
    merit.db.category = 'Mental'
    merit.db.range = [1]
    merit.db.prereq = 'get.target(subentry,statclass=\'Skill\') >= 3'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 45'
    merit.db.info = 'Your character has one particular knack that can contribute amazingly to an investigation. Choose a Skill when purchasing this Merit; when making rolls to Uncover Clues (see p. 79), she achieves exceptional success on three successes instead of five. As well, Clues that come from her use of that Skill start with one additional element.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Investigative_Prodigy')
    merit.db.longname = 'Investigative Prodigy'
    merit.db.category = 'Mental'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.wits() >= 3 and target.investigation >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 45'
    merit.db.info = 'Your character investigates instinctively, and can intuit details and connections in a scene without much time. He\'s a veritable Sherlock Holmes. Instead of simply uncovering Clues or not uncovering Clues when investigating (see p. 79), your character discovers multiple Clues in a single action. Your character can uncover Clues equal to his successes or his Merit dots as an instant action, whichever is lower.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Iron_Chin')
    merit.db.longname = 'Iron Chin'
    merit.db.category = 'Fighting'
    merit.db.range = [2, 4]
    merit.db.prereq = 'target.resolve() >= 3 and target.stamina() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 54'
    merit.db.info = 'Your character\'s taken her share of beatings and can\'t be scared by pain or the sight of her own blood. This Merit comes in two levels. At ** dots, she no longer suffers the Beaten Down Tilt from any amount of bashing damage. At **** dots, she never suffers Beaten Down, period. This is probably more foolhardy than brave. If your chronicle doesn\'t feature conflicts where Beaten Down features prominently, don\'t use this Merit.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Iron_Skin')
    merit.db.longname = 'Iron Skin'
    merit.db.category = 'Fighting'
    merit.db.range = [2, 4]
    merit.db.prereq = '(target.get(\'Martial Arts\') >= 2 or target.get(\'Street Fighting\') >= 2) and target.stamina >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 63'
    merit.db.info = 'Through rigorous conditioning, or extensive scarring, your character has grown resistant to harm. She can shrug off shots that would topple bigger fighters. She knows how to take a strike, and can even move into a hit from a weapon to minimize harm. She gains armor against bashing attacks; one point of armor with **, and two points of armor with ****. By spending a point of Willpower when hit, she can downgrade some lethal damage from a successful attack into bashing. Downgrade one damage at **, two with ****.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Iron_Stamina')
    merit.db.longname = 'Iron Stamina'
    merit.db.category = 'Physical'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.stamina() >= 3 or target.resolve() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 48'
    merit.db.info = 'Each dot eliminates a negative modifier (on a one-for-one basis) when resisting the effects of fatigue or injury. For example: A character with Iron Stamina ** is able to ignore up to a -2 modifier brought on by fatigue. The Merit also counteracts the effects of wound penalties. So, if all of your character\'s Health boxes are filled (which normally imposes a -3 penalty to his actions) and he has Iron Stamina *, those penalties are reduced to -2. This Merit cannot be used to gain positive modifiers for actions, only to cancel out negative ones.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Iron_Will')
    merit.db.longname = 'Iron Will'
    merit.db.category = 'Social'
    merit.db.range = [2]
    merit.db.prereq = 'target.resolve() >= 4'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 51'
    merit.db.info = 'Your character\'s resolve is unwavering. When spending Willpower to contest or resist in a Social interaction, you may substitute your character\'s Resolve for the usual Willpower bonus. If the roll is contested, roll with 8-again.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'K-9')
    merit.db.longname = 'K-9'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4]
    merit.db.prereq = 'target.wits() >= 3 and target.animal_ken() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 49-50'
    merit.db.info = 'Under your supervision a dog may perform exceptional actions. You purchase this Merit for your character, who may apply it to any dog she shares the Bonded Condition with after a reasonable amount of training time together. Police and military forces are the place to go to learn to work with an animal in combat, but independent trainers might know this style as well.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Kindred_Dueling')
    merit.db.longname = 'Kindred Dueling'
    merit.db.category = 'Vampire'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.template().lower() == \'vampire\' and target.composure() >= 3 and target.weaponry() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 117-118'
    merit.db.info = 'Your character is not only a competent fighter, but also one trained specifically to take advantage of Kindred variables in a fight. Use of Kindred dueling requires an edged weapon. While humans could theoretically learn some of these tricks, the practical experience required could prove deadly. Note that Kindred Dueling abilities may not be used together. If you\'re using Hamstring, you cannot benefit from Carving as well.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Kino_Mutai')
    merit.db.longname = 'Kino Mutai'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4]
    merit.db.prereq = 'target.dexterity() >= 2 and target.resolve() >= 3 and target.brawl() > = 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 50'
    merit.db.info = 'Your character learns to bite opponents, tear at soft tissues and gouge eyes with special skills. This is sometimes called "Kino Mutai" in Filipino martial arts, but it can be learned by anyone uninhibited enough to use these unconventional methods to the greatest extent possible for humans. Thus, this Fighting Style only works for beings with a human body plan and a decent set of teeth.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Kiss_of_the_Succubus')
    merit.db.longname = 'Kiss of the Succubus'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Clan\',statclass=\'Sphere\').lower() == \'daeva\''
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 113'
    merit.db.info = 'All Kindred can evoke lustful, passionate reactions with a bite. The Daeva\'s bite is downright addicting. Her Kiss causes the Addicted Condition in mortals as well as the Swooning Condition (for Addicted, see p. 301; for Swooning, see p. 306).'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Language')
    merit.db.longname = 'Language'
    merit.db.category = 'Mental'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 45'
    merit.db.info = 'Your character is skilled with an additional language, beyond her native tongue. Choose a language each time you buy this Merit. Your character can speak, read, and write in that language.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Laying_on_Hands')
    merit.db.longname = 'Laying on Hands'
    merit.db.category = 'Supernatural'
    merit.db.range = [3]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 57'
    merit.db.info = 'Your character\'s faith or force of devotion becomes a wholesome force that heals the sick and mends injuries. However, she takes some of those injuries upon herself by proxy.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Lethal_Mien')
    merit.db.longname = 'Lethal Mien'
    merit.db.category = 'Changeling'
    merit.db.range = [2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 117'
    merit.db.info = 'The Hedge warped some element of your character\'s fae mien, and left him with wicked nails, sharp teeth, or some other offensive trait. The changeling can inflict lethal damage while unarmed. If another power already gives him the capacity for lethal blows, such as the Beast seeming blessing, add one to his unarmed weapon modifier instead.|/|/The character may choose whether to use the benefit of these claws, fangs, spurs, or other dangerous element at will.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Lex_Terrae')
    merit.db.longname = 'Lex Terrae'
    merit.db.category = 'Vampire'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\', subentry=\'Carthian\', statclass=\'Merit\') >= 2 and target.get(\'Feeding Ground\', statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 116'
    merit.db.info = 'Territory is bond. Feeding ground is sacrosanct. Any blood poached from your character\'s Feeding Ground is tainted for Kindred she has not specifically allowed. When next a poacher sleeps, the blood dissolves in his gullet. When he wakes, he violently retches, taking one bashing damage per Vitae lost. As well, his lips and mouth stain with black streaks that paint him as a poacher. These marks last for one week.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Library')
    merit.db.longname = 'Library'
    merit.db.category = 'Mental'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 46'
    merit.db.info = 'Your character has access to a plethora of information about a given topic. When purchasing this Merit, choose a Mental Skill. The Library covers that purview. On any extended roll involving the Skill in question, add the dots in this Merit.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Light_Weapons')
    merit.db.longname = 'Light Weapons'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = '(target.get(\'Fighting Finesse\',\'Weaponry\') == 2 or target.wits() >= 3) and target.dexterity() >= 3 and target.athletics() >= 2 and target.weaponry() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 63'
    merit.db.info = 'Your character is trained with small hand-to-hand weapons which favor finesse over raw power. These maneuvers may only be used with one-handed weapons with a damage rating of two or less.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Lineage')
    merit.db.longname = 'Lineage'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and (target.get(\'Status\', subentry=target.get(\'Clan\',statclass=\'Sphere\'), statclass=\'Merit\') >= 1 or target.get(\'Status\',subentry=\'Clan\',statclass=\'Merit\') >= 1)'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 113'
    merit.db.info = 'You come from strong stock. Your sire\'s well known, and his influence bleeds onto your interactions. Once per chapter, this Merit can represent a single dot of one of the following Merits: Allies, Contacts, Mentor, Resources, or Status. The Merit must be one your sire may have possessed.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Living_Weapon')
    merit.db.longname = 'Living Weapon'
    merit.db.category = 'Werewolf'
    merit.db.range = [3, 4, 5]
    merit.db.prereq = 'target.stamina() >= 3 and target.survival() >= 2'
    merit.db.noteRestrictions = ['Dalu', 'Gauru', 'Urshul', 'Urhan']
    merit.db.reference = 'W:tF p. 107'
    merit.db.info = 'Your character has enhanced natural weapons in one form. Maybe her jaws are larger, her teeth are sharper, or her claws are hard as stone. Choose a form (Dalu, Gauru, Urshul, or Urhan) when purchasing this Merit, and choose either bite or claws. With three dots, the attack gains two levels of armor piercing (see p. 169). With four dots, increase the attack\'s damage by 1 atop its normal advantages. With five dots, it ignores any non-magical armor.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Lorekeeper')
    merit.db.longname = 'Lorekeeper'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\', subentry=\'Lancea et Sanctum\', statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 113'
    merit.db.info = 'The Spear is tasked with the acquisition and maintenance of history and mystical secrets. Most devoted members of the covenant establish and maintain libraries. Since most of this knowledge has to pass through mortal hands, the Sanctum also tends to attract those, likeminded, who wish to surround themselves with ancient secrets. When a member of the Lancea et Sanctum with this Merit buys the Library Merit (see p. 121), she also receives dots in the Retainers and Herd Merits, divided however she chooses.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Mandate_from_the_Masses')
    merit.db.longname = 'Mandate from the Masses'
    merit.db.category = 'Vampire'
    merit.db.range = [5]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\', subentry=\'Carthian\', statclass=\'Merit\') >= 5'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 116'
    merit.db.info = 'Carthians wield consensus the way a cop wields a baton. With the power of the Movement behind her, a ranking Carthian can call on the will of her people to strike weakness into the Movement\'s opposition. With her words and the mandate, she strips a Kindred enemy\'s blood down to nothingness. To enact this law, your character must make a clear and direct admonishment against one of the Movement\'s enemies. Cross a dot of Willpower off the Carthian\'s sheet. She must also garner the support of others of the Movement for a vote - from both Storyteller characters and players\' characters. If the vote favors the admonishment, add the total dots of Carthian Status in support (including the user\'s five). For every five dots, reduce the victim\'s Blood Potency by one dot. If this reduces him to zero dots, he effectively becomes a revenant (see p. 94 for rules on revenants).'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Mantle')
    merit.db.longname = 'Mantle'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['Spring', 'Summer', 'Autumn', 'Winter']
    merit.db.reference = 'CtL p. 117'
    merit.db.info = 'When a changeling joins a court, she accepts all its blessings and embodies it, the same way she does her own seeming and kith. Mantle represents the mystical connection a changeling has to the elements and emotions of her chosen court. As her Mantle rises, she becomes a better representation of what it is to be a courtier. A changeling with a high Mantle embodies the ideals of the court, and others who belong to the court recognize her dedication and give her respect, even if it\'s grudging.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Manymask')
    merit.db.longname = 'Manymask'
    merit.db.category = 'Changeling'
    merit.db.range = [3]
    merit.db.prereq = 'target.template().lower() == \'changeling\' and target.get(\'Wyrd\',statclass=\'Power\') >= 2 and target.manipulation() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 118-119'
    merit.db.info = 'A changeling is usually stuck with the same Mask he left the Hedge with, an immutable combination of remembered human traits. Some changelings develop control over the appearance of their Masks.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Market_Sense')
    merit.db.longname = 'Market Sense'
    merit.db.category = 'Changeling'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 119'
    merit.db.info = 'Understanding the value of a product is hard enough in the mortal world, but in the Hedge, relative worth is even more questionable. How does one weigh the importance of a dozen cherished memories against a music box that only plays near ghosts? Goblins make all sorts of strange requests in exchange for Contracts, but your character knows how to navigate these exchanges better than others.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Marksmanship')
    merit.db.longname = 'Marksmanship'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4]
    merit.db.prereq = 'target.composure() >= 3 and target.resolve() >= 3 and target.firearms() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 63'
    merit.db.info = 'When prepared and aimed, a gun is an ideal killing machine. Your character has trained to take advantage of the greatest features of a gun, usually a rifle, but this Style can be used with any gun. Because of the discipline and patience required for Marksmanship, your character cannot use her Defense during any turn in which she uses one of these maneuvers. These maneuvers may only be used after aiming for at least one turn.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Martial_Arts')
    merit.db.longname = 'Martial Arts'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.resolve() >= 3 and target.dexterity() >= 3 and target.athletics() >= 2 and target.brawl() >= 2'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 63-64 and HL p. 50'
    merit.db.info = 'Your character is trained in one or more formal martial arts styles. This may have come from a personal mentor, a dojo, or a self-defense class. It may have been for exercise, protection, show, or tradition. These maneuvers may only be used unarmed, or with weapons capable of using the Brawl Skill, such as a punch dagger, or a weapon using the Shiv Merit.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Meditative_Mind')
    merit.db.longname = 'Meditative Mind'
    merit.db.category = 'Mental'
    merit.db.range = [1, 2, 4]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 46'
    merit.db.info = 'Your character\'s meditation is far more fulfilling than for other characters. With the one-dot version of this Merit, the character does not suffer environmental penalties to meditation (see p. 75), even from wound penalties.|/|/With the two-dot version, when the character has successfully meditated, she gains a +3 bonus on any Resolve + Composure rolls during the same day, as she\'s steeled herself against the things in the world that would shake her foundation.|/|/At the four-dot level, she only needs a single success to gain the benefits of meditation for the day, instead of the normal four.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Medium')
    merit.db.longname = 'Medium'
    merit.db.category = 'Supernatural'
    merit.db.range = [3]
    merit.db.prereq = 'target.empathy() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 57'
    merit.db.info = 'Your character hears the words and moans of the dead. If he takes the time to parse their words, he can interact with them verbally.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Mentor')
    merit.db.longname = 'Mentor'
    merit.db.category = 'Social'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 51'
    merit.db.info = 'This Merit gives your character a teacher that provides advice and guidance. He acts on your character\'s behalf, often in the background, and sometimes without your character\'s knowledge. While Mentors can be highly competent, they almost always want something in return for their services. The dot rating determines the Mentor\'s capabilities, and to what extent he\'ll aid your character.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Mind_of_a_Madman')
    merit.db.longname = 'Mind of a Madman'
    merit.db.category = 'Supernatural'
    merit.db.range = [2]
    merit.db.prereq = 'target.empathy() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 57'
    merit.db.info = 'Your character gets deep under the skin of problems. If she\'s investigating a crime or other phenomenon, she can put herself in the mind of the culprit. This often helps with the case, however, it takes her to a dark place internally.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Moon-Kissed')
    merit.db.longname = 'Moon-Kissed'
    merit.db.category = 'Werewolf'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and subentry in find(target.get(\'Auspice\',statclass=\'Sphere\'),statclass=\'Auspice\')[0].db.auspice_skills and target.get(subentry,statclass=\'Skill\') >= 2'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'W:tF p. 107'
    merit.db.info = 'Your character\'s auspice affects her more than most. When taking this Merit, choose one of her three auspice Skills. That Skill has the 9-again quality. If you already have 9-again available, use 8-again. When her auspice moon is visible, spending Willpower gives +4 dice to rolls using that Skill instead of +3.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Mounted_Combat')
    merit.db.longname = 'Mounted Combat'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4]
    merit.db.prereq = 'target.dexterity() >= 3 and target.athletics() >= 2 and target.animal_ken() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 51'
    merit.db.info = 'Your character fights from horseback using the animal\'s size and maneuverability to make her attacks more effective. While trained cavalry regiments are largely a thing of the past, many police departments around the world still have officers who use techniques like these in the modern day.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Multilingual')
    merit.db.longname = 'Multilingual'
    merit.db.category = 'Mental'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 46'
    merit.db.info = 'Your character has a strong affinity for language acquisition. Each time you purchase this Merit, choose two languages. Your character can speak conversationally in those languages. With an Intelligence + Academics roll, he may also read enough of the language to understand context.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Mystery_Cult_Initiation')
    merit.db.longname = 'Mystery Cult Initiation'
    merit.db.category = 'Social'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 51-53'
    merit.db.info = 'Cults are far more common than people would like to admit. "Mystery cult" is the catch-all term for a phenomenon ranging from secret societies couched in fraternity houses, to scholarly cabals studying the magic of classical symbolism, to mystical suicide cults to the God-Machine.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Night_Doctor_Surgery')
    merit.db.longname = 'Night Doctor Surgery'
    merit.db.category = 'Vampire'
    merit.db.range = [3]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\', subentry=\'Carthian\', statclass=\'Merit\') >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 113-114'
    merit.db.info = 'Carthians have adapted a bit of real-world surgery and a little body horror into a series of morbid reconstruction techniques to help injured Kindred heal. Night Doctor Surgery helps bones reset, and speeds the knitting of flesh. With an hour of treatment, roll Intelligence + Medicine. Each success converts one point of lethal damage to bashing. Alternatively, three successes can convert one point of aggravated damage to lethal damage. Failure means the wounds remain; dramatic failure upgrades three points of bashing to lethal, or two lethal to aggravated. With Storyteller discretion, this Merit and Willpower expenditure may be used over time to make changes to facial appearance.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Noblesse_Oblige')
    merit.db.longname = 'Noblesse Oblige'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.template().lower() == \'changeling\' and target.get(\'Mantle\',subentry=subentry,statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = ['Spring', 'Summer', 'Autumn', 'Winter']
    merit.db.reference = 'CtL p. 119'
    merit.db.info = 'Your character knows how to harness the power of his Mantle to inspire others. Any time your character is in charge of a group of people who share his court, either through Mantle or Court Goodwill, he can grant benefits to the group (but not to himself) for a scene by spending a Willpower point. The benefit conferred depends on the court.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Notary')
    merit.db.longname = 'Notary'
    merit.db.category = 'Vampire'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'vampire\' and target.get(\'Status\',subentry=\'Invictus\',statclass=\'Merit\') >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 116-117'
    merit.db.info = 'The Invictus appointed your character a Notary, a scholar of Oaths. She presides over Oath agreements. Because of your standing as an arbiter of the status quo, Invictus may not use their Invictus Status in rolls against you. As well, each month, you may request access to a single dot of Allies, Contacts, Herd, Mentor, or Resources, granted by the covenant at large.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Nowhere_to_Run')
    merit.db.longname = 'Nowhere to Run'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template.lower() == \'werewolf\' and target.get(\'Tribe\',statclass=\'Sphere\').lower() == \'hunters in darkness\''
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 107'
    merit.db.info = 'Any Hunter in Darkness can track prey. Your character, however, has an instinctive awareness of his prey, and the places his prey considers "safe." Using subtle clues about his prey - like smells, fibers, and tracks - he can identify where his prey hides and recuperates. With a turn of scrutiny, he immediately knows basic details and a rough location of any Safe Place the prey has. With a Wits + Investigation roll, he can identify other dedicated sites, boltholes, and hiding places. Every success offers one such hangout.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Numbing_Touch')
    merit.db.longname = 'Numbing Touch'
    merit.db.category = 'Supernatural'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 58'
    merit.db.info = 'With Numbing Touch, your character\'s psychic gifts allow her to numb a person, rendering them sluggish and incompetent. With intense concentration, she can cause neurons to shut down.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Oath_of_Action')
    merit.db.longname = 'Oath of Action'
    merit.db.category = 'Vampire'
    merit.db.range = [4]
    merit.db.prereq = 'True'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'VtR p. 117'
    merit.db.info = 'With this Oath, a vassal swears to perform a service to his liege. The service must be a difficult task with definite criteria for accomplishment or failure. At the time of the swearing, both parties agree upon one of the liege\'s Disciplines. The vassal gains access to that Discipline. The liege\'s Blood Potency increases by one. This Oath stands as a rare exception to bloodline Disciplines: a vassal may temporarily access a liege\'s bloodline gift.'
    merit.db.cg_only = False
    merit.db.restricted = True

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Oath_of_Fealty')
    merit.db.longname = 'Oath of Fealty'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\', subentry=\'Invictus\', statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'VtR p. 117'
    merit.db.info = 'This most basic Oath establishes a foundation of trust within the Invictus. The vassal may draw a number of Vitae from his liege equal to his Invictus Status in a given week. This Vitae transfers mystically over any distance, and replenishes the vassal\'s pool without risk of Vitae addiction or blood bond. The liege always knows if the vassal lies to her, in voice or in writing.'
    merit.db.cg_only = False
    merit.db.restricted = True

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Oath_of_Penance')
    merit.db.longname = 'Oath of Penance'
    merit.db.category = 'Vampire'
    merit.db.range = [3]
    merit.db.prereq = 'True'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'VtR p. 117'
    merit.db.info = 'This Oath is a form of apology from a vassal to an aggrieved liege. For the agreed-upon term, the liege receives every tenth Vitae the vassal ingests. This Vitae comes over any distance, without risk of blood bond or addiction, and counts as Kindred Vitae. Some ancient Invictus use this Oath to skirt their need for Kindred blood, by establishing massive networks of "punished" vassals. During the same period, the vassal becomes immune to the liege\'s Discipline effects.'
    merit.db.cg_only = False
    merit.db.restricted = True

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Oath_of_Serfdom')
    merit.db.longname = 'Oath of Serfdom'
    merit.db.category = 'Vampire'
    merit.db.range = [2]
    merit.db.prereq = 'True'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'VtR p. 117'
    merit.db.info = 'This Oath is a contract between a landlord and a tenant. In Invictus domains, Princes often use this Oath as the go-to for granting territory. Young Invictus refer to this practice as "castling." Oath of Serfdom agreements typically involve "red rent," a certain blood tithe given to the landlord regularly.'
    merit.db.cg_only = False
    merit.db.restricted = True

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Object_Fetishism')
    merit.db.longname = 'Object Fetishism'
    merit.db.category = 'General'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 42'
    merit.db.info = 'Your character places immense trust and confidence in an object, often assuming it has mystical or otherworldly significance. He believes he\'s tied inexorably to the object. Choose a Skill Specialty when taking this Merit; that Specialty must be tied to your character\'s relationship to the object.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Omen_Sensititivity')
    merit.db.longname = 'Omen Sensititivity'
    merit.db.category = 'Supernatural'
    merit.db.range = [3]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 58'
    merit.db.info = 'Your character sees signs and patterns in everything. From the way the leaves fall, to the spray of antifreeze when his radiator pops, to the ratios of circumference on the shell he picked up on the sidewalk, everything has meaning. With some consideration, he can interpret these meanings. This would be far better if he could turn it off. Everything is important. Everything could mean the end of the world, the deaths of his friends, or other tragedies. If he misses an omen, it might be the wrong one.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Pack_Alpha')
    merit.db.longname = 'Pack Alpha'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Clan\', statclass=\'Sphere\').lower() == \'gangrel\''
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 114'
    merit.db.info = 'You\'re pack-minded. Your blood draws to blood. You may designate a coterie of Kindred and ghouls as your pack. Every Gangrel has a different method for the designation. Some anoint with blood. Some have hazing rituals. When the pack takes teamwork actions, the supporting characters gain the 8-again quality on their rolls. The anchor character does not, but still adds dice equal to the others\' successes.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Pack_Dynamics')
    merit.db.longname = 'Pack Dynamics'
    merit.db.category = 'Werewolf'
    merit.db.range = [3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 107'
    merit.db.info = 'Your character works with her pack the way she works with her own limbs. She intuitively understands their behaviors, and can instinctively compliment their actions with ease. Any time she participates in a teamwork action (see p. 162), add +1, +2, or +3 dice to her rolls at the three-, four-, and five-dot versions of this Merit, respectively. This bonus also adds to rolls using her Resistance Attributes (Resolve, Stamina, and Composure) when defending her pack.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Pandemonical')
    merit.db.longname = 'Pandemonical'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.template().lower() == \'changeling\' and target.get(\'Mantle\',subentry=subentry,statclass=\'Merit\') >= 6'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 119'
    merit.db.info = 'The changeling is more adept at inciting Bedlam than her fellows. Add the Merit\'s rating as a dice bonus to any rolls she makes to incite Bedlam (see p. 110).'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Parallel_Lives')
    merit.db.longname = 'Parallel Lives'
    merit.db.category = 'Changeling'
    merit.db.range = [3]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 119'
    merit.db.info = 'The changeling is deeply connected to his fetch. Each experiences occasional flashes of the other\'s emotional state when something affects one of them strongly, and gains two bonus dice to use Empathy or magic to read the other\'s intentions, or to enter his Bastion. By spending a point of Willpower, either can ride along with the other\'s senses for a number of minutes equal to his Wyrd rating, losing his Defense and the ability to perceive the world around him as he does. Either of them can also spend a Willpower point to send a vague message via thought to the other; it comes across not in words, but fleeting impressions and snippets of images, and can only encompass fairly simple ideas. A fetch could warn his changeling of a Huntsman\'s impending arrival, but without any detail about when or how. Likewise, the changeling could threaten his fetch\'s life, but couldn\'t make any specific demands. Whenever the fetch uses this connection to make the changeling\'s life more dangerous or inconvenient, gain a Beat.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Parkour')
    merit.db.longname = 'Parkour'
    merit.db.category = 'Physical'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.dexterity() >= 3 and target.athletics() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 48-49'
    merit.db.info = 'Your character is a trained and proficient free runner. Free running is the art of moving fluidly through urban environments with complex leaps, bounds, running tricks, and vaults. This is the type of sport popularized in modern action films, where characters are unhindered by fences, walls, construction equipment, cars, or anything else the city puts in their way.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Patient')
    merit.db.longname = 'Patient'
    merit.db.category = 'Mental'
    merit.db.range = [1]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 46'
    merit.db.info = 'Your character knows how to pace herself and take the time to do the job right the first time. When taking an extended action, you may make two additional rolls, above what your Attribute + Skill allows.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Peacemaker')
    merit.db.longname = 'Peacemaker'
    merit.db.category = 'General'
    merit.db.range = [2, 3]
    merit.db.prereq = 'target.wits() >= 3 and target.empathy() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 42-43'
    merit.db.info = 'Your character is keenly attuned to indications of imminent violence, and knows techniques to soothe hot tempers and calm emotions. At two dots, the character may act first in a violent scene to attempt to deescalate the behavior. He spends a point of Willpower and forces his opponent into a social maneuver. The opponent\'s base number of Doors is equal to the higher of her Resolve or Composure for this maneuver.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Phalanx_Fighter')
    merit.db.longname = 'Phalanx Fighter'
    merit.db.category = 'Fighting'
    merit.db.range = [2]
    merit.db.prereq = 'target.get(\'Weapon and Shield\',statclass=\'Merit\') >= 2 and target.get(\'Spear and Bayonet\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 54'
    merit.db.info = 'Your character is trained to wield a spear alongside a shield. She does not increase her spear\'s Strength requirement for using it one-handed as long as she\'s also using a shield. She can use a spear for any Weapon and Shield maneuvers.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Plausible_Deniability')
    merit.db.longname = 'Plausible Deniability'
    merit.db.category = 'Vampire'
    merit.db.range = [4]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\', subentry=\'Carthian\', statclass=\'Merit\') >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 116'
    merit.db.info = 'Carthians don\'t break laws; they defy laws. Influential Carthians can throw law to the wind, then laugh it off with an argument about the definition of the word "is." Any attempt to use a Discipline or other supernatural power to prove your character\'s guilt in breach of city law or Tradition automatically fails. She cannot be forced to confess by any means, and attempts to detect her honesty through mundane means suffer her Carthian Status as a penalty. She exhibits no stains on her aura from diablerie.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Police_Tactics')
    merit.db.longname = 'Police Tactics'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.brawl() >= 2 and target.weaponry() >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 64'
    merit.db.info = 'Your character is trained in restraint techniques, often used by law enforcement officers. This may reflect formal training, or lessons from a skilled practitioner.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Powered_Projectile')
    merit.db.longname = 'Powered Projectile'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4]
    merit.db.prereq = 'target.dexterity() >= 3 and target.athletics() >= 2 and target.firearms() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 51'
    merit.db.info = 'Your character is comfortable using premodern ranged weapons like crossbows, slingshots, and blowguns. Though long ago replaced by firearms, these weapons remain popular for hunting and are widely available in some countries.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Professional_Training')
    merit.db.longname = 'Professional Training'
    merit.db.category = 'Mental'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 46'
    merit.db.info = 'Your character has extensive training in a particular profession, which offers distinct advantages in a handful of fields. When choosing this Merit, choose or create a Profession for your character (see the sidebar). Mark the two Asset Skills on your character sheet. The advantages of Professional Training relate directly to those Asset Skills.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Psychokinesis')
    merit.db.longname = 'Psychokinesis'
    merit.db.category = 'Supernatural'
    merit.db.range = [3, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 58'
    merit.db.info = 'Your character has a psychic ability to manipulate the forces of the universe. Every type of Psychokinetic is different. For example, your character might have Pyrokinesis, Cryokinesis, or Electrokinesis, the control of fire, cold, or electricity, respectively. This is not an exhaustive list. He can intensify, shape, and douse his particular area of ability. With the three-dot version, some of the given force must be present for him to manipulate. With the five-dot version, he can manifest it from nothingness.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Psychometry')
    merit.db.longname = 'Psychometry'
    merit.db.category = 'Supernatural'
    merit.db.range = [3]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 58-59'
    merit.db.info = 'Psychometry is the psychic ability to read impressions left on physical objects. Your character can feel the emotional resonance left on an item, or can perceive important events tied to a location with this ability. The ability automatically hones in on the most emotionally intense moment tied to the item.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Pusher')
    merit.db.longname = 'Pusher'
    merit.db.category = 'Social'
    merit.db.range = [1]
    merit.db.prereq = 'target.persuasion() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 53'
    merit.db.info = 'Your character tempts and bribes as second nature. Any time a mark in a Social interaction accepts his soft leverage (see p. 82), improve your Impression as if you\'d satisfied his Vice as well as moving the impression up on the chart.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Quick_Draw')
    merit.db.longname = 'Quick Draw'
    merit.db.category = 'Physical'
    merit.db.range = [1]
    merit.db.prereq = 'target.wits() >= 3 and subentry in target.db.specialties'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 49'
    merit.db.info = 'Choose a Specialty in Weaponry or Firearms when you purchase this Merit. Your character has trained in that weapon or style enough that pulling the weapon is his first reflex. Drawing or holstering that weapon is considered a reflexive action, and can be done any time his Defense applies.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Relentless')
    merit.db.longname = 'Relentless'
    merit.db.category = 'Physical'
    merit.db.range = [1]
    merit.db.prereq = 'target.athletics() >= 2 and target.stamina() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 49'
    merit.db.info = 'Your character will not stop running, whether away from a pursuer or toward prey. In any chase (see p. 84) your opponents must achieve two additional successes against yours to catch her or elude her.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Relentless_Assault')
    merit.db.longname = 'Relentless Assault'
    merit.db.category = 'Werewolf'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.strength() >= 3 and target.stamina() >= 3 and target.brawl() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 109'
    merit.db.info = 'Your character fights with complete abandon. She throws herself at her opponents without thought or hesitation, turning herself into a ruthless killing machine. She\'s the first into the fight, and the last out of a fight. While this Style is more useful in Urshul and Gauru form, an Uratha can use it in any form. It only applies to attacks using the Brawl Skill, but can be used when in Kuruth.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Residential_Area')
    merit.db.longname = 'Residential Area'
    merit.db.category = 'Werewolf'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'W:tF p. 107'
    merit.db.info = 'Your pack\'s territory encompasses a residential area, and your character has secured it well. This area may be an apartment complex, a gated community, or any place where diverse groups of people lay their heads. Once per game session, you can access a number of Merit dots equal to your Residential Area Merit dots. These Merits can be split however you wish between Allies, Contacts, and Retainers. These Merits must make sense within the scope of the territory. A tenement in the slums probably won\'t have high-level Medical Allies, for example.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Resonance_Shaper')
    merit.db.longname = 'Resonance Shaper'
    merit.db.category = 'Werewolf'
    merit.db.range = [3]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Wisdom\', statclass=\'Renown\') >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 107'
    merit.db.info = 'Your character is adept at the way Essence flows and reshapes. To her capable hands, Essence is clearly mutable. Roll Manipulation + Occult as an extended action; each roll requires one hour of work on a small wellspring of Essence, or one day\'s work on a locus. She can change a single point of the Essence\'s resonance with five successes. With ten successes per level of the locus, she can change its resonance. How she does this is unique to her relationship with the Hisil. Some Uratha perform shaping through music, some through dance, some through literal molding of their surroundings.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Resources')
    merit.db.longname = 'Resources'
    merit.db.category = 'Social'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 53'
    merit.db.info = 'This Merit reflects your character\'s disposable income. She might live in an upscale condo, but if her income is tied up in the mortgage and child support payments, she might have little money to throw around. Characters are assumed to have basic necessities without Resources.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Retain_Weapon')
    merit.db.longname = 'Retain Weapon'
    merit.db.category = 'Fighting'
    merit.db.range = [2]
    merit.db.prereq = 'target.wits() >= 2 and target.brawl() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 54'
    merit.db.info = 'Your character has trained to resist being disarmed. Police and military forces often teach this, but your character might learn this as part of a traditional martial art, as part of a shooting course, or as a member of a private security service. When an attacker attempts to use the Control Weapon or Disarm grappling maneuvers to take his weapon, or otherwise take it away in combat, reduce successes by your character\'s Brawl dots.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Retainer')
    merit.db.longname = 'Retainer'
    merit.db.category = 'Social'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 53-54'
    merit.db.info = 'Your character has an assistant, sycophant, servant, or follower on whom she can rely. Establish who this companion is, and how he was acquired. It may be as simple as a paycheck. He might owe your character his life. However it happened, your character has a hold on him.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Riding_the_Wave')
    merit.db.longname = 'Riding the Wave'
    merit.db.category = 'Vampire'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.template().lower() == \'vampire\' and target.composure() >= 3 and target.resolve() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 117-118'
    merit.db.info = 'Your character runs with her Beast, and knows how to use it to her advantage. She\'s turned riding the wave into a raw, primal art. These maneuvers may only be used while riding the wave. They cannot be used in a normal frenzy, or outside of frenzy.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Right_of_Return')
    merit.db.longname = 'Right of Return'
    merit.db.category = 'Vampire'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\', subentry=\'Carthian\', statclass=\'Merit\') >= 2 and target.get(\'Status\', subentry=\'City\', statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 116'
    merit.db.info = 'This somewhat rare Merit allows a Carthian to work within another covenant without fear of her covenant\'s ostracism. After all, Carthians aim for human solutions, and nothing is more human than the ability to adapt and socialize.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Rigid_Mask')
    merit.db.longname = 'Rigid Mask'
    merit.db.category = 'Changeling'
    merit.db.range = [3]
    merit.db.prereq = 'target.template().lower() == \'changeling\' and target.subterfuge() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CtL p. 119'
    merit.db.info = 'For your character, the protection of the Mask extends far beyond the usual mortal camouflage. Perhaps she can sense the subtle magic that turns her smile into her Mask\'s smile, or her true face is strongly connected to the one that lets her interact with humanity. No one fooled by the Mask knows when she\'s lying or what she\'s feeling unless she allows it. Mortals automatically fail rolls to notice these things, as do polygraphs and other mundane lie-detecting devices. Supernatural creatures must engage in a Clash of Wills to notice her lies.|/|/Drawback: Intentionally dropping your character\'s Mask deals her a point of lethal damage in addition to the normal rules (p. 83).'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Roadkill')
    merit.db.longname = 'Roadkill'
    merit.db.category = 'Fighting'
    merit.db.range = [3]
    merit.db.prereq = 'target.get(\'Aggressive Driving\',statclass=\'Merit\') >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 55'
    merit.db.info = 'Your character has a knack for running down living creatures with her vehicle. When using with a vehicle to hit a human-sized target she adds two additional successes per 20 miles per hour (32 kilometers per hour) her vehicle is moving instead of one. She also inflicts the Knocked Down Tilt on her target even if she misses.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Safe_Place')
    merit.db.longname = 'Safe Place'
    merit.db.category = 'Social'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 54'
    merit.db.info = 'Your character has somewhere she can go where she can feel secure. While she may have enemies that could attack her there, she\'s prepared and has the upper hand. The dot rating reflects the security of the place. The actual location, the luxury, and the size are represented by equipment. A one-dot Safe Place might be equipped with basic security systems or a booby trap at the windows and door. A five-dot could have a security crew, infrared scanners at every entrance, or trained dogs. Each place can be an apartment, a mansion, or a hidey-hole.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Scarred')
    merit.db.longname = 'Scarred'
    merit.db.category = 'General'
    merit.db.range = [1]
    merit.db.prereq = 'target.get(\'Integrity\',subentry=\'Permanent\',statclass=\'Advantage\') <= 5 and target.get(\'Integrity\',subentry=\'Permanent\',statclass=\'Advantage\') > 0'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 43'
    merit.db.info = 'When your character fails the breaking point and loses Integrity, write down this Merit along with whatever event caused the breaking point. Your character no longer suffers breaking points from that influence or action.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Secret_Society_Junkie')
    merit.db.longname = 'Secret Society Junkie'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\',subentry=\'Ordo Dracul\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 114'
    merit.db.info = 'The Ordo Dracul exist within one of the most secret of secret societies. But many of its members participate in other such organizations in mortal (or other) spheres. Members of such secret societies tend to draw toward the Dragon, like a moths to a flame. When the vampire takes Status or Mystery Cult Initiation (see p. 121) reflecting non-Kindred organizations, she also gains Herd dots equal to the Merit.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Seizing_the_Edge')
    merit.db.longname = 'Seizing the Edge'
    merit.db.category = 'Physical'
    merit.db.range = [2]
    merit.db.prereq = 'target.wits() >= 3 and target.composure() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 49'
    merit.db.info = 'Your character is always ready for a chase. Whether to escape a threat or hunt down a rival, she\'s always geared and ready to go. She always has the Edge in the first turn of a chase scene (see p. 84). Additionally, the opponent must make a successful Wits + Composure roll, as if being ambushed, or your character does not have to account for her Speed or Initiative when calculating needed successes in the first turn.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Self-Control')
    merit.db.longname = 'Self-Control'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.resolve() >= 4'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 107'
    merit.db.info = 'Your character can stave off her spirit nature. When compelled to shift in a stressful situation due to low Harmony (see p. 96), you may spend a point of Willpower to allow her to remain in her current form for the scene. Doing so is a breaking point toward Flesh.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Shiv')
    merit.db.longname = 'Shiv'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2]
    merit.db.prereq = 'target.get(\'Street Fighting\') >= 2 and target.weaponry() >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 64'
    merit.db.info = 'Your character carries small, concealable weapons for use in a tussle. Rolls to detect the concealed weapon suffer your character\'s Weaponry score as a penalty. With the one-dot version, he can conceal a weapon with a zero damage rating. The two-dot version can conceal a one damage rating weapon. Your character may use the Brawl Skill to use this weapon.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Sleight_of_Hand')
    merit.db.longname = 'Sleight of Hand'
    merit.db.category = 'Physical'
    merit.db.range = [2]
    merit.db.prereq = 'target.larceny() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 49'
    merit.db.info = 'Your character can pick locks and pockets without even thinking about it. She can take one Larceny-based instant action reflexively in a given turn. As well, her Larceny actions go unnoticed unless someone is trying specifically to catch her.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Small_Unit_Tactics')
    merit.db.longname = 'Small Unit Tactics'
    merit.db.category = 'Social'
    merit.db.range = [2]
    merit.db.prereq = 'target.presence() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 54'
    merit.db.info = 'Your character is a proficient leader in the field. She can organize efforts and bark orders to remarkable effect. Once per scene, when making a coordinated action that was planned in advance, spend a point of Willpower and an instant action. A number of characters equal to your character\'s Presence can benefit from the +3 bonus gained from the Willpower expenditure.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Small-Framed')
    merit.db.longname = 'Small-Framed'
    merit.db.category = 'Physical'
    merit.db.range = [2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 49'
    merit.db.info = 'Your character is diminutive. He\'s not five feet, and it\'s easy to walk into him without noticing. He\'s Size 4, and thus has one fewer Health box. He gains +2 to any rolls to hide or go unnoticed, and this bonus might apply any time being smaller would be an advantage, such as crawling through smaller spaces.'
    merit.db.cg_only = True
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Song_in_your_Heart')
    merit.db.longname = 'Song in your Heart'
    merit.db.category = 'Werewolf'
    merit.db.range = [3]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Glory\',statclass=\'Renown\') >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 107'
    merit.db.info = 'Your character sings, howls, and tells stories like none other. Her words echo and reverberate through listeners, and inspire them to learn from her tales. This Merit acts as the Inspiring Merit (see p. 111). Your character does not need to meet the prerequisites for that Merit, and it can only be used when singing, howling, or storytelling. Listeners may take the Inspired Condition (see p. 308) as a Persistent Condition, gaining a Beat every time they take a significant action inspired by your character\'s tale.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Sounds_of_the_City')
    merit.db.longname = 'Sounds of the City'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Tribe\',statclass=\'Sphere\').lower() == \'iron masters\''
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 107'
    merit.db.info = 'Your Iron Master has his fingers on the pulse of the city, and can see the flow of its currencies. Not just money, but favors, popularity, and standing. With subtle manipulations, he can cut off that flow. The player rolls Wits + Politics; with success and a turn of scrutiny, the character can identify one Social Merit the prey possesses, chosen by the Storyteller.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Speaker_for_the_Silent')
    merit.db.longname = 'Speaker for the Silent'
    merit.db.category = 'Vampire'
    merit.db.range = [3]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\', subentry=\'Invictus\', statclass=\'Merit\') >= 1 and target.get(\'Dynasty Membership\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 114'
    merit.db.info = 'Any Kindred may be part of a dynastic house, but the Invictus take dynasty membership very seriously. Some members receive training to channel the minds of torpid dynasty members. With this Merit, the character can choose to act as a medium for a torpid elder\'s consciousness. While possessed, the Speaker is aware of what occurs around him, but the torpid Kindred has control of his body, and can speak through him. The torpid Kindred retains no access to her Disciplines while possessing a Speaker. At any time, the Speaker can spend a point of Willpower to eject the torpid mind. The torpid Kindred can relinquish her control at will.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Spear_and_Bayonet')
    merit.db.longname = 'Spear and Bayonet'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.strength() >= 3 and target.dexterity() >= 2 and target.weaponry() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 51'
    merit.db.info = 'Your character is trained with long weapons that end in a point. This could be anything from a traditional spear to a fixed bayonet on a modern rifle. This Style has countless variations around the world but is historically incorporated as part of military training.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Spin_Doctor')
    merit.db.longname = 'Spin Doctor'
    merit.db.category = 'Social'
    merit.db.range = [1]
    merit.db.prereq = 'target.manipulation() >= 3 and target.subterfuge() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 54'
    merit.db.info = 'Your character can fast-talk and sell bullshit stories as if they were completely flawless. When suffering from Tainted Clues (see p. 80), your character does not ignore successes. Instead, apply a -1 penalty for each relevant Tainted Clue. Using a Tainted Clue only levies a total -2 penalty with this Merit, which includes the -1 taken in lieu of ignoring successes.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Spiritual_Blockage')
    merit.db.longname = 'Spiritual Blockage'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Wisdom\',statclass=\'Renown\') >= 2 and target.brawl() >= 1 and target.occult() >= 3 and target.wits() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 109'
    merit.db.info = 'Your character can sense the ebb and flow of Essence in her opponents. With well-placed strikes, she can curb the flow of Essence in the body, denying a victim access to his spiritual fuel. You can choose to use Spiritual Blockage any time your character makes a Brawl or Weaponry attack against a creature that uses Essence. Make an attack with a -2 penalty. If the attack deals damage, the victim loses a point of Essence; on an exceptional success the victim loses two points. This Essence is considered spent, not lost. As such, it limits the amount a victim can spend in a turn.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Stable_Trod')
    merit.db.longname = 'Stable Trod'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CtL p. 119'
    merit.db.info = 'Your character\'s freehold has secured and maintained a trod (p. 201) with a rating equal to his Merit dots in Stable Trod. The trod bestows two additional advantages to those who have Hollows along it or travel it frequently:|/|/Hollows along the trod gain an extra one-dot Hollow enhancement (p. 116). The enhancement is the same for all such Hollows. This can benefit a number of Hollows equal to the Stable Trod Merit rating. This enhancement can bring the number of Hollow enhancements above the normal maximum a Hollow\'s rating allows.|/Goblin fruit trees cultivated along the trod produce additional fruit. You may roll your character\'s dots in Stable Trod as a dice pool once per story. Each success produces one additional generic fruit, which contains a point of Glamour.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Staff')
    merit.db.longname = 'Staff'
    merit.db.category = 'Social'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 54'
    merit.db.info = 'Your character has a crew of workers or assistants at his disposal. They may be housekeepers, designers, research assistants, animators, cheap thugs, or whatever else makes sense. For every dot in this Merit, choose one type of assistant, and one Skill. At any reasonable time, his staff can take actions using that Skill. These actions automatically garner a single success. While not useful in contested actions, this guarantees success on minor, mundane activities. Note that your character may have employees without requiring the Staff Merit; Staff simply adds a mechanical advantage for those groups.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Staff_Fighting')
    merit.db.longname = 'Staff Fighting'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4]
    merit.db.prereq = 'target.strength() >= 2 and target.dexterity() >= 3 and target.weaponry() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 51-52'
    merit.db.info = 'Your character uses a staff as her weapon of choice. These maneuvers are usually performed with a quarterstaff or bo staff, but anything of a suitable length and shape like a walking stick or a heavy curtain rod will work as well.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Status')
    merit.db.longname = 'Status'
    merit.db.category = 'Social'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 54'
    merit.db.info = 'Your character has standing, membership, authority, control over, or respect from a group or organization. This can reflect official standing, or merely informal respect. No matter the source, your character enjoys certain privileges within that structure.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Street_Fighting')
    merit.db.longname = 'Street Fighting'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.stamina() >= 3 and target.composure() >= 3 and target.brawl() >= 2 and target.streetwise() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 65'
    merit.db.info = 'Your character learned to fight on the mean streets. She may have had some degree of formal training, but the methodology came from the real world, in dangerous circumstances. Street Fighting isn\'t about form and grace, it\'s about staying alive. These maneuvers may only be used unarmed, or with weapons capable of using the Brawl Skill, such as punch daggers, or weapons concealed with the Shiv Merit.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Strength_Performance')
    merit.db.longname = 'Strength Performance'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4]
    merit.db.prereq = 'target.strength() >= 3 and target.stamina() >= 2 and target.athletics() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 52'
    merit.db.info = 'While the Strength Attribute covers all forms of issuing bodily force, your character has specifically trained in lifting, pushing, and pulling enormous weights. He learned this as an Olympic-style weightlifter, strongman competitor, or performer. This doesn\'t help your character hit things, but if he does, anything at the other end is going to break and hurt.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Strength_of_Resolution')
    merit.db.longname = 'Strength of Resolution'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\', subentry=\'Carthian\', statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 116'
    merit.db.info = 'A Carthian stands resolute in the face of that which would force her to violate the law. Add her Carthian Status to any dice pool to contest a Discipline or other supernatural power which would coax her to violate acknowledged city law.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Striking_Looks')
    merit.db.longname = 'Striking Looks'
    merit.db.category = 'Social'
    merit.db.range = [1, 2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 54'
    merit.db.info = 'Your character is stunning, alarming, commanding, repulsive, threatening, charming, or otherwise worthy of attention. Determine how your character looks and how people react to that. For one dot, your character gets a +1 bonus on any Social rolls that would be influenced by his looks. For two dots, the benefit increases to +2. Depending on the particulars, this might influence Expression, Intimidation, Persuasion, Subterfuge, or other rolls.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Strings_of_the_Heart')
    merit.db.longname = 'Strings of the Heart'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Tribe\',statclass=\'Sphere\').lower() == \'storm lords\''
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 108'
    merit.db.info = 'The first trick to making someone do what you want is finding out what they want, and promising it, threatening it, or offering it. Your Storm Lord has a knack for finding that very thing. After a turn scrutinizing her prey, ask his player, "What does your character want most?" Your Storm Lord instinctively knows the answer, even if she doesn\'t understand the context. "I want Davis\'s hand in marriage" is more useful if she knows who Davis is, but she doesn\'t have to know him to know that answer.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Stunt_Driver')
    merit.db.longname = 'Stunt Driver'
    merit.db.category = 'Physical'
    merit.db.range = [1, 2, 3, 4]
    merit.db.prereq = 'target.dexterity() >= 3 and target.drive() >= 3 and target.wits() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 49'
    merit.db.info = 'Your character is an expert behind the wheel, and can push a vehicle beyond normal limits. Each dot of this Merit grants access to another driving technique.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Support_Network')
    merit.db.longname = 'Support Network'
    merit.db.category = 'General'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.get(\'Allies\',subentry=\'Permanent\',statclass=\'Advantage\') >= 1 or target.get(\'Mentor\',subentry=\'Permanent\',statclass=\'Advantage\') >= 1 or target.get(\'Retainer\',subentry=\'Permanent\',statclass=\'Advantage\') >= 1 or target.get(\'True Friend\',subentry=\'Permanent\',statclass=\'Advantage\') >= 1'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'HL p. 43'
    merit.db.info = 'Your character has friends, family, teammates, or any other person or people who provide emotional support in the face of terrifying circumstances. This Merit must be tied to another Social Merit such as Allies, Mentor, Retainer, or True Friend, but can be tied to any Merit representing a person or group that the Storyteller deems fitting. Alternatively, any character with the Empath Merit (see above) can be the anchor point for this Merit.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Survivalist')
    merit.db.longname = 'Survivalist'
    merit.db.category = 'General'
    merit.db.range = [1]
    merit.db.prereq = 'target.survival() >= 3 and target.get(\'Iron Stamina\',statclass=\'Merit\') >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 43'
    merit.db.info = 'Your character has been trained to fight even through the most dangerous environmental extremes. When inflicted with the Extreme Cold Tilt or Extreme Heat Tilt (Chronicles of Darkness Rulebook, p. 282) she doesn\'t begin taking the normal -1 to her rolls until a number of hours equal to her Stamina.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Swarm_Form')
    merit.db.longname = 'Swarm Form'
    merit.db.category = 'Vampire'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Protean\',statclass=\'Discipline\') >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 114'
    merit.db.info = 'When taking the Beast\'s Skin, some Gangrel can instead become a swarm of small creatures: Size 0 or Size 1 animals. The character may perceive through any of the senses of any individual creature in the swarm, but the swarm acts as a single entity.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Sworn')
    merit.db.longname = 'Sworn'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\',subentry=\'Ordo Dracul\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 114-115'
    merit.db.info = 'Your character is not only a member of the Ordo Dracul, she\'s sworn to serve one of its branches. When taking this Merit, choose to which faction she belongs (the Axe, the Dying Light, or Mysteries typically). She gains dots equal to her Covenant Status to split between the Mentor and Retainer Merits. These reflect teachers and wards within the faction. She can swap these Merits out between chapters, as she receives new assignments.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Sympathetic')
    merit.db.longname = 'Sympathetic'
    merit.db.category = 'Social'
    merit.db.range = [2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 55'
    merit.db.info = 'Your character is very good at letting others get close. This gives him an edge in getting what he wants. At the beginning of a Social maneuvering attempt, you may choose to accept a Condition such as Leveraged, or Swooned in order to immediately eliminate two of the subject\'s Doors.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Systema')
    merit.db.longname = 'Systema'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.dexterity() >= 3 and target.athletics() >= 3 and target.wits() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 52'
    merit.db.info = 'Your character learns to move with exceptional suppleness, rolling with blows and obstacles. She redirects incoming force not as a technique, but an instinct. These abilities are often taught within Systema, a Russian martial art developed for intelligence services and special operations. It can also reflect the advanced body skills taught by "soft" martial arts such as Tai Chi or Aikido.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Tactical_Shifting')
    merit.db.longname = 'Tactical Shifting'
    merit.db.category = 'Werewolf'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.wits() >= 3 and target.dexterity() >= 3 and target.athletics() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 110'
    merit.db.info = 'Your character knows how to shift her form rapidly to maximize her effectiveness in a fight. She can slink down in form in order to evade an oncoming attack, or she can make a swift change in order to add force to a blow.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Takes_One_to_Know_One')
    merit.db.longname = 'Takes One to Know One'
    merit.db.category = 'Social'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower() != \'changeling\''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 55'
    merit.db.info = 'Normally, when Uncovering a Clue (see p. 79), your character suffers a -2 penalty if the crime aligns with his Vice. However, it takes a criminal to know a criminal, and your character has a deep-seated understanding of his particular weakness. Instead, take a +2 and the 9-again quality on any investigation rolls when the crime aligns with your character\'s particular Vice. The successful investigation is considered fulfilling his Vice.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Taste')
    merit.db.longname = 'Taste'
    merit.db.category = 'Social'
    merit.db.range = [1]
    merit.db.prereq = 'target.crafts() >= 2 and subentry in target.db.specialties and len(subentry.split(\':\')) == 2 and (subentry.split(\':\')[0].lower() == \'crafts\' or subentry.split(\':\')[0].lower() == \'expression\')'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 55-56'
    merit.db.info = 'Your character has refined tastes, and can identify minor details in fashion, food, architecture, and other forms of artistry and craftsmanship. Not only does this give her an eye for detail, it makes her a center of attention in critical circles. She can also appraise items within her area of expertise. With a Wits + Skill roll, depending on the creation in question (Expression for poetry, Crafts for architecture, for example), your character can pick out obscure details about the item that other, less discerning minds would not. For each success, ask one of the following questions, or take a +1 bonus to any Social rolls pertaining to groups interested in the art assessed for the remainder of the scene.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Telekinesis')
    merit.db.longname = 'Telekinesis'
    merit.db.category = 'Supernatural'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 59'
    merit.db.info = 'Your character has a psychic ability to manipulate the physical world with her mind. This means lifting, pushing, and pulling objects. Fine manipulation is beyond the scope of Telekinesis. By spending a Willpower point, she can activate Telekinesis for the scene. Her dots in this Merit determine her mind\'s effective Strength for the purpose of lifting and otherwise influencing her environment.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Telepathy')
    merit.db.longname = 'Telepathy'
    merit.db.category = 'Supernatural'
    merit.db.range = [3, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 59-60'
    merit.db.info = 'Your character can hear surface thoughts and read minds. With the five-dot version of this Merit, he can broadcast simple messages to others\' minds. He hears these thoughts as if they were spoken, which means they can sometimes be distracting. He can only hear thoughts at the range he can normal conversation, regardless of any ambient noise (so a telepath can hear the thoughts of someone next to him at a loud concert, even though he can\'t actually hear the subject talk, but cannot hear the thoughts of someone a football field away under quiet conditions).'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'The_Mother-Daughter_Bond')
    merit.db.longname = 'The Mother-Daughter Bond'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\', subentry=\'Circle of the Crone\', statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 113'
    merit.db.info = 'The Circle exists through tribulation and mentorship. Without tight-knit bonds, the Circle would never have survived its tumultuous early years. When a member of the Circle with this Merit purchases the Mentor Merit, that Mentor is protected by the True Friend Merit (see p. 124). The vampire does not have to purchase True Friend to take this advantage.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Thief_of_Fate')
    merit.db.longname = 'Thief of Fate'
    merit.db.category = 'Supernatural'
    merit.db.range = [3]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 60'
    merit.db.info = 'Your character is a magnet for fortune and fate. When she\'s close to someone, she unintentionally steals their good fortune. If she touches someone, this Merit takes effect unless she spends a point of Willpower to curb the effect for a scene. In the same day, any failures the subject makes are considered dramatic failures. If she\'s used this Merit at any time in a given day, she gains four dice any time she spends Willpower to increase a dice pool.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Thrown_Weapons')
    merit.db.longname = 'Thrown Weapons'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2]
    merit.db.prereq = 'target.dexterity() >= 3 and target.athletics() >= 2 and target.get(\'Quick Draw\',subentry=subentry,statclass=\'Merit\') >= 1 and target.get(subentry + \': *\')'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'HL p. 52'
    merit.db.info = 'Knives, darts, throwing stars, and tomahawks are all weapons your character can send flying in her enemy\'s direction. Many warrior cultures have used thrown projectiles in wartime or for hunting purposes and may teach this Style. Also, similar techniques are found among circus and sideshow acts. These maneuvers may only be performed with edged weapons Size 1 or smaller.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Token')
    merit.db.longname = 'Token'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CtL p. 119-120'
    merit.db.info = 'Your character or motley has one or more tokens (p. 222) - mystical items suffused with the power and danger of Faerie. Perhaps she made off with her Keeper\'s most prized possession as she fled out of spite, or found that twigs from the Hedge caught in her clothes became magical matchsticks upon her escape. Perhaps she traded away her name for an enchanted mirror at a Goblin Market. Perhaps she took the riding crop as a trophy when she killed the Huntsman, and now she\'s driven to hunt her own kind. Whatever the case, choose one or more tokens with a total dot rating equal to her rating in this Merit. She may have more than five dots in this Merit, but no single token may have a rating higher than five.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Tolerance_for_Biology')
    merit.db.longname = 'Tolerance for Biology'
    merit.db.category = 'Mental'
    merit.db.range = [1]
    merit.db.prereq = 'target.resolve() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 46'
    merit.db.info = 'Most people turn away at the sight of blood, other bodily fluids, or exotic biology. Your character has seen enough that nothing turns her stomach. When other characters must resist shock or physical repulsion from the disgusting and morbid, your character stands her ground. You do not need to make Composure, Stamina, or Resolve rolls to withstand the biologically strange. This doesn\'t mean she\'s immune to fear; she\'s just used to nature in all its nasty forms.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Totem')
    merit.db.longname = 'Totem'
    merit.db.category = 'Werewolf'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 108'
    merit.db.info = 'Your character has a relationship to a totem spirit, either personally or to a pack totem. Each dot invested in this Merit adds a totem point to create the totem (see p. 91). Note that any character can only have five points in this Merit. A pack totem is limited by the number of pack members, but can be massive with enough invested members. The Totem Merit also adds dice equal to its dots to any Social action with the totem spirit in question.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Touchstone')
    merit.db.longname = 'Touchstone'
    merit.db.category = 'Changeling and Vampire'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.template().lower() == \'changeling\' or target.template().lower() == \'vampire\''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CtL p. 120, VtR p. 115'
    merit.db.info = 'Your character has multiple Touchstones. Each dot in the Touchstone Merit allows for an additional Touchstone. Write each one beside the next available box to the right of the rightmost box with an associated Touchstone. If the last Clarity box already has a Touchstone, you cannot purchase this Merit again. For more on Touchstones, see p. 98.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Trained_Observer')
    merit.db.longname = 'Trained Observer'
    merit.db.category = 'Mental'
    merit.db.range = [1, 3]
    merit.db.prereq = 'target.wits() >= 3 or target.composure >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 46'
    merit.db.info = 'Your character has spent years in the field, catching tiny details and digging for secrets. She might not have a better chance of finding things, but she has a better chance of finding important things. Any time you make a Perception roll (usually Wits + Composure), you benefit from the 9-again quality. With the three-dot version, you get 8-again.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Transfer_Manuever')
    merit.db.longname = 'Transfer Manuever'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.intelligence() >= 2 and target.wits() >= 3 and target.get(subentry.split(\'/\')[0],statclass=\'Merit\') >= 3 and target.get(subentry.split(\'/\')[1],statclass=\'Merit\') >= 3'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'HL p. 54'
    merit.db.info = 'Many styles teach unarmed methods as a prerequisite for armed methods, and vice versa. This maneuver allows your character to transfer a maneuver from a Brawl-based Fighting Style to a Weaponry-based Style, or vice versa. The maneuver must not depend on the physical presence of a weapon, in that it can be applied with empty hands. The Storyteller decides which maneuvers are appropriate, though this can only be used on maneuvers worth no more than *** dots - after that, they\'re too specific to the original fighting method. Your character must know the maneuver in its original form, and you must purchase it again, at the same cost in dots and Experience.|/|/Entry for this merit should be in the form of <original group>/<target group>'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'True_Friend')
    merit.db.longname = 'True Friend'
    merit.db.category = 'Social'
    merit.db.range = [3]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 56'
    merit.db.info = 'Your character has a True Friend. While that friend may have specific functions covered by other Merits (Allies, Contacts, Retainer, Mentor, et cetera), True Friend represents a deeper, truly trusting relationship that cannot be breached. Unless your character does something egregious to cause it, her True Friend will not betray her. Additionally, the Storyteller cannot kill her True Friend as part of a plot without your express permission. Any rolls to influence a True Friend against your character suffer a five-die penalty. In addition, once per story, your character can regain one spent Willpower by having a meaningful interaction with her True Friend.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Trunk_Squeeze')
    merit.db.longname = 'Trunk Squeeze'
    merit.db.category = 'Fighting'
    merit.db.range = [2]
    merit.db.prereq = 'target.brawl() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 54'
    merit.db.info = 'By wrapping arms or legs around an opponent\'s torso, your character can practically crush the life out of him. While grappling, your character can use the Trunk Squeeze maneuver.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Two_Weapon_Fighting')
    merit.db.longname = 'Two Weapon Fighting'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4]
    merit.db.prereq = 'target.wits() >= 3 and target.get(\'Fighting Finesse\', statclass=\'Merit\') >= 2 and target.weaponry() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 53'
    merit.db.info = 'Your character fights with a weapon in each hand. She can amplify her attacks by using them together or balance between attack and defense by using one weapon for each. Different martial arts focus on different sets of weapons. Some employ a rapier and dagger, or a katana and wakizashi, while others use sticks or two light swords. This Style can be used to replicate any of them. Unless your character possesses the Ambidextrous Merit she takes the usual -2 penalty for using a weapon in her off-hand. Neither weapon can be above Size 2 for performing these maneuvers.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Unarmed_Defense')
    merit.db.longname = 'Unarmed Defense'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.dexterity() >= 3 and target.brawl() >= 2 and target.get(\'Defensive Combat\',\'Brawl\') == 1'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 65'
    merit.db.info = 'Your character is better at stopping people from hurting them than they are at hurting other people. Maybe they practice a martial art that redirects an opponent\'s blows, or are just very good at not being where their opponent wants them to be.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Undead_Menses')
    merit.db.longname = 'Undead Menses'
    merit.db.category = 'Vampire'
    merit.db.range = [2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 115'
    merit.db.info = 'Throughout history, various cultures attributed mystical significance to the menstrual cycle. Many of these myths carried stigmas against menses, due to the unhealthy fears of men in power.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Unnatural_Affinity')
    merit.db.longname = 'Unnatural Affinity'
    merit.db.category = 'Vampire'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'VtR p. 114'
    merit.db.info = 'Your character can take nourishment from the blood of some of the stranger creatures of the World of Darkness. Each dot of this Merit allows your character to gain sustenance from one type of supernatural creature. This may mean werewolves, ghosts, mummies, zombies, or stranger things still. This blood counts as Kindred Vitae for the purposes of feeding restrictions.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Unseen_Sense')
    merit.db.longname = 'Unseen Sense'
    merit.db.category = 'Supernatural'
    merit.db.range = [2]
    merit.db.prereq = ''
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CoD p. 60'
    merit.db.info = 'Your character has a "sixth sense" for a type of supernatural creature, chosen when you buy the Merit. For example, you may choose Unseen Sense: Vampires, or Unseen Sense: Fairies. The sense manifests differently for everyone. Her hair stands on end, she becomes physically ill, or perhaps she has a cold chill. Regardless, she knows that something isn\'t right when she is in the immediate proximity of the appropriate supernatural being. Once per chapter, the player can accept the Spooked Condition (p. 290), in exchange for which the character can pinpoint where the feeling is coming from. If the target is using a power that specifically cloaks its supernatural nature, however, this does not work (though the Condition remains until resolved as usual).'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Unsettling_Gaze')
    merit.db.longname = 'Unsettling Gaze'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Clan\',statclass=\'Sphere\').lower() == \'nosferatu\''
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 115'
    merit.db.info = 'All Haunts have an unsettling effect. Your character\'s Beast oozes with terror. When she evokes the monstrous Beast (see p. 91), she unsettles her target deeply and makes him question himself. Any time she infects a victim with the Bestial Condition and scores an exceptional success, she also forces a breaking point if the victim has a higher Humanity (or Integrity) than hers.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Untouchable')
    merit.db.longname = 'Untouchable'
    merit.db.category = 'Social'
    merit.db.range = [1]
    merit.db.prereq = 'target.manipulation() >= 3 and target.subterfuge() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 56'
    merit.db.info = 'Your character commits crimes, and is always a step ahead of pursuers. Because of his methodical planning, any roll to investigate him suffers the Incomplete Clue tag (see p. 80) unless it achieves exceptional success.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Vice-Ridden')
    merit.db.longname = 'Vice-Ridden'
    merit.db.category = 'Mental'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() != \'changeling\''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 46'
    merit.db.info = 'Your character is one of the worst examples of humanity in the Chronicles of Darkness. He has two Vices, although he may still only regain one Willpower per scene he indulges himself.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Virtuous')
    merit.db.longname = 'Virtuous'
    merit.db.category = 'Mental'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() != \'changeling\''
    merit.db.noteRestrictions = []
    merit.db.reference = 'CoD p. 46'
    merit.db.info = 'Your character is a light of good in the Chronicles of Darkness. She has two Virtues. The limitations of how many times she may refresh Willpower using a Virtue remain the same, but it\'s up to you which Virtue she uses each time.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Warcry')
    merit.db.longname = 'Warcry'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Glory\',statclass=\'Renown) >= 2 and target.presence() >= 3 and target.expression() >= 2 and target.intimidation() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 110'
    merit.db.info = 'Your character can howl out sharply and shake opponents to the core. Her howls reverberate on both sides of the Gauntlet, quaking spirit-stuff and flesh alike. Roll Presence + Expression as an instant action. The howl affects a number of listeners of your choice equal to the successes rolled. Those affected suffer a -1 penalty to Defense and attack rolls, and -2 to Initiative for the remainder of the scene. A character may only be subject to this effect once in a given scene.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Warded_Dreams')
    merit.db.longname = 'Warded Dreams'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3]
    merit.db.prereq = 'target.template().lower() == \'changeling\' and target.resolve() >= value'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CtL p. 120'
    merit.db.info = 'Whether through active mental discipline or natural stubbornness, your character\'s dream Bastion is particularly well fortified against intrusion. Each dot in Warded Dreams increases the Bastion\'s Fortification rating by one.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Weakest_Link')
    merit.db.longname = 'Weakest Link'
    merit.db.category = 'Werewolf'
    merit.db.range = [2]
    merit.db.prereq = 'target.template().lower() == \'werewolf\' and target.get(\'Tribe\', statclass=\'Sphere\').lower() == \'blood talons\''
    merit.db.noteRestrictions = []
    merit.db.reference = 'W:tF p. 108'
    merit.db.info = 'Your character can immediately work out the weakest points in a social dynamic. With a turn of scrutinizing two or more associated characters, your character identifies the weakest of those characters by whatever criteria the Storyteller feels is most appropriate to the situation. This doesn\'t require a roll.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Weapon_and_Shield')
    merit.db.longname = 'Weapon and Shield'
    merit.db.category = 'Fighting'
    merit.db.range = [1, 2, 3, 4]
    merit.db.prereq = 'target.strength() >= 3 and target.stamina() >= 3 and target.weaponry() >= 3'
    merit.db.noteRestrictions = []
    merit.db.reference = 'HL p. 53'
    merit.db.info = 'Your character knows how to fight from behind a shield with a one-handed weapon. These maneuvers strike a balance between protection and offense and are used in tandem with others, such as in a Viking shield wall or riot police formation.'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Where_the_Bodies_Are_Buried')
    merit.db.longname = 'Where the Bodies Are Buried'
    merit.db.category = 'Vampire'
    merit.db.range = [1]
    merit.db.prereq = 'target.template().lower == \'vampire\' and target.get(\'Status\',subentry=\'Invictus\',statclass=\'Merit\').lower() >= 2'
    merit.db.noteRestrictions = []
    merit.db.reference = 'VtR p. 115'
    merit.db.info = 'The Conspiracy of Silence covers up a lot of secrets... and your character\'s been quietly keeping track. A number of times equal to your Invictus Status per story, you can ask one of the following questions about another vampire whose name and covenant affiliation you know:'
    merit.db.cg_only = False
    merit.db.restricted = False

stats = data.find(name,statclass='Merit')
if len(stats) == 0:
    merit = create_script('typeclasses.scripts.meritScript',key = 'Workshop')
    merit.db.longname = 'Workshop'
    merit.db.category = 'Changeling'
    merit.db.range = [1, 2, 3, 4, 5]
    merit.db.prereq = 'target.template().lower() == \'changeling\' and target.get(\'Hollow\',statclass=\'Merit\') >= 1'
    merit.db.noteRestrictions = ['*']
    merit.db.reference = 'CtL p. 120'
    merit.db.info = 'Your character maintains, within her Hollow, a variety of equipment and tools that can help with the creation of natural and supernatural items. Whether in the form of a forge with metallurgy tools, an artist\'s loft, a laboratory filled with beakers and crucibles, or an orchard outfitted with the best gardening implements, your character\'s Hollow is outfitted with precisely the right things she needs to have on hand to create.'
    merit.db.cg_only = False
    merit.db.restricted = False

pass