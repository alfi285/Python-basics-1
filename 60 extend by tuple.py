# Add any iterable
# The extend() method does not have to append list
# you can add any iterable object (tuple,sets,dictionaries etc).

# Add elements of a tuple to a list

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)