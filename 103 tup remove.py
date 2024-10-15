# Remove items
#Note : You cannot remove an item in tuple

#Tuples are unchangeable so you cannot remove items from it
# but you can use the same work a round as we used for changing and adding tuple items

#Convert the tuple into a list remove item
# and convert it back into a tuple

thistup = ("a","b", "c", "d", "e", "f", "g")
y = list(thistup)
y.remove("d")
thistup = tuple(y)
print(thistup)
