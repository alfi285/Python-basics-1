#Customise sort function


# you can also customiza your function by
# using the keyword argument key = function

#the function will return
# a  number that will be used to sort the list (the lowest numbers first)

# sort the list based on how close the number is to 50

def myfunc(n):
    return abs(n - 50)
list1 = [45, 67, 34, 78, 79]
list1.sort(key= myfunc)
print(list1)

#myfunc(45) returns 45 - 50 = 5
#myfunc(67) returns 67 - 50 = 17
#myfunc(34) returns 34 - 50 =16
#myfunc(78) returns 78 - 50 = 28
#myfunc(79) returns 79 - 50 = 29
#its sorted -in base of these values we get 45,34,67,78,79