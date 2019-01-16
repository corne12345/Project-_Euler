"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containiing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all product whose multiplicand/multiplier/product identity can be written
as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it
once in your sum.
"""

# This can only be in the form .. * ... = .... or . * .... = ....

results = []
for a in range(12, 99):
    for b in range (123, 988):
        c = a * b
        if c <= 10000:
            # print (a, b, c)
            strA = str(a)
            strB = str(b)
            strC = str(c)
            check = [strA[0], strA[1], strB[0], strB[1], strB[2], strC[0], strC[1], strC[2], strC[3]]
            check = set(check)
            check.discard('0')
            if len(check) == 9:
                print(a, b, c)
                results.append(c)

for a in range(1, 10):
    for b in range (1234, 9877):
        c = a * b
        if c <= 10000:
            # print (a, b, c)
            strA = str(a)
            strB = str(b)
            strC = str(c)
            check = [strA[0], strB[0], strB[1], strB[2], strB[3], strC[0], strC[1], strC[2], strC[3]]
            check = set(check)
            check.discard('0')
            if len(check) == 9:
                print(a, b, c)
                results.append(c)

results = set(results)
final = 0
for i in results:
    final += i
print(results)
print(final)
