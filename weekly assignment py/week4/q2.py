def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

#test program
test_string = input("Enter a string: ")
upper, lower = count_case(test_string)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")

    