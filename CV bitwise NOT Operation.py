import cv2

images_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread(images_path + "\Art Amber.jpg")

processed_image = cv2.bitwise_not(image, mask = None)

cv2.imshow('Bitwise NOT Processed Image', processed_image)

cv2.waitKey(0)
cv2.destroyAllWindows