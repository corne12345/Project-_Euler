lst = []
for i in range(1, 1001):
    result = i ** i
    lst.append(result)
    #print(result)

end = str(sum(lst))
print(end[len(end) - 10: len(end)])