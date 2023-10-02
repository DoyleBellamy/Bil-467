# We will code histogran equalization without using OpenCv library
# Only use to read image 
import cv2 as cv
import numpy as np
import math
# 1. Read the image
image = cv.imread('test1.jpg',cv.IMREAD_GRAYSCALE)
#cv.imshow('First Image',image)

# Shows us the shape of our grayscale image
m,n = image.shape
TOTAL_PIXEL = m*n
MAX_PIXEL_VALUE = 255
print(image.shape)
# Shows us value of index (0,0) of our grayscale image
print(image[0][0])

# We will store the count of pixel values in an array
histogram_values = np.zeros(256)
# print(histogram_values.shape)

for i in range(m):
    for j in range(n):
        histogram_values[image[i][j]] += 1

histogram_distribution = np.zeros(256)

for i in range(m):
    histogram_distribution[i]=histogram_values[i]/TOTAL_PIXEL

temp_total_distribution = 0.0
histogram_equalization_pixel_matching = np.zeros(256)
for i in range(m):
    temp_total_distribution+=histogram_distribution[i]
    temp_value = temp_total_distribution*MAX_PIXEL_VALUE
    histogram_equalization_pixel_matching[i] = math.floor(temp_value+0.5)

new_image = image.copy()
print(histogram_equalization_pixel_matching)
for i in range(m):
    for j in range(n):
        new_image[i][j] = histogram_equalization_pixel_matching[new_image[i][j]]

cv.imshow('Output_1', new_image)

equ = cv.equalizeHist(image)
  
# stacking images side-by-side
#res = np.hstack((image, equ))
  
# show image input vs output
cv.imshow('Output_2', equ)

difference_image = np.zeros((m,n))
for i in range(m):
    for j in range(n):
        difference_image[i][j] = abs(new_image[i][j] - equ[i][j]) 

cv.imshow('Difference', difference_image)

cv.waitKey(0)

cv.destroyAllWindows()

