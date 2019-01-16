
def is_prime (result):
    best = 0
    for i in range(2, round(result * 0.5)):
        if result % i == 0:
            return False
            break
    else:
        return True

def max_n (a, b):
    for n in range(100):
        if is_prime( n ** 2 + a * n + b) == False:
            return n-1
            break


max_a, max_b, maximum = 0, 0, 0
for a in range(-999, 999):
    print(a)
    for b in range(-1000, 1000):
        temp = max_n (a,b)
        if temp > maximum:
            maximum = temp
            max_a = a
            max_b = b

print(maximum, max_a, max_b)
