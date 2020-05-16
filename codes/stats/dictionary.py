from typeclasses.scripts import Script

from evennia.utils.search import search_script_tag

class dictionaryScript(Script):

    def at_script_creation(self):
            self.persistent = True  # will survive reload
            self.tags.add('dictionary_data')

    def at_start(self):
        self.dictionary = {}
        self.lists = {}
        self.generate_data()

    def generate_data(self):
        stats = search_script_tag('stat_data')
        for stat in stats:
            self.insert(stat)

    def insert(self,stat):

        # Add stat to dictionary entries
        word = ''
        for letter in stat.db.longname:
            word = word + letter.lower()
            if word in self.dictionary:
                self.dictionary[word].append([stat.db.longname, stat.type(), stat.id])
            else:
                self.dictionary[word] = [[stat.db.longname, stat.type(), stat.id]]

        # Clear partial matches if given entry has a full match
        entries = self.dictionary[stat.db.longname.lower()]
        counter = 0
        keep_entries = []
        for item in entries:
            if stat.db.longname == item[0].strip():
                keep_entries.append(counter)
            counter = counter + 1
        new_entries = []
        for item in keep_entries:
            new_entries.append(entries[item])
        self.dictionary[stat.db.longname.lower()] = new_entries

        # Add to lists
        if stat.type() not in ['basic', 'power', 'sphere']:
            if stat.type() in self.lists:
                self.lists[stat.type()].append(stat.db.longname)
            else:
                self.lists[stat.type()] = [stat.db.longname]
