class fruit:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def display(self):
        print("the color of the fruit is {} and weight of the fruit is {}".format(self.color, self.weight))


apple = fruit("red", 12)
mango = fruit("yellow", 20)
orange = fruit("orange", 10)
apple.display()
mango.display()
orange.display()
