#Greetings program so that the first letter of the name entered is always in uppercase with rest in lowercase

name = input("Enter your name:").strip().capitalize()
if name:
    print(f"Hello,  {name}!")
else:
    print("hello, Stranger!")