#4.8 - Instance, Class and Static Methods Demystified

class MyClass:
    #Instance methods can modify the state of an obj state (through self) and class state (through self.__class__)
    def method(self): #self points to the instance of MyClass when the method is called
        return "Instance methods called", self

    #Class methods can modify the class state only
    @classmethod
    def classmethod(cls): #cls points to the class instance not obj instance
        return "Class methods called", cls

    #Static methods cannot modify any state
    @staticmethod
    def staticmethod():
        return "Static methods called"


obj = MyClass()
print(obj.method)
print(obj.method())
print(MyClass.method(obj)) #Can access obj instance
print(obj.__class__.__name__) #Can access Class instance

print(obj.classmethod()) #Can access Class instance only

print(obj.staticmethod())

print(MyClass.classmethod())
print(MyClass.staticmethod())
#print(MyClass.method()) --> TypeError: MyClass.method() missing 1 required positional argument: 'self'
print(MyClass.method('abc'))

class Pizza:
    def __init__(self,ing):
        self.ing = ing

    def __repr__(self):
        return f'Pizza({self.ing!r})'

    @classmethod
    def margherita(cls):
        return cls(['Cheese','Tomatoes']) #Using cls instaed of calling Pizza constructor directly

    @classmethod
    def prosciutto(cls):
        return cls(['Cheese', 'Tomatoes','Ham']) #margherita, prosciutto are called factory funcs

print(Pizza.margherita())
print(Pizza.prosciutto())

#@classmethod works the same way as that of __init__, but we can define more than one @classmethod but we can have only one __init__ in a class

import math
class PizzaTwo:
    def __init__(self,ing,rad):
        self.ing = ing
        self.rad = rad

    def __repr__(self):
        return f'PizzaTwo({self.ing!r} ingredients and {self.rad!r} radius)'

    def area(self):
        return self.circle_area(self.rad)

    @staticmethod
    def circle_area(r):
        return math.pi * r ** 2

p = PizzaTwo(['Tomatoes','Ham'],4)
print(p)
print(p.area())
print(p.circle_area(4))