# main

# start program by asking name
print("Welcome to the Creature Creator! What is your name?")
user_name = input("My name is: ")
print(f"Hello {user_name}! Time to create your creature.")

# class declaration
class Creature:
    def __init__(self,
                 new_type: str = "unnamed creature type",
                 new_name: str = "unnamed creature",
                 new_arm_count: int = 0,
                 new_leg_count: int = 0,
                 new_ability: int = 0):
        """Initialize a Creature"""
        self.type = new_type
        self.name = new_name
        self.arm_count = new_arm_count
        self.leg_count = new_leg_count
        self.ability = new_ability
        self.arm_units = "arms"     # unit attributes defined without variable so they cannot be changed
        self.leg_units = "legs"

