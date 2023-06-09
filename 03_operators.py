
# assignment operators
# ----------------------------------------------------------------------------
a = 5
a += 1 
a -= 1
a *= 3
a /= 5
a **= 3 # power
a %= 2 # modulus
a, b = 1, 2 # multi-assignment


# mathematical operators
# ----------------------------------------------------------------------------
b = 3

x = a + b
x = a - b
x = a / b # always returns floating point number
x = a // b # floor division; truncates decimal portion
x = a * b
x = a ** b
x = a % b


# logical operators
# ----------------------------------------------------------------------------
a, b = True, False

x = (a == b) # equals
x = (a != b) # not equals
x = (a | b) # or
x = (a & b) # and
x = (a ^ b) # xor