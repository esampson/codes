from typeclasses.scripts import Script

from evennia.utils.search import search_script_tag

typeclass_to_type = {'world.stats.skillScripts.skillScript' : 'skill',
                     'world.stats.advantageScripts.advantageScript' : 'advantage',
                     'world.stats.attributeScripts.attributeScript' : 'attribute',
                     'world.stats.basicStatScripts.basicStatScript' : 'basic',
                     'world.stats.contractScripts.contractScript' : 'contract',
                     'world.stats.meritScripts.meritScript' : 'merit',
                     'world.stats.powerStatScripts.powerStatScript' : 'power',
                     'world.stats.sphereStatScripts.sphereStatScript' : 'sphere'}

type_to_typeclass = {'skill' : 'world.stats.skillScripts.skillScript',
                     'advantage' : 'world.stats.advantageScripts.advantageScript',
                     'attribute' : 'world.stats.attributeScripts.attributeScript',
                     'basic' : 'world.stats.basicStatScripts.basicStatScript',
                     'contract' : 'world.stats.contractScripts.contractScript',
                     'merit' : 'world.stats.meritScripts.meritScript',
                     'power' : 'world.stats.powerStatScripts.powerStatScript',
                     'sphere' : 'world.stats.sphereStatScripts.sphereStatScript'}

class dictionaryScript(Script):
    
    def at_script_creation(self):
            self.persistent = True  # will survive reload
            self.tags.add('dictionary_data')
            self.name('Stat Dictionary')
            
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
                