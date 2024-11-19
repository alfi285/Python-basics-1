#Parse JSON - Convert from JSON to Python

#If you have a JSON string,
# you can parse it by using the json.loads() method.

#The result will be a Python dictionary.

# Convert from JSON to Python?

import json

#Some json

x = '{"name":"John","age":30,"city":"New york"}'

#  parses x

y = json.loads(x)

#The result is python dictionary

print(y)