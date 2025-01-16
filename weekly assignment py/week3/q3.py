password = input("Enter a password(8-12character):")
if len(password) < 8 or len(password) > 12:
    print("Error: Password must be between 8-12 characters.")
else:
  password1 = input("Re-enter your password to confirm:")
  if password == password1:
      print("Password set successfully!")
  else:
      print("Error: Passwords do not match.")