# color_detections

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

### Step 1: Import Libraries

### Step 2: Load image

### Step 3: Convert image to HSV color space
It is difficult to use RGB (BRG in OpenCV) color space for color detection due to variations in lighting conditions and complex relationships between the three channels (R, G, and B).

For example, let’s say we want to find a red apple in an image that has a green background. It can be hard to find the apple in the picture because the green background can look similar (mathematically) to the apple’s red color.

This happens because, in RGB color system, the red color of the apple is made up of a lot of “red” and very little “green” and “blue,”. Similarly, the green background might also have a similar combination of colors (R, G, and B).

This is the reason, we need to convert RGB color space to HSV. Because in the HSV color space, we only need to look at the Hue channel to detect the red color of the apple. We can set a specific range of values for the Hue channel to detect the red color of the apple.

### Step4: Define a color range to detect

To detect multiple colors, we just need to mention color ranges for those colors.

In our input image, we just need to extract red, green, and blue colors. So we need to define color ranges for those colors. The code will be same. Below Python code is to do multiple color detection using OpenCV.

### Step 5: Filtering part of image based on the color range

### Step 6: Contour Detection

### Step 7: Draw bounding box

### Step 8 Display the output 




