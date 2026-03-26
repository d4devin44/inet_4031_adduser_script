# INET4031 Add Users Script and User List

## Program Description

The program is a Python script that automates the task of adding new users to a Linux system. Without it, an administrator would need to manually run commands such as adduser to create accounts, passwd to assign passwords, and other commands to correctly group users. The script eliminates this repetitive process by reading user details from a file and executing all necessary commands automatically. It takes care of creating accounts, setting passwords, and managing group assignments all in one step. 

## Program User Operation

This program functions by reading the data from an input file and processing each line within that file. Each line represents one user and contains all the information required to create an account. 

### Input File Format

Input file utilize colons to represent each user. Each line has 5 different fields: username, password, last name, first name, and group list. The group list is able to contain multiple groups. If a user has a dash, then that lets us know that the user shouldn't be added onto any groups. If a line starts with a #, then the script will skip that line and move onto the next. In the case that a line doesn't have all 5 fields, then it will be deemed invalid and be skipped as well.


### Command Excuction

In order to run a script, a user will have to first have a file that is executable in the first place. Next, the script can be ran through redirecting the input file into the script. The script will then read each line from the input file and processes it in that way.



### "Dry Run"

A dry run allows a user to test the functionality of a script without having to actually run the entire program. The script goes through the logic and prints out the commands that would have been executed as without them actually happening. This is useful for testing and ensuring that the script is functioning correctly. It helps prevent mistakes and aids the user in what they should fix to ensure that when the script is actually ran, there are none/limited errors.

