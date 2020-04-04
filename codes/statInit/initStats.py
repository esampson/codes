from evennia import create_script
from codes.statInit import initAdvantages
from codes.statInit import initAttributes
from codes.statInit import initBasicStats
from codes.statInit import initContracts
from codes.statInit import initMerits
from codes.statInit import initPowerStats
from codes.statInit import initSkills
from codes.statInit import initSphereStats
create_script('typeclasses.scripts.dictionaryScript',key='Dictionary',persistent=True)