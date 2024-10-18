#You can use the & operator

# instead of the intersection() method
#and you will get the same result

#Use & to join two sets

set1 = {"a", "b", "c", "d"}
set2 = {"google", "a", "b"}

set3 = set1 & set2
print(set3)

#The & operator only allows you to join sets with sets
#and not with other data types
#like you can with the intersection() method