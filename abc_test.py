#from abc import ABC
from abc import ABCMeta
from abc import abstractmethod

#class Car(ABC):
class Car(metaclass=ABCMeta):
    def __init__(self):
        print("===Car class begin===")

    def greeting(self):
        return "Hello!"

    @abstractmethod
    def name(self):
        pass

    def __del__(self):
        print("===Car class end===")

class Firetruck(Car):
    def name(self):
        return "I'm a firetruck"

class PoliceCar(Car):
    def name(self):
        return "I'm a police car"

    def siren(self):
        return '"woo woo woo"'

class Ambulance(Car):
    def name(self):
        return "I'm an ambulance"

    def siren(self):
        return '"nee-naw nee-naw"'

class GarbageTruck():
    def name(self):
        return "I'm a garbagetruck"

class Bus():
    def name(self):
        return "I'm a bus"

    def drive(self):
        return '"round and round"'

firetruck = Firetruck()
print(isinstance(firetruck, Car))
print(firetruck.greeting())
print(firetruck.name())
del firetruck

policecar = PoliceCar()
print(isinstance(policecar, Car))
print(policecar.greeting())
print(policecar.name())
print(policecar.siren())
del policecar

#ambulance = Ambulance() # Cannot instantiate abstract class "Ambulance" with abstract attribute "name"
#print(isinstance(ambulance, Car))
#print(ambulance.greeting())
#print(ambulance.siren())
#del ambulance

Car.register(GarbageTruck)
garbagetruck = GarbageTruck()
print(isinstance(garbagetruck, Car))
print(garbagetruck.name())
del garbagetruck

Car.register(Bus) # registerを使うとエラーにならない
bus = Bus()
print(isinstance(bus, Car))
print(bus.drive())
del bus
