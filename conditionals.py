
x = 5
y = 10

# simple IF
if x > y:
    print(f'{x}>{y}')

# IF ELSE
if x > y:
    print(f'{x}>{y}')
else:
    print(f'{y}>{x}')

# ELIF
if x > y:
    print(f'{x}>{y}')
elif x == y:
    print(f'{x}={y}')
else:
    print(f'{y}>{x}')

# nested IF
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

# logical ops (AND OR NOT)
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# NOT
if not(x == y):
    print(f'{x} is not equal to {y}')

# membership operators
numbers = [1, 2, 3, 5]

if x in numbers:
    print(x in numbers)

if y not in numbers:
    print(y in numbers)

# identity operators (is, is not)
# compare if objects are the same - same memory location

a = 20
b = a

if a is b:
    print(f'{a} is {b}')
