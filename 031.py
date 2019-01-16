
counter = 0
cash = 200
options = [200, 100, 50, 20, 10, 5, 2, 1]

"""
a * 200 + b * 100 + c * 50 + d * 20 + e * 10 + f * 5 + g * 2 + h * 1 = 200
"""

for a in range (2):
    for b in range (3):
        for c in range (5):
            for d in range (11):
                for e in range (21):
                    for f in range (41):
                        for g in range (101):
                            cash = 200 - (a * 200 + b * 100 + c * 50 + d * 20 + e * 10 + f * 5 + g * 2)
                            if cash >= 0:
                                counter += 1

print (counter)
