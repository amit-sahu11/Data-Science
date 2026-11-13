class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("this is student class")

s1 = Student("amit",98)
print(s1.name,s1.marks)