#Class polymorphism

#Polymorphism is used often in class methods
#Where we can have multiple classes with the same method

#Different class with the same method

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car1 = Car("Ford","Mustang")
boat1 = Boat("Ibiza","Touring")
plane1 = Plane("Boeing","747")

for x in (car1,boat1,plane1):
    x.move()