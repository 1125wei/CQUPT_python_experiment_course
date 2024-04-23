# 定义列表
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88), ('Sophia', 96), ('Andy', 83)]
# 创建一个列表L，其中包含元组，每个元组包含一个名字和一个分数

sorted_L = sorted(L, key=lambda x: x[1], reverse=True)
# 使用sorted函数对列表L进行排序，排序依据是元组中的分数（x[1]），reverse=True表示降序排序

print(sorted_L)
# 打印排序后的列表sorted_L，输出将按照分数从高到低的顺序显示元组
