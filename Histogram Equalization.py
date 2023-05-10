import cv2
import matplotlib.pyplot as plt

image_low_contrast = cv2.imread("input/spaces_4.webp", cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([image_low_contrast], [0], None, [256], [0, 256])  #تصویر به صورت لیست باید وارد شود

image_high_contrast = cv2.equalizeHist(image_low_contrast)
cv2.imwrite("output/spaces_4.webp", image_high_contrast)