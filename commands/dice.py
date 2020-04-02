from evennia import Command
from evennia import InterruptCommand
from operator import itemgetter
import random
from evennia.utils import evtable
from world.scroll import scroll

class CmdRoll(Command):
    
    key = '+roll'
    arg_regex = '^[\s/][0-9a-zA-Z/\-\s+:]+$'
    
    
    def func(self):
        
        data = self.args.split(' ', 1)
        args = []
        reroll_target = 10
        rote = False
        for item in data[0].split('/'):
            if item.lower() == '8-again':
                reroll_target = 8
            elif item.lower() == '9-again':
                reroll_target = 9
            elif item.lower() == 'no-10-again':
                reroll_target = 11
            elif item.lower() == 'rote':
                rote = True
        roll_cmd = data[1]
        temp = roll_cmd.replace('+','@').replace('-','@').split('@')
        num_parts = []
        count = 0
        for item in temp:
            insert = [ len(item.strip()), count, item.strip() ]
            num_parts.append(insert)
            count = count + 1
        num_parts = sorted(num_parts, key=itemgetter(0), reverse=True)
        signs = roll_cmd
        for item in sorted(num_parts, key=itemgetter(0), reverse=True):
           signs = signs.replace(item[2],'@')
        temp = signs.split('@')
        sign_parts = []
        for item in temp:
            sign_parts.append(item.strip())
        temp = sorted(num_parts, key=itemgetter(1))
        num_parts = []
        for item in temp:
            num_parts.append(item[2])
        numbers = []
        error = False                        #Lets us know if there is a problem interpreting something
        pure_numbers = True                   #Lets us know if only numbers were entered
        for item in num_parts:
            if item.isnumeric():
                numbers.append(int(item))
            elif '/' in item:
                pure_numbers = False
                value = self.caller.get(item.split('/')[0], statclass= item.split('/')[1])     
                if value < 0:
                    error = True   
                numbers.append(value)
            else:
                pure_numbers = False
                value = self.caller.get(item)
                numbers.append(value)
        if not error:
            count = 1
            total_dice = numbers[0]
            if len(numbers) > 1:
                for item in numbers[1:]:
                    if sign_parts[count] == '+':
                        total_dice = total_dice + item
                    elif sign_parts[count] == '-':
                        total_dice = total_dice - item
                    else:
                        error = True
                    count = count + 1
            base_roll = roll_sequence(total_dice, reroll_target)
            total_successes = 0
            if pure_numbers:
                roll_string = str(total_dice) + ' dice'
            else:
                roll_string = roll_cmd
            if rote:
                rote_dice = 0
                for die in base_roll[0]:
                    if die < 8:
                        rote_dice = rote_dice + 1
                rote_roll = roll_sequence(rote_dice, reroll_target)
                for item in rote_roll:
                    for subitem in item:
                        if subitem > 7:
                            total_successes = total_successes + 1
                message = self.caller.name + ' rolls ' + roll_string + ' as a rote action'
            else:
                message = self.caller.name + ' rolls ' + roll_string
            for item in base_roll:
                for subitem in item:
                    if subitem > 7:
                        total_successes = total_successes + 1
            if reroll_target == 8:
                message = message + ' with 8-Again'
            if reroll_target == 9:
                message = message + ' with 9-Again'
            if reroll_target == 11:
                message = message + ' without 10-Again'
            message = message + ' for ' + str(total_successes) + ' successes:\\n\\n'
            message = message + roll_breakdown(base_roll)
            if rote:
                message = message[:-1] + '; ' + roll_breakdown(rote_roll)
            table = scroll(message,width=54, padding=10, replacements=[['8,','|R8|n,'],['8.','|R8|n '],['8;','|R8|n;'],
                                                                       ['9,','|R9|n,'],['9.','|R9|n '],['9;','|R9|n;'],
                                                                       ['10,','|R10|n,'],['10.','|R10|n '],['10;','|R10|n;'],
                                                                       ['1.','1 '],['2.','2 '],['3.','3 '],['4.','4 '],['5.','5 '],
                                                                       ['6.','6 '],['7.','7 ']])
            self.caller.location.msg_contents(table)
        else:
            self.caller.msg('I couldn\'t figure out what you wanted to roll.')
        
        
def roll(dice):
        
    rolls = []
    for roll in range(dice):
        rolls.append(random.randint(1,10))
    return rolls
    
def roll_sequence(dice, target):
    
    sequence = []
    current_roll = roll(dice)
    current_roll.sort()
    sequence.append(current_roll)
    reroll_dice = roll_again(current_roll,target)
    while reroll_dice > 0:
        current_roll = roll(reroll_dice)
        current_roll.sort()
        sequence.append(current_roll)
        reroll_dice = roll_again(current_roll,target)
    return sequence

def roll_again(roll, target):
    
    rerolls = 0
    for die in roll:
        if die >= target:
            rerolls = rerolls + 1
    return rerolls

def roll_breakdown(roll):
    breakdown = ''
    for item in roll:
        component = ''
        for subitem in item:
            component = component + str(subitem) + ', '
        component = component[:-2] + '; '
        breakdown = breakdown + component
    breakdown = breakdown[:-2]+'.'
    return breakdown
        
        