LSZ_dict = {"姓名": "李时珍", "出生日期": "1518", "籍贯": "湖北", "职业": "医生"}  # 定义一个字典
print("字典中所有的键—值：", end='')
for key, value in LSZ_dict.items():
    print(key, value, end=', ')  # 遍历输出所有键值对
print()
print("字典中所有的键：", end='')
for key in LSZ_dict.keys():  # 遍历输出所有的key值
    print(key, end=', ')
print()
