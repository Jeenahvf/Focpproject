#times table user selected

number = int (input("enter the number of the times table (0-12):"))
if 0 <= number <=12:
    for i in range(13):
        print(f"{i} x {number} = {i * number}")
    else:
        print("Error: Please enter number between 0-12")
        
            
