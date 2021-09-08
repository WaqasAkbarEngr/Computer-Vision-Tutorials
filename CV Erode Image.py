import cv2
import numpy

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread(image_path + "\Art Amber.jpg")

kernal = numpy.zeros((50,50), numpy.uint8)

eroded_image = cv2.erode (image, kernal)

cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows