#Nested if
# if statement inside if statement
#This is called nested if

x = 11

if x > 10:
    print("greater than 10")
    if x > 20:
        print("Greater than 20")
    else:
        print("not above 20")
else:
    print("below ten")