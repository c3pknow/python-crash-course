# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

## Import core python module
import datetime
from datetime import date
import time


today = datetime.date.today()
print(today)

today2 = date.today()
print(today2)

timestamp = time.time()
print(timestamp)

from time import time
timestamp2 = time()
print(timestamp2)


## Import external module with PIP
# $ pip install camelcase   # Global install
# $ pip freeze              # Shows what is installed

from camelcase import CamelCase
c = CamelCase()
print(c.hump('hello there world, how are you today?'))


## Import custom module
from validator import validate_email
print(validate_email('john.doe@microsoft.com'))
print(validate_email('john.doe@!microsoft.com'))

