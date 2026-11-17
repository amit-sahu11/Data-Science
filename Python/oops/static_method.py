class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    @staticmethod
    def hello():
        print("hello everyone")
    
s = Student("amit",97)
print(s.name,s.marks)
s.hello()