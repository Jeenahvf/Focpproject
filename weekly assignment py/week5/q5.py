#Last week you wrote a program that processed a collection of temperature readings entered by the user and displayed the maximum, minimum, and mean. Create a version of that program that takes the values from the command-line instead. Be sure to handle the case where no arguments are provided!

import sys

#Program to process temperature readings from command-line arguments
if len(sys.argv) > 1:
    temps = [float(arg) for arg in sys.argv[1:]] #converts arguments to float
    print(f"Max: {max(temps):.2f}C, Min: {min(temps):.2f}C, mean: {sum(temps)/len(temps):.2f}C")
else:
    print("No temperatures provided. Please provide temperatures as arguments.")