"""
猜数字小游戏
"""
import random  # 导入random

print("开始游戏")
random_num = int(random.randint(0, 100))  # 在0-100随机生成一个数字，保证其为int类型
for i in range(1, 6):  # 循环5次对应5次机会
    print("输入数字：")
    gases_no = int(input())  # 变量b接收输入
    if gases_no > random_num:
        print("猜大了")
        print("还剩" + str(5 - i) + "机会")  # 比较大小，输出剩余机会
        continue  # 继续循环
    elif gases_no < random_num:  # 同上逻辑
        print("猜小了")
        print("还剩" + str(5 - i) + "次机会")
        continue
    else:
        print("猜对了")
        print("你使用了" + str(i) + "次机会")
        exit()  # 猜对的情况，直接退出程序
print("游戏结束，你失败了")
