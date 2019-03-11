# almost everything in python is an object

# create class


class User:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def increase_age(self):
        self.age += 1


# create object
user1 = User('Jill', 24)
print(user1.name, type(user1))

# call class method
print('*******')
print(user1.age)
user1.increase_age()
print(user1.greeting())
print(user1.age)

# extend class

print('*******')


class Customer(User):
    def __init__(self, name, age):
        User.__init__(self, name, age)
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


james = Customer('James', 53)
print(james.greeting())
print(james.balance)
james.set_balance(132.44)
print(james.balance)
