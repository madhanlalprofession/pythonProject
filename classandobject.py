"""class love:
    male_name = "sins"
    female_name = "mia_khalifa"

    def work(self):
        print("enjoying")


male = love()
female = love()


print(male.male_name, "and",female.female_name,end=" ")
female.work()"""
class Laptop:
    price = ""
    processor = ""
    RAM = ""
HP = Laptop()
lenovo = Laptop()
dell = Laptop()
HP.price = "10000"
HP.processor = "intel"
HP.RAM = "12"
lenovo.processor = "intel"
lenovo.price = "100000"
lenovo.RAM = "16gb"
dell.RAM = "8gb"
dell.price = "10"
dell.processor = "AMD"
print("the price of HP is {} and RAM is {} and processor is {}".format(HP.price, HP.RAM, HP.processor))
print("the price of dell is {} and RAM is {} and processor is {}".format(dell.price, dell.RAM, dell.processor))
print("the price of lenovo is {} and RAM is {} and processor is {}".format(lenovo.price, lenovo.RAM, lenovo.processor))

