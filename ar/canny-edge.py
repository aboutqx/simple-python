import cv2
import numpy as np
capture = cv2.VideoCapture(0)
print capture.get(cv2.CAP_PROP_FPS)

w = 640.0

while True:
    ret, image = capture.read()
    img_height, img_width, depth = image.shape
    scale = w / img_width
    h = int(img_height * scale)
    w = int(w)
    image = cv2.resize(image, (0, 0), fx=scale, fy=scale)

    # Apply filters
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blured = cv2.medianBlur(grey, 15)


    t = 100  # threshold for Canny Edge Detection algorithm

    # Compose 2x2 grid with all previews

    grid = np.zeros([2*h, 2*w, 3], np.uint8)
    grid[0:h, 0:w] = image

    # We need to convert each of them to RGB from grescaled 8 bit format
    grid[h:2*h, 0:w] = np.dstack([cv2.Canny(grey, t / 2, t)] * 3)
    grid[0:h, w:2*w] = np.dstack([blured] * 3)
    grid[h:2*h, w:2*w] = np.dstack([cv2.Canny(blured, t / 2, t)] * 3)

    cv2.imshow('Image previews', grid)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
