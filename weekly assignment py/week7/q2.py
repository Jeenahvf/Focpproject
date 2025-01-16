# Write and test three functions that each take two words (strings) as parameters and return sorted lists (as defined above) representing respectively: Letters that appear in at least one of the two words. Letters that appear in both words. Letters that appear in either word, but not in both.
def unique_sorted_letters(s):
    """Helper function to return a sorted list of unique letters in a string."""
    return sorted(set([char for char in s if char.isalpha()]))

def letters_in_at_least_one(word1, word2):
    """Returns sorted list of letters that appear in at least one of the two words."""
    set1 = set(unique_sorted_letters(word1))
    set2 = set(unique_sorted_letters(word2))
    return sorted(set1 | set2)  # Union of both sets

def letters_in_both(word1, word2):
    """Returns sorted list of letters that appear in both words."""
    set1 = set(unique_sorted_letters(word1))
    set2 = set(unique_sorted_letters(word2))
    return sorted(set1 & set2)  # Intersection of both sets

def letters_in_either_but_not_both(word1, word2):
    """Returns sorted list of letters that appear in either word, but not both."""
    set1 = set(unique_sorted_letters(word1))
    set2 = set(unique_sorted_letters(word2))
    return sorted(set1 ^ set2)  # Symmetric difference between both sets

# Test the functions
word1 = "cheese"
word2 = "seeds"

print("Letters in at least one:", letters_in_at_least_one(word1, word2))  
print("Letters in both:", letters_in_both(word1, word2)) 
print("Letters in either but not both:", letters_in_either_but_not_both(word1, word2))  