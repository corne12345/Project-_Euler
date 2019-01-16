"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

def make_primes(upper_bound):
    """
    returns a list of prime numbers
    """
    primes = [2]
    for i in range(3, upper_bound, 2):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

def get_prime_factors(number, primes):
    """
    returns the amount of prime factors a number has
    """
    counter = 0
    for entry in primes:
        if entry >= int(number/(2 * 3 * 5)):
            break
        if number % entry == 0:
            counter += 1
        if counter == 4:
    return counter

primes = make_primes(100000)
print("primes obtained")
prime_factors_list = []
for i in range(999999):
    temp = get_prime_factors(i, primes)
    # print(i, temp, sep = '\t')
    prime_factors_list.append(temp)
    if prime_factors_list[i] == 4 and prime_factors_list[i-1] == 4 and prime_factors_list[i-2] == 4 and prime_factors_list[i-3] == 4:
        print (i-3)
        break
