#Write a Python program to determine
# the type of a triangle
# based on the lengths of its three sides (a, b, and c).

#First, check if the three sides form a valid triangle:
#A triangle is valid if the sum of any two sides is greater
# than the third side.
#If it is a valid triangle, check the following conditions:
#If all three sides are equal, print "Equilateral Triangle".
#If only two sides are equal, print "Isosceles Triangle".
#If no sides are equal, print "Scalene Triangle".
#If the sides do not form a valid triangle, print "Not a Triangle".

a = 10
b = 10
c = 10

if (a+b > c) and (a+c > b) and (b+c > a):
    if (a==b==c):
        print("Equilateral Triangle")
    elif (a == b) or (b==c) or (a==c):
        print("Isosceles Triangle")
    else:print("Scalene Triangle")
else:print("Not a valid triangle")