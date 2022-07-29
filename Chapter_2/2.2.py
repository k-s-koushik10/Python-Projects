#2.2 - Complacent Comma Placement - works for Lists, Sets, Dictionaries

#Lets take a list of names as below and try to add a name at last

#1
names = [
    'Alice',
    'Bob',
    'Ceaser'
]

print(names)

#2
names = [
    'Alice',
    'Bob',
    'Ceaser'
    'James'
]

print(names)
#The names dont add properly and merge
#The above is called string literal concatenation and useful only when we are typing multiple lines

#3 Below is new solution
names = [
'Alice',
    'Bob',
    'Ceaser',
]

print(names)

#4 Name added correctly now
names = [
'Alice',
    'Bob',
    'Ceaser',
    'James'
]

print(names)