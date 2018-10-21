import os

def listFiles():
    numFiles = 0
    for f in os.listdir("practice"):
        numFiles += 1
    print(os.listdir("practice"))
    print(str(numFiles) + " total files.")

if __name__ == "__main__":

    listFiles()
