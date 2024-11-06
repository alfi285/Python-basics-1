# Write a Python function, power_func,
# that takes one argument n and returns a lambda function
# that raises any number passed to it to the power of n.
# In the same program, create both square and cube functions using power_func.
# Test them by squaring the number 5 and cubing the number 3.

def power_fn(n):
    return lambda a:a**n
sqr = power_fn(2)
cube = power_fn(3)

print(sqr(10))
print(cube(3))