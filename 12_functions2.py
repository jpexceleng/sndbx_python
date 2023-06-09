

# default argument values
# ----------------------------------------------------------------------------
# - since no default value assigned to arg_1, arg_1 is required
# - remaining 
def confirm_ok(prompt, retries=3, reminder="Try again!"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
# 'in' keyword tests whether a value is contained in a sequence.


# different ways of calling this function:
# ----------------------------------------------------------------------------
# confirm_ok()        # <-- ERROR! 'prompt' arg is required!
confirm_ok("Ok?")   # <-- using default args
confirm_ok("Are you sure?", 2, "Oops!")
confirm_ok(prompt="Really?", reminder="Oh no!")


# default value is evaluated only once:
# ----------------------------------------------------------------------------
def f(a, L=[]):
    L.append(a)
    return L

print(f(1)) # prints [1]
print(f(2)) # prints [1, 2]
print(f(3)) # prints [1, 2, 3]


# to prevent default from being shared between subsequent calls, use this:
# ----------------------------------------------------------------------------
def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f2(1)) # prints [1]
print(f2(2)) # prints [2]
print(f2(3)) # prints [3]