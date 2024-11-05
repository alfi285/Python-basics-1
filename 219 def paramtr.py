#Default Parameter Value

#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:

def my_func(country="Norway"):
    print("I am from "+country)

my_func("Swedan")
my_func("India")
my_func()
my_func("Brazil")