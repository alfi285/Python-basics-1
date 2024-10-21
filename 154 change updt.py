#Make a change in a original dictionary
#and see that the items lists gets updated as well

dict1 = {
    "name" : "Alfi",
    "age" : 31,
    "place" : "Pallikkal"
    }

x = dict1.items()
print("Before : ", x)

dict1["Subject"] = "Computer Science"
print("After:",x)