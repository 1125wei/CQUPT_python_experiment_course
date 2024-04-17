"""
访问字典的值
"""
dicts = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']:", dicts['Name'])
print("dict['Age']:", dicts['Age'])
dicts['Age'] = 8  # 修改键值对
dicts['School'] = "DPS School"
del dicts['Name']  # 删除Name条目
dicts.clear()  # 清空字典
del dicts  # 删除字典

