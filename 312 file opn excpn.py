#Try to open and write to a file that is not writable

try:
    f = open("demofile.txt")
    try:
        f.write("KIiiiiiiiiiiiiii")

    except:
        print("Something went wrong when writting to the file")
    finally:
        f.close()
except:
    print("Something wrong in open file")
