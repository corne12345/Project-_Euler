"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by
cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in
value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value
of the denominator.
"""
better = dict()
for i in range (10, 100):
    for j in range (10, 100):
        str_i = str(i)
        str_j = str(j)


        if i/j < 1 and str_i[0] == str_j[0]:
            if int(str_j[1]) != 0:
                # print (i, j, int(str_i[1]) / int(str_j[1]), sep = '\t')
                if i / j == int(str_i[1]) / int(str_j[1]):
                    better[i] = j
        elif i/j < 1 and str_i[0] == str_j[1]:
            if int(str_j[0]) != 0:
                # print (i, j, int(str_i[1]) / int(str_j[0]), sep = '\t')
                if i / j == int(str_i[1]) / int(str_j[0]):
                    better[i] = j
        elif i/j < 1 and str_i[1] == str_j[0]:
            if int(str_j[1]) != 0:
                # print (i, j, i/j, int(str_i[0]) / int(str_j[1]), sep = '\t')
                if i / j == int(str_i[0]) / int(str_j[1]):
                    better[i] = j
        elif i/j < 1 and str_i[1] == str_j[1]:
            if int(str_j[1]) != 0:
                # print (i, j, int(str_i[0]) / int(str_j[0]), sep = '\t')
                if i / j == int(str_i[0]) / int(str_j[0]):
                    better[i] = j

num = 1
den = 1
for k, v in better.items():
    num *= k
    den *= v

print (num/den)
print(better)
