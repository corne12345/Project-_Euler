
def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)

checksum = 0
sm = str(factorial(100))
for c in sm:
    checksum += int(c)

print(checksum)