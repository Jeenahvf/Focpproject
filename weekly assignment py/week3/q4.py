#Check against common password

BAD_PASSWORDS = ['password', 'let me in', 'sesame', 'hello', 'justin bieber']

# Get user input for the password
password = input("Enter a password (8-12 characters): ")

# Check if the password length is valid
if len(password) < 8 or len(password) > 12:
    print(f"Error: Password must be between 8-12 characters.")

# Check if the password is too common
elif password in BAD_PASSWORDS:
    print(f"Error: This password is too common. Please choose a different one.")

# If the password passes both checks, ask for confirmation
else:
    password1 = input("Re-enter your password to confirm: ")
    
    # Check if the passwords match
    if password == password1:
        print(f"Password set successfully!")
    else:
        print(f"Error: Passwords do not match.")
