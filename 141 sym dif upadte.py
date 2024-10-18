#The symmetric_difference_update() method
#will also keep all but the duplicates
#but it will change the original set instead of returning a new set

# use the symmetric method method to kleep the items


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "apple", "microsoft"}
set1.symmetric_difference_update(set2)
print(set1)