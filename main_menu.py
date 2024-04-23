# main menu function
import os
from creature import Creature
from creature import read

def main_menu(object_Creature):
    """Main menu for program

    Args:
        object_Creature (object): passes Creature object through
    """
    while True:

        print( "Main Menu:\n\n1. Display Attributes\n2. Edit Attributes\n3. Upgrade XP Level\n4. Save creature file\n5. Open creature file\n6. Exit\n7. Testing")
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
                os.system('cls')
                print("You have entered test mode.")
                while True:
                    print( "Test Menu:\n1. Test File\n2. Test Object Creation\n3. Exit")
                    test_select = int(input("\nEnter selection -> ")) # user selects menu item
                    match test_select:
                        case 1:
                            # open test file
                            os.system('cls')
                            print("Opening test file test_creature")
                            try:
                                file = input("Enter test file to open: ")
                                object_Creature = read(file) 
                                print(f"File {file} successfully opened!")
                                
                                if object_Creature.type == str("type\n"):
                                    print("Type test: PASSED")
                                else:
                                    print("Type test: FAILED")
                                    
                                if object_Creature.name == str("name\n"):
                                    print("Name test: PASSED")
                                else:
                                    print("Name test: FAILED")
                                    
                                if object_Creature.arm_count == 1000:
                                    print("Arm count test: PASSED")
                                else:
                                    print("Arm count test: FAILED")
                                    
                                if object_Creature.leg_count == 1000:
                                    print("Leg count test: PASSED")
                                else:
                                    print("Leg count test: FAILED")
                                    
                                if object_Creature.ability == 3:
                                    print("Ability test: PASSED")
                                else:
                                    print("Ability test: FAILED")
                                
                                if object_Creature.xp == 1000:
                                    print("XP test: PASSED")
                                else:
                                    print("XP test: FAILED")
                                    
                            except FileNotFoundError:
                                input("File not found!\nPress enter to return to menu.")
                        case 2:
                            # test object creation
                            os.system('cls')
                            try:
                                #create new object
                                test_creature = Creature()
                                print(f"Creating new creature object\n {test_creature.display_attributes()}")
                            except:
                                print("Creature object creation failed\n")
                                input("Press enter to return to menu.")
                                
                        case 3:
                            os.system('cls')
                            print("Exiting to main menu.")
                            break
                        case _:
                            os.system('cls')
                            print("Invalid input. Try again.")
                            
            case _:
                # error handling bad input, returns to main menu
                os.system('cls') 
                print("Invalid input. Try again.") # returns to main menu