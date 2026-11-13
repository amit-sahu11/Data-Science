class Car:
    color = "Blue"
    name = "tata"
    def __init__(self,fullname):
        self.name = fullname
        print(self)
        print("adding new student in database..")

c1 = Car("maruti")
print(c1.name)
print(c1.color)