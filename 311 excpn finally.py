#Finally

#The finally block if specified will be execute regardless if the try block raises an error or not

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("try except is finished")