num = int(input("enter a number"))
sasi = False
if num <= 0:
    print("the given number is not prime")
elif num > 0:
    for x in range(2,num):
        if (num%x) == 0:
            sasi = True
            break
    if sasi:
        print("the given number is not prime")
    else:
        print("the given number is  prime")