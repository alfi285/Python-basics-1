# Make a change in the original dictionary
# and see that the values list gets updated as well

dict1 = {
    "name" : "Alfi",
    "age" : 31,
    "place" : "Pallikkal"
    }

x = dict1.values()
print("Before change values: ", x)

dict1["age"] = 30
print("After change values: ", x)