#Recursion
#Python also accepts function recursion
#Which means a defined function can call itself

#Example of recursion function

def factorial(x):
    if x==1:
        return 1
    else:
        return x * factorial(x - 1)

num =5
print(f"Factorial of {num} is {factorial(num)}")