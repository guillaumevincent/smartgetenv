import os

from smartgetenv import get_env, get_bool, get_list, get_float, get_int

os.environ['NAME'] = 'Guillaume'
os.environ['AGE'] = '30'
os.environ['WEIGHT'] = '80.2'
os.environ['HOBBIES'] = 'diving;making software'
os.environ['DEBUG'] = 'False'

# try to get env variable
# NAME="Guillaume"
user = get_env('NAME')
assert user == 'Guillaume'

# try to get env variable and cast into an int
# AGE="30"
age = get_int('AGE')
assert age == 30

# try to get env variable and cast into a float
# WEIGHT="80.2"
weight = get_float('WEIGHT')
assert weight == 80.2

# try to get env variable and cast into an list
# HOBBIES="diving;making software"
hobbies = get_list('HOBBIES')
assert hobbies == ['diving', 'making software']

# try to get env variable and cast into a boolean
# DEBUG="False"
debug = get_bool('DEBUG')
assert debug is False

name = get_env('UNSET_ENV_VARIABLE', 'foo')
assert name == 'foo'
