class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


s1 = Student("amit",97)
print(s1.name,s1.marks)
del s1
print(s1)