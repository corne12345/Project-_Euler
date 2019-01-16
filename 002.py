fibonacci = [1, 2]
sum = fibonacci[1]
for i in range(10000):
    new = fibonacci[i] + fibonacci[i+1]
    if new > 4000000:
        break
    if new % 2 == 0:
        sum = sum + new
    fibonacci.append(new)

print(sum)
print(fibonacci)