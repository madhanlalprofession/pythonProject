a = list([])
for x in range(5):
    b = int(input())
    a.append(b)
a.sort()
print(a[0] + a[1] + a[2] + a[3], a[1] + a[2] + a[3] + a[4])
