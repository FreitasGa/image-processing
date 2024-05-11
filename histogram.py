import cv2 as cv
from matplotlib import pyplot as plt

path = "assets/nepal.jpg"

# Read image
original = cv.imread(path)

# Resize image
original = cv.resize(original, (0, 0), fx=0.2, fy=0.21)

# Show original image
cv.imshow("Original", original)

# Convert to grayscale
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)

# Show grayscale image
cv.imshow("Gray Scale", gray)

# Calculate histogram
hist = cv.calcHist([gray], [0], None, [256], [0, 256])

# Plot histogram
plt.plot(hist, label="Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()

# Wait for any key to close windows
cv.waitKey(0)
cv.destroyAllWindows()
