"""
An irrational decimal fraction can be created by concatenating the  positive integers:
                0.1234567890101112131415....
It can be seen that the 12th digit of the fractional part is 1
If dn represents the nth digit of the fractional part, find the value of the following:
d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""

string = ''
for i in range (1, 200000):
    string += str(i)

print(int(string[0]) * int(string[9]) * int(string[99]) * int(string[999]) * int(string[9999]) * int(string[99999]) * int(string[999999]) )
