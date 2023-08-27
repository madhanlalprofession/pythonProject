
def unique_number(a):
    num = 0
    for x in a:
       if x in a:
           num += 1
       if num == 2:
           return False
       elif num != 2:
           return True
print(unique_number(a=[1,2,1,4]))
