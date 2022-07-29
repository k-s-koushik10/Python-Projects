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
