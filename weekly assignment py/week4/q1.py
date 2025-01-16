def is_in_range(value):
     return 0 <= value <= 100
 
 #test program
test_value = int(input("Enter a number:"))
if is_in_range(test_value):
    print("The number is in range (0-100).")
else:
    print("The number is out of range(0-100).")
 