import os
import random
import string
import time


def random_string(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


def rename_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            file_stats = os.stat(file_path)
            file_mtime = time.strftime('%Y%m%d%H%M%S', time.localtime(file_stats.st_mtime))
            new_filename = f"{file_mtime}{file_extension}"
            new_file_path = os.path.join(directory, new_filename)

            while os.path.exists(new_file_path):
                new_filename = f"{file_mtime}-{random_string(3)}{file_extension}"
                new_file_path = os.path.join(directory, new_filename)

            os.rename(file_path, new_file_path)


# 使用示例
rename_files("E:\\Python_Code\\python实验1\\实验8\\文件批量重命名测试")  # 修改为自己的路径
"""
需要在路径中创建多个任意名字文件
"""
