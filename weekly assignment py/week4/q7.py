#Write a program that reads 6 temperatures (in the same format as before), and displays the maximun, minimum, and mean of the values.

temps = []
for _ in range(6):
    temp_input = input("Enter a temperature (e.g., 24C):").strip()
    if temp_input [-1].upper() == 'C' and temp_input[:-1].isdigit():
        
        temps.append(float(temp_input[:-1]))
    else:
        print("Invalid input format. Skipping.")
        if temps :
            print(f"Max: {max(temps):.2f}C, Min:{min(temps):.2f}C, Mean: {sum(temps)/len(temps):.2f}C")
        else:
            print("No valid temperatures entered.")
            
    