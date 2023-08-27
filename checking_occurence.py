arr = [2, 3, 5, -2, -5, 0]
z = len(arr)
count = 0
count1 = 0
count2 = 0
for x in arr:
     if x > 0:
        count += 1
     elif x < 0:
        count1 += 1
     elif x == 0:
        count2 += 1
a = count/z
b = count1/z
c = count2/z
print("the ratio of positive number is {} and the ratio of negative number is {} and the ratio of zero is {}".format(a, b, c))
