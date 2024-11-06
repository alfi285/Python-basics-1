#Lambda function

#Function defnition to make a function
#That always double the number you send in

#Function defnition
def myfunc(n):
    return lambda a:a*n

#myfunc takes one argument n,it returns lambda function , lambda a: a*n,
# Which is an anonymous(unnamed) function,this lambda takes one argument a and result of a * n

#Creating a multiplier:
mydoubler = myfunc(2)

#Here myfunc(2) is called with n =2
#This returns a lambda function equivalent to
#lambda a:a*2(because n =2)
#mydoubler now holds a reference to this lambda function
#So mydoubler(a) will double any input a

print(mydoubler(3))

#function definition to make a function
# that always triples the number you send in ?
#create triplr

mytripler = myfunc(3)
print(mytripler(5))