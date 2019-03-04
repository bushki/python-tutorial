'''
Multi line comment
'''
x= 1 # cast as int by default
y = 2.5 # floating point
name = 'john' #str 
is_programmer = True # bool

# multiple assignment
x, y, name, is_programmer = (10,98.6, 'smith', False)

# output 
print ('hello python')
print (name)
print (x,y,is_programmer)

# math 
a = x+y
print (a)

# check type
print(type(a))

# casting / conversion 
print('casting')
y = int(y)
z = float(y)
print('type and value', type(z), z)

print(type(x))
x = str(x)
print(type(x))
