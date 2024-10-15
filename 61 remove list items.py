# Remove List items

#The remove() method removes the specified item

#Remove " red"

clrlist = ["red","green", "blue"]
clrlist.remove("red")
print(clrlist)

#if there are more than one item with the specified value
# the remove() method removes the first occurence:

#remove the first occurence of red

clrlist2 = ["orange","blue", "red","green", "red"]
clrlist2.remove("red")
print(clrlist2)