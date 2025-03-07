# ==============================================================================================
# Inheritance is a fundamental concept in object-oriented programming. 
# It allows you to define a new class based on an existing class. 
# The new class inherits attributes and methods from the existing class. 
# Inheritance is useful because it allows you to reuse code and create a hierarchy of classes.
# ==============================================================================================

# Example,
# +> Car is a vehicle
# +> Bike is a vehicle, then both are vehicles derived from the vehicle class.

class Vehicle:
    def __init__ (self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print("Starting the vehicle")
    
    def stop(self):
        print("Stopping the vehicle")

class Car(Vehicle):
    def __init__(self, brand, model, year, color): # color is an additional attribute for the Car class
        super().__init__(brand, model, year)       # Call the constructor of the parent class 
        self.color = color                         # Initialize the color attribute of the Car class

class Bike(Vehicle):
    def __init__(self, brand, model, year, engine):
        super().__init__(brand, model, year)
        self.engine = engine
        
car = Car("Toyota", "Corolla", 2019, "Red") # Create an instance of the Car class
bike = Bike("Honda", "CBR", 2020, "250cc") # Create an instance of the Bike class

print(car.__dict__) # print the attributes of the car object as a dictionary
print(bike.__dict__)