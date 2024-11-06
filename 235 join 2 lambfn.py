#Program to make a join

def myfunc(n):
    return lambda a:a*n

doubler = myfunc(2)
tripler = myfunc(3)

print(doubler(10))
print(tripler(10))