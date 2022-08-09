#4.2 - String conversion (Every Class needs a __repr__)

class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage

my_car = Car('Blue',500)
print(my_car) #Prints the obj memory address in CPython
print(my_car.color,my_car.mileage)

#We can use __str__ and __repr__ in the above ex

class MyCar:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return f'{self.color} car'

my_car = MyCar('Red',1000)
print(my_car) #Fetched __str__ method
print(str(my_car))
print('{}'.format(my_car))

class ReprMyCar:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return '__str__ of class'
    def __repr__(self):
        return '__repr__ of class'

reprcar = ReprMyCar('Black',100)
print(reprcar)
print(str([reprcar])) #Fetches repr since lists and dicts always use the result of repr to represent the obj
#reprcar --> This works only in Py interpreter
print(repr(reprcar))

import datetime
today = datetime.date.today()
print(today)
print(str(today)) #O/P not very useful
print(repr(today))

class ReprMyCarClass:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
    def __repr__(self):
        return f'ReprMyCarClass holds ({self.color!r} color car,' \
               f'{self.mileage} mileage)' #!r is used for ''
myreprcar = ReprMyCarClass('White',5000)
print(myreprcar)
print(str(myreprcar)) #Even if str is not present, repr is printed by default of str

#Instead of using ReprMyCarClass name we can use __class__.__name__ in __repr__. Hence weven if the class name changes we dont have to modify the repr func

class ReprMyCarClassRe:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
    def __repr__(self):
        return f'{self.__class__.__name__} holds ({self.color} color car,' \
               f'{self.mileage} mileage)'
myreprcar1 = ReprMyCarClassRe('White',5000)
print(myreprcar1)
print(str(myreprcar1))
