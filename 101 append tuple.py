# append() method

# Convert the tuple into a list add "Orange" and
# convert a new tuple with the value "orange

thistup = ("a","b", "c", "d", "e", "f", "g")
thist = ("Orange",)
tup = list(thistup)
tup.append(thist)
thistup = tuple(tup)
print(thistup)