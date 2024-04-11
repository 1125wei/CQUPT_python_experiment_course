x = '我的名字是{}，我今年{}'.format('小明', 29)  # format使用，{}作为占位符
print(x)
print('我的名字是{1}，我今年{0}岁'.format(10, 'jerry'))  # 使用整数数字作为占位符
print('我的名字是{name}，我今年{age}岁了'.format(89, 'xiaomin', name='henry', age=45))  # 使用变量名作为占位符
print('我的名字是{1}，我今年{age}岁了，他是{name}，他今年{0}岁了'.format(12, 'merry', name='jerry', age=45))  # 整数和变量名占位符混合使用
print('我的名字{}，我今年{age}岁了，他是{name}，他今年{}岁'.format('chris', 18, name='tony', age=20))  # {}和变量名占位符混合使用
