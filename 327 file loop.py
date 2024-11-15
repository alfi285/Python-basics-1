#Loop through the file line by line

f= open("demofile.txt","r")
for x in f:
    print(x)

f.close()

#Close files
#it is a good practice to close the opened file always
#Sometime if we did not close the file the changes may not show untill we close the file
