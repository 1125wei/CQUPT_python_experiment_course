import os
import time

print("当前工作路径：", os.getcwd())  # 当前所在路径
path = os.path.abspath('test.txt')
print(path)
print(os.path.abspath('.'))

print("当前路径和文件列表", os.listdir())
os.mkdir("newDir")
print("创建新目录后：", os.listdir())
os.chdir("newDir")
print("改变当前工作路径后：", os.getcwd())
os.rename(r"E:\Python_Code\python实验1\实验8\test1.txt", r"E:\Python_Code\python实验1\实验8\test3.txt")

print(os.listdir('.'))
for file in os.listdir('.'):
    if file.endswith('.txt'):
        print(file)

path = r'D:\py'
print(os.walk(path))
for parent, dirnames, filenames in os.walk(path):
    print(parent, dirnames, filenames)
    print(type(parent), type(dirnames), type(filenames))

path = r'D:\py'
print("(路径，文件)", os.path.split(path))
print("目录存在？", os.path.exists(path))
print("文件否？", os.path.isfile(path + '\\test.txt'))

file = 'D:\\py\\test.txt'

print(time.strftime('%Y-%m-%d %H:%M:', time.localtime(os.path.getmtime(file))))
print(time.strftime('%Y-%m-%d %H:%M:', time.localtime( os.path.getmtime(file))))
print(time.strftime('%Y-%m-%d %H:%M:', time.localtime( os.path.getmtime(file))))
