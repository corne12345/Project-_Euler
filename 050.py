"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains
21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

def make_primes(upper_bound):
    primes = [2]
    for i in range(3, upper_bound, 2):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

record = 0
primes = make_primes(1000000)
for i in range(len(primes)):
    sum = 0
    for j in range(i, len(primes)):
        sum += primes[j]
        terms = j - i + 1
        if sum in primes and terms > record:
            print(sum, terms, primes[i], sep = '\t')
            record = terms
