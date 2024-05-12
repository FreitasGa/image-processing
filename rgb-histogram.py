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

# Show original image
cv.namedWindow("Original", cv.WINDOW_NORMAL)
cv.imshow("Original", original)
cv.resizeWindow("Original", display_width, display_height)

# Calculate and plot histogram
channels = cv.split(original)
colors = ("b", "g", "r")

for (channel, color) in zip(channels, colors):
    hist = cv.calcHist([channel], [0], None, [256], [0, 256])

    # Normalize histogram
    hist /= hist.sum()

    plt.plot(hist, color=color)
    plt.title("RGB Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

plt.show()

# Wait for any key to close windows
cv.waitKey(0)
cv.destroyAllWindows()
