import os
def eat(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            try:
                spaghetti = open (path, "w")
                spagehetti.close()
            except:
                print ("an error occured")
        else:
            print ("This file is not a regular file")
    else:
        print ("path doesnt exist")
