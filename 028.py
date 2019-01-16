maximum = 1001 * 1001
counter = 1
enlarger = 2
total = 1
while True:
    for i in range(4):
        counter += enlarger
        if counter <= maximum:
            total += counter
        else:
            print(total)
            quit()
    enlarger +=2

print(total)