#4.4 - Cloning objects for Fun and Profit

#For immutable obj, copying the objs means they dont create a copy of objs, they mearly bind names to the obj

#But for mutable obj like lists, dicts, sets shallow copy and deep copy can be used

#Shallow copy - Constructing a new collection obj and populating it with reference to the child obj found in original.

#Shallow copy is only one level deep and they do not recurse, hence they do not create copies of the child obj themselves.

#Deep copy - Constructiong a new collection obj and then recursvely populating it with copies of the child objs found in original.

#Deep copy is two levels deep and they recurse, hence copying this way walks the whole object tree to create a fully independent clone of the original and all of its children.

#Shallow copy ex-
#We can use copy.copy() or just use list, dict, sets as usual

xs = [[1,2,3],[4,5,6],[7,8,9]]
ys = list(xs) #Shallow copy

print(xs)
print(ys)

xs.append(['Extra'])

print(xs) #Org Child obj
print(ys)

xs[1][0] = 10

print(xs)
print(ys) #The changes made to org is reflected since the references of xs are copied to ys
#Both lists share the same child obj

xs.append(['New list'])

print(xs)
print(ys) #No change since new reference is created at last

#Deep copy ex-

import copy

xd = [[1,2,3],[4,5,6],[7,8,9]]
yd = copy.deepcopy(xd)

print(xd)
print(yd)

xd.append(['Extra'])
#Works as usual

print(xd) #Org Child obj
print(yd)

xd[1][0] = 10

print(xd)
print(yd) #No change in zs since they are independent

xd.append(['New list'])

print(xd)
print(yd) #No change

#Copying arbitary values

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x!r}, {self.y!r})"

a = Point(5,6)
b = copy.copy(a)

#Here the point obj uses immutable types ints for the coordinates, so anyways there is no difference between shallow and deep copy
print(a)
print(b) #Same op as a

class Rect:
    def __init__(self,tl,br):
        self.tl = tl
        self.br = br

    def __repr__(self):
        return f'{self.__class__.__name__}({self.tl!r},{self.br!r})'

rec = Rect(Point(0,1),Point(10,20)) #Overrides the Point __repr__
srect = copy.copy(rec)

print(f"Child --> {rec}")
print(f"Shallow --> {srect}")

drect = copy.deepcopy(rec)

print(f"Child --> {rec}")
print(f"Deep --> {drect}")

rec.tl.x = 50 #Changing to check ex

print("----After changing coordinates of child----")
print(f"Child --> {rec}")
print(f"Shallow --> {srect}")
print(f"Deep --> {drect}")

print("----After changing coordinates of deep----")
drect.tl.x = 299
print(f"Child --> {rec}")
print(f"Shallow --> {srect}")
print(f"Deep --> {drect}")

#If we change the child obj, it wont reflect in Deep similarly if we change deep obj, child and shallow wont reflect

#We can also use __copy__() and __deepcopy__()