#test a function that converts temperature measured in degrees centigrade into the equivalent in fahrenheit, and another that does the reverse.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) +32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

#Test program
c = float (input ("Enter temperature in Celsius: "))
print (f"{c}Â°C={celsius_to_fahrenheit(c)}Â°F")

f = float(input ("Enter temperature in Fahrenheit: "))
print(f"{f}Â°F={fahrenheit_to_celsius(f)}Â°C")
