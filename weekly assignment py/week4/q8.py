#Modify the previous program so that it can process any number of values. The input terminates when the user just presses "Enter at the prompt rathe than entering a value.

temps =[]
while True:
    temp_input = input("Enter a temperature (e.g., 25C) or press Enter to stop: ").strip()
    if not temp_input:
        break
    if temp_input[-1].upper() == 'C' and temp_input[:-1].isdigit():
        temps.append(float(temp_input[:-1]))
    else:
        print("Invalid input format. try again.")
        if temps:
            print(f"Max: {max(temps):.2f}C, Min: {min(temps):2f}C, Mean: {sum(temps)/len(temps):.2f}C")
        else:
            print("No valid temperature entered.")
    
    