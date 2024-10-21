#Add a new item to the original dictionary
# and see that the key list gets updated as well

dict1 = {
    "name" : "Alfi",
    "age" : 31,
    "place" : "Pallikkal"
    }
x = dict1.keys() #before change
print("Before change : ", x)

dict1["subject"] = "CS"
print("After the change: ",x) #After the change