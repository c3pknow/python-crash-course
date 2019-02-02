# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

## Sample JSON

userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

## Parse to dictionary
user = json.loads(userJSON)
print(user)

## Get item
print(user['first_name'])


car = {'make': 'Subaru', 'model': 'Outback', 'year': 2016}
carJSON = json.dumps(car)
print(carJSON)