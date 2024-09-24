# What is `None` in Python?
#- `None` is a constant in Python that represents the absence of a value or a null value.
# It is an object of its own datatype 'NoneType'."


#  When is it Commonly Used?
# - As a **default return value** for functions that don’t explicitly return anything.
# - In optional arguments of functions to signify that no argument was provided.
# - To initialize variables that may later hold a value.
# - As a placeholder in data structures or algorithms to denote "no value."


# Equivalent in Other Programming Languages:
# - In other languages, `None` is similar to:
#   - 'null' in Java, JavaScript, and C#
#   - 'nil' in Ruby and Swift
#   - 'NULL' in SQL
#   - 'undefined' in JavaScript


# What Happens When You Convert `None` to a Boolean?
#- When `None` is converted to a boolean, it evaluates to `False`.

if not None:
    print('False')
