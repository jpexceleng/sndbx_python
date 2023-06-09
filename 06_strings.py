# basics of strings
# - immutable (need a different string? make a new one)
# - is a sequence   

# ----------------------------------------------------------------------------
# string declaration
s1 = 'string with single quotes'
s2 = "string with double quotes"


# ----------------------------------------------------------------------------
# use '\' to escape special symbols (e.g. \n is newline)
s3 = "\"Hello\", they said."


# ----------------------------------------------------------------------------
# interpret as raw strings by prefixing strings with 'r':
s4 = 'C:\some\name' # \n is interpreted as newline character
s5 = r'C:\some\name' # escape character ignored.


# ----------------------------------------------------------------------------
# use '+' for concatenation
s6 = "this is a"
s7 = " string"
print(s6 + s7)


# ----------------------------------------------------------------------------
# access characters of a string by index:
word = 'python'
print(word[0]) # prints 'p'
print(word[-1]) # prints 'n'

# think of indices as being between values:
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1

# use slicing to obtain substring:
# NOTE: should read [<included>:<excluded>]
print(word[:3]) # prints 'pyt'
print(word[2:4]) # prints 'th'

# python strings are immutable:
# word[3] = 'e' # <-- ERROR! 

# accessing index outside of range:
# print(word[100]) # <-- ERROR!
print(word[0:100]) # <-- this is fine.

# use len() method to determine length of a string:
print(len(word)) # 6