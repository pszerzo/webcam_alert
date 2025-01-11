import numpy
import cv2

"""read"""
array = cv2.imread("image.png")
print(array)

"""create"""
a = numpy.array(
[[[255,   0,  0],
  [255, 255, 255],
  [255, 255, 255],
  [187,  41, 160]],

 [[255, 255, 255],
  [255, 255, 255],
  [255, 255, 255],
  [255, 255, 255]],

 [[255, 255, 255],
  [0, 0, 0],
  [47, 255, 173],
  [255, 255, 255]]]
)

cv2.imwrite("myimage.png", a)

