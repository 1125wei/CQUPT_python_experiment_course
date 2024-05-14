class People:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def speak(self):
        print("我是%s，我今年%s" % (self.name, self.age))


class Student(People):
    def __init__(self, n, a, g):
        People.__init__(self, n, a)
        self.grade = g

    def speak(self):
        print("我是%s，我今年%d，读%d年级" % (self.name, self.age, self.grade))


if __name__ == '__main__':
    s = Student("张三", 10, 4)
    s.speak()
