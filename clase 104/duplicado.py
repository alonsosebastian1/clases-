import cv2
img = cv2.imread("cohete.jpeg")
cohete = img [120:360,400:500]
img[0:240,500:600] = cohete
text_to_show = "alonso haciendo imagenes"
cv2.putText(img,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
fontScale=1,color=(0,0,255))
cv2.imshow("resultado",img)
cv2.waitKey(0)