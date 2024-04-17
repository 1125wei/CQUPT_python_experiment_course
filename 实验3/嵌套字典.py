"""
嵌套字典
"""
data = {
    '北京': {
        '昌平': {
            '沙河': ['oldboy', 'test'],
            '天通苑': ['链家地产']
        },
        '朝阳': {
            '望京': ['奔驰', '陌陌'],
            '国贸': ['CICC'],
            '东直门': ['Advent', '飞信']
        },
        '海淀': {

        },
    },
    '山东': {
        "德州": {},
        "青岛": {},
        "济南": {},
    }
}
"""
嵌套字典的基础输出
"""
print(data.keys())
print(data.values())
print(data['北京'].keys())
print(data['北京'].values())
print(data['北京']['昌平'].keys())
print(data['北京']['昌平'].values())
print(data['北京']['昌平']['沙河'])
"""
层次访问
"""
exit_flag = False
while not exit_flag:
    # 打印第一层
    for i in data:
        print(i)
    choice = input("选择进入1>>")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t", i2)
            choice2 = input("选择进入2>>")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print('\t\t', i3)
                    choice3 = input("选择进入3>>")
                    if choice3 in data[choice][choice2][choice3]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t\t", i4)
                        choice4 = input("最后一层，按b返回")
                        if choice4 == 'b':
                            pass
                        elif choice4 == 'q':
                            exit_flag = True
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_flag = True
    if choice == 'q':
        exit_flag = True
