# tuple - collection, unchangeable, allows dupes

'''
When to use tuples vs list?

Apart from tuples being immutable there is also a semantic distinction that should guide their usage. 
Tuples are heterogeneous data structures (i.e., their entries have different meanings), 
while lists are homogeneous sequences. Tuples have structure, lists have order.
Using this distinction makes code more explicit and understandable.

One example would be pairs of page and line number to reference locations in a book, e.g.:

my_location = (42, 11)  # page number, line number

https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples
'''

# create tuple - use parenthese 
fruits  = ('apples', 'oranges', 'grapes')

print (type(fruits))
print (fruits)

# if only one item and no trailing comma, type will be string
test_tuple = ('orange')
print (test_tuple, type(test_tuple))

# always use trailing comma if you want to make tuple with single item
test_tuple = ('orange',)
print (test_tuple, type(test_tuple))

# get a value - zero-based
print(fruits[1])

# cannot change value
# fruits[0] = 'something else' # TypeError: 'tuple' object does not support item assignment

# delete entire tuple
del test_tuple
#print (test_tuple)

# length 
print(len(fruits))

# SETS - collection of unordered and unidexed. No dupes.

#create set (use curly braces)
fruits_set = {'Apples', 'Oranges', 'Mango'}


# check if element is in set 
print ('Apples' in fruits_set)

# add to set 
fruits_set.add('grape')
print(fruits_set)

# remove from set (will throw error if element not found)
fruits_set.remove('grape')
print(fruits_set)

# clear set 
fruits_set.clear()
print(fruits_set)

# delete set 
del fruits_set
