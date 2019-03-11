# dictionary is unordered, changeable and indexed. No dupes allowed.

# create dictionary
person = {
    'first_name': 'John',
    'last_name' : 'Smith',
    'age': 31
}

print(person,  type(person))

# use constructor 
person2 = dict(first_name = 'Jane', last_name='Brown')
print(person2,  type(person))

# get value
print(person['first_name'])
print(person.get('last_name'))

# add key/value
person['phone'] = '555-123-4567'
print(person)

# get dict keys
print(person.keys())

# get dict items
print(person.items())

# copy dict
person3 = person.copy()
person3['city'] = 'Los Angeles'
print(person3)

# remove item
del(person['age'])
print(person)

person.pop('first_name')
print(person)

# clear 
person.clear()
print(person)

# list of dicts
people =  [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 13},
]

print(people)

# get name of first person
print(people[1]['name'])