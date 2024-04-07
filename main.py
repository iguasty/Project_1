
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
        self.xp_units ="Level"  # unit attributes defined without variable so they cannot be changed
        self.arm_units = "arms"     
        self.leg_units = "legs"

    def upgrade(self):
        """Upgrade this Creatures XP"""
        self.xp += 5

    def display_attributes(self):
        """Display creatures attributes"""
        return f"{self.upgrade}:\n"

    def edit_attributes(self):
        """Edit creatures attributes"""


# main 
# start program by asking name
print("Welcome to the Creature Creator! What is your name?")
user_name = input("My name is: ")
print(f"Hello {user_name}! Time to create your creature.")

my_creature = Creature(input("What is the creatures type? (Ex. unicorn)\n-> "),
                       input("What is the creatures name?\n-> "),
                       int(input("How many arms does the creature have?\n->")),
                       int(input("How many legs does the creature have? ")),
                       int(input(f"What ability does your creature have? Choose 1,2, or 3\n 1. Flight\n 2. Invisibility\n 3. Fire resistance\n-> "))
                       )

print(my_creature.display_attributes)
