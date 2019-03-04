# List is a collection like JS array, allows dupes

# create list
numbers = [5,3,1]
fruits = ['apples', 'oranges', 'grapes', 'bananas']
print (type(fruits))

# using constructor
numbers2 = list((4,7,3))

print(numbers, numbers2)

# get value 
print(fruits[2])

# get length 
print(len(fruits))

# append to end list 
fruits.append('papaya')
print(fruits)

# remove from list 
fruits.remove('grapes')
print(fruits)

# insert to specific position
fruits.insert(1, 'pear')
print(fruits)

# remove from position
fruits.pop(0)
print(fruits)

# change value
fruits[0] = 'strawberries'

# reverse list 
fruits.reverse()
print(fruits)

# sort alpha
fruits.sort()
print(fruits)

# reverse sort 
fruits.sort(reverse=True)
print(fruits)



