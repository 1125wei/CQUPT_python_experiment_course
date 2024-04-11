i, n, Sum = 1, 10, 0  # 初始化 i，n，Sum
while i <= n:  # 设置循环条件 i<=n
    if i % 2 == 1:  # 如果i是奇数跳过
        i = 1 + i
        continue
    Sum = Sum + i  # i为偶数进行累加
    i = i + 1
print("sum = ", Sum)  # 输出1~10全部偶数的和
