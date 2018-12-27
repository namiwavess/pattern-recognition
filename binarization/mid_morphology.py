# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 12:37:56 2018

@author: blueo
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# 元画像
image = np.array([[0,1,1,0, 0,0,0,0],
[0,1,1,1, 1,0,0,0],
[0,0,1,1, 1,0,0,0],
[0,0,1,1, 1,0,0,0],
[0,0,0,0, 0,0,0,0],
[0,0,1,1, 1,1,1,1],
[0,0,1,1, 1,1,0,0],
[0,0,1,1, 1,1,0,0]],np.uint8)

# 4近傍の定義
nei4 = np.array([[0, 1, 0],
[1, 1, 1],
[0, 1, 0]],np.uint8)
 
# 8近傍の定義
nei8 = np.array([[1, 1, 1],
[1, 1, 1],
[1, 1, 1]],np.uint8)

kernel = np.ones((5,5),np.uint8)

#erosion(erode) 収縮 f
#dilate 膨張 g
image_f4 = cv2.erode(image,nei4,iterations=1)
image_g4 = cv2.dilate(image,nei4,iterations=1)
image_f8 = cv2.erode(image,nei8,iterations=1)
image_g8 = cv2.dilate(image,nei8,iterations=1)

image_g4f4 = cv2.erode(image_g4,nei4,iterations=1)
image_g8f8 = cv2.erode(image_g8,nei8,iterations=1)
image_f4g4 = cv2.dilate(image_f4,nei4,iterations=1)
image_f8g8 = cv2.dilate(image_f8,nei8,iterations=1)

# 作った画像を拡大
size = (480,480)
image_g4f4 = cv2.resize(image_g4f4*255,size,interpolation=cv2.INTER_NEAREST)
image_g8f8 = cv2.resize(image_g8f8*255,size,interpolation=cv2.INTER_NEAREST)
image_f4g4 = cv2.resize(image_f4g4*255,size,interpolation=cv2.INTER_NEAREST)
image_f8g8 = cv2.resize(image_f8g8*255,size,interpolation=cv2.INTER_NEAREST)

# 画像を表示
cv2.imshow("image", image)

# 画像を保存
cv2.imwrite("image_g4f4.png" , image_g4f4)
cv2.imwrite("image_g8f8.png" , image_g8f8)
cv2.imwrite("image_f4g4.png" , image_f4g4)
cv2.imwrite("image_f8g8.png" , image_f8g8)

# 画像のうえでキーがおされるまで待つ
cv2.waitKey(0)
cv2.destroyAllWindows()