# user input
# ----------------------------------------------------------------------------
# use input() method to get input from user:
x = input("Please enter any input: ")
print("You entered:", x)


# input validation
# ----------------------------------------------------------------------------
# restrict user input to a certain data type:
y = int(input("Please enter an integer: "))
print("You entered the integer:", y)
# NOTE: Must be integer, "987.87" throws exception.


# interpreting user input as boolean
z = bool(input("Enter a boolean value: "))
print("You entered:", z)
# NOTE: 
# - any input other than NULL character results in 'True'
# - includes the string "False"