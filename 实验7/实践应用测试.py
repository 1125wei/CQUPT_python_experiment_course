class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_borrowed = False  # 初始状态为未借出

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False


class BookManager:
    def __init__(self):
        self.books = []  # 初始化书籍列表

    def menu(self):
        print("欢迎使用书籍管理系统")
        print("1. 显示所有书籍")
        print("2. 添加书籍")
        print("3. 借出书籍")
        print("4. 检查书籍是否存在")
        print("5. 退出")
        choice = input("请输入您的选择：")
        return choice

    def show_all_books(self):
        for book in self.books:
            print(f"书名：{book.name}, 价格：{book.price}, 状态：{'已借出' if book.is_borrowed else '未借出'}")

    def add_books(self):
        name = input("请输入书籍名称：")
        price = float(input("请输入书籍价格："))
        new_book = Book(name, price)
        self.books.append(new_book)
        print(f"书籍《{name}》添加成功！")

    def lend_books(self):
        name = input("请输入要借出的书籍名称：")
        for book in self.books:
            if book.name == name:
                if book.is_borrowed:
                    print(f"书籍《{name}》已经被借出。")
                else:
                    book.borrow()
                    print(f"书籍《{name}》借出成功！")
                return
        print(f"书籍《{name}》不存在。")

    def check_books(self):
        name = input("请输入要检查的书籍名称：")
        for book in self.books:
            if book.name == name:
                print(f"书籍《{name}》存在。")
                return
        print(f"书籍《{name}》不存在。")


# 简单的交互式程序
if __name__ == "__main__":
    manager = BookManager()
    while True:
        choice = manager.menu()
        if choice == '1':
            manager.show_all_books()
        elif choice == '2':
            manager.add_books()
        elif choice == '3':
            manager.lend_books()
        elif choice == '4':
            manager.check_books()
        elif choice == '5':
            print("退出系统。")
            break
        else:
            print("无效的选择，请重新输入。")
