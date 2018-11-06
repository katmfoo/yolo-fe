import os
import cv2
import numpy as np

def inverte(imagem):
    img = cv2.bitwise_not(imagem)
    cv2.imwrite("inverted_image.jpg",img)


if __name__ == '__main__':
   im_in = cv2.imread("C:/Users/shapi/yolo-fe/datasets/edge_detecited_people_dataset/edge_detected_people4.jpg", cv2.IMREAD_GRAYSCALE)
   img = inverte(im_in)
  #  cv2.imwrite("inverted_image.jpg",img)
