#3.2 - Lambda's are single expression funcs

#Small anonymous funcs mostly used for whenever function objects are required

def add_func(x,y):
    return x+y

print(add_func(5,6))

print((lambda a,b: a+b)(4,5))

#Lambdas are restriccted to a single func, hence cannot use statements, annotations, returns

#But the output values of lambdas return with an implicit return statement, hence called single expression functions

tup = [(1,'d'),(2,'b'),(4,'a'),(3,'c')]
print(sorted(tup))
print(sorted(tup,key=lambda x:x[1]))
print(sorted(tup,key=lambda x:x[0]))

print(list(filter(lambda x:x*x, range(-5,6)))) #x*x wont work, since filter is used.
print(list(filter(lambda x:x%2==0, range(-5,6)))) #x%2==0 will work, since filter is used.
print(sorted(range(-1,3),key = lambda x:x-x)) #x-x wont work

#Lambdas work for lexical closures too similar to funcs

def adder(n):
    return lambda x: x-n #x is 5, n is 3

adding = adder(3)
print(adding(5))

#Below not recommended!
print(list(filter(lambda x:x%2==0,range(10))))

#Below is recommended!
print(list(x for x in range(10) if x%2==0))