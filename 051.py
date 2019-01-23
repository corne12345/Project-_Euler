"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime
with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""

"""
To find 8 primes in a set of 10 distinct numbers is only possible when 3 of the
digits change. Otherwise, at least 3 out of 10 times, the number will be
divisible by 3.

The smallest of the primes will be the one with the repeating 0, 1 or 2.
This means a suspect solution needs to have 3 0's, 1's or 2's.

All primes greater than 10 end with 1, 3, 7 or 9. That are only 4 options,
meaning that the last digit can't be one of the 3 repeating numbers.

This means we have to search for primes containing 3 times 0 or 3 times 1 or
3 times 2, excluding the last digit.
"""

def create_primes(upper_bound):
    primes = [2]
    for i in range(3, upper_bound, 2):
        for j in range(3, int(i ** 0.5) +1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

def possible_solutions(primes):
    options = []
    for i in primes:
        temp = str(i)
        zeros = 0
        ones = 0
        twos = 0
        searching = temp[:-1]
        for digit in searching:
            if digit == '0':
                zeros += 1
            elif digit == '1':
                ones += 1
            elif digit == '2':
                twos += 1
        if zeros >= 3 or ones >= 3 or twos >= 3:
            # print("succes", i, temp, zeros, ones, twos)
            options.append(i)
    return options

def get_solution(options, primes):
    for i in range(len(options)):
        result = str(options[i])
        checklist = []
        if result.count('0') >= 2:
            digit = 0
            # print("Zeros check out " + result)
        elif result.count('1') >= 2:
            digit = 1
            # print("Ones check out " + result)
        elif result.count('2') >= 2:
            digit = 2
            # print("Twos check out " + result)
        for i in range(10):
            temp = result.replace(str(digit), str(i), 3)
            if int(temp) in primes and temp[0] != '0':
                checklist.append(temp)
        if len(checklist) >= 8:
            print(result, checklist)
            # print(checklist)
            # print(counter)

primes = create_primes(1000000)
# print(primes[:-1000])
print(len(primes))
options = possible_solutions(primes)
print(len(options))
get_solution(options, primes)
