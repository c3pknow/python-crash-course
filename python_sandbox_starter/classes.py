# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

## Create a class

class User:
    
    ### Constructor (uses `self` instead of `this`)
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    ### Methods in a class take in `self`
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old.'

    def hasBirthday(self):
        self.age += 1

## Init user object
brad = User('Rad Brad', 'radbrad@microsoft.com', 37)
print(type(brad))

print(brad.name)
print(brad.email)
print(brad.greeting())

brad.hasBirthday()
print(brad.greeting())

## Extend a class - pass the base class in as a parameter
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old and my balance is {self.balance}.'

## Init Customer
janet = Customer('Janet Milhouse', 'janetm@microsoft.com', 33)

janet.setBalance(552)
print(janet.balance)
print(janet.greeting())

janet.hasBirthday()
print(janet.greeting())