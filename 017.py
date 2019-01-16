to_10 = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
to_20 = to_10 + 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
to_100 = to_20 + 10* (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) + 8 * to_10
to_1000 = 100 * to_10 + 900 * len('hundred') + 891 * len('and') + 10 * to_100 + len('onethousand')

print(to_10)

print(to_100)

print(to_1000)