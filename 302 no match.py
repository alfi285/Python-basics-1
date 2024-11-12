#Make a search that returns no match..returns None


import  re

txt = "The rain in Spain"
x = re.search("Portugal",txt)
print(x)

y = re.search("ai",txt)
print(y)

#Match object
#If match it returns a match object


#Print the position (start-and -end position) of the first match occurence
#That start with an upper case
z = re.search(r"\bS\w+",txt)
print(z.span())

#Print the string passed into the function
a = re.search(r"\bS\w+",txt)
print(a.string)

#Print the part of the string where there was a match
b = re.search(r"\bS\w+",txt)
print(b.group())

