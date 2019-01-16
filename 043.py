"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the
digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility
property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations

# Create a list containing all the mentioned primes
primes = []
for i in range(2, 18):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        primes.append(i)
# print(primes)

# Create a list of all the permutations of 0 to 9 pandigital numbers
options = []
for p in permutations('0123456789'):
    temp = ''.join(p)

    options.append(temp)

# print(options)
results = []
total = 0

for permutation in options:
    for i in range(len(primes)):
        temp = permutation [i+1: i+4]
        if int(temp) % primes[i] != 0:
            break
    else:
        results.append(permutation)
        total += int(permutation)

# print(results)
print(total)
