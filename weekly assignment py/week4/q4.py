#Write and test a function that takes a string parameter and returns it with the last character removed.(if the string contains one or fewer characters, return it unchanged. )

def remove_last_char(s):
    return s[:-1] if len(s) > 1 else s
#test program
test_string = input ("Enter a string:")
print("String after removing last character:", remove_last_char(test_string))