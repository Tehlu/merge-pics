# First install the cv2 and numpy packages
# Installing them using pip command: pip install opencv-python or numpy
import cv2
import numpy as np

# Reading the two images, image_x will read the variable x image where we change the transparency
# image_b will be the base image onto the which the variable image will merge.
image_x = cv2.imread("BezSlackPic.png")
image_b = cv2.imread("Malaysia.jpg")

print("Processed")
# We'll change the image format first if there's an issue


