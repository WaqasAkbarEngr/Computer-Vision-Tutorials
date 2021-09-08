import cv2

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread (image_path + "\Tomcat.jpg",-1)

converted_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow ('Original Image', image)

cv2.imshow ("GreyScaled Image", converted_image)
