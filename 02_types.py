# python supports the usual types as found in other programming languages.

# ----------------------------------------------------------------------------
# declare some variables:
var_str = "This is a string"
var_int = 4
var_float = 3.4
var_bool = True

# ----------------------------------------------------------------------------
# you can use python's built-in type() method to determine a variable's type:
print(type(var_str)) # <class 'str'>
print(type(var_int))    # <class 'int'>
print(type(var_float))  # <class 'float'>
print(type(var_bool))   # <class 'bool'>

# ----------------------------------------------------------------------------
# how does the interpreter handle operations between two different data types?

# no problem:
result = var_float + var_int
print(result)

# bool values False and True are interpreted as 0 or 1, respectively
result = var_bool + var_int
print(result)

# str can only be concatenated with str
# result = var_str + var_float # <-- produces error