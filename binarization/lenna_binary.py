# -*- coding: utf-8 -*-
"""
@author: namiwavess
"""

# http://postd.cc/image-processing-101/

import cv2
import matplotlib.pyplot as plt

def showlenna():
    # read an image
    img = cv2.imread('lena_std.tif')

    # preprocess by blurring and grayscale
    img_preprocessed = cv2.cvtColor(cv2.GaussianBlur(img, (7,7), 0), cv2.COLOR_BGR2GRAY)
 
    # find binary image with thresholding
    _, img_thresh = cv2.threshold(img_preprocessed, 140, 255, cv2.THRESH_BINARY)
    plt.imshow(cv2.cvtColor(img_thresh, cv2.COLOR_GRAY2RGB))

    #save image
    cv2.imwrite("Lenna_binary.jpg", img_thresh)

if __name__ == "__main__":

    showlenna()
