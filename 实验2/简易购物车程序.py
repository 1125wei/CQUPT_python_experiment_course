# 定义一个商品列表，每个元素是一个包含商品名称和价格的元组
products = [
    ('iphone', 5800),
    ('mac pro', 9800),
    ('watch', 6800),
    ('coffee', 30),
    ('notebook', 15)
]

# 初始化一个空的购物车列表
shopping_list = []

# 提示用户输入工资
salary = input("请输入你的工资：")

# 检查工资输入是否为数字
if salary.isdigit():
    salary = int(salary)

    # 无限循环，用于用户不断选择商品
    while True:
        # 遍历商品列表，并打印商品编号和商品信息
        for index, item in enumerate(products):
            print(index, item)

            # 提示用户输入要购买的商品编号
        option = input("请输入你要购买的商品编号，或者输入'q'退出：")

        # 检查用户输入是否为数字
        if option.isdigit():
            option = int(option)

            # 检查商品编号是否在有效范围内
            if 0 <= option <= len(products) - 1:
                option_product = products[option]

                # 检查余额是否足够购买商品
                if option_product[1] <= salary:
                    # 将商品加入购物车，并更新余额
                    shopping_list.append(option_product)
                    salary -= option_product[1]

                    # 打印购买成功信息和当前余额
                    print("您选择的%s已经加入购物车，您的余额为\033[31;1m%s\033[0m" % (option_product[0], salary))
                else:
                    # 余额不足，打印提示信息
                    print("\033[41;1m您的当前余额为%s，余额不足！\033[0m" % salary)
            else:
                # 商品编号无效，打印提示信息
                print("抱歉，商品不存在！")

                # 检查用户是否输入'q'退出
        elif option == 'q':
            # 打印购物车列表和剩余余额
            print("-----------购物车列表-------------")
            for p in shopping_list:
                print(p)
            print("您的余额为:%s" % salary)

            # 退出程序
            exit()
        else:
            # 用户输入不合法，打印提示信息
            print("您的选择不合法")
else:
    # 工资输入不正确，打印提示信息
    print("您的工资输入不正确！")