file = open("names.txt", "r").read()
names = file.split(",")
names.sort()
print(names)
total = 0

for i in range(len(names)):
    name_sum = 0
    for c in names[i]:
            name_sum += ord(c) - 64
    total += (name_sum + 60) * (i+1)

print(total)