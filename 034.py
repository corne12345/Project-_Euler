# highest digit, 9!, is 362880
# A 7 digit number will have the maximum value of less than 3 million, so this is the max

from math import factorial

total = 0
for i in range(3, 3000000):
    sum_factorials = 0
    for char in str(i):
        sum_factorials += factorial(int(char))
    if sum_factorials == i:
        total += i

print(total)
