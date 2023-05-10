import cv2
import numpy as np

image = cv2.imread("input/Medianfilterp1.webp", cv2.IMREAD_GRAYSCALE)


# برای کاهش نویز استفاده میشود
result = cv2.medianBlur(image, 3)  # 3 ابعاد ماسک 
cv2.imwrite("output/Medianfilterp2.webp", result)