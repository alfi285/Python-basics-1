# Update Tuples

# Change tuple value
#Once a tuple is created you cannot change its values
#Tuples are unchangeable or immutable as it also is called

# You can convert the tuple into a list
# Change the list and convert the list back into a tuple

#Convert the tuple into a list to be able to change it

thistup = ("a","b", "c", "d", "e", "f", "g")
list1 = list(thistup)
list1[1] = "Z"
thistup = tuple(list1)
print(thistup)