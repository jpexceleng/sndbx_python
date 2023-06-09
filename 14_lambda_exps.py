
# lambda expressions
# ----------------------------------------------------------------------------
# - syntactically restricted to single expression
# - syntax reminds me of how mathematical sequences are described in language

#  returns a lambda expression
def make_incrementor(n):
    return lambda x: x + n

# variable f is assigned a lambda function
f = make_incrementor(42)
print(f(0))
print(f(1))