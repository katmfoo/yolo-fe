import os

def listFiles():
    totalFiles = 0
    subsets = os.listdir('dirname')
    for sets in subset: 
        numFiles = 0
        if os.isdir(sets):
            images = os.listdir(sets)
            for i in images:
                numFiles += 1
            print("Dataset " + sets + " contains " + str(numFiles) + "images.")
            totalFiles = numFiles

if __name__ == "__main__":

    listFiles()
