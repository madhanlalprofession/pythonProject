def add():
    print(a + b)


def sub():
    print(a-b)


def mul():
    print(a * b)


def div():
    print(a / b)


def mod():
    print(a % b)


print("""
1-addition
2-subtraction
3-multipication
4-division
5-modulus
""")
c = int(input("select a number for above operation "))
a = int((input("enter the first number ")))
b = int((input("enter the second number ")))
if c == 1:
    add()
elif c == 2:
    sub()
elif c == 3:
    mul()
elif c == 4:
    div()
elif c == 5:
    mod()
