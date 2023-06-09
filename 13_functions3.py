# special function parameters

# arbitrary argument lists
# ----------------------------------------------------------------------------
# *name maps to a tuple
# **name maps to a dictionary

def f(*args, **keywords):
    for arg in args:
        print(arg)
        
    for key in keywords:
        print(key, ":", keywords[key])

# function is called like so: 
f(1, 2, 3, 4, 5, a=897, b=98273, c=93875, d=938757)
# where:
# - "1, 2, 3, 4, 5" make up the args tuple and
# - "a=897, b=98273, c=93875, d=938757" makes up keywords dictionary


# unpacking argument lists
# ----------------------------------------------------------------------------
# - if you want to pass a list/tuple to a function that takes an argument
#   list, you must unpack it first using "*" or "**".
ls = [98, 97, 96]
dic = {"a": 101, "b": 102}
f(*ls, **dic)


# indicating parameter kind
# ----------------------------------------------------------------------------
# - args before '/' are positional-only parameters 
# - args after '*' are keyword-only parameters
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# combined_example(1, 2, 3) # ERROR!
# combined_example(1, 2, kwd_only=3) # ok
combined_example(1, standard=2, kwd_only=3) # ok
# combined_example(pos_only=1, 2, kwd_only=3) # ERROR! positional arg can't appear
                                            # after a keyword arg