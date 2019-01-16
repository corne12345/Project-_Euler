def longest_reciprocal(maximum):
    maximum_length = 0
    maxi = 0
    for i in range(1, maximum):
        divider = 1
        lst = []
        result =''
        while len(result) < i and divider != 0:
            while divider < i:
                divider *= 10
            if divider in lst:
                break
            lst.append(divider)
            result += str(divider//i)
            divider = divider % i
        # print(result)
        if len(result) > maximum_length:
            maximum_length = len(result)
            maxi = i
    print(maxi)

longest_reciprocal(1000)