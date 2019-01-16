"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call
192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?

Options:
1   1   1   1   1   1   1   1   1
1   1   1   1   1   1   1   2
1   1   1   1   1   2   2
1   1   1   2   2   2
1   2   2   2   2
2   2   2   3
3   3   3
4   5
"""

options = []
for i in range(10000):
    string = ''
    finished = False
    multiplicator = 1
    while finished == False:
        string += str(multiplicator * i)
        multiplicator += 1
        if len(string) >= 9:
            finished = True
    if len(string) == 9:
        check = set()
        for k in string:
            check.add(k)
        if len(check) == 9 and '0' not in check:
            options.append(string)
    # print(string)

options.sort()
print(options)
