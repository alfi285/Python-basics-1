
# Loop through nested dictionaries

#you can loop through a dictionary by using the items() method like this

#Loop through the keys and values of all nested dictionaries

myfamily = {
    "Child1":{
    "Name" : "Alfi",
    "Year" : 1993
    },
    "Child2" : {
        "Name" : "Shad",
        "Year" : 1999
    },

    "Child3": {
        "Name" : "Shanu",
        "year" : 1989
    }
}

for x , z in myfamily.items():
    print(x)

    for y in z :
        print(y , " - ", z[y])