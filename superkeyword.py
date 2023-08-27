class a():
    def __init__(self):
        print("A")


class b():
    def __init__(self):
        super().__init__()
        print("B")


class c(b, a):
    def __init__(self):
        super().__init__()

        print("c")


lal = c()
