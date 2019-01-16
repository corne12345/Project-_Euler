palindromes = []
for i in range (1000000):
    selected = str(i)
    if len(selected) == 1:
        palindromes.append(int(selected))
    elif len(selected) == 2 or len(selected) == 3:
        if selected[0] == selected[-1]:
            palindromes.append(int(selected))
    elif len(selected) == 4 or len(selected) == 5:
        if selected[0] == selected[-1] and selected[1] == selected[-2]:
            palindromes.append(int(selected))
    elif len(selected) == 6:
        if selected[0] == selected[5] and selected[1] == selected[4] and selected[2] == selected[3]:
            palindromes.append(int(selected))

print(palindromes)
print(len(palindromes))

final = 0
for i in range(len(palindromes)):
    selected = str(bin(palindromes[i]))
    selected = selected[2:]
    # print(selected)
    # print(len(selected))
    if len(selected) == 1:
        final += int(selected)
        print("Final is", final)
    else:
        while len(selected) > 1:
            # print(selected)
            if selected[0] == selected[-1]:
                selected = selected[1:-1]
                # print(selected)
            else:
                break
        else:
            final += palindromes[i]
            print("Final is", final)

print(final)
