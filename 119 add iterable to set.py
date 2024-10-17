#Add any iterable

#The object in the update() method does not have to be a set
#It can be any iterable object (tuples,list,dictionaries etc)

myset = {"red", "blue", "white"} #set
mylist = [1, 2, 3]  #List

myset.update(mylist)
print(myset)