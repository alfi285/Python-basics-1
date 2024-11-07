#The self Parameter!
#The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.
#It does not have to be named self ,
# you can call it whatever you like,
# but it has to be the first parameter of any function in the class:
# Use the words mysillyobject and abc instead of self ?

class Person:
    def __init__(init,name,age):
        init.name = name
        init.age= age

    def disp(display):
        print(f"Name:{display.name}\nAge:{display.age}")

p1 = Person("Zaara",6)
p1.disp()