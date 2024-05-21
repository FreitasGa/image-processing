import cv2 as cv
import numpy as np

path = "assets/kyoto.jpg"
display_width = 600

# Read image
original = cv.imread(path)

# Define display height
height, width = original.shape[:2]
aspect_ratio = width / height
display_height = int(display_width / aspect_ratio)

# Show original image
cv.namedWindow("Original", cv.WINDOW_NORMAL)
cv.imshow("Original", original)
cv.resizeWindow("Original", display_width, display_height)

# Split image into RGB channels
(blue, green, red) = cv.split(original)

# Show channels in color
# zeros = np.zeros(original.shape[:2], dtype="uint8")
# blue = cv.merge([blue, zeros, zeros])
# green = cv.merge([zeros, green, zeros])
# red = cv.merge([zeros, zeros, red])

# Show Red channel image
cv.namedWindow("Red", cv.WINDOW_NORMAL)
cv.imshow("Red", red)
cv.resizeWindow("Red", display_width, display_height)

# Show Green channel image
cv.namedWindow("Green", cv.WINDOW_NORMAL)
cv.imshow("Green", green)
cv.resizeWindow("Green", display_width, display_height)

# Show Blue channel image
cv.namedWindow("Blue", cv.WINDOW_NORMAL)
cv.imshow("Blue", blue)
cv.resizeWindow("Blue", display_width, display_height)

# Wait for any key to close windows
cv.waitKey(0)
cv.destroyAllWindows()
