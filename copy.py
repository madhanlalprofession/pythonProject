a=[1, 2, 3, 4 ]
b=a[:]
print(b)
c=[2,0]
c.extend(b)
print(c)
d=list[c]
print(d)
d=c.copy()
print(d)