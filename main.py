# importing libraries

import cv2 as cv
import numpy as np

# for an image
# img=cv.imread("image.jpg")

# For live webcam
cap = cv.VideoCapture(0)

# For a video file
# cap = cv.VideoCapture("path of video file")

while True:
    ret, img = cap.read()
    img = cv.resize(img, dsize=(700, 500))
    # convert BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # defining red color
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])

    # defining green color
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([190, 255, 255])

    # defining blue color

    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # create mask for the red color , green color & blue color
    mask_red = cv.inRange(img, lower_red, upper_red)
    mask_green = cv.inRange(img, lower_green, upper_green)
    mask_blue = cv.inRange(img, lower_blue, upper_blue)

    # find contours in the red mask
    contours_red, _ = cv.findContours(mask_red, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv.findContours(mask_green, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours_blue, _ = cv.findContours(mask_blue, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # looping throughout the red contours

    for cnt in contours_red:
        contours_area = cv.contourArea(cnt)
        if contours_area > 1000:
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.putText(img, "RED", (x, y - 10), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=4, color=(0, 0, 255),
                       thickness=3)
    # looping throughout the green contour
    for cnt in contours_green:
        contours_area = cv.contourArea(cnt)
        if contours_area > 1000:
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(img, "GREEN", (x, y - 10), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=4, color=(0, 255, 0),
                       thickness=3)
    # loop in throughout the blue color

    for cnt in contours_blue:
        contours_area = cv.contourArea(cnt)
        if contours_area > 1000:
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv.putText(img, "BLUE", (x, y - 10), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=4, color=(255, 0, 0),
                       thickness=3)

    # Displaying image
    cv.imshow("image", img)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv.destroyAllWindows()
