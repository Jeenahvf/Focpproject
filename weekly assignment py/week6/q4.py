#Computers are commonly used in encryption. A very simple form of encryption (more accurately "obfuscation") would be to remove the spaces from a message and reverse the resulting string. Write, and test, a function that takes a string containing a message and "encrypts" it in this way.

def encrypt_message(message: str) -> str:
    message_no_spaces = message.replace(" ", "")
    
    encrypt_message = message_no_spaces[::-1]
    return encrypt_message
#test cases
print(encrypt_message("send cheese"))
print(encrypt_message("send love"))
print(encrypt_message("hello"))
print(encrypt_message("how can"))

    
    