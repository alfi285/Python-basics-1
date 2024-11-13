#Many Exceptions

#You can define as many exception blocks as you want
#e,g if you want to execute a special block of code for a special kind of error

#Print one message if they try block raises a nameerror and another for others

try:
    print(x)

except NameError:
    print("Variable x is not defined")

except:
    print("Something went wrong")


