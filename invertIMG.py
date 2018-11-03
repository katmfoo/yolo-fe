import os
import cv2
import numpy as np

def inverte(imagem):
    img = cv2.bitwise_not(imagem)
    cv2.imwrite("inverted_image.jpg",img)


if __name__ == '__main__':
   im_in = cv2.imread("C:/Users/DaddyEJ/Downloads/yolo-fe-master/yolo-fe-master/datasets/edge_detected_people_dataset/people1.jpg",cv2.IMREAD_GRAYSCALE)
   img = inverte(im_in)
  #  cv2.imwrite("inverted_image.jpg",img)
