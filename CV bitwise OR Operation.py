import cv2

images_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

first_image = cv2.imread(images_path + "\Art Amber.jpg")
second_image = cv2.imread(images_path + "\Balls Graphic.jpg")

processed_image = cv2.bitwise_or(first_image, second_image, mask = None)

cv2.imshow('Bitwise OR Modified Image', processed_image)

cv2.waitKey(0)
cv2.destroyAllWindows