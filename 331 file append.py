#4
#append-mode

f = open("work.txt", "a")
f.write("Now the file has more content!")
f.close()

#write-mode

f = open("myfile.txt", "w")
f.write("all gone")
f.close()