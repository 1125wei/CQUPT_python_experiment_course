list = ['sichuan', 'chongqing', 'guangdong', 'hunan']  # 初始化列表，建议更换变量名称，因为list为类型名
list.append('jiangsu')  # 向列表末尾添加
list.insert(2, '杭州')  # 向列表指定索引位置插入
list.extend(["重庆", "武汉"])  # 拓展列表，加入新的列表在原表表尾
list[0] = ' '  # 替换指定索引位置内容
list[1:3] = ["芒果", "木瓜"]  # 切片替换内容
print()

