class Person(object):
    def __init__(self, name, age, speak):
        self.name = name
        self._age = age
        self.__speak = speak


class Student(Person):  # 继承父类Person
    def construction(self, name, age, speak):
        self.name = name
        self._age = age
        self.__speak = speak


s1 = Student('jack', 25, 'Chinese')
print(s1.name, s1._age)
print(s1.name, s1._age, s1.__speak)
