import cv2 as cv


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

# Convert to grayscale
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)

# Show grayscale image
cv.namedWindow("Grayscale", cv.WINDOW_NORMAL)
cv.imshow("Grayscale", gray)
cv.resizeWindow("Grayscale", display_width, display_height)

# Wait for any key to close windows
cv.waitKey(0)
cv.destroyAllWindows()
