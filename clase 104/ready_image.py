import cv2
import numpy as np

img = cv2.imread("feather.jfif")
cv2.imshow("mostrar la imagen",img)
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("escala de grises",gray_img)
print(gray_img)
#print(img)
cv2.waitKey(0)
