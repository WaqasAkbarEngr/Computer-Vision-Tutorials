import cv2

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread(image_path + "\Art Amber.jpg")

bordered_image = cv2.copyMakeBorder(image, 50, 50, 50, 50, cv2.BORDER_CONSTANT, None, value = 0)

cv2.imshow('Bordered Image', bordered_image)

cv2.waitKey(0)
cv2.destroyAllWindows