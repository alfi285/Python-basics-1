# Write a Python function, make_calculator,
# that takes one argument n and returns a lambda function
# that adds n to any number passed to it.
# In the same program, create both add_ten and subtract_five functions
# using make_calculator.
# Test them by adding 10 to the number 7 and
# subtracting 5 from the number 20.

def make_calculator(n):
    return lambda a:a+n
add_ten = make_calculator(10)
subtract_five = make_calculator(-5)

print(add_ten(10))
print(subtract_five(10))