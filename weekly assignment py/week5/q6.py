#Write a program that takes the name of a file as a command-line argument, and creates a backup copy of that file. The backup should contain an exact copy of the contents of the original and should, obviously, have a different name. Hint: By now, you should be getting the idea that there is a built-in way to do the heavy lifting here! Take a look at the "Brief Tour of the Standard Library" in the docs.

import sys
import shutil

# Program to create a backup of a file
if len(sys.argv) > 1:
    file_name = sys.argv[1]
    backup_name = f"{file_name}.backup"
    
    try:
        shutil.copy(file_name, backup_name)
        print(f"Backup created: {backup_name}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found")
    except Exception as e:
        print(f"Error creating backup: {e}")
else:
    print("Please provide a file name as a command-line argument.")
 
