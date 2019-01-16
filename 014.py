maxi = 0
for n in range(1, 1000000, 2):
    number = n
    length = 1
    #n = 13
    #print(n, end = "\t")
    while True:
        if n % 2 == 0:
            n = n /2
            length = length + 1
            #print(n)
        elif n == 1:
            if length > maxi:
                maxi = length
                print(number, end = '\t')
                print(maxi)
            #print(length)
            break
        else:
            n = n * 3 + 1
            #print(n)
            length = length + 1