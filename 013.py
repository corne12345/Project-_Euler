
file = open("problem_13.txt", "r")
numbers = file.readlines()
file.close()

total = 0
for i in range(len(numbers)):
    numbers[i] = int(numbers[i].rstrip())
    total += numbers[i]
#print(numbers)
print(str(total)[:10])