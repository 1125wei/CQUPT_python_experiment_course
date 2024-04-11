str = '我是Python3'  # 定义变量
str_utf8 = str.encode("utf-8")  # 生成utf-8编码赋值给变量
str_gbk = str.encode("GBK")  # 生成gbk编码赋值给变量
print(str)  # 打印变量
print("UTF-8 编码：", str_utf8)
print("GBK 编码L：", str_gbk)
print("UTF-8 解码：", str_utf8.decode("utf-8"))  # uft-8进行解码
print("GBK解码：", str_gbk.decode("GBK"))  # gbk进行解码

