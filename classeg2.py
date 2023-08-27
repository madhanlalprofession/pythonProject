class teacher:
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no

    def display(self):
        print("the name of the student is ", self.name, "and the register number of the student is ", self.reg_no)


t1 = teacher("madhan", 32)
t2 = teacher("revathi", 42)
t3 = teacher("rema",1234)
t1.display()
t2.display()
t3.display()
