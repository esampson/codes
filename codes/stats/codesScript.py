from typeclasses.scripts import Script

tags = { 'advantage_stat' : 'advantage',
         'attribute_stat' : 'attribute',
         'basic_stat' : 'basic',
         'contract_stat' : 'contract',
         'merit_stat' : 'merit',
         'power_stat' : 'power',
         'seeming_stat' : 'seeming',
         'skill_stat' : 'skill',
         'sphere_stat' : 'sphere' }

tag_list = [ 'advantage_stat', 'attribute_stat', 'basic_stat', 'contract_stat',
             'merit_stat', 'power_stat', 'seeming_stat', 'skill_stat',
             'sphere_stat' ]

class codesScript(Script):
    
    def at_script_creation(self):
            self.persistent = True  # will survive reload
            
    def type(self):
        
        result = 'unidentified'
        script_tags = self.tags.all()
        for item in script_tags:
            if item in tag_list:
                result = tags[item]
        return result