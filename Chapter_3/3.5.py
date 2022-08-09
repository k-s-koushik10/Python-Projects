#3.5 - Function argument unpacking

#With *, ** we can also unpack the arguments from sequences, dict

def vector(x,y,z):
    return (f'<{x}>, <{y}>, <{z}>')

print(vector(1,2,3))

#If we are printing anything in 3D args, using tuple/list might be not the best choice

tup_vec = (1,0,1)
list_vec = [1,0,1]
print(vector(tup_vec[0],
             tup_vec[1],
             tup_vec[2]))

print(vector(list_vec[0],
             list_vec[1],
             list_vec[2]))

#Using * before an iterable in a func call will unpack the args and pass its elements as seperate positional args to the called funcs

print(vector(*tup_vec))
print(vector(*list_vec))

#Also can be used in generator exp

exp = (x*x for x in range(3))
print(exp)
print(*exp)

#For dicts like below

dict_keys = {'y':1,'z':3,'x':2}
print(vector(**dict_keys)) #With respect to keys (x,y,z)
print(vector(*dict_keys)) #With respect to positions (1st,2nd,3rd)

