row_01 = [75]
row_02 = [95, 64]
row_03 = [17, 47, 82]
row_04 = [18, 35, 87, 10]
row_05 = [20, 4, 82, 47, 65]
row_06 = [19, 1, 23, 75, 3, 34]
row_07 = [88, 2, 77, 73, 7, 63, 67]
row_08 = [99, 65, 4, 28, 6, 16, 70, 92]
row_09 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
row_10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
row_11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
row_12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 69, 17, 57]
row_13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
row_14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
row_15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

rows = {1 : row_01, 2: row_02, 3: row_03, 4: row_04, 5: row_05, 6: row_06, 7: row_07, 8: row_08, 9: row_09, 10: row_10, 11: row_11, 12: row_12, 13: row_13, 14: row_14, 15: row_15}
# print(len(rows))

for i in range(2, len(rows) + 1):
    current_row = rows[i]
    previous_row = rows[i -1]
    for j in range(len(rows[i])):
        if j == 0:
            current_row[j] += previous_row[0]
        elif j == len(current_row) - 1:
            current_row[j] += previous_row[-1]
        else:
            current_row[j] += max(previous_row[j], previous_row[j -1])

lst_15 = rows[15]
print(max(lst_15))