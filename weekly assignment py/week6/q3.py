#Write and test a function that determines if a given integer is a prime number. A prime number is an integer greater than 1 that cannot be produced by multiplying two other integers.
import math

def is_prime(n: int) -> bool:
    # Edge case: numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    #Check divisibility from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:  # If divisible, it's not a prime number
            return False
    return True

# Test cases
print(is_prime(11))  
print(is_prime(22))
print(is_prime(12)) 
print(is_prime(1))   
print(is_prime(23)) 