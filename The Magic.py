import cv2
import numpy as np
image = cv2.imread("input/magic.tif", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5)) / 25  
result = cv2.filter2D(image, -1, kernel)
cv2.imwrite("output/magic.jpg", result)