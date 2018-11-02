import os
import shutil

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

if __name__ == "__main__":

    edgeDetection('people')
