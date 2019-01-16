CONSTANT = 600851475143
for i in range(2, round(CONSTANT**0.5)):
    if CONSTANT % i == 0:
        CONSTANT = CONSTANT/i
        print(i)
        i = 0
