sum = 5
for i in range (3, 2000000, 2):
    for j in range(3, int(i **0.5) + 4, 2):
        if i % j == 0:
            break
        elif j >= int(i**0.5):
            sum = sum + i
            #print(i, end = ' ')
            #print(sum)
            break

print(sum)