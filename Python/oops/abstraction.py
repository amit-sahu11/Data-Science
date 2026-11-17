class Car:
    def __int__(self):
        self.acc = False
        self.brk = False
        self.cluch = False
    
    def start(self):
        self.acc = True
        self.clutch = True
        print("car started..")

car1 = Car()
car1.start()