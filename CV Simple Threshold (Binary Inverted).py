import cv2

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread(image_path + "\Art Amber.jpg", 0)

ret, binary_inverted_threshold = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY_INV)

cv2.imshow ('Binary Inverted Threshold', binary_inverted_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows