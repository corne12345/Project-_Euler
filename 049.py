"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit
numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting
this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

# First create a list of all 4-digit primes
# Make combinations of 3 primes being permutations of each other
# Check if their difference is the same

def make_4_digit_primes():
    """
    Function that returns a list of all 4 digit primes
    """
    primes = []
    for i in range(1001, 10000, 2):
        for j in range (3, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

def cluster_permutations(primes):
    """
    cluster all primes in lists of its permutations
    """
    permutations = {}
    for element in primes:
        element = str(element)
        element_list = [element[0], element[1], element[2], element[3]]
        element_list.sort()
        element_list = str(element_list)
        # print(element_list)
        if element_list not in permutations:
            permutations[element_list] = [element]
        else:
            permutations[element_list].append(element)
    return permutations

def find_solution (permutations):
    for key, value in permutations.items():
        if len(value) >= 3:
            # print(len(value), value, sep = '\t')
            for i in range(len(value)):
                first = value[i]
                for j in range(len(value)):
                    second = value[j]
                    temp = int(value[j]) - int(value[i])
                    temp_2 = temp + int(value[j])
                    # print(temp)
                    if str(temp_2) in value and temp != 0:
                        print(value[i] + value[j] + str(temp_2))


test = make_4_digit_primes()
# print(len(test))
permutations = cluster_permutations(test)
# print(permutations)
find_solution(permutations)
