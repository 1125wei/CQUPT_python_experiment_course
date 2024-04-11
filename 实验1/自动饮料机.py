import sys

PutCoin = int(input("请投币："))
while True:
    if PutCoin == 0:  # 条件判断
        print("设备停止工作")
        sys.exit()
    elif PutCoin == 1:
        print("冰露纯净水")
        sys.exit()
    elif PutCoin == 2:
        print("农夫山泉矿泉水")
        sys.exit()
    elif PutCoin == 3:
        print("冰红茶")
        sys.exit()
    elif PutCoin == 4:
        print("脉动")
        sys.exit()
    elif PutCoin == 5:
        print("红牛")
        sys.exit()
    else:
        print("非法投币，正在退币")
    PutCoin = int(input("请投币："))
        


