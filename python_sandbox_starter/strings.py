# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brian'
age = 38

# Concatenate
print('Hello, ' + name + '.  You are ' + str(age) + ' years old.' )

# String Formatting

## Positional arguments
print('My name is {name} and I am {age} years old.'.format(name=name, age=age))

## F-Strings (Python v3.6+)
print(f'Hello, my name is {name} and I am {age} years of age.')



# String Methods

s = 'hello world'

## Capitalize
print(s.capitalize())

## Swap Case
print(s.swapcase())

## To Upper
print(s.upper())

## To Lower
print(s.lower())

## String Length
print(len(s))

## Replace
print(s.replace('world', 'everyone'))

## Count
letter = 'o'
print(s.count(letter))

## Starts With
print(s.startswith('hello'))

## Ends With
print(s.endswith('world'))

## Split into a list
print(s.split())

## Find Position
print(s.find('r'))

## Is all alphanumeric
print(s.isalnum())   # returns False because of space (' ')

## Is all alphabetic
print(s.isalpha())  # returns False because of space (' ')

## Is all numeric
print(s.isnumeric())



