#3.1 - Python's functions are first-class

#Functions in Py are also objects and hence behave the same way as objects behave

def yell(name):
    return name.upper() +"!"

print(yell("Hello"))

bark = yell #Behaving like objects

print(bark("Hi"))

del yell

#print(yell("Hello")) --> NameError: name 'yell' is not defined, since deleted

print(bark("Hi there")) #Will pickup since obj reference of yell already passed to bark

print(bark.__name__) #Just a name identifier

funcs = [bark,str.lower,str.capitalize] #Can be passed like objects to a data structure (lists,set,dict)

print(funcs)

for f in funcs:
    print(f("Hello world"),f) #Just like passing an obj to a list

#Below need to check
#fin = (f for f in funcs)
#print(fin("Hey"))

print(funcs[0]("Hey Func")) #Also possible without assigning to a variable

#When functions are passed to other functions they are called as "Higher Order Functions", typical ex is Map function

def greet(fun):
    return fun("Hello, this is a greet func") #fun here is actually bark

print(greet(bark))

print(list(map(bark,["hello","hi","welcome"])))

#Funcs can be nested like below

def speak(text):
    def speaker(t):
        return (t.lower())
    return (speaker(text))

print(speak("HOW DO YOU DO?"))

#print(speaker("Hello")) --> NameError: name 'speaker' is not defined

#If we want to access the inner func outside the scope of func, we can follow -

def get_speak(volume):
    def whisper(text):
        return text.lower()+"!"
    def yell(text):
        return text.upper()+"!"
    if volume > 0.5:
        return yell
    else:
        return whisper

speak_fun = get_speak((0.3))
print(speak_fun)
print(speak_fun("Volume check"))

print(get_speak(0.7),"Volume hello") #Does not fetch the inner fun, hence need to assign to new variable like above

#Funcs can capture local state, they are called lexical closures/closures, since they can access the parent func's state (text) in the nexted func

def get_speak_sec(volume,text):
    def whisper():
        return text.lower()+"!"
    def yell():
        return text.upper()+"!"
    if volume > 0.5:
        return yell
    else:
        return whisper

print(get_speak_sec(0.8,"Sound check")()) #() is important since that only calls the func, else returns nothing

#Another ex

def make_add(x):
    def adder(n):
        return n-x #x is 3, n is 7
    return adder #return adder(x) shows 'int' object is not callable, even if we add int() in line 95

plus_add = make_add(3)
print(plus_add(7))

#Obj can behave like funcs

#All obj are funcs but obj are not funcs. Obj can be made callable using __call__ which treates them like funcs

class Adder:
    def __init__(self,n):
        self.n = n

    def __call__(self, x):
        return self.n - x #n is 4, x is 3

add_sum = Adder(4)
print(add_sum(3))

#We can check whether a func obj is callable or not from the __call__ using below callable func

print(callable(Adder))
print(callable(add_sum))
print(callable(bark))
print(callable("hello"))
