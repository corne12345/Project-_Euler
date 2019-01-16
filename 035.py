"""
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import copy

primes = [2]
for i in range(3, 1000001):
    for j in range(2, round(i**0.5)+1):
        if i % j == 0:
            break
    else:
        primes.append(i)

# print(len(primes))

circular = set()
for i in range(len(primes)):
    selected = str(primes[i])
    # print(selected, end='\t')

    for j in range(len(str(primes[i]))):
        first = selected[0]
        selected = selected[1:]
        selected += first
        # print(selected, end='\t')
        if int(selected) not in primes:
            break
    else:
        # print(selected)
        circular.add(selected)
    # print('\n')

print(len(circular))
print(list(circular))
