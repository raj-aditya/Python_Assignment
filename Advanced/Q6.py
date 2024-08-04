class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return "Starting the vehicle"

class Car(Vehicle):
    def drive(self):
        return "Driving the car"

class ElectricCar(Car):
    def charge(self):
        return "Charging the electric car"

# Example usage
tesla = ElectricCar("Rivian")
print(tesla.brand)
print(tesla.start())
print(tesla.drive())
print(tesla.charge())