#Create a class named Vehicle,
# with brand and year properties, and a print_info method:
# Use the Vehicle class to create an object,
# and then execute the print_info method:

class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def print(self):
        print(f"Vehicle brand:{self.brand} - Year:{self.year}")

# Create a class named Car,
# which will inherit the properties and methods from the Vehicle class
class Car(Vehicle):
    pass

v1 = Car("Benz",2023)
v1.print()
