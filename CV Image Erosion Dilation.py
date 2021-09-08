import cv2
import numpy

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread(image_path + "\Tomcat.jpg")

kernel = numpy.zeros((50,50), numpy.uint8)

eroded_image = cv2.erode(image, kernel, iterations = 1)
dilated_image = cv2.dilate(image, kernel, iterations = 1)

cv2.imshow("Eroded Image", eroded_image)
cv2.imshow("Dilated Image", dilated_image)

cv2.waitKey(0)
cv2.destroyAllWindows