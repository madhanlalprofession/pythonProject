"""for x in range(1,11):
  print(x," * 2 =",x*2)

for x in range(1,11):
   print(x, "*3 =", x * 3)
a = int(input("enter a number"))
b = int(input("enter a number"))
count = 0
count1 = 0
for x in range(a , b):
    if x % 2 != 0:
        count += 1
    elif x % 2 == 0:
        count1 += 1
print("the number of even number in given range is ", count1)
print("the number of odd numbers in given range is ", count)
count = 0
for x in range(1,100):
    if x % 3 == 0 and x % 5 == 0:
        count += 1
print(count)
count = 0
for x in range(1,6):
    count = count + x
print(count)

a = []
for x in range(4):
    b = int(input("enter a number " + str(x+1)+" "))
    a.append(b)
print(a)
sum = 0
count = 0
for i in a:
    count += 1
    sum += i
print(sum)
print(count)
print("the average of the given numbers are "+str(sum/count))
A = []
sum = 0
for x in range(3):
    B = int(input("enter a number "))
    A.append(B)
print(A)
for y in A:
    sum += y
print(sum)
a = []
count = 0
for x in range(4):
    b = int(input("enter a number"))
    a.append(b)
print(a)
for x in range(1, 1+2):
    print("week ", x)
    for y in range(1, 3):
    print("  day ", y)
arr = int(input([6]))
print(arr)"""

def function(arr):
    total_number = len(arr)
    positive_number = 0
    negative_number = 0
    neutral_number = 0
    for x in arr:
        if x > 0:
            positive_number += 1
        elif x < 0:
            negative_number += 1
        elif x == 0:
            neutral_number += 1
        positive_ratio = positive_number / total_number
        negative_ratio = negative_number / total_number
        neutral_ratio = negative_number / total_number

        print("{:.6f}".format(positive_ratio))
        print("{:.6f}".format(negative_ratio))
        print("{:.6f}".format(neutral_ratio))



