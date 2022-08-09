#4.5 - Abstract Base Classes keep Inheritance in Check

#ABCs (Abstract Base Classes) make sure that derived classs implments particular methods from base class

#Sometimes we might forget to implement any sub class methods derived from base classes. In that case the op may not be correct

class BaseClass:
    def foo(self):
        return "Base foo()"

    def bar(self):
        return "Base bar()"

class DerivedClass(BaseClass):
    def foo(self):
        return "foo() overridded"

    #def bar(self):
    #    return "bar() overridded"

b = BaseClass()
print(b.foo())
print(b.bar())

c = DerivedClass()
print(c.foo())
print(c.bar()) # --> We forgot to implement dervied bar() method hence it is calling the base bar() method which is wrong

#Downsides -
#1 - We can instantiate base class without any error
#2 - Provide incomplete subclass, instatiating DerivedClass() does not throw error since one of the derived class method not implemented


from abc import ABCMeta, abstractmethod

class BaseCl(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        return "Base Class foo()"

    @abstractmethod
    def bar(self):
        return "Base Class bar()"

class DerivedCl(BaseCl):
    def foo(self):
        return "foo() overridden"

    #def bar(self):
    #    return "bar() overridden"

#c = DerivedCl() --> line 52, in <module> c = DerivedCl() TypeError: Can't instantiate abstract class DerivedCl with abstract method bar
#b = BaseCl() --> line 53, in <module> b = BaseCl() TypeError: Can't instantiate abstract class BaseCl with abstract methods bar, foo

#The above errors prove to be valuable when working in derived class methods. Its only a debugging-aid not an alternative for complie time error

assert issubclass(DerivedCl,BaseCl) # --> No issues since derived class is correctly derived from base class
