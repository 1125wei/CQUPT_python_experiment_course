cityList = ["珠海", "威海", "信阳", "惠州", "厦门", "金华", "柳州", "曲靖", "九江", "绵阳"]
del cityList[8]  # 删除索引为8元素
cityList.pop()  # 删除表尾元素
cityList.pop(6)  # 删除索引为6的元素
cityList.remove("厦门")  # 删除“厦门”
cityList[4:] = []  # 将索引4到表尾删除
cityList.clear()  # 清空表，释放内存
print()
