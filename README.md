# color_detection

## OBJECTIVE
The objective the project is to detect color the object in the image or video file or live stream video
Color detection is an important task in computer vision where we identify a specific or multiple colors in an image or video.
It has various applications in fields such as robotics, object tracking, image processing,etc., 

## Understand Color Spaces

Before we start writing our code, let’s understand the concept about different types of color spaces. A color space is nothing but how we represent a set of colors (or an image) mathematically.

In computer vision or image analysis most commonly used color spaces are RGB, HSV, and YUV.

**RGB** :represents colors using red, green, and blue values (RGB). Note that OpenCV uses BGR color code instead of RBG.

**HSV**:This type of color space separates the color information from the brightness information of an image. It represents colors using hue, saturation, and value.
Hue  represents the color of a pixel, such as red, green, blue. We can measure this in degrees with range of 0 to 360. 0 represents red, 120 represents green, and 240 represents blue.
Saturation represents how pure the color is. A highly saturated color is pure, while a less saturated color is mixed with white. Saturation is measured in percentages with range of 0% to 100%. 0% means white and 100% means purest color.
Value represents the brightness of the pixel. A high value represents a bright pixel, while a low value represents a dark pixel. We can also measure in percentage. 0% represents black and 100% represents white.

**YUV**:We can use this color space to separate color information into luminance (Y) and chrominance (UV). It is slightly more complex than HSV.

You need to install required libraries

    pip install opencv-python

    pip install numpy

These two libraries for important to run the code
### Step 1: Import Libraries

         import cv2 as cv

         import numpy as np

### Step 2: Load image

      img=imread("image.jpg)

      cv.imshow("image",img) to display

#for an image

      img=cv.imread("image.jpg")

#For live webcam

     cap = cv.VideoCapture(0)

#For a video file

     cap = cv.VideoCapture("path of video file")

    while True:

     ret, img = cap.read()
    
      img = cv.resize(img, dsize=(700, 500))

### Step 3: Convert image to HSV color space

It is difficult to use RGB (BRG in OpenCV) color space for color detection due to variations in lighting conditions and complex relationships between the three channels (R, G, and B).

For example, let’s say we want to find a red apple in an image that has a green background. It can be hard to find the apple in the picture because the green background can look similar (mathematically) to the apple’s red color.

This happens because, in RGB color system, the red color of the apple is made up of a lot of “red” and very little “green” and “blue,”. Similarly, the green background might also have a similar combination of colors (R, G, and B).

This is the reason, we need to convert RGB color space to HSV. Because in the HSV color space, we only need to look at the Hue channel to detect the red color of the apple. We can set a specific range of values for the Hue channel to detect the red color of the apple.

     hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

### Step4: Define a color range to detect

To detect multiple colors, we just need to mention color ranges for those colors.

In our input image, we just need to extract red, green, and blue colors. So we need to define color ranges for those colors. The code will be same. Below Python code is to do multiple color detection using OpenCV.

                         
Eg.
    
    lower_red = np.array([0, 50, 50]) H,S,V

    upper_red = np.array([10, 255, 255])

### Step 5: Filtering part of image based on the color range
    mask_red = cv.inRange(img, lower_red, upper_red)
 
    mask_green = cv.inRange(img, lower_green, upper_green)
  
    mask_blue = cv.inRange(img, lower_blue, upper_blue)

### Step 6: Contour Detection

    contours_red, _ = cv.findContours(mask_red, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
  
    contours_green, _ = cv.findContours(mask_green, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
  
    contours_blue, _ = cv.findContours(mask_blue, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

### Step 7: Draw bounding box
    
       
    for cnt in contours_red:
        contours_area = cv.contourArea(cnt)
        if contours_area > 1000:
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.putText(img, "RED", (x, y - 10), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=4, color=(0, 0, 255),
                       thickness=3)

### Step 8 Display the output 

# Displaying image
    cv.imshow("image", img)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    cap.release()
    cv.destroyAllWindows()


