# Create a class named Car.
# Use the __init__() function
# to assign values for make, model, and year.

class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

c1 = car("H","Benz",2024)

print(c1.make)
print(c1.model)
print(c1.year)