# module is a file containing set of functions to include in your app
# there are core python modules, modules you can install using the pip package manager
# including django as well as custom modules

# import core module

#import datetime
# import just date
from validator import validate_email
from datetime import date
from time import time

# import Pip module
from camelcase import CamelCase

#today = datetime.date.today()
today = date.today()
print(today)

timeStamp = time()
print(timeStamp)

# pip install camelcase
# or py -m pip (if not in PATH in windows)
# see what is installed: py -m pip freeze

# use camelcase
c = CamelCase()
print(c.hump('hello there world'))

# import custom module
myEmail = 'test@b.com'
if(validate_email(myEmail)):
    print(f'{myEmail} is valid email')
else:
    print(f'{myEmail} is bad')
