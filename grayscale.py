import cv2 as cv

path = "assets/nepal.jpg"

# Read image
original = cv.imread(path)

# Resize image
original = cv.resize(original, (0, 0), fx=0.2, fy=0.2)

# Show original image
cv.imshow("Original", original)

# Convert to grayscale
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)

# Show grayscale image
cv.imshow("Gray Scale", gray)

# Wait for any key to close windows
cv.waitKey(0)
cv.destroyAllWindows()
