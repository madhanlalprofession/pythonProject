import re
a = input("enter a string")
b = re.compile('[!@#$%^&*()_+=<>?/|:]')
if b.search(a):
    print("present")
else:
    print("not present")
