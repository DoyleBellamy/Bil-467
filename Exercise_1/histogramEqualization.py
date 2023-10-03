import cv2 as cv
import numpy as np
import math

#First Part

image = cv.imread('test1.jpg',cv.IMREAD_GRAYSCALE)

m,n = image.shape
TOTAL_PIXEL = m*n
MAX_PIXEL_VALUE = 255
print(image.shape)

histogram_values = np.zeros(256)

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
histogram_values_2 = np.zeros(256)
lowest_pixel_value = 255
for i in range(m):
    for j in range(n):
        if image[i][j]<lowest_pixel_value:
            lowest_pixel_value = image[i][j]
        histogram_values_2[image[i][j]] += 1
histogram_values_2_cumulative = np.zeros(256)
histogram_values_2_cumulative[0] = histogram_values_2[0]
for i  in range(1,256):
    histogram_values_2_cumulative[i] = histogram_values_2[i]+histogram_values_2_cumulative[i-1]

histogram_equalization_pixel_matching_2 = np.zeros(256)
Hmin=histogram_values_2_cumulative[lowest_pixel_value]
for i in range(256):
        temp1 = histogram_values_2_cumulative[i]-Hmin
        temp2 = m*n-Hmin
        histogram_equalization_pixel_matching_2[i] = round((temp1/temp2)*255)
new_image_2 = image.copy()
for i in range(m):
    for j in range(n):
        new_image_2[i][j] = histogram_equalization_pixel_matching_2[new_image[i][j]]

cv.imshow('Output 3', new_image_2)
difference_image_2 = image.copy()
for i in range(m):
    for j in range(n):
        # print(str(new_image_2[i][j])+" and "+str(equ_opencv[i][j]))
        difference_image_2[i][j] = abs(int(new_image_2[i][j]) - int(equ_opencv[i][j]))
cv.imshow('Difference2', difference_image_2)
print(difference_image_2)
cv.waitKey(0)

cv.destroyAllWindows()
