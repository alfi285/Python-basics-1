#The difference_update() method will also keep the items
#from the fist set that are not in the other set
#but it will change the original in both sets

#Use the difference_update() method to keep the item
#that are not present in both sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "apple", "microsoft"}

set2.difference_update(set1)
print(set2)
#set1.difference_update(set2)
#print(set1)