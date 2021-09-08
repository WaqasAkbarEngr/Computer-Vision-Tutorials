import cv2

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread(image_path + "\Art Amber.jpg")

resized_image = cv2.resize(image, (780,320))

cv2.imshow('Resized Image', resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows