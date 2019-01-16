primes = [2]
for i in range(3, 100000000000000, 2):
    for j in range(2, int(i**0.5) + 2):
        if i % j == 0:
            break
        if j == int(i**0.5) + 1:
            primes.append(i)
    if len(primes) == 10001:
        print(primes[-1])
        break

#print(primes)