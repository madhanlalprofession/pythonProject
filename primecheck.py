a = int(input("enter a number"))
if a > 1:
    for x in range(1, a):
        if (a % x) == 0:
            print("the given number is not prime")
            break
        else:
         print("the given number is prime")
else:
    print("the given number is not prime")

