class Student:
    college_name = "global college"

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        print("hello students")
    
    def welcome(self):
        print("hello hii",self.name)

    def get_marks(self):
        return self.roll_no


s1 = Student("amit",20)
s1.welcome()
print(s1.college_name)
print(Student.college_name)
print(s1.get_marks())