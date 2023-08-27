book = {
    "date" : "today",
    "time" : "thistime"
}
print(book)
print(book["date"])
book["time"] = "tomorrow"
print(book)
for x in book:
    print(x)
    print(book[x])
for x1 in book.values():
    print(x1)
for x2 , y2 in book.items():
    print(x2, y2)
if "date" in book:
    print("yes,tfr4aq")
book["color"] = "red"
print(book)
food = dict(veg="dosa",nonveg="parotta")
print(food)
