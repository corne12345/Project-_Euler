import itertools
lst =[]

a = '0123456789'
k = 10
for p in itertools.permutations(a, k):
    result = "". join(p)
    lst.append(result)

print(lst[999999])
