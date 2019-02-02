# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

## Create function
def sayHello(name = 'you there!'):
    print(f'Hello {name}')

sayHello('Henry Harper')
sayHello()
sayHello(4)

## Return Values
def getSum(num1, num2):
    total = num1 + num2
    return total

answer = getSum(3, 7)
print(answer)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getDifference = lambda num1, num2 : num1 - num2
answer = getDifference(15, 12)
print(answer)
