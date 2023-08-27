def unique_names(names1,names2):
  c = set(names1+names2)
  return c

names1 = ["Ava","Emma","Olivia"]
names2 = ["Olivia","Sophia","Emma"]

print(list(unique_names(names1,names2)))
