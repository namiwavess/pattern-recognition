# -*- coding: utf-8 -*-
"""
@author: satoshi
@author: namiwavess
"""

# http://postd.cc/image-processing-101/

import cv2
import matplotlib.pyplot as plt

def showlenna():
    # read an image
    # 画像読み込み
    img = cv2.imread('lena_std.tif')

    # preprocess by blurring and grayscale
    # 単純化とノイズの除去を行うためのガウスぼかしとグレースケールによる前処理
    img_preprocessed = cv2.cvtColor(cv2.GaussianBlur(img, (7,7), 0), cv2.COLOR_BGR2GRAY)

    # find binary image with thresholding
    # 閾値で二値化した画像を出力(140)
    _, img_thresh = cv2.threshold(img_preprocessed, 140, 255, cv2.THRESH_BINARY)
    plt.imshow(cv2.cvtColor(img_thresh, cv2.COLOR_GRAY2RGB))

    #save image
    #処理後の画像をjpgで保存
    cv2.imwrite("Lenna_binary.jpg", img_thresh)

if __name__ == "__main__":

    showlenna()
