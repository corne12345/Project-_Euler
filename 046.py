"""
It was proposed by Christian Goldbach that every odd composite number can be written as the
sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a
square?
"""

def make_primes(upper_bound):
    """
    returns a list of primes up to the upper bound
    """
    primes = [2]
    non_primes = []
    for i in range(3, upper_bound, 2):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                non_primes.append(i)
                break
        else:
            primes.append(i)
    return primes, non_primes

def make_2_squares (upper_bound):
    """
    returns a list of double squares up to the upper bound
    """
    squares = []
    for i in range(1, upper_bound):
        total = 2 * i**2
        squares.append(total)
    return squares

primes, non_primes = make_primes(10000)
# print(non_primes)
squares = make_2_squares(50)
# print(squares)

for i in non_primes:
    results = True
    for j in range(min(i, len(primes))):
        for k in range(len(squares)):
            if primes[j] + squares[k] == i:
                results = False
                break
    if results == True:
        print(i)
        break
