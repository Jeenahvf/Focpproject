#Write a function that accepts a positive integer as a parameter and then returns a representation of that number in binary (base 2).
def to_binary(n: int) -> str:
    if n <= 0:
        raise ValueError("Only positive integers are allowed.")
    return f"{n:b}" #the 'b' in the format string represents binary
#Test 
print(to_binary(10)) 
print(to_binary(255)) 
print(to_binary(1))
print(to_binary(22))