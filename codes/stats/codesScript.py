from typeclasses.scripts import Script

tags = { 'advantage_stat' : 'advantage',
         'attribute_stat' : 'attribute',
         'basic_stat' : 'basic',
         'contract_stat' : 'contract',
         'kith_stat' : 'kith',
         'merit_stat' : 'merit',
         'power_stat' : 'power',
         'seeming_stat' : 'seeming',
         'skill_stat' : 'skill',
         'sphere_stat' : 'sphere' }

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