import cv2

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

image = cv2.imread (image_path + '\Art Amber.jpg', 0)

converted_image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

cv2.imshow('Image Converted from GreyScale to RGB', converted_image)

cv2.waitKey(0)
cv2.destroyAllWindows