#第三题 杨辉三角
def Pascal_triangle(k):
    row = [1]
    #循环公式
    for i in range(k):
        new_row = [1]
        for j in range(len(row) - 1):
            new_row.append(row[j] + row[j + 1])
        new_row.append(1)
        row = new_row

    print(row)

Pascal_triangle(100)
Pascal_triangle(200)