result = 2520
prime = 2


while True:
    if prime == 20:
        print (result)
        break
    elif result % prime == 0:
        prime = prime + 1
    else:
        result = result + 2520
        prime = 2