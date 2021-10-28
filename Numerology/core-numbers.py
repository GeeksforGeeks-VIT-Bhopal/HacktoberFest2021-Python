import datetime 
class Numerology():
    # Pythagorean Numerology 
    def __init__(self, month, year, day, first_name, last_name, middle_name=""):
        """ The birth day number is the day one was born so it will automatically be placed into the profile (below)"""
        # The date of Birth
        self.DOB = [day, month, year]
        # Birth Name (Middle Name is an optional input). 
        # self.name is 2 strings, one that is more efficient for necessary calculations and one that is formatted for the output at the end.
        self.name = str(first_name + middle_name + last_name).replace(' ', '').lower(), " ".join([first_name.capitalize(), middle_name.capitalize(), last_name.capitalize()])
        # Pythagorean key for converting letters to their corresponding numeric value
        self.conversion = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':1,'k':2,'l':3,'m':4,'n':5,'o':6,'p':7,'q':8,'r':9,'s':1,'t':2,'u':3,'v':4,'w':5,'x':6,'y':7,'z':8}
        # The consistent Vowels in the english alphabet. 
        self.vowels = 'aeiou'
        
    def add_and_reduce(self, num):
        """ This method is going to do the 'recursive' math for each of the core number groupings (see methods below). """
        """ It takes in a multi-digit value (102, 81, 2005, etc) then adds it together and reduces it until it becomes a 'numerology number' (one that is between 1 and 9) """ 
        number = sum([int(x) for x in str(num) if int(num) >= 9])
        if len(str(number)) > 1: 
            number = sum([int(x) for x in str(number) if int(number) >= 9])
        return number
        
        
class Core_Numbers(Numerology):
    """ This will be the user's core number profile. """
    def __init__(self, month, year, day, first_name, last_name, middle_name=""):
        Numerology.__init__(self, month, year, day, first_name, last_name, middle_name)
            
        self.core_numbers = {"Birth Day Number": str(day)}

    def birth_day_number(self):
        """ If the birth day number is a two digit number, change the value in the core_numbers dict to reflect the alrernative birthday number (which is the two digits added together) """ 
        day_number = self.core_numbers["Birth Day Number"]
        # add together the singular digits if apllicable. Not using the 'add_and_reduce' function here because birthday numbers can be larger than the number 9 
        alt_day_num = [(int(day_number[0])+int(day_number[1])) for number in day_number if len(day_number) > 1]
        # add to core_numbers dict if applicable
        if alt_day_num != []:
            self.core_numbers["Birth Day Number"] = "{} \nAlternative Birth Day Number: {}".format(day_number, alt_day_num[0])
        # if not applicable, keep the dictionary the same.
        else: 
            self.core_numbers["Birth Day Number"] = day_number
        return self.core_numbers

    def lifepath_number(self):
        """ Lifepath Number = the date of birth """ 
        lifepath = self.add_and_reduce(sum(self.DOB))
        self.core_numbers["Lifepath Number"] = lifepath
        return lifepath
        
        
    def destiny_number(self):
        """ Destiny Number = all letters in the full birth name """ 
        destiny = self.add_and_reduce(sum([self.conversion[letter] for letter in self.name[0]]))
        self.core_numbers["Destiny Number"] = destiny
        return destiny
        
    def hearts_desire_number(self):
        """ Heart's Desire Number = the vowels in the full birth name """
        hearts_desire = self.add_and_reduce(sum([self.conversion[letter] for letter in self.name[0] if letter in self.vowels]))
        self.core_numbers["Heart's Desire Number"] = hearts_desire
        return hearts_desire
        
    def personality_number(self):
        """ Personality Number = the consonants in the full birth name """
        personality = self.add_and_reduce(sum([self.conversion[letter] for letter in self.name[0] if letter not in self.vowels]))
        self.core_numbers["Personality Number"] = personality
        
        return personality
        
    def core_profile_wrapper(self):
        """ Call all the above functions/methods in order to fill the core_numbers (dict) profile. Returns a formatted string that consists of each dict pair [{key}:  {value}]"""
        all_numbers = self.birth_day_number(), self.personality_number(), self.hearts_desire_number(),self.lifepath_number(),self.destiny_number()
        return "".join(["\n{}: {}".format(number[0], number[1]) for number in self.core_numbers.items()])
    
    def __str__(self):
        """ Returns each number in the user's Numerological Core profile """
        return "Core Numbers Profile for {} \nBorn on {} \n{}".format(self.name[1],  datetime.datetime(self.DOB[2], self.DOB[1], self.DOB[0]).strftime("%A, %d %B %Y"), self.core_profile_wrapper())
        
        
def main_menu():
    """ Retrieve all input from end user and create their Numerology instance """ 
    print("Enter your name as it appears on your birth certificate: ")
    # Full name: First, Middle, Last
    first = input('First Name: ')
    print("If you do not have a middle name, press enter to continue")
    middle = input('Middle Name: ')
    last = input('Last Name: ')
    print("\nEnter your Date of Birth (numerically). ")
    # birth month (MM or M is fine)
    dob_month = int(input('Month: '))
    # birth day (DD or D is fine)
    dob_day = int(input('Day: '))
    # birth year (YYYY)
    dob_year = int(input('Year: '))
    # In case the User enters their birth year as a two digit number instead of a 4 digit number
    if len(str(dob_year)) < 4:
        print("ERROR! \nPlease Enter Your FOUR DIGIT Birth Year (YYYY)")
        dob_year = int(input('Year: '))
    # Return a New Instance of the Core_Numbers class, with the user's details 
    user = Core_Numbers(dob_month, dob_year, dob_day, first, last, middle)
    return user
    
if __name__ == '__main__':
    # if this program is run directly, it will prompt the user for all necessary input and then print out the user's core numerological numbers in a very basic text 'report' 
    user = main_menu()
    print(user.__str__())
