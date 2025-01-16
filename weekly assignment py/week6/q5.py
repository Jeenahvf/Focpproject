#Another way to hide a message is to include the letters that make it up within seemingly random text. The letters of the message might be every fifth character, for example. Write and test a function that does such encryption. It should randomly generate an interval (between 2 and 20), space the message out accordingly, and should fill the gaps with random letters. The function should return the encrypted message and the interval used. For example, if the message is "send cheese", the random interval is 2, and for clarity the random letters are not random: send cheese s e n d c h e e s e sxyexynxydxy cxyhxyexyexysxye

import random
import string

def encrypt_with_interval(message: str) -> str:
    # Generate a random interval between 2 and 20
    interval = random.randint(2, 20)
    
    # Prepare the encrypted message by adding random letters at intervals
    encrypted_message = []
    
    # Iterate through the message and insert random letters at the interval
    message_index = 0
    while message_index < len(message):
        encrypted_message.append(message[message_index])
        
        # Insert random letters for the gap
        for _ in range(interval - 1):  # Insert (interval-1) random characters
            encrypted_message.append(random.choice(string.ascii_lowercase))
        
        message_index += 1

    encrypted_message_str = ''.join(encrypted_message)
    
    return encrypted_message_str, interval

# Test cases
encrypted_message, interval_used = encrypt_with_interval("send cheese")
print(f"Encrypted Message: {encrypted_message}")
print(f"Interval Used: {interval_used}")

encrypted_message, interval_used = encrypt_with_interval("hello world")
print(f"Encrypted Message: {encrypted_message}")
print(f"Interval Used: {interval_used}")
