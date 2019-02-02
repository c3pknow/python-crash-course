# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

## Create a dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

other_person = dict(first_name='Sara', last_name='Williams')
print(person, type(person))
print(other_person, type(other_person))

## Get Value
print(person['first_name'])

print(person.get('last_name'))

## Add Key/Value
person['phone'] = '555-555-5555'
print(person)

## Get dictionary keys
print(person.keys())

## Get dictionary items
print(person.items())

## Copy a dictionary
different_person = person.copy()
different_person['city'] = 'Los Angeles'
print(different_person)

## Remove Item
del(person['age'])
print(person)

person.pop('phone')
print(person)

## Clear
person.clear()
print(person)

## Length
print(len(other_person))

# List of Dictionaries
people = [
    {'name': 'Martha', 'age': 28},
    {'name': 'Kevin', 'age': 25}
]
print(people)
print(people[1]['name'])