# parese JSON with python

import json

# create sample json
userJSON = '{"first_name": "John", "age": 21}'

# parse json
user = json.loads(userJSON)
print(user)
print(user['first_name'])

# take dictionary to JSON
car = {'make': 'Honda', "year": 1989}
carJSON = json.dumps(car)

print(carJSON)
