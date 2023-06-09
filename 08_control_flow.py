# control flow


# if statment
# ----------------------------------------------------------------------------
if (3 > 8):
    print("3 is greater than 8.")
else:
    print("3 is less than or equal to 8.")


# for statment
# ----------------------------------------------------------------------------
# python for iterates over items of any sequence in the order that they 
# appear in the sequence; this differs from for loops in C/CPP where user
# specifies a numerical progression.
nums = [3, 5, 2, 6]
for n in nums:
    print(n)


# range()
# ----------------------------------------------------------------------------
# use range() method to iterate over items in a numerical progression similar
# to for loops in C/CPP:
for i in range(5):
    print(i)

# combine len() and range() to iterate over indices of a sequence:
for i in range(len(nums)):
    print(nums[i])


# while statement
# ----------------------------------------------------------------------------
i = 5
while (i > 0):
    print(i)
    i -= 1