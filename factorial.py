factorial = 1
num = int(input("enter a number"))
if num < 0:
    print("the factorial is not possible for negative number")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for x in range(1,num+1):
        factorial *= x
    print(factorial)
