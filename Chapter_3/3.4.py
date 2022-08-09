#3.4 - Fun with *args and **kwargs

#* args for positional arguments and ** kwargs for keyword arguments

#* args accepts positional arguments and stores as tuple

#**kwargs accepts keyword arguments and stores as dictionaries

#Both args and kwargs will be empty if no extra arguments are passed into them

def foo(req,*args,**kwargs):
    print (req)
    if args:
        print (args)
    if kwargs:
        print (kwargs)

#print(foo()) --> TypeError: foo() missing 1 required positional argument: 'req'
foo("Hello")
foo("Hello",1,2,3)
foo("Hello",1,2,3,key1='value',key2=999)

#* and ** are the keywords, instaed of args/kwargs we can use any name

#Usually used when we need to add/modify additional input outside of out scope

class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage

class AlwaysBlueCar(Car):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.color = 'Blue'

print(AlwaysBlueCar('Green',500).color)

#Here even if the behaviour of the parent class is changed, the sub class will function as usual

#But the downside is that we dont know which argument is to be passed without looking up to the parent class

import functools
def trace(f):
    @functools.wraps(f)
    def wrap(*args,**kwargs):
        print(f,*args,**kwargs)
        res = f(*args,**kwargs)
        return res
    return wrap

@trace
def names(title,name):
    return f'{title}. {name}'

print(names("Mr","Koushik"))