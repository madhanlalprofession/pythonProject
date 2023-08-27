a = [5, 12, 6, 8]
b = max(a)
c = min(a)
print("the maximum number is {} and the minimum number is {}".format(b, c))
d = sorted(a)
print(d)
print("the smallest number in the list is {} and the largest number in the list is {}".format(d[0], d[-1]))
# second largest and smallest
print(d[1], d[-2])
