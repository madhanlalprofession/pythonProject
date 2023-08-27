a = [1, 2, 3, 4, 5]
for x in a:
    print(x)
b = ["madhan"]
for y in b:
    print(y)
c = list["car", "bike", "van", "lorry"]
for z in [c]:
    print(z,"is present in the index ",c.index)
    if z == "bike":
        break
d = ['hi', 'iam', 'ma', 'dh', 'an', 'lal', 'ho', 'wa', 're']
for g in d:
    if g == "ma":
     continue
    print(g)

for x in range(5):
    print(x)
else :
    print("this is else in for")

x = ["a", "b"]
y = ["a", "b"]
for x1 in x:
    for x2 in y:
        print(x1,x2)
