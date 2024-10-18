#Symmetric difference

#The symmetric_difference() method will keep only
#the elements that are not in both sets

# keep the items that are not present in both sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "apple", "microsoft"}

set3 = set1.symmetric_difference(set2)
print(set3)