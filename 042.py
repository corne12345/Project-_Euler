"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten
triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value. For example, the word value for SKY is 19
+ 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a
triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing
nearly two-thousand common English words, how many are triangle words?
"""

result = 0
triangle_numbers = []
sum = 0
for i in range(1, 50):
    sum += i
    triangle_numbers.append (sum)
print(triangle_numbers)

words_list = []
filename = "p042_words.txt"
f = open(filename, "r")
for line in f:
    words_list = line.split('","')

# print(len(words_list))
print(words_list[0])

for word in words_list:
    sum_numbers = 0
    for letter in word:
        sum_numbers += ord(letter) - 64
    # print(word, sum_numbe rs, sep='\t')
    if sum_numbers in triangle_numbers:
        result += 1

print(result)
