import cv2

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread(image_path + "\Art Amber.jpg")

blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

cv2.imshow('Blurred Image', blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows