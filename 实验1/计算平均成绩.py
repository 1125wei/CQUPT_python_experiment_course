total, count = 0, 0  # 预设总成绩，计数器
score = int(input("请输入学生英语成绩:"))
while score != "-1":  # 输入成绩为-1时退出循环
    total = int(total) + int(score)  # 每次循环total加上score
    count += 1  # 学生人数计数
    score = input("请输入学生英语成绩:")
print("录入学生成绩%d份，学生英语总成绩%d，学生英语平均成绩%4.2f." % (count, total, total / count))
