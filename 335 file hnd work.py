#work  # create an txt file named work.txt?
# add 5 lines using write ?
# add 2 lines to end using append?
# print first 4 lines using readline()?
# overwrite using another 2 lines?
#last read all

f = open("work1.txt","x")

f.write("hi all")
f.write("India is my country")
f.write("All indians are my brothers")
f.write("Sisters")
f.write("i love my country")
f.close()

f1 = open("work1.txt","a")
f1.write("to my country")
f1.write(" and my people")
f1 = open("work1.txt","r")
print(f1.readline())
print(f1.readline())
print(f1.readline())
print(f1.readline())
f1.close()

f2 = open("work1.txt","w")
f2.write("hiiiiiiii")
f2.write("indianssssssss")
f2= open("work1.txt","r")
print(f2.read())
f2.close()