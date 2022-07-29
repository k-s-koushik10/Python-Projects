#2.4 - Underscores, Dunders and More

#1. Single leading Underscore - _name --> Hint to programmer that its for internal use. Defined as per PEP8 convention. Py Interpreter will work as it is.

#Variables
class LeadUnderScore:
    def __init__(self):
        self.bar = 10
        self._foo = 42

l = LeadUnderScore()
print(l.bar)
print(l._foo) #Works as usual in Py

#Methods
'''
Under my_module.py -->
def _internal_func(self):
    pass

main.py -->
from my_module import * --> Usually * (Wild card imports) are not recommended
print(_internal_func()) --> Error name _internal_func() not defined

Alternative -->
import my_module
my_module._internal_func() --> Func will be fetched
'''

#2. Single trailing Underscore - name_ --> Used only when there is already a Py keyword present. Py Interpreter will work as it is.

class TrailUnderScore:
    def __init__(self):
        self.class_ = 100
        self.not_ = 101

t = TrailUnderScore()
print(t.class_)
print(t.not_)

#3. Double leading Underscore - __name --> Causes Py interpreter to rewrite attribute name to avoid naming conflict with its own subclass. Concept known as "Name Mangling".

#Ex 1
class Test:
    def __init__(self):
        self.foo = 10
        self._bar = 100
        self.__baz = 1000

t = Test()
print(t.foo)
print(t._bar)
#print(t.__baz) --> Error since Py has done Name Mangling
print(dir(t))
print(t._Test__baz) #Correct convention

class Extend(Test):
    def __init__(self):
        super().__init__()
        self.foo = "overridden"
        self._bar = "overridden"
        self.__baz = "overridden"

et = Extend()
print(et.foo)
print(et._bar)
#print(et.__baz) --> Error since Py has done Name Mangling
print(dir(et))
print(et._Extend__baz) #Correct convention

#Ex 2
class Mangling:
    def __init__(self):
        self.__mangle = "hello"

    def mang(self):
        return self.__mangle

print(Mangling().mang())
#print(Mangling().__mangle) --> Error since Py has done Name Mangling

#Ex 3
class Mang:
    def __meth(self):
        return 42

    def call_it(self):
        return self.__meth()

print(Mang().call_it())
#print(Mang().__meth()) --> Error since Py has done Name Mangling

#Ex 4
_Mangled__mangling = 25

class Mangled:
    def test(self):
        return __mangling

print(Mangled().test())

#4. Double leading and trailing Underscore - __name__ --> Works as usual in Py interpreter but usually reserved for special methods like __init__, __call__

class LeadAndTrailUnderSc:
    def __init__(self):
        self.__bam__ = 16

print(LeadAndTrailUnderSc().__bam__)

#5. Single Underscore - _ --> Used as stand-alone to indicate its temproary or insignificant

#Ex 1
for _ in range(5):
    print("Hello")

car = ('Red',12,13,20,1000)
color,_,_,mileage,km = car

#Ex 2
print(color)
print(_)

#Ex 3
print(50+5)
print(_)