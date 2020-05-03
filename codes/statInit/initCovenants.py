from evennia import create_script

covenant = create_script('typeclasses.scripts.covenantScript',key = 'Carthian_Movement')
covenant.db.longname = 'Carthian Movement'
covenant.db.reference = 'VtR p. 32-34'
covenant.db.info = 'The Carthian Movement uses the ideologies of the living to bring democracy to the dead. Anyone who disagrees with that gets their haven firebombed.'
covenant.db.restricted = False

covenant = create_script('typeclasses.scripts.covenantScript',key = 'Circle_of_the_Crone')
covenant.db.longname = 'Circle of the Crone'
covenant.db.reference = 'VtR p. 35-37'
covenant.db.info = 'Vampires in other covenants hide their monstrous natures behind veneers of self-control, or hellfire religion, or politesse, or ideological fire. But the vampires of the Circle of the Crone are the howling beasts who roam in bloodstained packs. In other covenants, the dead try to hold fast to religions and ideologies, maintaining hierarchies and rigid systems of control. The Acolytes believe that you must change. Other covenants believe that to be a monster, you must do the will of God, or have a will to power, or study dark secrets. But the Mother\'s Army is made of monsters just because it\'s the way they are.'
covenant.db.restricted = False

covenant = create_script('typeclasses.scripts.covenantScript',key = 'Invictus')
covenant.db.longname = 'Invictus'
covenant.db.reference = 'VtR p. 38-40'
covenant.db.info = 'The Invictus knows where the bodies are buried. And they know which ones are only sleeping. This is the legend: The beast that sits in the center of a huge empire, the cultured monster wearing a coronet. The old money. The Prince of Darkness.'
covenant.db.restricted = False

covenant = create_script('typeclasses.scripts.covenantScript',key = 'Lancea_et_Sanctum')
covenant.db.longname = 'Lancea et Sanctum'
covenant.db.reference = 'VtR p. 41-43'
covenant.db.info = 'The Lancea et Sanctum is, quite simply, the organized church of the Kindred. God cursed vampires to be hungry and dead, and in their damnation they are called to do God\'s work. In the Book of Job, Satan is God\'s agent in the torment of an innocent man, tempting him to blasphemy. The Sanctified see themselves as doing the same: They torment the innocent, and root out those whose faith is weak.'
covenant.db.restricted = False

covenant = create_script('typeclasses.scripts.covenantScript',key = 'Ordo_Dracul')
covenant.db.longname = 'Ordo Dracul'
covenant.db.reference = 'VtR p. 44-46'
covenant.db.info = 'The dead scientist who experiments on humans, werewolves, and fairies in a sterile white laboratory. The occult archaeologist who rifles through the tombs of the terrifying beasts of old. The chillingly plausible preacher who leads his disciples into self-mutilation and surgical alteration. The robed cultists whose rituals depend on the sacrifice of angels. These are the Ordo Dracul. They are the Order of the Dragon, the children of Dracula himself.'
covenant.db.restricted = False

covenant = create_script('typeclasses.scripts.covenantScript',key = 'VII')
covenant.db.longname = 'VII'
covenant.db.reference = 'VtR p. 47-49'
covenant.db.info = 'They are vampires who hunt vampires. They leave behind the wreckage of their Kindred victims, often creatively destroyed, along with the three characters that make the Roman numeral for seven, displayed prominently on a wall, or a sheet of paper, or on a screen. And that\'s all. They are the subjects of whispered rumor and terrified speculation. The fear of VII is the thing the five great covenants have in common.'
covenant.db.restricted = False

pass