def PrintInfo(name: str, age=35):
    # 定义一个名为PrintInfo的函数，接收两个参数：name和age
    # name参数是一个字符串类型，用于表示姓名
    # age参数是一个整数类型，默认值为35，用于表示年龄

    print("Name:", name)  # 打印姓名信息
    print("Age:", age)  # 打印年龄信息
    return  # 函数返回，由于没有指定返回值，默认返回None


PrintInfo(age=50, name="miki")  # 调用PrintInfo函数，指定age为50，name为"miki"
PrintInfo(name="miki")  # 调用PrintInfo函数，只指定name为"miki"，age使用默认值35
