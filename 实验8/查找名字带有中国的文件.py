import os
import re

def find_china_in_files(directory):
    pattern = re.compile(r'中国')
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.txt'):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    line_number = 0
                    for line in f:
                        line_number += 1
                        if pattern.search(line):
                            print(f"文件：{file_path}, 行号：{line_number}, 内容：{line.strip()}")

# 使用示例
find_china_in_files("E:\\Python_Code\\python实验1\\实验8\\查找筛选文件名测试")  # 修改为自己的路径
"""
需要创建一个或多个文件内容带有中国的txt文件
"""