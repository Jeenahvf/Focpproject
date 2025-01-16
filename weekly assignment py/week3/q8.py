#Times Table for negative Input will print Backward

number = int(input("Enter the number of the times table (0-12, negative for reverse):"))

if abs(number) > 12:
    print ("Error: please enter a number between -12 to 12.")
else:
    if number >=0:
        for i in range (13):
            print(f"{i} x {number} = {i * number}")
        else:
            number = abs(number)
            for i in range(12, -1, -1):
                print (f"{i} x {number} = {i * number}")