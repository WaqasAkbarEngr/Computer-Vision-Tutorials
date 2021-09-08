import cv2

image_path = 'G:\Save Files\Python Save Files\CV Tutorials\images'

image = cv2.imread(image_path + '\Art Amber.jpg', 0)

adaptive_threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 91, 5)

cv2.imshow('Adaptive Threshold (Mean)', adaptive_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows