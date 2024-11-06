# Create a Python function, add_n,
# that takes one argument n and returns a lambda function
# that adds n to any number passed to it.
# Use this function to create add_five,
# a function that always adds 5 to any number.
# Test it by adding 5 to the number 10.

def add_n(n):
    return lambda a:a+n

adder = add_n(5)
print(adder(3))