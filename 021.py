dctn = dict()

for i in range(10000):
    sum = 0
    for j in range(1, int(i/2) + 1): # maximum dividor is half the original
        if i % j == 0:
            sum += j
    dctn[i] = sum

#print(dctn)

checksum = 0
for k, v in dctn.items():
    for l, w in dctn.items():
        if k == w and v == l and k != l:
            checksum += k

print(checksum)