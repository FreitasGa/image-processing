import cv2 as cv
from matplotlib import pyplot as plt

path = "assets/atacama.jpg"

# Read image
original = cv.imread(path)

# Resize image
original = cv.resize(original, (0, 0), fx=0.2, fy=0.21)

# Show original image
cv.imshow("Original", original)

# Calculate histogram
colors = ("b", "g", "r")

for i, color in enumerate(colors):
    hist = cv.calcHist([original], [i], None, [256], [0, 256])
    plt.plot(hist, color=color, label=f"{color.upper()} channel")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

plt.show()

# Wait for any key to close windows
cv.waitKey(0)
cv.destroyAllWindows()
