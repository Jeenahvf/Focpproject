BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter a new password (8-12 characters): ").strip()
    password2 = input("Re-enter the new password: ").strip()

    if password1 != password2:
        print("Error: Passwords do not match.")
    elif not (8 <= len(password1) <= 12):
        print("Error: Password must be between 8 and 12 characters.")
    elif password1 in BAD_PASSWORDS:
        print("Error: Password is too common.")
    else:
        print("Password Set!")
        break