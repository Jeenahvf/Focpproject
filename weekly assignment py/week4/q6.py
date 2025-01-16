#write a program that takes a centigrade temperature and displays the equvalent in fahrenheit. The input should be a number followed by a letter C. The output should be in the same format.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

#program
temp_input = input("Enter a temperature (e.g., 32C): ").strip()
if temp_input[-1].upper() == 'C' and temp_input[:-1].isdigit():
    celsius=float(temp_input[:-1])
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}C = {fahrenheit:.2f}F")
else:
    print("Invalid input format.")
