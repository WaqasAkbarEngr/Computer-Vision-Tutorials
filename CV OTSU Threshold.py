import cv2

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread( image_path + '\Art Amber.jpg', 0)

ret, otsu_threshold = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow ('OTSU Threshold', otsu_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows