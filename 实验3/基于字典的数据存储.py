dictionary = {}
flag = 'a'
pape = 'a'
while flag == 'a' or 'c':
    flag = input("添加或查找单词？（a/c）")
    if flag == 'a':
        key = input("输入单词：")
        value = input("输入释义：")
        dictionary[key] = value
        pape = input("是否要查看字典内容？(y/n)")
        if pape == 'y' or 'Y':
            print(dictionary)
        else:
            continue
    elif flag == 'c':
        key = input("输入要查找单词：")
        if key in dictionary:
            print("单词存在！")
            print("单词释义为：", dictionary[key])
        else:
            print("该值不存在！")
    else:
        print("error type")
        break