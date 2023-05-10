import cv2
import numpy as np

image = cv2.imread("input/1.jpg", cv2.IMREAD_GRAYSCALE)

# # 1. Edge detection filter
# kernel = np.array([[-1 , -1 , -1],
#                    [-1 ,  8 , -1],
#                    [-1 , -1 , -1]])

# 2. Sharpening filter
# kernel = np.array([[0  , -1 ,  0],
#                    [-1 ,  5 , -1],
#                    [0  , -1 ,  0]])

# 3. Emboss filter
# kernel = np.array([[-2 , -1 ,  0],
#                    [-1 ,  1 ,  1],
#                    [0  ,  1 ,  2]])

# # 4. Identity filter
kernel = np.array([[0  ,  0 ,  0],
                   [0  ,  1 ,  0],
                   [0  ,  0 ,  0]])

result = cv2.filter2D(image, -1, kernel)


cv2.imwrite("output/Identity.jpg", result)