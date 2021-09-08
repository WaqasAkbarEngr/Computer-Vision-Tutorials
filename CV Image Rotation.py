import cv2

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread(image_path + "\Tomcat.jpg")

(rows, columns) = image.shape[:2]
#image_center = (columns/2 , rows/2)

rotation_matrix = cv2.getRotationMatrix2D((columns/2 , rows/2), 10, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (columns,rows))

cv2.imshow("Rotated Image", rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows