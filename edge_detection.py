import shutil
import cv2
import os
from PIL import Image

def edgeDetection(dataset, color):
    if color == 'white':
        new_ending = '-edw'
    elif color == 'black':
        new_ending = '-edb'

    new_dataset_path = 'datasets/' + dataset + new_ending

    if os.path.isdir(new_dataset_path):
        shutil.rmtree(new_dataset_path)

    print("Creating copy of dataset '" + dataset + "' called '" + dataset + new_ending + "'")
    shutil.copytree('datasets/' + dataset, new_dataset_path)

    all_files = os.listdir(new_dataset_path)

    print("Applying edge detection to all images within '" + dataset + new_ending + "' (this may take a while)")
    for item in all_files:
        if os.path.isdir(new_dataset_path + '/' + item):
            all_files2 = os.listdir(new_dataset_path + '/' + item)
            for item2 in all_files2:
                filename, file_extension = os.path.splitext(new_dataset_path + '/' + item + '/' + item2)
                if file_extension in ['.jpg', '.jpeg', '.png']:
                    if color == 'white':
                        applyEdgeDetection(new_dataset_path + '/' + item + '/' + item2)
                    elif color == 'black':
                        applyEdgeDetectionBlack(new_dataset_path + '/' + item + '/' + item2)
    
    old_names_file = new_dataset_path + "/" + dataset + ".names"
    new_names_file = new_dataset_path + "/" + dataset + new_ending + ".names"
    os.rename(old_names_file, new_names_file)
    
    os.remove('temp_edges.png')
    os.remove('temp_transparent.png')

def applyEdgeDetection(path):
    img = cv2.imread(path) 

    edges = cv2.Canny(img,100,200)

    cv2.imwrite("temp_edges.png", edges)
    edges = cv2.imread('temp_edges.png')

    tmp = cv2.cvtColor(edges, cv2.COLOR_BGR2GRAY)

    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)

    b, g, r = cv2.split(edges)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)

    cv2.imwrite("temp_transparent.png", dst)
    overlay = cv2.imread('temp_transparent.png')

    added_image = cv2.addWeighted(img,1,overlay,1,0)

    cv2.imwrite(path, added_image)

def applyEdgeDetectionBlack(path):
    img = cv2.imread(path)
    edges = cv2.Canny(img,100,200)
    cv2.imwrite("temp_edges.png", edges)

    trans = Image.open('temp_edges.png')
    trans = trans.convert("RGBA")
    datas = trans.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((0, 0, 0, 255))
        else:
            newData.append((255, 255, 255, 0))

    trans.putdata(newData)
    trans.save("temp_transparent.png", "PNG")

    overlay = cv2.imread('temp_transparent.png')
    img = cv2.imread(path)
    added_image = cv2.addWeighted(img,1,overlay,0.2,0)
    cv2.imwrite(path, added_image)