# basics of lists.
# - example of a 'compound' data type
# - are mutable
# - is a sequence

# ----------------------------------------------------------------------------
# declare a list
ls = [0, 99, 33, 85, 81]

# ----------------------------------------------------------------------------
# modify list element
ls[3] = 999

# ----------------------------------------------------------------------------
# index into list
i = ls[0]
i = ls[-5]

# ----------------------------------------------------------------------------
# slicing
ls = ls[:100]
ls = ls[-3:]

# ----------------------------------------------------------------------------
# append element to a list
ls.append(9873)

# ----------------------------------------------------------------------------
# assignment slicing
print(ls) 

ls[1:2] = [101, 102, 103] # clear the list
print(ls) 

# if number of elements in assignment is greater than assignment range, all
# values are inserted into the list
ls[1:3] = [104, 105, 106, 107, 108] 
print(ls) 

# ----------------------------------------------------------------------------
# clear a list
ls[:] = [] # clear the list

# ----------------------------------------------------------------------------
# find number of elements in list
num = len(ls)

# ----------------------------------------------------------------------------
# lists can be nested
ls1 = [1, 2, 3]
ls2 = ['a', 'b', 'c']
ls3 = [ls1, ls2]