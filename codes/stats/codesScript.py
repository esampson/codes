from typeclasses.scripts import Script

tags = { 'advantage_stat' : 'advantage',
         'arcana_stat' : 'arcana',
         'attribute_stat' : 'attribute',
         'auspice_stat' : 'auspice',
         'basic_stat' : 'basic',
         'clan_stat' : 'clan',
         'contract_stat' : 'contract',
         'coil_stat' : 'coil',
         'covenant_stat' : 'covenant',
         'cruac_rite_stat' : 'cruac rite',
         'devotion_stat' : 'devotion',
         'discipline_stat' : 'discipline',
         'gift_stat' : 'gift',
         'kith_stat' : 'kith',
         'lodge_stat' : 'lodge',
         'merit_stat' : 'merit',
         'order_stat' : 'order',
         'path_stat' : 'path',
         'power_stat' : 'power',
         'renown_stat' : 'renown',
         'scale_stat' : 'scale',
         'seeming_stat' : 'seeming',
         'skill_stat' : 'skill',
         'spell_stat' : 'spell',
         'sphere_stat' : 'sphere',
         'theban_rite_stat' : 'theban miracle',
         'tribe_stat' : 'tribe',
         'werewolf_rite_stat' : 'werewolf rite' }

class codesScript(Script):
    
    def at_script_creation(self):
            self.persistent = True  # will survive reload
            
    def type(self):
        
        result = 'unidentified'
        tag_list = list(tags.keys())
        script_tags = self.tags.all()
        for item in script_tags:
            if item in tag_list:
                result = tags[item]
        return result