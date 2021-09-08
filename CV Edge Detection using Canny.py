import cv2

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread(image_path + "\Tomcat.jpg")

edge_detection = cv2.Canny(image, 130, 60)

cv2.imshow("Edge Detection", edge_detection)

cv2.waitKey(0)
cv2.destroyAllWindows