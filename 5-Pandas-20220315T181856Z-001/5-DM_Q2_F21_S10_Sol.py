# ----------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
# -------------------------------Part 1---------------------------------
# Read the face.png image and convert them to a matrix of numbers.
# Print the shape of the matrix.

import matplotlib.pyplot as plt

f = plt.imread('face.png')
plt.imshow(f)
plt.show()

print(f'shape of this image is {f.shape}')
# -------------------------------Part 2---------------------------------
# Convert the color image to a gray scale image. Color image has 3 dim and grey scale image has 12 dim.
# Plot the grey scale image.
# Hint: You should not use a complex function to convert it to grey scale. Just think of how you can reduce dimensions in numpy.

img = f.sum(2) / (255*3)
plt.imshow(img)
plt.show()
# -------------------------------Part 3---------------------------------
# Rotate this image 90 degree.
# Use matrix operation and you should not use a complex function.
# Plot the results.
img0 = img.copy()
img0 = img0.transpose()

plt.imshow(img0)
plt.title("rotated")
plt.show()

# -------------------------------Part 4---------------------------------
# Add a frame around the image.
# Plot the results.
img1 = np.pad(img, ((100,100),(100,100)), mode='constant')
plt.imshow(img1)
plt.title("padded")
plt.show()


# -------------------------------Part 5---------------------------------
# Trim the image in a way just the face racoon is in the image.
# Plot the results.
img2 = img[200:600, 500:800]
plt.imshow(img2)
plt.title('Trimmed')
plt.show()


