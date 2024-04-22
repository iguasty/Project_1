# main menu function
import os
from creature import read

def main_menu(object_Creature):
    """Main menu for program

    Args:
        object_Creature (object): passes Creature object through
    """
    while True:

        print( "Main Menu:\n\n1. Display Attributes\n2. Edit Attributes\n3. Upgrade XP Level\n4. Save creature file\n5. Open creature file\n6. Exit")
        select = int(input("\nEnter selection -> ")) # user selects menu item

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
                    read(file)
                    print(f"File {file} successfully opened!")
                except FileNotFoundError:
                    input("File not found!\nPress enter to return to menu.")
            case 6:
                # exit program
                os.system('cls') 
                print("Goodbye!")
                break    
            case _:
                # error handling bad input, returns to main menu
                os.system('cls') 
                print("Invalid input. Try again.") # returns to main menu