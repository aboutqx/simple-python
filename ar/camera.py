import cv2
capture = cv2.VideoCapture(0)

while True:
    ret, image = capture.read()
    width, height, depth = image.shape
    scale = 640.0 / width
    image = cv2.resize(image, (0,0), fx=scale, fy=scale)
    cv2.imshow('Camera stream', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    