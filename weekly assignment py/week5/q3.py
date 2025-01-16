#Write a program that takes a bunch of command-line arguments, and then prints out the shortest. If there is more than one of the shortest length, any will do.

import sys

#Program to find the shortest command-line argument
if len(sys.argv) > 1:
    shortest_arg = min(sys.argv[1:], key=len)
    print(f"Shortest argument: {shortest_arg}")
else:
    print("No arguments provided.")
    