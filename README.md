# Project_1

Project 2 is an extension of Project 1. It adds try and except clauses, test functions, and fileio.
The program runs a menu that the user interacts with attributes of the object from the class. 

This program is called Creature Creator. The function is to make creatures with user inputted attributes. It allows for saving creatures as files, opening a saved creature file, and even editing creature files. It features error handling for fileio, value errors, and object creation errors.

The driver file is named 'main.py'. When its run, the user will be asked for their name. The user will then be asked to input attributes for a new creature. After this, the main menu is displayed with multiple options that the user can choose from. The program supports displaying creature attributes, editing creature attributes, upgrading creature's XP level, saving creature as a file, opening an existing creature file, and a test mode. 

There are 2 example creature files already included: 'Jimwart' and 'Bob'

Test mode: 

There are a few test functions for this program. "Test File" compares 2 files to a newly created creature object with unedited attributes. "Test Object Creation" is a simple test that creates a new blank creature object and displays the attributes. If it fails to create one then will return "Creature object creation failed".

Test File:
    Step 1. 
        When using the program, select "5. Testing" and enter test_creature as the file name. Then select in the menu "1. Display attributes". 
        The attributes in test_creature are compared to the blank creature object below:

            Name: unnamed creature

            XP Level 0
            Creature type: unnamed creature type

            0 arms
            0 legs
            Ability: None

    Step 2. 
        Now we can test to see if these values PASS as the same compared to the new creature object's attributes. Go back to the main menu and select "7. Testing". When in the "Test Menu" select "1. Test File" and enter test_creature as the file name. Pressing enter will then create the new blank creature object and output whether each value PASSED or FAILED as being the same values. 

    Step 3.
        Repeat Step 1 and Step 2 but this time use the filename test_creature_bad. This file should display these bad attributes: 

            Name: bar

            XP Level 100
            Creature type: foo

            100 arms
            100 legs
            Ability: None
        
        These values are once again compared to the new creature object that is created while testing.

Test Object Creation:
    Step 1.
        Select "2. Test Object Creation". This will attempt to create a new blank creature object. If it succeeds then it will output:

            Creating new creature object
            Name: unnamed creature
            XP Level 0
            Creature type: unnamed creature type
            0 arms
            0 legs
            Ability: None
        
        If it fails, then it will output "Creature object creation failed".


Known Bugs:
    -When testing the test_creature file to see if the attribute values PASS as the same as a new blank creature object, the name and type attributes always FAIL even when they are set to the same value.