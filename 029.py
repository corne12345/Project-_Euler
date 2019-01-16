
total = set()
for a in range (2, 101):
    for b in range(2, 101):
        summed = a ** b
        total.add(summed)

print(len(total))