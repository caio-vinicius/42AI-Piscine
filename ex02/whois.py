import sys

if len(sys.argv) > 1:
    if len(sys.argv) > 2:
        print ("ERROR")
    else:
        if sys.argv[1].isnumeric():
            if int(sys.argv[1]) == 0:
                print ("I'm zero")
            elif int(sys.argv[1]) % 2 == 0:
                print ("I'm even")
            else:
                print ("I'm odd")
        else:
            print ("ERROR")
else:
    pass

