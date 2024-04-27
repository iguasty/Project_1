# main menu function
import os
from creature import Creature
from creature import read
from test_mode import test_mode

def main_menu(object_Creature):
    """Main menu for program

    Args:
        object_Creature (object): passes Creature object through
    """
    while True:
        select = None # sets value to None so that if a bad input is given for the first try then it raises ValueError
        print( "Main Menu:\n\n1. Display Attributes\n2. Edit Attributes\n3. Upgrade XP Level\n4. Save creature file\n5. Open creature file\n6. Exit\n7. Testing")
        try:
            select = int(input("\nEnter selection -> ")) # user selects menu item
        except ValueError:
            os.system('cls')
            print("Invalid input. Try again.")

        # match case for selecting menu item
        match select:
            case 1:
                # display attributes
                os.system('cls') # clears terminal screen
                print(f"Here are your creatures attributes:\n\n{object_Creature.display_attributes()}\n") # calls method from class Creature to display objects attributes
            case 2:
                # edit attributes
                os.system('cls')
                object_Creature.edit_attributes()
            case 3:
                # upgrade XP level
                os.system('cls') 
                print(f"XP increased to {object_Creature.upgrade()}!\n")
            case 4:
                # save creature file
                os.system('cls')
                # try:
                object_Creature.write()
                print("Saved creature file")
                input("Press enter to return to menu.\n")
                # except:
                    # print("File save failed!\nPress any key and hit enter to return to menu.")
                    
            case 5:
                # open creature file 
                os.system('cls')
                try:
                    file = input("Enter file name to open: ")
                    object_Creature = read(file) 
                    print(f"File {file} successfully opened!")
                except FileNotFoundError:
                    input("File not found!\nPress enter to return to menu.")
            case 6:
                # exit program
                os.system('cls') 
                print("Goodbye!")
                break    
            case 7:
                # test mode
                test_mode(object_Creature) # calls test_mode function
                            
            case _:
                # error handling bad input, returns to main menu
                os.system('cls') 
                print("Invalid input. Try again.") # returns to main menu