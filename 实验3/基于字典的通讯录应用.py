print("""|——————欢迎进入通讯录程序——————|
|——————1、 查询联系人资料——————|
|——————2、 插入新的联系人——————|
|——————3、 删除已有联系人——————|
|——————4、 退出通讯录程序——————|
""")
addressBook = {}
while True:
    temp = input("请输入指令代码：")
    if not temp.isdigit():
        print("输入指令错误，请重新输入！")
        continue
    temp = int(temp)
    if temp == 4:
        print("|——————感谢使用通讯录程序——————|")
        break
    if temp == 1:
        name = input("请输入姓名：")
        if name in addressBook:
            print(name+": "+str(addressBook[name]))
            continue
        else:
            print("该联系人不存在！")
    if temp == 2:
        name = input("请输入联系人姓名：")
        if name in addressBook:
            print(name+": "+str(addressBook[name])+"该联系人已经存在！")
            isEdit = input("是否修改联系人资料(Y/N)：")
            if isEdit == "Y":
                userPhone = input("请输入联系人电话：")
                addressBook[name] = userPhone
                print("联系人修改成功！")
            else:
                continue
        else:
            userPhone = input("请输入电话号码：")
            addressBook[name] = userPhone
            print("联系人添加成功！")
            continue
    if temp == 3:
        name = input("输入联系人姓名：")
        if name in addressBook:
            del addressBook[name]
            print("删除成功！")
        else:
            print("联系人不存在！")

