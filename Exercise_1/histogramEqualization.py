import cv2 as cv
import numpy as np
import math
import os 
#First Part
image = cv.imread(os.path.join(os.getcwd(),'test1.jpg'),cv.IMREAD_GRAYSCALE)

m,n = image.shape
TOTAL_PIXEL = m*n
# 256 ya çevir TODO
MAX_PIXEL_VALUE = 255
print(image.shape)

histogram_values = np.zeros(256)
LOWEST_PIXEL_VALUE = 256

for i in range(m):
    for j in range(n):
        if image[i][j]<LOWEST_PIXEL_VALUE:
            LOWEST_PIXEL_VALUE = image[i][j]
        histogram_values[image[i][j]] += 1

histogram_distribution = np.zeros(256)
for i in range(m):
    histogram_distribution[i]=histogram_values[i]/TOTAL_PIXEL

total_distribution_cumulative_1 = 0.0
histogram_equalization_pixel_matching = np.zeros(256)
for i in range(m):
    total_distribution_cumulative_1+=histogram_distribution[i]
    temp_value = total_distribution_cumulative_1*MAX_PIXEL_VALUE
    histogram_equalization_pixel_matching[i] = math.floor(temp_value+0.5)

new_image = image.copy()
for i in range(m):
    for j in range(n):
        new_image[i][j] = histogram_equalization_pixel_matching[new_image[i][j]]

cv.imshow('Output_1', new_image)

equ_opencv = cv.equalizeHist(image)

cv.imshow('Output_2', equ_opencv)

difference_image = image.copy()
for i in range(m):
    for j in range(n):
        difference_image[i][j] = abs(new_image[i][j] - equ_opencv[i][j])
cv.imshow('Difference', difference_image)

# SECOND PART
# We will use histogram_values as we calculated before
histogram_values_2_cumulative = np.zeros(256)
histogram_values_2_cumulative[0] = histogram_values[0]
for i  in range(1,256):
    histogram_values_2_cumulative[i] = histogram_values[i]+histogram_values_2_cumulative[i-1]

histogram_equalization_pixel_matching_2 = np.zeros(256)
Hmin=histogram_values_2_cumulative[LOWEST_PIXEL_VALUE]
for i in range(256):
    dividend = histogram_values_2_cumulative[i]-Hmin
    divisor = m*n-Hmin
    histogram_equalization_pixel_matching_2[i] = round((dividend/divisor)*(MAX_PIXEL_VALUE))
        
new_image_2 = image.copy()
for i in range(m):
    for j in range(n):
        new_image_2[i][j] = histogram_equalization_pixel_matching_2[new_image_2[i][j]]

cv.imshow('Output 3', new_image_2)
difference_image_2 = image.copy()

for i in range(m):
    for j in range(n):
        difference_image_2[i][j] = abs(int(new_image_2[i][j]) - int(equ_opencv[i][j]))

cv.imshow('Difference2', difference_image_2)
print(difference_image_2)

# If any of the pixels of images OpenCv created and my second algorithm created are different
# It prints WRONG on the screen
for i in range(256):
    for j in range(256):
        if difference_image_2[i][j] != 0:
            print("WRONG")

cv.waitKey(0)

cv.destroyAllWindows()
