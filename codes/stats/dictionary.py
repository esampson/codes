from typeclasses.scripts import Script

from evennia.utils.search import search_script_tag
from evennia import search_script

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
            if stat.type() not in ['basic', 'power', 'sphere']:
                if stat.type() in lists:
                    lists[stat.type()].append( stat.db.longname )
                else:
                    lists[stat.type()] = [ stat.db.longname ]
            word = ''
            for letter in stat.db.longname:
                word = word + letter.lower()
                if word in dictionary:
                    dictionary[word].append( [stat.db.longname, stat.type(), stat.id] )
                else:
                    dictionary[word] = [ [stat.db.longname, stat.type(), stat.id] ]
        for stat in stats:
            list = dictionary[stat.db.longname.lower()]
            counter = 0
            keep_list = []
            for item in list:
                if stat.db.longname == item[0].strip():
                    keep_list.append(counter)
                counter = counter + 1
            new_list = []
            for item in keep_list:
                new_list.append(list[item])
            dictionary[stat.db.longname.lower()] = new_list
        return [dictionary, lists]
                