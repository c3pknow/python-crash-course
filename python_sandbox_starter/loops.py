# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Peter', 'Jonas']

## For loop
for person in people:
    print(f'Current Person: {person}')

print('\n')

## Break
for person in people:
    if person == 'Peter':
        break
    print(f'Current Person: {person}')

print('\n')

## Continue
for person in people:
    if person == 'Peter':
        continue
    print(f'Current Person: {person}')

print('\n')

## Range
for i in range(len(people)):
    print(people[i])

for i in range(2, 11):
    print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0

while count <= 10:
    print(f'Count: {count}')
    count += 1
