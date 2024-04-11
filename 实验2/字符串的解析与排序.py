word = """rguiwrgieheojhoss
dseugfiuwbehsigufbskgbk
sgrbksgbsgavbckjsbvouerihqofnoerighut"""  # 初始化变量
list1 = list(word)  # 赋值为list类型
word.replace('\n', '')  # 替换掉换行符
list2 = sorted(list1)  # 进行排序
list3 = list(set(list1))  # 转化为集合然后转化为列表，去除重复字母
list4 = []
list5 = []
for i in list3:  # 遍历i
    j = list2.count(i)  # 计算i的出现次数
    list4.append((i, j))  # 将字符和次数作为元组储存进列表
list4 = sorted(list4, key=lambda x: x[1], reverse=True)  # 对列表进行排序，排序依据是元素的第二个数据，降序排序
print(list4)
list5 = list4[:10]  # 取前10个
print(list5)
