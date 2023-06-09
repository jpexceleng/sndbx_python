# collections in python:
# -

# iterating over a collection
# ----------------------------------------------------------------------------
# use the items() method to access items in a collection:
users = {'0987': 'active', '1987': 'inactive', '2898': 'active'}
for user, status in users.items():
    print(user, status)


# modifying items while iterating 
# ----------------------------------------------------------------------------
# can be tricky. best done by either...

# (Method 1) iterating over a copy of the collection:
users = {'0987': 'active', '1987': 'inactive', '2898': 'active'}
for user, status in users.copy().items():
    if (status == 'inactive'):
        del users[user] # delete the item from original collection

print(users)

# Or (Method 2) by creating a new collection:
users = {'0987': 'active', '1987': 'inactive', '2898': 'active'}

active_users = {}
for user, status in users.items():
    if (status == "active"):
        active_users.append

print(active_users)