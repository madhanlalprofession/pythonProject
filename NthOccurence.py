a = ["madhan", "lal", "madhan"]
word = "madhan"
n = 2
count = 0
for x in range(0,len(a)):
    if( a[x] == word ):
        count += 1
        if(count==n):
         del a[x]
         print(a)
