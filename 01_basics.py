# This is a comment.

""" This 
    is
    a
    multi-line
    comment.
"""

# ----------------------------------------------------------------------------
# This is a variable declaration. Values are assigned to variables using the 
# assignment operator '='.
string = "Hello, world!"

# Python is a "dynamically typed" language; means that there is no need for
# programmer to explicitly specify the data type before assigning a value to 
# a variable. The python interpreter automatically binds the type to its 
# variable.

# ----------------------------------------------------------------------------
# The following prints value of a variable to standard out:
print(string)

# ----------------------------------------------------------------------------
# Using python's built-in "id()" method we can determine the location in 
# memory a variable's value is stored:
print(id(string))