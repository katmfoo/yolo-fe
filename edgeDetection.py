import os
import shutil
import cv2 as cv

def edgeDetection(dataset):
    print("Beginning edge detection for new dataset.")
    os.chdir('datasets')
    newDataset = 'edge_detected_'+dataset
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
    images_2 = os.listdir(os.getcwd())
    for img_2 in images_2:
        if(not img_2.endswith(".txt")):
            if(os.path.isfile(img_2)):
                runCV(img_2)

    print("Completed edge detection on " + dataset + " dataset.")
    print("Edge detected images located in " + newDataset + " directory.")

def runCV(image):
    img = cv.imread(image,0)
    edges = cv.Canny(img,100,200)
    cv.imwrite('edge_detected_'+image+'.jpg',edges)

if __name__ == "__main__":

    edgeDetection('people_dataset')
