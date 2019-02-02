# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1, 2, 3, 4, 5]
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)

# Index based lookup
fruits = ['apples', 'oranges', 'bananas', 'grapes']
print(fruits[1])

# Length of List
print(len(fruits))

# Append
fruits.append('mangoes')
print(fruits)

# Remove by name (remove) from list
fruits.remove('grapes')
print(fruits)

# Insert into specific position
fruits.insert(2, 'pineapple')
print(fruits)

# Remove by position (pop)
fruits.pop(3)
print(fruits)

# Reverse the list
fruits.reverse()
print(fruits)

# Sort the list (alphabetically)
fruits.sort()
print(fruits)

# Sort in reverse (reverse alphabetically)
fruits.sort(reverse=True)
print(fruits)

# Change a value
fruits[0] = 'blueberries'
print(fruits)
