import os
from creature import Creature
from main_menu import main_menu
# init
# start program by asking name

os.system('cls') # clears terminal screen 

print("Welcome to the Creature Creator! What is your name?")
user_name = input("My name is:\n-> ") 
os.system('cls') 
print(f"Hello {user_name}! Time to create your creature.")


my_creature = Creature()    # creates new Creature object from imported creature class


my_creature.edit_attributes()   # calls edit_attributes method to set attributes


main_menu(my_creature)  # calls imported main_menu function 