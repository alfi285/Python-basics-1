# check if a number x is between two other numbers y and z (inclusive).
# Additionally, check if x is not equal to a given number k.
from os import PathLike

#Use and to ensure x is between y and z.
#Use not to ensure x is not equal to k.
#Use or to add an alternative condition
# that will pass if x is exactly twice the value of k.
#If the conditions are met,
# print "Conditions are met!",
# otherwise print "Conditions are not met!".

x = 99
y = 10
z = 100
k = 200

if y <= x <= z and x != k or x == 2*k:
    print("Conditions are met")
else:
    print("Conditions not met")

    # First Condition: (y <= x <= z and x != k)

    # y <= x: This checks if y (10) is less than or equal to x (25),
    # which is True.

    # x <= z: This checks if x (25) is less than or equal to z (30),
    # which is also True.

    # Therefore, y <= x <= z evaluates to True.

    # x != k: This checks if x (25) is not equal to k (12), which is True.
    # Since both parts of the and condition are True, the entire first condition evaluates to True.

    # Second Condition: x == 2 * k

    # This checks if x (25) is equal to 2 * k (which is 2 * 12 = 24).
    # This is False since 25 is not equal to 24.

