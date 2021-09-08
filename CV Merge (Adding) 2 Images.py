import cv2

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

first_image = cv2.imread (image_path + "\Art Amber.jpg", 1)

second_image = cv2.imread (image_path + "\Balls Graphic.jpg", 1)

print(first_image)

merged_image = cv2.addWeighted(first_image, 0.5, second_image, 0.4, 0)

cv2.imshow('First Image', first_image)
cv2.imshow('Second Image', second_image)

cv2.imshow ('Merged Image', merged_image)
