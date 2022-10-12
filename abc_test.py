#from abc import ABC
from abc import ABCMeta
from abc import abstractmethod

#class Car(ABC):
class Car(metaclass=ABCMeta):
    def __init__(self):
        print("Car class begin")

    def greeting(self):
        return "Hello!"

    @abstractmethod
    def name(self):
        pass

    def __del__(self):
        print("Car class end")

class Firetruck(Car):
    def name(self):
        return "I'm a firetruck"

class PoliceCar(Car):
    def name(self):
        return "I'm a police car"

    def siren(self):
        return '"woo woo woo"'

class Ambulance(Car):
    def siren(self):
        return '"nee-naw nee-naw"'

class GarbageTruck():
    def name(self):
        return "I'm a garbagetruck"

class Bus():
    def drive(self):
        return '"round and round"'

print("###FIRETRUCK###")
firetruck = Firetruck()
print(f"is instance: {isinstance(firetruck, Car)}")
print(f"is subclass: {issubclass(firetruck.__class__, Car)}")
print(firetruck.greeting())
print(firetruck.name())
del firetruck

print("###POLICECAR###")
policecar = PoliceCar()
print(f"is instance: {isinstance(policecar, Car)}")
print(f"is subclass: {issubclass(policecar.__class__, Car)}")
print(policecar.greeting())
print(policecar.name())
print(policecar.siren())
del policecar

#ambulance = Ambulance() # Cannot instantiate abstract class "Ambulance" with abstract attribute "name"

print("###GARBAGETRUCK###")
Car.register(GarbageTruck)
garbagetruck = GarbageTruck()
print(f"is instance: {isinstance(garbagetruck, Car)}")
print(f"is subclass: {issubclass(garbagetruck.__class__, Car)}")
#print(garbagetruck.greeting()) # "GarbageTruck" has no attribute "greeting"
print(garbagetruck.name())
del garbagetruck

print("###BUS###")
Car.register(Bus) # registerを使うとエラーにならない
bus = Bus()
print(f"is instance: {isinstance(bus, Car)}")
print(f"is subclass: {issubclass(bus.__class__, Car)}")
#print(bus.greeting()) # "Bus" has no attribute "greeting"
print(bus.drive())
del bus

