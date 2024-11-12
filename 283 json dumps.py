#Convert from json to python

#If you have a python object you can convert it into json string
#by using the json.dumps() method

#Convert from python to JSON

import  json

#Python object (dict)

x = {
    "name":"Alfi",
    "age":23,
    "city":"Norway"
}

#Convert it into python
y = json.dumps(x)
#Result is json string
print(y)