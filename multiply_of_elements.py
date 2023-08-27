from math import prod

a = [1, 2, 3, 4]
count = 1
for x in a:
    count = count * x
print(count)
b = prod(a)
print(b)