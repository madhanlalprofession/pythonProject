#single inheritance
"""class madhan():
    def bag(self):
        print("madhan is a good boy")


class lal(madhan):
    def shoe(self):
        print("madhan is great")


madhanlal = lal()
madhanlal.bag()
madhanlal.shoe()"""
#multiple inheritance
class biriyani():
    def rice(self):
        print("biriyani is tasty")
class parotta():
    def maida(self):
        print("parotta is tasty")
class salna(biriyani,parotta):
    def grey(self):
        print("salna is useful for both biriyani and parotta")


madhanlal = salna()
madhanlal.rice()
madhanlal.maida()
madhanlal.grey()
