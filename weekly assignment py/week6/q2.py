#Write and test a function that takes an integer as its parameter and returns the factors of that integer. (A factor is an integer which can be multiplied by another to yield the original).

def factors(n: int):
    if n <=0:
        raise ValueError("Only positive integers are allowed.")
    factors_lists =[i for i in range(1, n + 1) if n % 1 == 0]
    return factors_lists
#Test cases
print(factors(28))
print(factors(22))
print(factors(8))
print(factors(21))
