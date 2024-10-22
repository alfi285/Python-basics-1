#Update dictionary

#The update() method will update the dictionary
# with the items from the  given argument

#The argument must be a dictionary
# or an iterable object with key : value pair.
#Update the "year" of the car by using the update() method

dict1 = {
    "name" : "Alfi",
    "age" : 31,
    "place" : "Pallikkal"
    }

dict1.update({"place" : "Calicut"})
print(dict1)