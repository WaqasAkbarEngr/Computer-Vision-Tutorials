import cv2
import numpy

x=100
y=100

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread(image_path + "\Tomcat.jpg")
(rows, columns) = image.shape[:2]

translation_matrix = numpy.float32([[1,0,x],[0,1,y]])

translated_image = cv2.warpAffine(image, translation_matrix, (rows,columns))

cv2.imshow("Translated Image", translated_image)

cv2.waitKey(0)
cv2.destroyAllWindows