#The intersection_update() method

#Will also keep only the duplications
#But it will change the original set instead of returning a new set

#Keep the items that exists in both set1 and set2

set1 = {"a", "b", "c", "d"}
set2 = {"google", "a", "b"}

set1.intersection_update(set2)
print(set1)