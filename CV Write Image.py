import cv2

path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread(path+"\Tomcat.jpg")

cv2.imwrite('CV_Write_Image.jpg',image)
