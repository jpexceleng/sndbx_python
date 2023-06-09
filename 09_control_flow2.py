# control flow2


# break
# ----------------------------------------------------------------------------
# use break keyword to exit a for or while loop; similar to C/CPP
i = 5
while (True): # <-- infinite loop
    i -= 1
    if (i == 0):
        break


# continue
# ----------------------------------------------------------------------------
# continues with next iteration of for or while loop; borrowed from c
for i in range(100):
    if (i != 10):
        continue
    else:
        print(i)


# pass
# ----------------------------------------------------------------------------
# - does nothing.
# - use when syntatically required.
# while True:
#     pass # infinite loop that does nothing.



# match statement
# ----------------------------------------------------------------------------
# - similar to switch statement in C/CPP
# - requires python 3.10 or greater.
status = 400
x = True

match status:
    case 400 if (x == True): # using a guard statement
        print("400: Bad request")
    case 404:
        print("404: Not found")
    case 418:
        print("418: Not sure what this means.")
    case 425 | 426 | 427:
        print("425, 426, 427: these values don't exist")
    case _:
        print("Something else uncaught...")
# NOTE:
# - '_' is a special catch-all character; similar to default keyword in
# C/CPP.