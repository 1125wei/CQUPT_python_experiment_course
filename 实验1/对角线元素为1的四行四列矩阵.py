for i in range(1, 5):  # 行数
    for j in range(1, 5):  # 列数
        if i == j or i + j == 5:  # 判断对角线
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
