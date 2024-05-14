class Student:
    chinese = 142
    english = 141
    maths = 1

    def __init__(self, name):
        self.name = name


s = Student('马允')
print(s.name + "的语文成绩：" + str(Student.chinese))
print(s.name + "的数学成绩" + str(Student.maths))
print(s.name + "的英语成绩" + str(Student.english))
print(s.name + "的语文成绩：" + str(s.chinese))
print(s.name + "的数学成绩" + str(s.maths))
print(s.name + "的英语成绩" + str(s.english))
