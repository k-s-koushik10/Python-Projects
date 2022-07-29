#2.5 - String Formatting

#Below are 4 ways to format a sting -

#1. % operator used in Py 2

name = "Bob"
errno = 50159747054
print("The name is %s" %name)
print("There is an error at 0x%x" %errno)

#2. .foramt() style

name ="Henry"
errno = 50159747054
print("The name is {}".format(name))
print("There is an error at 0x{errno:x}".format(errno=errno))

#3. f-string style

name = "Marcus"
errno = 50159747054
print(f"The name is {name}")
print(f"Sum : {2+3}")
print(f"There is an error at {errno:#x}")

#4. Template string style

name = "Zeus"
errno = 50159747054
from string import Template
t = Template("The name is $name")
print(t.substitute(name=name))
print(t)
temp_str = Template("There is an error at $errno")
print(temp_str.substitute(errno=hex(errno)))
print(temp_str)

#Point to remember - If our string is user-supplied, we can use Template strings to avoid security issues else we can use f string style



