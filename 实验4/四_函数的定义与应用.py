def welcome():
    print("""|——————欢迎进入通讯录程序——————|  
    |——————1、 查询联系人资料——————|  
    |——————2、 插入新的联系人——————|  
    |——————3、 删除已有联系人——————|
    |——————4、 更新已有联系人——————|  
    |——————5、 退出通讯录程序——————|  
    """)
    return


def add_card():
    name = input("输入联系人姓名：")
    Book[name] = input("输入联系方式：")
    print("添加完成!")


def delete_card():
    name = input("请输入需要删除的联系人姓名：")
    del Book[name]
    print("删除完成!")


def find_card():
    name = input("输入你需要查找的姓名：")
    if name in Book:
        print("找到联系人!")
        print(Book[name])
    else:
        print("未找到!")


def update_card():
    name = input("请输入需要更新的联系人姓名：")
    Book[name] = input("输入新的联系方式：")


if __name__ == '__main__':
    Book = {}
    while True:
        welcome()
        choice = input("选择你需要的功能：")
        if choice == "1":
            find_card()
        if choice == "2":
            add_card()
        if choice == "3":
            delete_card()
        if choice == "4":
            update_card()
        if choice == "5":
            exit()
