#3.6 - Nothing to Return here

#Py returns an implicit Return None at the end of a func. Hence we can declare None explicitly or do nothing to return.

#Therefore if a func returns no value, it will return None by default

def foo1(val):
    if val:
        return val
    else:
        return None

def foo2(val):
    if val:
        return val
    else:
        return

def foo3(val):
    if val:
        return val

print(foo1(0))
print(foo2(0))
print(foo3(0))
