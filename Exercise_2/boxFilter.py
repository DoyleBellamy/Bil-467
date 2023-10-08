import cv2 as cv
import os 
import numpy as np
#First Part
image = cv.imread(os.path.join(os.getcwd(),'lena_grayscale_hq.jpg'),cv.IMREAD_GRAYSCALE)

m,n = image.shape

def box_filter_function(m, n, image,box_filter_size):
    #Box filter size User Input Part

    # box_filter_size = 0
    # # Getting filter size
    # while True:
    #     try:
    #         user_input = input("Enter box filter size: ")
    #         box_filter_size = int(user_input)
    #         if box_filter_size<0:
    #             raise ValueError("Box filter size cannot be negative")
    #         elif box_filter_size == 0:
    #             raise ValueError("Box filter size cannot be zero")
    #         elif box_filter_size % 2 == 1:
    #             raise ValueError("Box filter size cannot be odd number")
    #         elif box_filter_size > m or box_filter_size >n:
    #             raise ValueError("Box filter size cannot be greater than row or column size of image")
    #         break  # Exit the loop if conversion is successful

    #     except ValueError as e:
    #         print("Error:",e)

    box_filter_image = image.copy()

    box_filter_upper_bound = int((box_filter_size / 2))
    box_filter_lower_bound = -box_filter_upper_bound

    divider_box_filter = box_filter_size ** 2
    for i in range(m):
        for j in range(n):
            total_of_values_pixels = 0
            for k in range(box_filter_lower_bound,box_filter_upper_bound+1):
                for l in range(box_filter_lower_bound,box_filter_upper_bound+1):
                    if((i+l) >= 0 and (j+k) >= 0 and (i+l) < m and (j+k) < n):
                        total_of_values_pixels += image[i+l][j+k]
            box_filter_image[i][j] = int(total_of_values_pixels / divider_box_filter)
    
    return box_filter_image

def openCVBoxFilter(box_filter_size):
    kernel = np.ones((box_filter_size,box_filter_size),np.float32)/(box_filter_size**2)
    padding_size = int(box_filter_size/2)
    image_padded = cv.copyMakeBorder(image,padding_size,padding_size,padding_size,padding_size,cv.BORDER_CONSTANT,value = 0)
    dst = cv.filter2D(image_padded,-1,kernel)
    result_1_1 = dst[padding_size:-padding_size,padding_size:-padding_size]

    return result_1_1

def getDifferenceImage(m,n,image1,image2):
    difference_image_1_2 = image.copy()
    for i in range(m):
        for j in range(n):
            difference_image_1_2[i][j] = abs(int(image1[i][j]) - int(image2[i][j]))
            if difference_image_1_2[i][j] > 3:
                print("HATA")
    return difference_image_1_2

cv.imshow('Input image',image)

# 3x3 Filter
box_filter_size = 3
image_3_3 = box_filter_function(m,n,image,box_filter_size)
cv.imshow('output1_1', image_3_3)
image_3_3_openCv = openCVBoxFilter(box_filter_size)
cv.imshow('output1_2', image_3_3_openCv)
differenceImage_1_2_1 = getDifferenceImage(m,n,image_3_3,image_3_3_openCv)
cv.imshow('Difference_1_2_1', differenceImage_1_2_1)

# 11x11 Filter
box_filter_size = 11
image_11_11 = box_filter_function(m,n,image,box_filter_size)
cv.imshow('output2_1', image_11_11)
image_11_11_openCv = openCVBoxFilter(box_filter_size)
cv.imshow('output2_2', image_11_11_openCv)
differenceImage_1_2_2 = getDifferenceImage(m,n,image_11_11,image_11_11_openCv)
cv.imshow('Difference_1_2_2', differenceImage_1_2_2)

# 21x21 Filter
box_filter_size = 21
image_21_21 = box_filter_function(m,n,image,box_filter_size)
cv.imshow('output3_1', image_21_21)
image_21_21_openCv = openCVBoxFilter(box_filter_size)
cv.imshow('output3_2', image_21_21_openCv)
differenceImage_1_2_3 = getDifferenceImage(m,n,image_21_21,image_21_21_openCv)
cv.imshow('Difference_1_2_3', differenceImage_1_2_3)

cv.waitKey(0)