import cv2 as cv
from matplotlib import pyplot as plt

path = "assets/kyoto.jpg"
display_width = 600

# Read image
original = cv.imread(path)

# Define display height
height, width = original.shape[:2]
aspect_ratio = width / height
display_height = int(display_width / aspect_ratio)

# Convert to grayscale
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)

# Show grayscale image
cv.namedWindow("Grayscale", cv.WINDOW_NORMAL)
cv.imshow("Grayscale", gray)
cv.resizeWindow("Grayscale", display_width, display_height)

# Calculate histogram
hist = cv.calcHist([gray], [0], None, [256], [0, 256])

# Normalize histogram
hist /= hist.sum()

# Plot histogram
plt.plot(hist)
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()

# Wait for any key to close windows
cv.waitKey(0)
cv.destroyAllWindows()
