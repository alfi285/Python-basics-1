#Add a new item to the original dictionary
#and see that the values lists gets updated as well

dict1 = {
    "name" : "Alfi",
    "age" : 31,
    "place" : "Pallikkal"
    }

x = dict1.values()
print("Before change : ",x)

dict1["Subject"] = "CS"
print("After change: ",dict1)
print("After change values: ",x)