"""
从列表中获取键值创建列表
"""
key_list = ["name", "age", "hobby"]
val = "test"
d = {}
"""
不指定值
"""
d = d.fromkeys(key_list)
print("新字典", d)
"""
指定值
"""
d = d.fromkeys(key_list, val)
print("新字典", d)
