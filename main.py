import os
import random

# class declaration
class Creature:
    def __init__(self,
                 new_type: str = "unnamed creature type",
                 new_name: str = "unnamed creature",
                 new_arm_count: int = 0,
                 new_leg_count: int = 0,
                 new_ability: int = 0,
                 new_xp: int = 0):
        """Initialize a Creature"""
        self.type = new_type
        self.name = new_name
        self.arm_count = new_arm_count
        self.leg_count = new_leg_count
        self.ability = new_ability
        self.xp = new_xp
        self.xp_units ="XP Level"  # unit attributes defined without variable so they cannot be changed
        self.arm_units = "arms"     
        self.leg_units = "legs"

    def upgrade(self):
        """Upgrade this Creature's XP"""
        self.xp += random.randint(1, 50)
        return self.xp
    
    def ability_set(self, ability_num):
        """Determines ability"""
        # match case for determining ability type
        match ability_num:
            case 1:
                return "Flight"
            case 2:
                return "Invsibility"
            case 3:
                return "Fire resistance"
            case _:
                return "Not set"
                    
        

    def display_attributes(self):
        """Display creatures attributes"""
        return  f"Name: {self.name}\n" \
                f"{self.xp_units} {self.xp}\n" \
                f"Creature type: {self.type}\n" \
                f"{self.arm_count} {self.arm_units}\n" \
                f"{self.leg_count} {self.leg_units}\n" \
                f"Ability: {self.ability_set(self.ability)}"
               
# main
# start program by asking name

os.system('cls') # clears terminal screen 

print("Welcome to the Creature Creator! What is your name?")
user_name = input("My name is:\n-> ") 
os.system('cls') 
print(f"Hello {user_name}! Time to create your creature.")

# create object instance and ask user input for attribute values
my_creature = Creature(input("What is the creatures type? (Ex. unicorn)\n-> "),
                       input("What is the creatures name?\n-> "),
                       int(input("How many arms does the creature have?\n-> ")),
                       int(input("How many legs does the creature have?\n-> ")),
                       int(input("What ability does your creature have? Choose 1,2, or 3\n 1. Flight\n 2. Invisibility\n 3. Fire resistance\n-> "))
                       )


os.system('cls')

# enter while loop for menu
loop_program = True
while loop_program:
    print( "Main Menu:\n\n1. Display Attributes\n2. Edit Attributes\n3. Upgrade XP Level\n4. Exit program")
    
    select = int(input("\nEnter selection -> ")) # user selects menu item

    # match case for selecting menu item
    match select:
        case 1:
            os.system('cls') # clears terminal screen
            print(f"Here are your creatures attributes:\n\n{my_creature.display_attributes()}\n") # calls method from class Creature to display objects attributes
        case 2:
            os.system('cls')
            # sets new values to objects attributes
            my_creature.__init__(input("Set creature type\n-> "),
                                        input("Set creature name\n-> "),
                                        int(input("Set arm amount\n-> ")),
                                        int(input("Set leg amount\n-> ")),
                                        int(input("Set ability. Choose 1,2, or 3\n 1. Flight\n 2. Invisibility\n 3. Fire resistance\n-> "))
                                        )
        case 3:
            os.system('cls') 
            print(f"XP increased to {my_creature.upgrade()}!\n")
        case 4:
            os.system('cls') 
            print("Goodbye!")
            loop_program = False  # exits program
        case _:
            os.system('cls') 
            print("That is not a valid option. Try again.") # returns to main menu
            