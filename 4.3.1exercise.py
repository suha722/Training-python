"""
Create a class that represents a logger mechanism and implements the Singleton design pattern.
"""

class Logger:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance
    def log(self,massege):
        print(massege)
l=Logger()
l1=Logger()

print(l is l1)
class VehicleFactory:
    def create_vehicle (type_vehicle):
        if type_vehicle=="car":
            Car()


class Vehicale:
    def drive(self):
        pass
class Car(Vehicale):
    def drive(self):
        print("You drive Car ")
class Truck(Vehicale):
    def drive(self):
        print("You drive Truck ")
class Bus (Vehicale):
    def drive(self):
        print("You drive Bus ")

