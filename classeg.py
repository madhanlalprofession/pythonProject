"""class student:
    def __init__(self):
        self.name = ""
        self.register_number = ""

    def display(self):
            print("student name ",self.name)
            print("student register number",self.register_number)
madhan = student()
madhan.name = "madh"
madhan.register_number = "1234"
madhan.display()"""


class Laptop:
    def __init__(self, price, RAM, proc):
        self.Price = price
        self.RAM = RAM
        self.proc = proc

    def display(self):
        print("the price is {} ".format(self.Price))
        print("the RAM is {}".format( self.RAM))
        print("the proc is {}".format(self.proc))
        print()


HP = Laptop(10,6,"i4")
dell = Laptop(20,3,"i5")
lenovo = Laptop(20,16,"i2")
HP.display()
dell.display()
lenovo.display()
