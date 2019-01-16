# A palindromic number reads the same both ways. The largest palindrome made from the
# product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Multiplying two 3-digit numbers will result in an 5 or 6 digit number. The largest
# palindrome will probably contain 6 digits.

largest = 0
for i in range(999, 100, -1):
    for j in range (999, 100, -1):
        result = str(i * j)
        left = result[0:3]
        # print(left, end='\t')
        right = result[-1] + result [-2] + result[-3]
        # print(right)
        if left == right:
            if int(result) > int(largest):
                largest = result
                print (largest)