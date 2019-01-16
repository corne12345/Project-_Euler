known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci (n-2)
    known[n] = res
    return res

for i in range(10000):
    if len(str(fibonacci(i))) >= 1000:
        print(fibonacci(i))
        print(i)
        break