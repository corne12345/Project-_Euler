
import math

counter = 0
for i in range(0, 10001):
    string = ''
    for j in range(0, i+ 1):
        temp = int(math.factorial(i) / (math.factorial(j) * math.factorial(i - j)))
        string += str(temp) + ' '
        if temp % 7 == 0:
            counter += 1
            # print(counter, temp, sep = '\t')
    # print(string)
print(counter)
