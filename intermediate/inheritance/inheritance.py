# Inheritance in Python

# Parent Class
class Vehicle:
    def __init__(self, name, fuel_type):
        self.name = name
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"The {self.name}'s engine starts.")

# Child Class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, name, fuel_type, doors):
        # Call the parent class constructor to initialize name and fuel_type
        super().__init__(name, fuel_type)
        self.doors = doors

    # Overriding a parent method
    def start_engine(self):
        print(f"The {self.name} car purrs softly with {self.fuel_type}.")

    def open_sunroof(self):
        print(f"Opening sunroof of the {self.name}.")

# Child Class inheriting from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, name, fuel_type, has_sidecar):
        super().__init__(name, fuel_type)
        self.has_sidecar = has_sidecar

    # Overriding parent method
    def start_engine(self):
        print(f"The {self.name} motorcycle roars to life!")

# Create objects of the child classes
my_car = Car("Tesla Model 3", "electric", 4)
my_car.start_engine()  # calls overridden method in Car
my_car.open_sunroof()

print("-" * 20)

my_bike = Motorcycle("Harley Davidson", "petrol", False)
my_bike.start_engine()  # calls overridden method in Motorcycle
