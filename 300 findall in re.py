#The findall() Function

#it returns a list of all matches

import re

txt = "The rain in Spain"
x = re.findall("ai",txt)
y = re.findall("hi",txt)
print(x)
print(y) #No match so we get an empty list

