#Sources used
#https://www.geeksforgeeks.org/python-list-files-in-a-directory/
#https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
#https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/
#https://docs.python.org/3/library/re.html
# https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/
#Reading and writing to a file
#https://www.geeksforgeeks.org/read-content-from-one-file-and-write-it-into-another-file/


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
    directory =os.getcwd()
    listDirectory = os.listdir(directory) #This will list all the files in the directory
    #This is for important for the pattern match for same file named files.
    fileMatch = [file for file in listDirectory if re.fullmatch(patternMatch, file)]

    #Also need to account for these situations
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            print(os.path.join(directory, file))

    if len(fileMatch) == 0:
        print("Error, no files found matching the file pattern:  ")
        return
    elif len(fileMatch) == 1:
        print("File found:  ", fileMatch[0])
    elif len(fileMatch) > 1:
        print(f"Error: Multiple unique files found matching the file pattern: {fileMatch}")
        return# Show at least two unique files
    #If there is EXACTLY 1 file matching the pattern, then it will copy the file to FOUNDit.txt
    if len(fileMatch) == 1:
        with open(fileMatch[0], 'r') as file:
            with open('FOUNDit.txt', 'w') as newFile:
                newFile.write(file.read())
        print("File contents copied to FOUNDit.txt")

    newFile = open('FOUNDit.txt', 'r')
    print("The contents of the file cam from :", fileMatch)
    print(newFile.read())
    newFile.close()
    #Now print the file successfully copied to FOUNDit.txt with an ending message
    print("!SUCCESS. The file has been copied")




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
