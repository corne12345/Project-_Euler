"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

counter = []
for a in range(1, 500):
    for b in range(1, 500):
        c = (b**2 + a**2) ** 0.5
        if c % 1 == 0 and a+b+c <= 1000:
            # print(a, b, c, a+b+c,  sep = '\t')
            total = a+b+c
            counter.append(total)

# print(counter)

final = dict()
for i in range(len(counter)):
    selected = counter[i]
    if counter[i] not in final:
        final[selected] = 1
    else:
        final[selected] += 1

print([max(final, key=final.get)])


print(final)
