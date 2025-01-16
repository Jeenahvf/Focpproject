#Write a program that decrypts messages encoded as above.
import random
import string

def decrypt_with_interval(encrypted_message: str, interval: int) -> str:
    # Initialize the original message (a list to store characters)
    original_message = []
    
    # Iterate through the encrypted message, picking every `interval`-th character
    for i in range(0, len(encrypted_message), interval):
        original_message.append(encrypted_message[i])
    
    # Join the list into a string to get the original message
    return ''.join(original_message)

# Example of usage
# Encrypt a message first
def encrypt_with_interval(message: str) -> str:
    interval = random.randint(2, 20)  # Generate a random interval between 2 and 20
    encrypted_message = []
    message_index = 0
    while message_index < len(message):
        encrypted_message.append(message[message_index])
        for _ in range(interval - 1):  # Insert (interval-1) random characters
            encrypted_message.append(random.choice(string.ascii_lowercase))
        message_index += 1
    return ''.join(encrypted_message), interval

# Test cases for encrypting and decrypting
original_message = "send cheese"
encrypted_message, interval_used = encrypt_with_interval(original_message)

print(f"Original Message: {original_message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Interval Used: {interval_used}")

# Decrypt the message using the interval
decrypted_message = decrypt_with_interval(encrypted_message, interval_used)
print(f"Decrypted Message: {decrypted_message}")
