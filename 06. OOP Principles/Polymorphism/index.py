# Polymorphism is the ability to use a common interface for multiple forms (data types). (Many Forms)

class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
    
    def start(self):
        print("Starting the car")
    
    def stop(self):
        print("Stopping the car")

class Motorcycle:
    def __init__(self, brand, model, year, engine):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine
    
    def start(self):
        print("Starting the motorcycle")
    
    def stop(self):
        print("Stopping the motorcycle")


# Create list of vehicles to inspect
Vehicles = [
    Car("Toyota", "Corolla", 2019, "Red"),
    Motorcycle("Honda", "CBR", 2020, "250cc"),
    Car("Ford", "Fiesta", 2018, "Blue"),
    Motorcycle("Yamaha", "YZF", 2019, "300cc")
]

# Loop through the list of vehicles and inspect them
for vehicle in Vehicles:
    if isinstance(vehicle, Car):
        print(f"{vehicle.brand} {vehicle.model} is a car")
        vehicle.start() # start method in the Car class
        vehicle.stop()
    elif isinstance(vehicle, Motorcycle):
        print(f"{vehicle.brand} {vehicle.model} is a motorcycle")
        # also we can use the start and stop methods in the Motorcycle class as previously
    else:
        raise Exception("Unknown vehicle type")