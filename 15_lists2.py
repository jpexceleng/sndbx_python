# more on lists

# declare an empty list
ls = []

# append an element to the list
ls.append('a')

# retrieve element by index
a = ls[0]

# extend the list with another list
other_ls = ['b', 'c', 'e']
ls.extend(other_ls)

# insert element at a specific index in the list
ls.insert(3, 'd')

# remove a single occurrence of the specified element starting from the
# beginning of the list:
ls.remove('a')

# remove an element by index
del ls[0]

# pop element from end of list
a = ls.pop()

# count number of occurrences of a specific element in list
b = ls.count("b")

# determine number of elements in list
num = len(ls)

# clear elements from list
ls.clear()

# reverse elements in the list
ls.reverse()

# a list can contain different data types
ls = [None, "this is a string", 1, 5.9, True] 