# Surprisingly there are only three numbers that can be written as the sum of fourth
# powers of their digits:
# Find the sum of all the numbers that can be written as the sum of fifth powers of
# their digits

# 9^5 = 59049. So the longest number to look at would be a 6 digit numbers, since
# the largest 7 digit numbers are at least 1 million, which needs 15 fifth powers
# 300.000 is even above the max

total = 0
for i in range(2, 360000):
    sum = 0
    for char in str(i):
        sum += int(char) ** 5
    if sum == i:
        total += sum

print(total)
