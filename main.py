# Cornell Stokes, 01/25/2025, CMPSCI 4500-001 Software Profession
import os
import re

def tagMatch ():
    #This is for the specific pattern Check. It must have a number 0-9, non negative, and be a English letter
    patternMatch = r'^[A-Za-z][0-9][A-Za-z]\.txt$'
    #https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
    #We first must make sure the directory exists at all.
    #https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/
    directory ="C:\\Users\\corne\\Downloads\\Individual1B"
    listDirectory = os.listdir(directory) #This will list all the files in the directory
    print(list)
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            print(os.path.join(directory, file))



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
        tagMatch()

    else:
        print("You did not press ENTER")


execution()
