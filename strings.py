name = "John"
age = 26

# concat 
print('Hello my name is ' + name + ' and I am ' + str(age))

# string formatting

print('My name is {nameplaceholder} and I am {ageplaceholder}'.format(nameplaceholder=name, ageplaceholder=age))

# using f-string (version 3.6 and after)
print(f'I am {age} years old')

# string methods
s ="george washington"

print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.replace('washington', 'smith'))

# count instances of substring
sub = 'g'
print(s.count(sub))

# split words into list
print(s.split())

# find position (zero-based)
print(s.find('e'))

# is alphanumeric (space is not alpha!!)
print(s.isalnum())

# is alpha
print(s.isalpha())

# is isnumeric
print(s.isnumeric())

