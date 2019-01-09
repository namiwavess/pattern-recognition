# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:44:53 2017

@author: satoshi
@author: namiwavess
"""

# http://postd.cc/image-processing-101/

import cv2
import matplotlib.pyplot as plt
import numpy as np

# 矢印キー
CV_WAITKEY_CURSORKEY_TOP    = 2490368;
CV_WAITKEY_CURSORKEY_BOTTOM = 2621440;
CV_WAITKEY_CURSORKEY_RIGHT  = 2555904;
CV_WAITKEY_CURSORKEY_LEFT   = 2424832;
# エンターキーとか
CV_WAITKEY_ENTER            = 13;
CV_WAITKEY_ESC              = 27;
CV_WAITKEY_SPACE            = 32;
CV_WAITKEY_TAB              = 9;

def showlenna():
    # read an image
    img = cv2.imread('lena.tif')

    # show image format (basically a 3d array of pixel color info, in BGR format)
    #print (img)

    #convert image to RGB color for matplotlib
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #ret, img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,21,20)
    #ret, img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    #show image with matplotlib
    #plt.imshow(img)
    #plt.imshow(img, cmap='binary_r')
    return img

if __name__ == "__main__":



    capture = cv2.VideoCapture(0)
    if capture.isOpened() is False:
        raise("IO Error")

    cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)

    iter = 4

    while True:
        img = showlenna()
        ret = True
        #ret, img = capture.read()

        if ret == False:
            continue

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        ret, img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #カーネルサイズ指定
        kernel = np.ones((iter,iter),np.uint8)
        #収縮
        erode = cv2.erode(img,kernel)
        #膨張
        dilate = cv2.dilate(img,kernel)
        #オープニング・収縮の後に膨張
        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        #クロージング・膨張の後に収縮
        closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        #モルフォロジー勾配
        gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

        cv2.imshow("Capture", \
                   cv2.vconcat([ \
                               cv2.hconcat([img, erode, dilate]),\
                               cv2.hconcat([gradient, opening, closing])]))
        #cv2.imshow("Capture", img)

        key = cv2.waitKey(33)
        print (key)
        if key == CV_WAITKEY_ESC:
            cv2.imwrite("img.png", img)
            cv2.imwrite("erode.png", erode)
            cv2.imwrite("dlate.png", dilate)
            cv2.imwrite("gradient.png", gradient)
            cv2.imwrite("opening.png", opening)
            cv2.imwrite("closing.png", closing)
            capture.release()
            break
        elif key == ord('1'): #CV_WAITKEY_CURSORKEY_TOP:
            iter = iter+1
        elif key == ord('2'): #CV_WAITKEY_CURSORKEY_BOTTOM:
            if (iter > 1):
                iter = iter-1

    cv2.destroyAllWindows()
