"""
The number 3797 has an interesting property. Being prime itself, it is possible to
continuously remove digits from left to right, and remain prime at each stage: 3797, 797,
97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and
right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

numbers = []
numbers_check=[]
for i in range(2, 1000000):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        numbers.append(i)
        if i < 100000:
            numbers_check.append(i)

# print(numbers)

total = 0
final = []
for i in range(len(numbers)):
    # print(numbers[i], end= '\t')
    left_to_right = True
    right_to_left = True

    selected = str(numbers[i])
    # print(selected, end='\t')
    while len(selected) > 1:
        selected = selected [1:]
        # print(selected)
        if int(selected) not in numbers_check:
            left_to_right = False
            break

    if left_to_right == True:
        selected = str(numbers[i])
        while len(selected) > 1:
            selected = selected[:-1]
            if int(selected) not in numbers_check:
                right_to_left = False
                break

    # print(left_to_right, right_to_left, sep='\t')
    if right_to_left and left_to_right == True and numbers[i] > 10:
        final.append(numbers[i])
        total += numbers[i]
        print(numbers[i])

print(final)
print(total)
