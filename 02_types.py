# python supports the usual types as found in other programming languages.

# ----------------------------------------------------------------------------
# declare some variables:
a = True
b = 4
c = 3.4
d = "This is a string"

# ----------------------------------------------------------------------------
# you can use python's built-in type() method to determine a variable's type:
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'float'>
print(type(d))  # <class 'str'>

# ----------------------------------------------------------------------------
# how does the interpreter handle operations between two different data types?

# bool and float/int types? no problem:
result = a + b
print(result) # 5

result = a + c
print(result) # 4.4
# bool are really ints where False = 0 and True = 1.

# int and float types? no problem:
result = b + c
print(result) # 7.4

# str and int/float/bool type?
# result = a + d # <-- ERROR!
# result = b + d # <-- ERROR!
# result = c + d # <-- ERROR!
# str type is only compatible with str type.