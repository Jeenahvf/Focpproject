#2. Write a program that, when run from the command line, reports how many arguments were provided. (Remember that the program name itself is not an argument)

import sys

#Program to count command-line arguments 
arg_count = len (sys.argv) - 1
print (f"Number of arguments provided: {arg_count}") 
