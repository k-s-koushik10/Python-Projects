#4.7 - Class VS Instance variables pitfalls

#Class variables are declared inside class definition. They are not tied to any instance of class.
#The class variables store their contents in the class itself and all objs created from a particular class share access to the same set of class variables.
#Hence is a class variable is changed, it affects all obj instance.

#Instance variables are declared as a part of obj instance. They are not stored on the class, they are stored on each individual obj created from class.
#The contents of obj variable are completely independent to other obj variables. Modifying an instance variable affects that particular obj only.

class Dog:
    num_legs = 4 #Class variable

    def __init__(self,name):
        self.name = name #Instance variable

my_dog_1 = Dog('Rufus')
my_dog_2 = Dog('Puppy')
print(my_dog_1.name)
print(my_dog_2.name)

print(my_dog_1.num_legs)
print(my_dog_2.num_legs)
print(Dog.num_legs)

#print(Dog.name) --> AttributeError: type object 'Dog' has no attribute 'name'

Dog.num_legs = 6 #Updating the class variable

print(Dog.num_legs)
print(my_dog_1.num_legs)
print(my_dog_2.num_legs)

#Modifying a class variable on the class namespace 'Dog' affected all class variables

Dog.num_legs = 4
my_dog_1.num_legs = 6

print("<---After modifying Class variable--->")
print(Dog.num_legs)
print(my_dog_1.num_legs)
print(my_dog_2.num_legs)
print(my_dog_1.__class__.num_legs)
print("<------>")

class CountObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances+= 1

print(CountObject.num_instances)
print(CountObject.num_instances) #Gives 0 only since we are not calling the init constructor
print(CountObject().num_instances)
print(CountObject().num_instances)
print(CountObject().num_instances)
print(CountObject.num_instances) #Final result will be 3 not 0 since it returns num_instances obj variable

class DupCountObject:
    num_instance = 0

    def __init__(self):
        self.num_instance+= 1

print(DupCountObject.num_instance) #0
print(DupCountObject().num_instance) #1
print(DupCountObject().num_instance) #No incrementation
print(DupCountObject().num_instance) #No incrementation
print(DupCountObject.num_instance) #Returns 0 since the class variable num_instance was shadowed by creating an instance variable of the same name of constructor
#The counter works but then stores the result in an instance variable, which means other instance of the class never see the updated counter value
