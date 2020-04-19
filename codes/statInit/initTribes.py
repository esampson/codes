from evennia import create_script

tribe = create_script('typeclasses.scripts.tribeScript',key = 'Blood_Talons')
tribe.db.longname = 'Blood Talons'
tribe.db.renown = 'Glory'
tribe.db.tribe_gifts = ['Inspiration', 'Rage', 'Strength']
tribe.db.info = 'The Blood Talons are violence incarnate. Every hunt is just a warm-up, a prelude to the clash of fang and claw and the inevitable killing blow. Every conflict is an opportunity to overcome, to crush the opposition and scatter them to the winds. “Compromise” is just another way to say “surrender,” and the Blood Talons swore an oath long ago: Nu Sum Ghumur Nu Su Ghid. “Offer No Surrender You Would Not Accept.”'
tribe.db.reference = 'W:tF p. 34-36'
tribe.db.restricted = False

tribe = create_script('typeclasses.scripts.tribeScript',key = 'Bone_Shadows')
tribe.db.longname = 'Bone Shadows'
tribe.db.renown = 'Wisdom'
tribe.db.tribe_gifts = ['Death', 'Elemental', 'Insight']
tribe.db.info = 'The Bone Shadows are keepers of secret wisdom, explorers plumbing the depths of the Shadow and of otherworlds even stranger. They understand the laws that govern those worlds, and they know the rites that allow them to punish the things that would violate them. The world has slewed out of balance since Father Wolf was slain, and the Bone Shadows constantly dance back and forth upon the scales, holding the line between the physical and the ephemeral. Other tribes confront the symptoms, but the Hirfathra Hissu strike at the source of the disease, for long ago they swore an oath: Su A Sar-Hith Sa. “Pay each spirit in kind.”'
tribe.db.reference = 'W:tF p. 37-39'
tribe.db.restricted = False

tribe = create_script('typeclasses.scripts.tribeScript',key = 'Ghost_Wolves')
tribe.db.longname = 'Ghost Wolves'
tribe.db.renown = ''
tribe.db.tribe_gifts = []
tribe.db.info = 'Ghost Wolves aren’t a tribe. They’re the werewolves who have rejected the Firstborn and turned their backs on Luna and the spirit courts alike. Many are simply ignorant. The People can’t be everywhere, and sometimes a First Change goes unremarked. Others try to deny their natures and cling to their human lives. Still others simply find no resonance with the Tribes of the Moon or the Pure, and strike out to make their own destinies.'
tribe.db.reference = 'W:tF p. 49-50'
tribe.db.restricted = False

tribe = create_script('typeclasses.scripts.tribeScript',key = 'Hunters_in_Darkness')
tribe.db.longname = 'Hunters in Darkness'
tribe.db.renown = 'Purity'
tribe.db.tribe_gifts = ['Nature', 'Stealth', 'Warding']
tribe.db.info = 'The Hunters in Darkness are the quintessential werewolves, at least as popular culture imagines them. Beasts cleverer than any wolf and more savage than any man, they tolerate no intruders in their territory. They stalk and harry, picking off the weakest and most isolated first, building the rest to a fever pitch of terror and a headlong dash through the night. It’s not enough to simply drive interlopers off. The Meninna’s hunt only ends one way, for long ago they swore an oath: Nu Mus Halhala. “Let No Sacred Place in Your Territory Be Violated.”'
tribe.db.reference = 'W:tF p. 40-42'
tribe.db.restricted = False

tribe = create_script('typeclasses.scripts.tribeScript',key = 'Iron_Masters')
tribe.db.longname = 'Iron Masters'
tribe.db.renown = 'Cunning'
tribe.db.tribe_gifts = ['Knowledge', 'Shaping', 'Technology']
tribe.db.info = 'The Iron Masters are adapters, survivors, and innovators. Constantly questioning themselves, they preserve that which deserves to stay and ruthlessly cull what no longer has a place. Traditions, ethoses, institutions, even people — if the Iron Masters say your time is up, no force on Earth can save you. They dwell among humans, because like it or not humans are leading the charge on innovation and adaptation. They aren’t the “modern tribe,” because that’s a false categorization. All the tribes live in the modern world, and they all employ its conveniences. What the Iron Masters do is adapt: They judge every change they see to know whether it is good or bad. They attach themselves to specific institutions or areas of their territories and either change them to be better or protect them from change, for long ago they swore an oath: Kul Kisura Udmeda. “Honor Your Territory in All Things.”'
tribe.db.reference = 'W:tF p. 43-45'
tribe.db.restricted = False

tribe = create_script('typeclasses.scripts.tribeScript',key = 'Storm_Lords')
tribe.db.longname = 'Storm Lords'
tribe.db.renown = 'Honor'
tribe.db.tribe_gifts = ['Evasion', 'Dominance', 'Weather']
tribe.db.info = 'The Storm Lords are cold, ruthless hunters. Even in the throes of Death Rage, they seem to have an icy calm about them. Pain does not faze them, pity does not move them, and nothing, absolutely nothing, will stop them. The prey can run. The prey can even hide. But running is tiring. Hiding gnaws at the mind with fear of being found. And every time the prey closes its eyes it knows that they are coming for it and they will not stop. For long ago they swore an oath: Nu Si Gid Namtar. “Allow No One to Witness or to Tend Your Weakness.”'
tribe.db.reference = 'W:tF p. 46-48'
tribe.db.restricted = False

pass