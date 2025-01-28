#Sources used
#https://www.geeksforgeeks.org/python-list-files-in-a-directory/
#https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
#https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/
#https://docs.python.org/3/library/re.html
# https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/


#This is the main file for the program. This is done in Python, and create in Pycharm
#This program scans the current directory for files and lists their names.
#It searches for a file matching the patterrn AXB.txt pattern, where A and B are letters, and X is a single digit (0-9).
#If exactly one match is found, it copies the file to FOUNDit.txt, then displays whats inside the file.


# Name: Cornell Stokes
# Date: 01/25/2025
# Class Section: CMPSCI 4500-001 Software Profession
import os
import re

def fileManagement ():
    #This is for the specific pattern Check. It must have a number 0-9, non negative, and be a English letter
    #We first must make sure the directory exists at all.
    # file for regex
    # file = 'C:\\Users\\corne\\Downloads\\Individual1B\\A0B.txt' IT MUST BE IN THIS FORMAT FOR PROGRAM TO SEARCH
    patternMatch = r'^[A-Za-z][0-9][A-Za-z]\.txt$'
    directory ="C:\\Users\\corne\\Downloads\\Individual1B"
    listDirectory = os.listdir(directory) #This will list all the files in the directory
    #This is for important for the pattern match for same file named files.
    fileMatch = [file for file in listDirectory if re.fullmatch(patternMatch, file)]
    #Also need to account for these situations
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            print(os.path.join(directory, file))
        if re.fullmatch(patternMatch, file):
            print("File:  ", file)
        if




def execution():
    ent = input(
        "This program scans the current directory for files and lists their names.\n"
        "It then searches for a file matching the pattern AXB.txt, where A and B are letters,\n"
        "and X is a single digit (0-9).\n\n"
        "If exactly one matching file is found, its contents are copied to FOUNDit.txt\n"
        "and displayed on the screen.\n\n"
        "Press ENTER to proceed."
    )

    if ent == "":
        print("You pressed ENTER")
        fileManagement()

    else:
        print("You did not press ENTER")


execution()
