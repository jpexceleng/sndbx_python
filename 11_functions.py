

# function declaration
# ----------------------------------------------------------------------------
# - declared using 'def' keyword
# - docstring is optional and must be first statement in function
def fib(n):
    """Prints fibonacci series up to n. """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# call the function
# ----------------------------------------------------------------------------
fib(2000)


# function return value
# ----------------------------------------------------------------------------
# function doesn't explicitly use the 'return' keyword, but still returns 
# "None"
x = fib(0)
# print(x) # returns 'None'


# read function's documentation string
# ----------------------------------------------------------------------------
print(fib.__doc__)