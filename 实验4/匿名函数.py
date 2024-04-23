def calc(x, y):
    return x + y

# 这段代码定义了一个名为calc的函数，它接收两个参数x和y，并返回它们的和。
# 然而，这个函数定义后立即被下面的lambda表达式覆盖了。

calc = lambda x, y: x ** y
# 这里使用lambda表达式重新定义了calc，使其成为一个匿名函数，接收两个参数x和y，并返回x的y次幂。
print(calc(2, 5))
# 调用calc函数，并传入参数2和5，打印出结果32，因为2的5次幂等于32。

def calc(x, y):
    if x > y:
        return x * y
    else:
        return x / y

# 这段代码再次定义了一个名为calc的函数，它根据x和y的大小关系返回它们的乘积或商。
# 但是，这个函数同样被下面的lambda表达式覆盖了。

calc = lambda x, y: x * y if x > y else x / y
# 这里使用lambda表达式重新定义了calc，使其成为一个匿名函数，接收两个参数x和y，
# 如果x大于y，则返回x和y的乘积，否则返回x和y的商。
print(calc(2, 5))
# 调用calc函数，并传入参数2和5，打印出结果10，因为2不大于5，所以返回2除以5的结果2.0。
