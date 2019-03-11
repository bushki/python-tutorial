# python uses indentation (tabs or spaces) instead of curly braces

# create function 
def sayHello(name= 'Jim'): 
    print(f'Hello my name is {name}')

sayHello('Bob')
sayHello() # run with no argument

# return values
def getSum(num1, num2):
    total = num1+num2
    return total

print(getSum(1,2))
num = getSum(3,3)
print(num)

# lambda function is small anonymous functions
# similar to arrow functions in JS

getSumLambda = lambda num1, num2 : num1 + num2

print(getSumLambda(10,5))