import math

for a in range (3, 600):
    for b in range (3, 600):
        if math.sqrt(b**2 + a**2) - int(math.sqrt(b**2 + a**2)) == 0 and a + b + math.sqrt(b**2 + a **2) == 1000:
            print (a * b * math.sqrt(b**2 + a**2))
            break