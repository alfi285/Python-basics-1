# The values True and 1 are considered the same value
#The same goes for False and 0

#Join sets that contains the values
#True,False ,1 and 0 and see what is considered as duplicates

set11 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set11.intersection(set2)
print(set3)