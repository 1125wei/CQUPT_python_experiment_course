def PrintInfo(arg1, *VarTable):  # 打印传入参数
    print("输出：")
    print(arg1)
    print("VarTable:", VarTable)
    return


PrintInfo(10)
PrintInfo(70, 60, 50)


def func(**args):
    for key, value in args.items():
        print("%s:%s" % (key, value))


func(新发明1="高铁", 新发明2="扫描支付", 新发明3="共享单车", 新发明4="网购")
