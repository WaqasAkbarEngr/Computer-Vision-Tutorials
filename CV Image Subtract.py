import cv2

images_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

first_image = cv2.imread (images_path + "\Balls Graphic.jpg")
second_image = cv2.imread (images_path + "\Anatomy.jpg")

subtracted_image = cv2.subtract(first_image, second_image)

cv2.imshow ('Subtracted Image', subtracted_image)
