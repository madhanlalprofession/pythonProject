a = [1, 2, 3, 4, 5]
element = 2
flag = 0
for x in a:
    if (x == element):
        print("yes present")
        flag = 1
        break
if (flag == 0):
        print("not present")

b = [1, 3,  5, 6]
ele = 5
if(ele in b):
    print("element found")
else:
    print("not present")
