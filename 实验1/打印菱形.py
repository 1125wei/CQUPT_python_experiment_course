for i in range(0, 4):
    print(" " * (3 - i) + "*" * (1 + 2 * i) + " " * (3 - 1))  # 打印菱形上半部分
for i in range(1, 4):
    print(" " * int(i) + "*" * (7 - (i * 2)) + " " * int(i))  # 菱形下半部分
