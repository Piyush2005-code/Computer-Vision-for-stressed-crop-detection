import cv2
import numpy as np

image = cv2.imread("/IMG-20250708-WA0070.jpg")  # Replace with image path
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

lower_yellow = np.array([25, 155, 120])
upper_yellow = np.array([35, 255, 255])

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

kernel = np.ones((3, 3), np.uint8)
mask_clean = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask_clean = cv2.morphologyEx(mask_clean, cv2.MORPH_CLOSE, kernel)

cv2.imwrite("mask.png", mask_clean)