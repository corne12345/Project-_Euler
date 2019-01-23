"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same
digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x and 6x, contain the
same digits.
"""

"""
Since it mentioned that only the multiples have to be permutations of each other, it is
sure that the double of x has to have the same amount of digits as 6x. This means x has
to begin with at least a 5.
- Create list of numbers starting with at least a 5
- For each number:
    - Create its double
    - Make permutations of this double
    - Check if 3x, 4x, 5x and 6x are in the list of permutations
"""

from itertools import permutations

def possible_solutions(upper_bound):
    """
    Gives a list of digits starting with a 5 or higher
    """
    result = []
    for number in range(0, upper_bound):
        temp = str(number)
        if temp[0] == '1':
            result.append(number)
    return result

def check_validity(number):
    lst = []
    double = 2 * number
    permuts = permutations(str(double))
    for item in permuts:
        item = int(''.join(item))
        lst.append(item)
    if number * 3 in lst:
        if number * 4 in lst:
            if number * 5 in lst:
                if number * 6 in lst:
                    print(number)
                    return True

solutions = possible_solutions(1000000)
print(solutions)

for i in solutions:
    result = check_validity(i)
    if result == True:
        break
