#Modify the value of the first array item

cars = ["ford","volvo","BMW","Honda"]
cars[0] = "Toyota"
print(cars)

#Return length

print("Length of an array:",len(cars))

#Looping array

for x in cars:
    print(x)

#add one element to array..append() it adds at the end of the array
cars.append("Benz")
print(cars)

#Removing array elements
#Remove second element using pop()..simply deletes last element,
# if we add index deletes current element in that index

cars.pop(1)
print(cars)

#Remove one data from array,if there is multiple items with same value it removes first occurence
cars.remove("Honda")
print(cars)