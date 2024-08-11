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

# Converting to rgba
imagex_rgba = cv2.cvtColor(image_x, cv2.COLOR_BGR2BGRA)

# Alpha channel with 50% Opacity (128/255)
alpha_channel = np.ones(imagex_rgba.shape[:2], dtype=image_x.dtype) * 1.5

# Adding the alpha channel to the rgba file
imagex_rgba[:, :, 3] = alpha_channel

# convert base image from jpeg to png
cv2.imwrite("image_b_conv.png", image_b)

# Reading the new converted file
image_b_png = cv2.imread("image_b_conv.png")

# Resize 2nd (base) image to match the first image_x
image_b_resized = cv2.resize(image_b_png, (image_x.shape[1], image_x.shape[0]))

# Convert image2 to BGRA
image_b_rgba = cv2.cvtColor(image_b_resized, cv2.COLOR_BGR2BGRA)

# Blend the images
result = cv2.addWeighted(imagex_rgba, 0.5, image_b_rgba, 0.5, 0)

# Saving the result as a PNG file to preserve transparency
cv2.imwrite('merged_image1.png', result)
