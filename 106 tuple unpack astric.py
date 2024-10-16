#Using asterisk *

#If the number of variable is less than the number of values
#you can add an * to the variable name
# and the values will be assigned to the variables as a list

# Assign the rest of the values as a list called "c"

fr = ("apple", "mango", "cherry", "grapes", "lemon")
(a, b, *c) = fr
print(a)
print(b)
print(c)