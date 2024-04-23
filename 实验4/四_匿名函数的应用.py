# 定义列表
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88),('Sophia', 96), ('Andy',83)]
sorted_L = sorted(L, key=lambda x: x[1], reverse=True)  # 使用sorted函数和lambda匿名函数进行排序
print(sorted_L)