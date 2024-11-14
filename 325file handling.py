#File Handling
#Python File Open
# open() function-used to open a file!
#The open() function takes two parameters; filename, and mode.
# There are four different methods (modes):----------
# "r" - Read - Default value. Opens a file for reading,
# error if the file does not exist

# "a" - Append - Opens a file for appending,
# creates the file if it does not exist

# "w" - Write - Opens a file for writing,
# creates the file if it does not exist

# "x" - Create - Creates the specified file,
# returns an error if the file exists


f= open("demofile.txt","r")
print(f.read())


d = open("C:\Alfi datahub\welcome.txt")
print(d.read())

f = open("demofile.txt","r")
print(f.read(5))