#Else

#You can use the else keyword to define a block of code to be executed if no errors were raised:

#in this example the try block does not generate any error

try:
    print("Hello")
except:
    print("Some error occured")
else:
    print("Nothing occured")
