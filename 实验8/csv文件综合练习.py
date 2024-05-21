import csv

headers = ['NO', 'Name', 'Sex', 'Age', 'Salary']
rows = [('1001', 'Jack', 'male', 28, 12800),
        ('1002', 'Rose', 'female', 22, 8800),
        ('1003', 'Tim', 'male', 26, 10800)]
try:
    with open('salary.csv', 'w', newline='') as file:
        fw = csv.writer(file)
        fw.writerow(headers)
        fw.writerows(rows)
        print("写入数据成功！")
except:
    print("写入数据失败！")

print("读取数据结果：")
try:
    with open('salary.csv', 'r') as file:
        fr = csv.reader(file)
        rows = [row for row in fr]
        print("标题:", rows[0])
        print("第1行数据:", rows[1])
        column = [row[1] for row in rows]
        print("第1列数据：", column)
        print("第1行第1列数据:", rows[1][1])
except:
    print("读取数据失败!")
