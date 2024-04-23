def Swap(x: int, y: int):  # 定义两个形参
    print("交换前：x = %d, y = %d" % (x, y))
    x, y = y, x  # 交换形参的值
    print("交换后：x = %d, y = %d" % (x, y))


a = 5  # 定义两个参数
b = 6
print("调用前：a = %d, b = %d" % (a, b))
Swap(a, b)  # 调用函数
print("调用后a = %d, b = %d" % (a, b))


def chang(mylist: list) -> list:
    mylist.append([1, 2, 3, 4])  # 添加值
    print("函数内取值:", mylist)
    return mylist


mylist = [10, 20, 30]
print("原始取值：", mylist)
chang(mylist)
print("函数外取值：", mylist)

