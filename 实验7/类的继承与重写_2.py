class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


class Child(Person):
    def __init__(self, name, sex, mother, father):
        Person.__init__(self, name, sex)
        self.mother = mother
        self.father = father


May = Child('May', 'feale', 'April', 'June')
print(May.name, May.sex, May.mother, May.father)

