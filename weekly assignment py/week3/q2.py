password=input("Enter your password:")
confirm=input("Re-enter your password:")
if password == confirm:
    print("Password is set.")
else:
    print("Error: Password do not match.")