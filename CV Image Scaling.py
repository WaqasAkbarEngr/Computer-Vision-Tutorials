import cv2

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread(image_path + "\Tomcat.jpg")

(rows, columns) = image.shape[:2]

scaled_image = cv2.resize(image, (int(rows/4), int(columns/4)))

cv2.imshow("Scaled Image", scaled_image)

cv2.waitKey(0)
cv2.destroyAllWindows