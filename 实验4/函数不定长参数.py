def PrintInfo(arg1, *VarTable):  # 打印传入参数
    print("输出：")
    print(arg1)
    print("VarTable:", VarTable)  # 将打印剩余所有
    return


PrintInfo(10)
PrintInfo(70, 60, 50)


def func(**args):  # 输入所以元组
    for key, value in args.items():
        print("%s:%s" % (key, value))


# *：传递元组 **：传递字典

func(新发明1="高铁", 新发明2="扫描支付", 新发明3="共享单车", 新发明4="网购")
