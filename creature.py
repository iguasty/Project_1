# creature class
import random

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
        """Upgrades Creature object's XP level with random number 1-50

        Returns:
            _type_: XP level
        """
        self.xp += random.randint(1, 50)
        return self.xp
    
    def ability_set(self, ability_num):
        """Assigns ability type to int input

        Args:
            ability_num (int): 1,2, or 3

        Returns:
            _type_: ability type
        """
        # match case for determining ability type
        if ability_num == 1:
                return "Flight"
        elif ability_num == 2:
                return "Invsibility"
        elif ability_num == 3:
                return "Fire resistance"
    
    def edit_attributes(self):
        """Edits the attribute values of class Creature

        Raises:
            ValueError: raised if self.ability has bad input
        """
        while True:
                try:
                    self.type = input("Set creature type -> ")
                    break
                except:
                    print("Invalid input. Try again")
        while True:
                try:
                    self.name = input("Set creature name -> ")
                    break
                except:
                    print("Invalid input. Try again")
        while True:
                try:
                    self.arm_count = int(input("Set arm amount -> "))
                    break
                except:
                    print("Invalid input. Try again")
        while True:
                try:
                    self.leg_count = int(input("Set leg amount -> "))
                    break
                except:
                    print("Invalid input. Try again")
        while True:
                try:
                    
                    ability = int(input("What ability does your creature have? Choose 1,2, or 3\n 1. Flight\n 2. Invisibility\n 3. Fire resistance\n-> "))
                    if ability == 1:
                        self.ability = ability
                        break
                    elif ability == 2:
                        self.ability = ability
                        break
                    elif ability == 3:
                        self.ability = ability
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid input. Try again")
                    

    def display_attributes(self):
        """Displays Creature objects attributes

        Returns:
            _type_: all attributes
        """
        return  f"Name: {self.name}\n" \
                f"{self.xp_units} {self.xp}\n" \
                f"Creature type: {self.type}\n" \
                f"{self.arm_count} {self.arm_units}\n" \
                f"{self.leg_count} {self.leg_units}\n" \
                f"Ability: {self.ability_set(self.ability)}"
    
    def write(self) -> None:
        output_file = open(self.name, "w")
        output_file.write(self.type + "\n")
        output_file.write(self.name + "\n")
        output_file.write(str(self.arm_count) + "\n")
        output_file.write(str(self.leg_count) + "\n")
        output_file.write(str(self.ability) + "\n")
        output_file.write(str(self.xp) + "\n")
        output_file.close()
        
def read(filename: str) -> Creature:
    input_file = open(filename, "r")
    lines = input_file.readlines()
    
    object_Creature = Creature()
    object_Creature.type = lines[0]
    object_Creature.name = lines[1]
    object_Creature.arm_count = int(lines[2])
    object_Creature.leg_count = int(lines[3])
    object_Creature.ability = int(lines[4])
    object_Creature.xp = int(lines[5])
    input_file.close()
    return object_Creature
        