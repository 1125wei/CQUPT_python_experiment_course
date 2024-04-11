for i in range(1, 10):  # 9行
    for j in range(1, i + 1):  # 每行列数取决于行号
        print(str(i) + "*" + str(j) + "=" + str(i * j), end=" ")  # 打印算式以空格结尾
    print()  # 换行
