#THe split() function

#The split() function returns a list where the string has been split at each match

#Split at each white-space character

import re

txt = "The rain in spain"
x = re.split("\s",txt)
print(x)

y= re.split("\s",txt,1)
print(y)

#You can control the number of occurences by specifying the maxsplit parameter
#hr splitted only in one occurence