#Python iterators

#An iterator is an object that contain a countable number of values
#
#An iterator is an object which consists of the methods
#__iter__() and __next__()
#Return an iterator from a tuple and print each value

mytuple = ("Apple","Banana","Cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

