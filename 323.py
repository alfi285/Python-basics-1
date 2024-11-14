
#Filtering out even numbers from a list
number=[1,3,4,5,6,7]
even_num = list(filter(lambda x:x % 2 == 0,number))
print(even_num)

# Key Differences:
# map(): Transforms each element of the iterable based on the given function.
# filter(): Selects only those elements that satisfy a given condition (i.e., when the function returns True).