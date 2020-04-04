from typeclasses.scripts import Script

from evennia.utils.search import search_script_tag

typeclass_to_type = {'codes.stats.skillScripts.skillScript' : 'skill',
                     'codes.stats.advantageScripts.advantageScript' : 'advantage',
                     'codes.stats.attributeScripts.attributeScript' : 'attribute',
                     'codes.stats.basicStatScripts.basicStatScript' : 'basic',
                     'codes.stats.contractScripts.contractScript' : 'contract',
                     'codes.stats.meritScripts.meritScript' : 'merit',
                     'codes.stats.powerStatScripts.powerStatScript' : 'power',
                     'codes.stats.sphereStatScripts.sphereStatScript' : 'sphere'}

type_to_typeclass = {'skill' : 'codes.stats.skillScripts.skillScript',
                     'advantage' : 'codes.stats.advantageScripts.advantageScript',
                     'attribute' : 'codes.stats.attributeScripts.attributeScript',
                     'basic' : 'codes.stats.basicStatScripts.basicStatScript',
                     'contract' : 'codes.stats.contractScripts.contractScript',
                     'merit' : 'codes.stats.meritScripts.meritScript',
                     'power' : 'codes.stats.powerStatScripts.powerStatScript',
                     'sphere' : 'codes.stats.sphereStatScripts.sphereStatScript'}

class dictionaryScript(Script):
    
    def at_script_creation(self):
            self.persistent = True  # will survive reload
            self.tags.add('dictionary_data')
            
    def at_start(self):
        data = self.generate_data() 
        self.dictionary = data[0]
        self.lists = data[1]
    

    def generate_data(self):
        dictionary = {}
        lists = {}
        stats = search_script_tag('stat_data')
        for stat in stats:
            if typeclass_to_type[stat.typeclass_path] not in ['skill', 'advantage', 'attribute', 'basic', 'power', 'sphere']:
                if typeclass_to_type[stat.typeclass_path] in lists:
                    lists[typeclass_to_type[stat.typeclass_path]].append( stat.db.longname )
                else:
                    lists[typeclass_to_type[stat.typeclass_path]] = [ stat.db.longname ]
            word = ''
            for letter in stat.db.longname:
                word = word + letter.lower()
                if word in dictionary:
                    dictionary[word].append( [stat.db.longname, typeclass_to_type[stat.typeclass_path], stat.id] )
                else:
                    dictionary[word] = [ [stat.db.longname, typeclass_to_type[stat.typeclass_path], stat.id] ]
        return [dictionary, lists]
                