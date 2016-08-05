[![Build Status](https://travis-ci.org/guillaumevincent/smartgetenv.svg)](https://travis-ci.org/guillaumevincent/smartgetenv)

# smartgetenv

version 0.1.0

smartgetenv is a python module that helps you to cast env variables.


```python
from smartgetenv import get_env, get_bool, get_list, get_float, get_int


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
```

all methods accept a default value as second parameter like default os.getenv method.

```python
from smartgetenv import get_env

name = get_env('UNSET_ENV_VARIABLE', 'foo')
assert name == 'foo'
```


## Installation

Install it with pip:

    pip install smartgetenv

## API

#### get_env(variable_name[, default])
return env variable with `variable_name`. 

If `variable_name` is not set return default value. 

By default `Default` value is `None`.

#### get_bool(variable_name[, default])
return `variable_name` env variable and cast into a boolean

#### get_int(variable_name[, default])
return `variable_name` env variable and cast into an int

#### get_float(variable_name[, default])
return `variable_name` env variable and cast into a float

#### get_list(variable_name[, default, separator])
return `variable_name` env variable and cast into a list. 

Use `separator` to split `variable_name`

By default `separator` is equal to semicolon `;`.

## Test

run tests

    python test_smartgetenv.py

## License

MIT - See License file