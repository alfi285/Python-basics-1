#Update()

#The update() method inserts all items from one set ino another
# The update() changes the original set and does not return a new set


set1 = {"a", "b", "c", "d"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)