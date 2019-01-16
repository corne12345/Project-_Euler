"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?


The largest pandigital prime would theoretically consist of the numbers 0 through 9
Problem is that the sum of these numbers is 45, which means every number would be
divisible by 3. All 8-digit pandigital nuumbers are 36 summed, so this means the highest
possible pandigital prime would have 7 digits
Actually, the only possibility are 4 and 7 digits, but the guess is one 7-digit number
will exist; so the range is 1234567 to 7654321.
"""

max = 0
for i in range(1234567, 7654321, 2):
    number = str(i)
    test = set()
    for k in range(len(number)):
        test.add(number[k])
    if len(test) == 7 and '9' not in test and '8' not in test and '0' not in test:
        # print(i)
        for j in range(2, int(i**0.5)):
            if i % j == 0:
                break
        else:
            max = i
            print (max)

        # for j in range(2, int(i**0.5)):
        #     if i % j == 0:
        #         break


"""
Second option
"""

from itertools import permutations

options = []
for p in permutations('1234567'):
    options.append(''.join(p))

# print(options)
# print(len(options))

max = 0
for i in options:
    i = int(i)
    for j in range(2, int(i**0.5)):
        if i % j == 0:
            break
    else:
        max = i

print(max)
