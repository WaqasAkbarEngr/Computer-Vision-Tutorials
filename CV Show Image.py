import cv2

image = cv2.imread("G:\Save Files\Python Save Files\Capture.jpg",1)

cv2.imshow("Opened Picture", image)
cv2.waitKey(0)
