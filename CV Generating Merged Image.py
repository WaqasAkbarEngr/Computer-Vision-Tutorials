import cv2

image_path = "G:\Save Files\Python Save Files\CV Tutorials\images"

first_image = cv2.imread( image_path + "\Falcon Jet.jpg")

second_image = cv2.imread( image_path + "\Lightning.jpg")

merged_image = cv2.addWeighted ( first_image, 0.6, second_image, 0.7, 0)

cv2.imwrite ("G:\Save Files\Python Save Files\CV Tutorials\Generated Images\CV Generating Merged Image.jpg", merged_image)
