file = open(r"d:\data99.txt", "r")
file.close()

file = open(r"d:\data1.txt", "w")
print("文件名字", file.name)
print("访问模式", file.mode)
print("是否已关闭", file.closed)
file.close()
print("是否已关闭", file.closed)

str_ = ["好雨知时节,当春乃发生。\n", "随风潜入夜，润物细无声。"]
with open("杜甫.txt", "w") as file:
    file.writelines(str_)
    print("写入字符序列成功!")

str_ = "作者:杜甫"
with open("杜甫.txt", "a") as file:
    file.write("\n")
    num = file.write(str_)
    print("向文件中追加字符%d个!" % (num))

with open("杜甫.txt", "r") as file:
    str = file.read()
    file.seek(0)
    print(str)
    str = file.read(6)
    print(str)

with open("杜甫.txt", "r") as file:
    fr1 = file.read()
    file.seek(0)
    fr2 = file.readline()
    file.seek(0)
    fr3 = file.readlines()
print(fr1)
print(fr2)
print(fr3)
print(type(fr3))

with open("杜甫.txt", "r") as file:
    str = file.read(2)
    print(str)
    print("当前指针位置: ", file.tell())
    str = file.read(4)
    print(str)
    print("当前指针位置: ", file.tell())
    file.seek(0)
    str = file.read(2)
    print(str)
"""
需要在d盘创建 data99.txt和data1.txt文件，或者更改上面的路径
"""