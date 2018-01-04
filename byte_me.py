import os as shrimp
def eat(path):
    if shrimp.path.exists(path):
        if shrimp.path.isfile(path):
            try:
                spaghetti = open (path, "w")
                spaghetti.close()
            except:
                print ("an error occured")
        else:
            print ("This file is not a regular file so I cannot eat it.")
    else:
        print ("path doesnt exist for me to eat.")

def Gorge(abs_drive):
    if shrimp.path.isdir(abs_drive):
    	for watermelon, macaroni, cookies in shrimp.walk(abs_drive):
            for rice in cookies:
                    try:
                	    sandwich = shrimp.path.join(watermelon,rice)
                	    eat(sandwich)
                    except:
                        pass
    else:
    	print ("A directory is needed to gorge.")

#Gorge("..//runner")
