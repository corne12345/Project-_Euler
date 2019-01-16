import math
lst = []

# Creating all abundant numbers below 28112(since 12 is the lowest abundant)
for i in range(1, 28113):
    div_sum = 1
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            div_sum += j
            if j != i/j:
                div_sum += int(i/j)
    if div_sum > i:
        lst.append(i)

#print(lst)

#Create a list containing all positive integers up to and including 28123
numbers = set(range(28124))

# Create all sums of combinations of abundant numbers smaller than 281244
sum_set = set()
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if lst[i] + lst[j] >= 28124:
            break
        else:
            sum_set.add(lst[i] + lst[j])
#print(sorted(sum_set))
print(sum(sum_set ^ numbers))
