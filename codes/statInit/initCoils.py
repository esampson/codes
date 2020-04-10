from evennia import create_script

coil = create_script('typeclasses.scripts.coilScript',key = 'Mystery_of_the_Ascendant')
coil.db.longname = 'Mystery of the Ascendant'
coil.db.prereq = ''
coil.db.reference = 'VtR p. 155-156'
coil.db.info = 'The Mystery of the Ascendant follows one strict doctrine: The sun is the enemy; to overcome its rays is to overcome all adversity. Initiates of the Mystery believe that by overcoming the banes of fire and sunlight a Dragon can in turn defeat her every infirmity. This is not to be mistaken with a return to mortality. Such a change would be seen as an exchange of weaknesses, rather than true transcendence, and would be likely to get a vampire laughed at and his research ignored.'
coil.db.restricted = False

coil = create_script('typeclasses.scripts.coilScript',key = 'Mystery_of_the_Voivode')
coil.db.longname = 'Mystery of the Voivode'
coil.db.prereq = ''
coil.db.reference = 'VtR p. 158-159'
coil.db.info = 'In blood there is power; this is the creed of the King. While other Dragons concern themselves with banes and the Beast, those who follow the Mystery of the Voivode focus on the blood bond. They aim to rise above the petty politics and slaveries of the Damned, becoming beings of pure and transcendent will. In life, Dracula was called Voivode, and was not questioned. In death, his disciples will reclaim his authority.'
coil.db.restricted = False

coil = create_script('typeclasses.scripts.coilScript',key = 'Mystery_of_the_Wyrm')
coil.db.longname = 'Mystery of the Wyrm'
coil.db.prereq = ''
coil.db.reference = 'VtR p. 157-158'
coil.db.info = 'The common view of vampirism treats the condition as a curse, a supernatural affliction of body and soul. Initiates of the Wyrm spurn this notion. Within their doctrine the Requiem is a blessing. But for all its power the Beast is savage and easily roused to panic. The Mystery of the Wyrm intends to correct this, to refine the Beast and make it obedient to a Dragon’s desires.'
coil.db.restricted = False

pass