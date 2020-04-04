"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter
from _testcapi import call_in_temporary_c_thread
from world.data import find
from world.data import get
from world.data import meets_prereqs


class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """

    pass

    def at_object_creation(self):

        """
        Called only at initial creation. This is a rather silly
        example since ability scores should vary from Character to
        Character and is usually set during some character
        generation step instead.
        """
        #set temporary command set
        self.cmdset.add('commands.character_commands.unfinished_character',
                                                        permanent=True)
        #set persistent attributes
        
        self.db.basics = {}
        
        self.db.sphere = {} 
        
        self.db.attributes = { 'Intelligence':1, 'Wits':1, 'Resolve':1,
                           'Strength':1, 'Dexterity':1, 'Stamina':1,
                           'Presence':1, 'Manipulation':1, 'Composure':1 }
        
        self.db.skills = { 'Academics':0, 'Computer':0, 'Crafts':0,
                          'Investigation':0, 'Medicine':0, 'Occult':0,
                          'Politics':0, 'Science':0, 'Athletics':0,
                          'Brawl':0, 'Drive':0, 'Firearms':0, 'Larceny':0,
                          'Stealth':0, 'Survival':0, 'Weaponry':0, 
                          'Animal Ken':0, 'Empathy':0, 'Expression':0,
                          'Intimidation':0, 'Persuasion':0, 'Socialize':0,
                          'Streetwise':0, 'Subterfuge':0 }
        
        self.db.advantages = {'Willpower':0, 'Health':[0,0,0] }
        
        self.db.power = {}
        
        self.db.specialties = []
        
        self.db.contracts = {}
        
        self.db.merits = []
        
    def template(self):
        return self.db.basics['Sphere']
    
    def intelligence(self):
        return self.db.attributes['Intelligence']
    
    def wits(self):
        return self.db.attributes['Wits']
    
    def resolve(self):
        return self.db.attributes['Resolve']
    
    def strength(self):
        return self.db.attributes['Strength']
    
    def dexterity(self):
        return self.db.attributes['Dexterity']
    
    def stamina(self):
        return self.db.attributes['Stamina']
    
    def presence(self):
        return self.db.attributes['Presence']
    
    def manipulation(self):
        return self.db.attributes['Manipulation']
    
    def composure(self):
        return self.db.attributes['Composure']
    
    def academics(self):
        return self.db.skills['Academics']
    
    def computer(self):
        return self.db.skills['Computer']
    
    def crafts(self):
        return self.db.skills['Crafts']
    
    def investigation(self):
        return self.db.skills['Investigation']
    
    def medicine(self):
        return self.db.skills['Medicine']
    
    def occult(self):
        return self.db.skills['Occult']
    
    def politics(self):
        return self.db.skills['Politics']
    
    def science(self):
        return self.db.skills['Science']
    
    def athletics(self):
        return self.db.skills['Athletics']
    
    def brawl(self):
        return self.db.skills['Brawl']
    
    def drive(self):
        return self.db.skills['Drive']
    
    def firearms(self):
        return self.db.skills['Firearms']
    
    def larceny(self):
        return self.db.skills['Larceny']
    
    def stealth(self):
        return self.db.skills['Stealth']
    
    def survival(self):
        return self.db.skills['Survival']
    
    def weaponry(self):
        return self.db.skills['Weaponry']
    
    def animal_ken(self):
        return self.db.skills['Animal Ken']
    
    def empathy(self):
        return self.db.skills['Empathy']
    
    def expression(self):
        return self.db.skills['Expression']
    
    def intimidation(self):
        return self.db.skills['Intimidation']
    
    def persuasion(self):
        return self.db.skills['Persuasion']
    
    def socialize(self):
        return self.db.skills['Socialize']
    
    def streetwise(self):
        return self.db.skills['Streetwise']
    
    def subterfuge(self):
        return self.db.skills['Subterfuge']
    
    def get(self, entry, subentry='', statclass=''):
        try:
            result = get(self,entry,subentry=subentry,statclass=statclass)
        except:
            return -1
        else:
            return result
    
    def meets_prereqs(self, entry, statclass='', subentry='',value=0 ):
        try:
            result = meets_prereqs(self,entry,statclass=statclass,subentry=subentry,value=value)
        except:
            return False
        else:
            return result
    

    

        
        
                