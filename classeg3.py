class calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def mul(self):
        print(self.a,self.b)
    def div(self):
        print(self.a/self.b)
    def mod(self):
        print(self.a%self.b)
addition = calc(1,1)
subtraction = calc(10,2)
multipication = calc(2,2)
division = calc(10,2)
modulus = calc(10001,4321)
addition.add()
subtraction.sub()
multipication.mul()
division.div()
modulus.mod()

