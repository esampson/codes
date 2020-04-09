from typeclasses.scripts import Script

tags = { 'advantage_stat' : 'advantage',
         'attribute_stat' : 'attribute',
         'basic_stat' : 'basic',
         'clan_stat' : 'clan',
         'contract_stat' : 'contract',
         'covenant_stat' : 'covenant',
         'cruac_rite_stat' : 'cruac rite',
         'devotion_stat' : 'devotion',
         'discipline_stat' : 'discipline',
         'kith_stat' : 'kith',
         'merit_stat' : 'merit',
         'power_stat' : 'power',
         'seeming_stat' : 'seeming',
         'skill_stat' : 'skill',
         'sphere_stat' : 'sphere',
         'theban_rite_stat' : 'theban rite' }

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