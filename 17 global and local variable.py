# Local variables

def localvariablefun():
    z = "fantastic-local"
    # z is an local variable, can be accessed only inside the function

    print(z)
localvariablefun()


#Global keyword
def globalvariablefun():
    global x
    x = "fantastic..!-global"

globalvariablefun()
print("Python is " + x)
