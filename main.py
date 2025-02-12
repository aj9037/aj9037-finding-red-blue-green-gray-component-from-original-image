import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('your_image_path.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Split the image into red, green, and blue components
b, g, r = cv2.split(image)

# Calculate the total number of pixels
total_pixels = image.shape[0] * image.shape[1]

# Calculate the sum of each component
sum_red = np.sum(r)
sum_green = np.sum(g)
sum_blue = np.sum(b)

# Calculate the percentage of each component
percentage_red = (sum_red / total_pixels) * 100
percentage_green = (sum_green / total_pixels) * 100
percentage_blue = (sum_blue / total_pixels) * 100

# Convert the gray image to float for later calculations
gray_image_float = gray_image.astype(np.float32)

# Normalize the gray image
normalized_gray_image = (gray_image_float - np.min(gray_image_float)) / (np.max(gray_image_float) - np.min(gray_image_float))

# Calculate the sum of pixel values in the normalized gray image
sum_gray = np.sum(normalized_gray_image)

# Calculate the percentage of gray in the image
percentage_gray = (sum_gray / total_pixels) * 100

# Display the images and percentages
plt.figure(figsize=(10, 8))

plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(r, cmap='Reds')
plt.title('Red Component\n{:.2f}%'.format(percentage_red))
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(g, cmap='Greens')
plt.title('Green Component\n{:.2f}%'.format(percentage_green))
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(b, cmap='Blues')
plt.title('Blue Component\n{:.2f}%'.format(percentage_blue))
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image\n{:.2f}%'.format(percentage_gray))
plt.axis('off')

plt.show()
