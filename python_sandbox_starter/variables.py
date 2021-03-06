# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1           # int
y = 2.5         # float
name = 'Brian'  # str
  # can be either single or double quotes
is_cool = True  # bool
  # Capital 'T' for True, and 'F' for False

a, b, title, is_rad = (1, 2.5, 'Brian', True)
  # same as above, minus variable names, just compact

print('Hello World')
print('Hello', a, b, title, is_rad)

print(type(x))

x = str(x)
print(type(x), x)

z = float(x)
print(type(z), z)