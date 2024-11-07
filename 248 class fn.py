# Create a method in the Animal class.
# Insert a function that prints the animal's name and sound,
# and execute it on the a1 object.

class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def disp(self):
        print(f"Animal name:{self.name}\nAnimal sound:{self.sound}")

a1 = Animal("Dog","bow..bow..")

a1.disp()