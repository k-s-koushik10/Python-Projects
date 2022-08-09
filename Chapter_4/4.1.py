#4.1 - Object comparison 'is' vs '=='

#'==' compares equality and 'is' compares identity

a = [1,2,3]
b = a
print(a)
print(b)
print(a == b) #Equal in values
print(a is b) #Both objs pointing to same one list obj

c = list(a)
print(c)

print(a == c)
print(a is c)

#'==' is True when the variables referred to by the obj are equal (same contents)
#'is' is True if the two vaiables point to the same(identical) object