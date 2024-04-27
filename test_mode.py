import os
from creature import Creature
from creature import read

def test_mode(object_Creature):
    os.system('cls')
    print("You have entered test mode.")
    while True:
        print( "Test Menu:\n1. Test File\n2. Test Object Creation\n3. Exit")
        test_select = None # sets value to None so that if a bad input is given for the first try then it raises ValueError
        try:
            test_select = int(input("\nEnter selection -> ")) # user selects menu item
        except:
            os.system('cls')
            print("Invalid input. Try again.")
        match test_select:
            case 1:
                # open test file
                os.system('cls')
                try:
                    #create new object
                    test_creature = Creature()
                    print(f"Creating new creature object\n {test_creature.display_attributes()}")
                except:
                    print("Creature object creation failed\n")
                    input("Press enter to return to menu.")
                try:
                    file = input("Enter test file to open: ")
                    object_Creature = read(file) 
                    print(f"File {file} successfully opened!")
                    
                    if object_Creature.type == str(test_creature.type):
                        print("Type test: PASSED")
                    else:
                        print("Type test: FAILED")
                        
                    if object_Creature.name == str(test_creature.name):
                        print("Name test: PASSED")
                    else:
                        print("Name test: FAILED")
                        
                    if object_Creature.arm_count == test_creature.arm_count:
                        print("Arm count test: PASSED")
                    else:
                        print("Arm count test: FAILED")
                        
                    if object_Creature.leg_count == test_creature.leg_count:
                        print("Leg count test: PASSED")
                    else:
                        print("Leg count test: FAILED")
                        
                    if object_Creature.ability == test_creature.ability:
                        print("Ability test: PASSED")
                    else:
                        print("Ability test: FAILED")
                    
                    if object_Creature.xp == test_creature.xp:
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
                # error handling bad input, returns to main menu
                os.system('cls') 
                print("Invalid input. Try again.") # returns to main menu