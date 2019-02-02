# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

fruits = ('apples', 'oranges', 'grapes') 
fruits2 = tuple(('apples', 'oranges', 'bananas'))

print(fruits, fruits2)

## Single value needs trailing comma to be a tuple
fruits3 = ('bananas')
print(type(fruits3))


fruits3 = ('bananas',)
print(type(fruits3))

print(fruits[1])

## Can't change a tuple value
# fruits[1] = 'peaches'

## Delete a tuple
del fruits2
# print(fruits2)

## Length of tuple
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

## Create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}

## Check if in set
print('Apples' in fruits_set)

## Add to set
fruits_set.add('Grapes')
print(fruits_set)

## Remove from set
fruits_set.remove('Grapes')
print(fruits_set)

## Clear set
fruits_set.clear()
print(fruits_set)


## Delete set
del fruits_set
#print(fruits_set)