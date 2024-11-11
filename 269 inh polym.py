#Inheritance class polymorphism

#The child class inherit the vehicle methods

#Create a class called Vehicle and make Car,Boat,Plane child classes of Vehicle

class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def  move(self):
        print("Move...!")


class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail...!")

class Plane(Vehicle):
    def move(self):
        print("Fly..!")

car1 = Car("Benze","B")
boat1 = Boat("Ibiz","Touring")
plane1 = Plane("Boeing","747")

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()
#Child class inherits the properties of parent class.