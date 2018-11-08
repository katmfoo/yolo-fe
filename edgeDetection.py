import os
import shutil
import cv2 as cv
from PIL import Image
import numpy as np




def edgeDetection(dataset):
    print("Beginning edge detection for new dataset.")
    os.chdir('datasets')
    newDataset = 'edge_detecited_'+dataset
    if( not os.path.isdir(newDataset)):
        os.mkdir(newDataset)
    print("Copying images from old dataset to new dataset")
    images = os.listdir('./'+dataset)
    for img in images:
        full_path = os.path.join('./'+dataset,img)
        if(os.path.isfile(full_path)):
            shutil.copy(full_path, newDataset)

    print("Beginning edge detection on images in new directory.")
    os.chdir(newDataset)
    images = os.listdir(os.getcwd())
    for img_2 in images:
        if(not img_2.endswith(".txt")):
            if(os.path.isfile(img_2)):
                runCV(img_2)

    print("Making edge detected images transparent")
    images = os.listdir(os.getcwd())
    for img_3 in images:
        if("edge_detected" in img_3):
            makeTransparent(img_3)


    print("Completed edge detection on " + dataset + " dataset.")
    print("Edge detected images located in " + newDataset + " directory.")

def runCV(image):
    img = cv.imread(image,0)
    edges = cv.Canny(img,100,200)
    invert_edges = cv.bitwise_not(edges)
    cv.imwrite('edge_detected_' + image + '.jpg', invert_edges)

def makeTransparent(img_3):
    
    img = Image.open(img_3)
    img.save(img_3+'.png')
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(img_3+"transparent", "PNG")


if __name__ == "__main__":

    edgeDetection('people_dataset')

