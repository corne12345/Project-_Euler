lst = [0]
for i in range(0, 100000):
    counter = 0
    number = lst[i] + i + 1

    for j in range(1, int(number**0.5 + 1)):
        if number % j == 0:
            counter = counter + 1
    if counter > 250:
        print (number)
        break

    lst.append(number)

#print(lst)