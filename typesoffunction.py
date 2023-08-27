class student():
    charger = "c type"
    @classmethod
    def dis(cls):
        charger = "b type"
        print(charger)
    @staticmethod
    def info():
        print("y type")
madhan = student()

madhan.dis()
madhan.info()
