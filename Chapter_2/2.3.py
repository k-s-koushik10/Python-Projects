#2.3 - Contect managers and "with" statement

#With is used to simplify common resource patterns by abstracting their functionality and allowing them to be factored out and reused

with open('hello.txt', 'w') as f:
    f.write("Hello World")

#Without "with" we ahve to use try/finally which is not recommended since "with" will automatically close the file once execution completed

#One of the main use cases of "with" is in "threading.Lock()"

#Context Managers are protocols that our obj needs to follow to support the "with" statement. They should have __enter__ and __exit__ methods

class ManageFile:
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name,'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManageFile('hello_world.txt') as f:
    f.write("This is new line\n")
    f.write("Bye")

#Using contexual managers with "contextlib"

from contextlib import contextmanager

@contextmanager
def manage(name):
    try:
        f = open(name,'w')
        yield f
    finally:
        f.close()

with manage('hello_new.txt') as f:
    f.write("This is Hello_New")



