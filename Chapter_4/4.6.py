#4.6 - What NamedTuples are good for

#NamedTuples are an extension of tuple data type (immutable). These can be used as an alternative to creating immutable classes manually

#Tuples objs can be retrieved only through index and we cannot give names to individual properties in tuples

#Tuples are always an ad-hoc structure so we cant find if 2 tuples have the same fields and properties

import json
from collections import namedtuple
Car = namedtuple('Car','color mileage')
#Color and mileage are the two parameters
#Car is the class we are creating and they are called 'typename'
#We are passing color and mileage as strings, since Py will split these strings internally and store them
#This will behave as if 'Car' class is defined and 'color and mileage' are its constructor passing the values
#They are memory efficient than classes and equally memory efficient to tuples

my_car = Car('Red',500)
print(my_car)
print(my_car.color)
print(my_car.mileage)
print(my_car[0])
print(tuple(my_car))
color, mileage = my_car
print(mileage)
print(my_car)
print(*my_car) #Tuple unpacking
#my_car.color='blue' --> AttributeError: can't set attribute (Immutable)

class MyCar(Car):
    def hexcolor(self):
        if self.color == 'red':
            return "#ff0000"
        else:
            return "#000000"

mycar_class = MyCar('Red',1234)
print(mycar_class)
print(mycar_class.color) #Works as usual like extending the Car and adding properties/functions

#To extend the namedtuple used ._fields as below
ElectricCar = namedtuple('ElectricCar',Car._fields + ('charge','Make','Country'))
elc = ElectricCar('Blue',500,4,'Audi','Germany')
print(elc)

#Usually naming with _ as prefix means its a local variabe and not a part of public class/interface. But thats the opposite for namedtuples
#Namedtuples helper methods start with _ only and are part of public class/interface.
#_asdict() returns as Dict

print(json.dumps(my_car._asdict())) #For JSON op

#_replace() inplace func creates a shallow copy and selectively replaces some of its fields
print(my_car._replace(color='White'))

#_make() classmethod creates new instances from a sequence or iterable
print(Car._make(['Hello',999]))
