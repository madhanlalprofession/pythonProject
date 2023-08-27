"""try:
    a = int(input("enter a number"))
    b = int(input("enter a number"))
    print(a+b)
except Exception:
    print("sorry error occurs")"""
try:
    a = int(input("enter a number"))
    b = input("enter a number")
    print(a / b)
    print(c)
    print(a,b)

except TypeError as e:  # this error if the input given not operatable data type eg dividing of int and str
    print("TypeError", e)
except ValueError as e:  # this error occur if the syntax one but the input given by user is other
    print("ValueError", e)
except NameError as e:  # this error occur if there is no variable given but called
    print("NameError", e)
finally:
    print("successfull")
