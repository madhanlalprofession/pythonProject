"""class shape():
    def area(self):
        return 0


class rectangle(shape):
    def area(self, a1, b1):
        a = a1
        b = b1
        return a * b


rc = rectangle()
print(rc.area(5, 2))

class person():
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__ (self,grade):
        super().__init__()
        self.grade = grade
    def display(self):
        print(self.name,self.grade)
s = student("a")
v = person("v")

class vehicle():
    def start(self):
        return "vehicle starts"
class car(vehicle):
    def start(self):
        return "car started"
ca = car()
print(ca.start())"""


class employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class manager(employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print(self.name, self.salary, self.department)


ca = manager("madhan", "100000", "cse ")
ca.display()
