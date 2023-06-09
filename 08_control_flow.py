# control flow statements


# if statements
# ----------------------------------------------------------------------------
if (3 > 8):
    print("3 is greater than 8.")
else:
    print("3 is less than or equal to 8.")


# for statements
# ----------------------------------------------------------------------------
# python for iterates over items of any sequence in the order that they 
# appear in the sequence
nums = [3, 5, 2, 6]
for n in nums:
    print(n)
    
# iterating over a collection
users = {'0987': 'active', '1987': 'inactive', '2898': 'active', '3285': 'inactive'}
for user, status in users.items():
    print(user, status)
# NOTE: reading is simple; modifying elements in a collection is tricky. best 
# done by either...

# (1) iterating over a copy of the collection
for user, status in users.copy().items():
    if (status == 'inactive'):
        del users[user] # delete the item from original collection

print(users)

# or (2) creating a new collection
