pascal = {}
pascal[0] = [1]
pascal[1] = [1,1]

for i in range(2, 41):
    pascal[i] = [1]
    before = pascal[i-1]
    for j in range(1, len(pascal[i-1])):
        pascal[i].append(before[j] + before[j-1])
    pascal[i].append(1)


print(max(pascal[40]))

