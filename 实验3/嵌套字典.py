# 这是一个嵌套字典的示例，包含多个城市以及对应地区的列表
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
            # 海淀区域当前为空
        },
    },
    '山东': {
        "德州": {},
        "青岛": {},
        "济南": {},
    }
}

# 以下是嵌套字典的基础输出操作
"""  
嵌套字典的基础输出  
"""
# 打印外层字典的键
print(data.keys())
# 打印外层字典的值（即内层字典）
print(data.values())
# 打印北京地区下所有区域的键
print(data['北京'].keys())
# 打印北京地区下所有区域的值（即街道下的列表）
print(data['北京'].values())
# 打印昌平地区下所有街道的键
print(data['北京']['昌平'].keys())
# 打印昌平地区下所有街道的值（即列表）
print(data['北京']['昌平'].values())
# 打印昌平地区沙河街道下的列表
print(data['北京']['昌平']['沙河'])

# 以下是层次访问的操作，用户可以通过输入选择进入不同层次的字典
"""  
层次访问  
"""
exit_flag = False
while not exit_flag:
    # 打印第一层城市名称
    for i in data:
        print(i)
        # 用户选择进入哪个城市
    choice = input("选择进入的城市（输入q退出）>>")
    # 如果用户选择的是字典中的城市
    if choice in data:
        while not exit_flag:
            # 打印当前城市下的所有区域名称
            for i2 in data[choice]:
                print("\t", i2)
                # 用户选择进入哪个区域
            choice2 = input("选择进入的区域（输入b返回上一层，输入q退出）>>")
            # 如果用户选择的是当前城市下的区域
            if choice2 in data[choice]:
                while not exit_flag:
                    # 打印当前区域下的所有街道名称
                    for i3 in data[choice][choice2]:
                        print('\t\t', i3)
                        # 用户选择进入哪个街道（但是当前字典结构并没有街道下的子项）
                    choice3 = input("选择进入的街道（当前字典结构没有街道下的子项，输入b返回上一层，输入q退出）>>")
                    # 如果用户尝试进入不存在的子项（这里应该是个错误，因为街道下没有子项）
                    if choice3 in data[choice][choice2][choice3]:
                        # 假设街道下有子项，打印它们（但实际情况中不应该有这一行）
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t\t", i4)
                            # 用户操作提示
                        choice4 = input("已经是最后一层，按b返回上一层，输入q退出>>")
                        # 如果用户选择返回上一层
                        if choice4 == 'b':
                            # 退出当前循环，返回上一层循环
                            break
                            # 如果用户选择退出程序
                        elif choice4 == 'q':
                            exit_flag = True
                            # 如果没有进入街道下的子项（即用户输入了b或q）
                    # 则退出当前循环，返回上一层循环
            # 如果用户选择返回上一层（即输入了b）
            if choice2 == 'b':
                # 退出当前循环，返回上一层循环
                break
                # 如果用户选择退出程序（即输入了q）
            elif choice2 == 'q':
                exit_flag = True
                # 如果用户选择退出程序（即输入了q）
    if choice == 'q':
        exit_flag = True

    # 注意：上面的代码中，当用户尝试进入街道下的子项时，存在逻辑错误，因为当前字典结构中街道下并没有子项。
# 如果需要实现街道下的子项访问，需要在字典中添加相应的子项结构。