#Write a program that processes a string representing a message and reports the six most common letters, along with the number of times they appear. Case should not matter, so "E" and "e" are considered the same. Hint: There are many ways to do this. It is obviously a dictionary, but we will want zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so best to ignore that initially, and then check the usual resources for the runes.
from collections import Counter

def frequency_analysis(message):
    message = message.lower()
    
    filtered_message = [char for char in message if char.isalpha()]
    
    # Use Counter to count the frequency of each letter
    letter_counts = Counter(filtered_message)
    
    most_common = letter_counts.most_common(6)
    
    print("The six most common letters are:")
    for letter, count in most_common:
        print(f"{letter}: {count}")

# Test the function
message = "Hello there! This is a test message for frequency analysis."
frequency_analysis(message)
