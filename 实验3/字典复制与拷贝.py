"""
复制与拷贝的区别
复制相当于引用，浅拷贝是对一级目录拷贝，二级目录引用
"""
Alex = [12, 'sing']  # 列表
Thea = {20, 'dance'}  # 字典
dict1 = {'Alex': Alex, 'Thea': Thea}  # 定义字典，value值嵌套上面的字典和列表
dict_cp1 = dict1  # 相当于引用，dict_cp1的地址和dict1的地址相同
dict_cp2 = dict1.copy()  # 一级目录拷贝，二级目录引用
print("原始字典dict1：", dict1)
dict1["Alex"] = Thea
print("修改后的字典dict1", dict1)
print("字典dict1的复制（与原字典一致）：", dict_cp1)
print("浅拷贝字典dict1（不会随着原字典一级目录改变而改变）",dict_cp2)

