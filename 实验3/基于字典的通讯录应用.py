# 打印欢迎进入通讯录程序的提示信息
print("""|——————欢迎进入通讯录程序——————|  
|——————1、 查询联系人资料——————|  
|——————2、 插入新的联系人——————|  
|——————3、 删除已有联系人——————|  
|——————4、 退出通讯录程序——————|  
""")

# 初始化一个空字典用于存储通讯录信息
addressBook = {}

# 进入一个无限循环，等待用户输入指令
while True:
    # 获取用户输入的指令代码
    temp = input("请输入指令代码：")

    # 如果输入的指令不是数字，则提示用户输入错误并重新输入
    if not temp.isdigit():
        print("输入指令错误，请重新输入！")
        continue

        # 将输入的指令代码转换为整数
    temp = int(temp)

    # 如果输入的指令是4，则打印感谢使用信息并退出程序
    if temp == 4:
        print("|——————感谢使用通讯录程序——————|")
        break

        # 如果输入的指令是1，则进入查询联系人资料的功能
    if temp == 1:
        # 获取用户想要查询的联系人姓名
        name = input("请输入姓名：")
        # 如果通讯录中存在该联系人
        if name in addressBook:
            # 打印该联系人的信息
            print(name + ": " + str(addressBook[name]))
            continue
        else:
            # 如果通讯录中不存在该联系人，则提示用户该联系人不存在
            print("该联系人不存在！")

            # 如果输入的指令是2，则进入插入新的联系人的功能
    if temp == 2:
        # 获取用户想要添加的联系人姓名
        name = input("请输入联系人姓名：")
        # 如果通讯录中已经存在该联系人
        if name in addressBook:
            # 打印提示信息并询问用户是否要修改该联系人的资料
            print(name + ": " + str(addressBook[name]) + "该联系人已经存在！")
            isEdit = input("是否修改联系人资料(Y/N)：")
            # 如果用户选择修改，则获取新的电话号码并更新通讯录
            if isEdit == "Y":
                userPhone = input("请输入联系人电话：")
                addressBook[name] = userPhone
                print("联系人修改成功！")
            else:
                # 如果用户选择不修改，则跳过此次循环，继续等待下一个指令
                continue
        else:
            # 如果通讯录中不存在该联系人，则获取用户输入的电话号码并添加到通讯录中
            userPhone = input("请输入电话号码：")
            addressBook[name] = userPhone
            print("联系人添加成功！")
            continue

            # 如果输入的指令是3，则进入删除已有联系人的功能
    if temp == 3:
        # 获取用户想要删除的联系人姓名
        name = input("输入联系人姓名：")
        # 如果通讯录中存在该联系人
        if name in addressBook:
            # 从通讯录中删除该联系人
            del addressBook[name]
            print("删除成功！")
        else:
            # 如果通讯录中不存在该联系人，则提示用户联系人不存在
            print("联系人不存在！")

        # 程序结束，退出循环

