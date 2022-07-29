#3.3 - The power of Decorators

#Decorators in Py are used extend and modify the behaviour of a callable(funcs,methods,classes) without permanently modifying the callable itself!

#General use cases -

# Logging
# Enforcing access control and auth
# Instrumentation and timing funcs
# Rate-limiting
# Caching

def null_dec(fun): #Decorator func since fun is callable and returns
    return fun

def greet():
    return "Hello"

#Both below will work but we are going to replace this with Decorator
g = null_dec(greet())
print(g)
g1 = null_dec(greet)
print(g1())

#Decorator
@null_dec
def greeting():
    return "Hello world"

print(greeting())

#@ immediately decorators at the definiton time

def uppercase(f): #uppercase is the decorator.
    def wrap(): #Closure
        org_res = f()
        mod_res = org_res.upper() #Behaviour of the decorator(uppercase) is modified when using this line
        return mod_res
    return wrap

@uppercase
def greet():
    return "Hey there"

print(greet())
#OR return wrap()
#print(greet)

#Only way to change the behaviour of the input func(uppercase) it decorates is to wrap the input func with closure(wrap)

#Uppercase(Decorator) is not permanently modified, the behaviour is only changed by calling a wrapper func.

#We can apply more than 1 decorator at a time. Py runs those from bottom to top

def strong(f):
    def wrap():
        return '<strong>'+ f() +'</strong>'
    return wrap

def emphasis(f):
    def wrap():
        return '<em>'+ f() +'</em>'
    return wrap

@strong
@emphasis
def greet():
    return "Multiple decorators"

print(greet())

#Decorators take in arguments using args, kwargs

#The wrapper closure collects all positional arguments and keyword arguments through * and ** and stores them in variables args and kwargs

#It returns the stored arguments to the original func through * and ** "argument unpacking"

def trace(f):
    def wrapper(*args, **kwargs):
        print(f"Trace: calling {f.__name__}()"
              f" with {args}, {kwargs}")
        org_res = f(*args,**kwargs)
        print(f"Trace: {f.__name__}()"
              f" returned {org_res!r}") #!r is used to represent single quotes in o/p
        return org_res
    return wrapper

@trace
def say(name,title):
    return f'{name} {title}'

print(say("Koushik","Mr."))

#While using dec, the org func name, docstring, parameter are hidden by wrapper closure

@uppercase
def grt():
    '''This func return the string'''
    return "Docstring ex"

print(grt())
print(grt.__doc__) #Doesn't return any Docstring so hidden. Hence use the built-in functools.wraps
print(grt.__name__)

import functools
def up(f):
    @functools.wraps(f)
    def wrap():
        return f().upper()
    return wrap

@up
def greeting():
    '''Returns wrapper from functools docstring'''
    return "Wrapper from functools"

print(greeting())
print(greeting.__doc__)
print(greeting.__name__)