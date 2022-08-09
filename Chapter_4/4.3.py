#4.3 - Defining your own Exception Classes

#When we use bulit-in exceptions, it might be hard to debug, hence using custom exception classes can be used

def validate(name):
    if len(name) < 10:
        raise ValueError

#print(validate('Koushik')) --> line 7, in validate raise ValueError ValueError. Hard to debug for others.from

class NameTooShortError(ValueError):
    pass

def val(name):
    if len(name) < 10:
        raise NameTooShortError(name)
    else:
        print(name)

#print(val('Koushik')) --> line 16, in val raise NameTooShortError(name) __main__.NameTooShortError: Koushik

#the above exception is well defined and easy to debug

print(val('Hello World'))

#Trying to create and use a custom exception Base class and deriving the exceptions from it will be helpful and easier to maintain

class BaseCustomException(ValueError):
    pass

class NameTooShort(BaseCustomException):
    pass

class NameTooLong(BaseCustomException):
    pass

#name = "Koushika" --> line 43, in validateName raise NameTooShort(name) __main__.NameTooShort: Koushika
#name = "Koushikkoushik" --> line 46, in validateName raise NameTooLong(name) __main__.NameTooLong: Koushikkoushik
name = "Koushik"

def validateName(name):
    if len(name) == 7:
        print(name)
    elif len(name) < 10:
        raise NameTooShort(name)
    elif len(name) > 10:
        raise NameTooLong(name)

try:
    validateName(name)
except BaseCustomException as err:
    raise BaseCustomException(err)