# Without list compression

# You will have to write a for statement with a conditional test inside:'

fruits = ["apple", "cherry", "orange", "kiwi", "mango","banana"]
newlist = []

for x in fruits :
    if "a" in x:
        newlist.append(x)

print(newlist)

# using list compression
fruits = ["apple", "cherry", "orange", "kiwi", "mango","banana"]
newliist2 = [x for x in fruits if "a" in x]
print(newliist2)