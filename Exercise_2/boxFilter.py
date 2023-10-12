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

# # 3x3 Filter
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

# Second Part
def box_filter_function_separate(m, n, image,box_filter_size):
    
    box_filter_image = image.copy()

    box_filter_upper_bound = int((box_filter_size / 2))
    box_filter_lower_bound = -box_filter_upper_bound
    for i in range(m):
        for j in range(n):
            total_of_values_pixels = 0
            for k in range(box_filter_lower_bound,box_filter_upper_bound+1):
                if i+k >= 0 and i+k<m:
                    total_of_values_pixels += image[i+k][j]
            box_filter_image[i][j] = int(total_of_values_pixels / box_filter_size)
    return box_filter_image

def tranpose_image(image):
    m,n = image.shape
    image_transposed = image.copy()
    for i in range(m):
        image_transposed[:,i] = image[i,:]
    return image_transposed

# 3x3 Filter Part 2 
box_filter_size = 3
# We pass through with first filter 
image_3_3_seperate_first = box_filter_function_separate(m,n,image,box_filter_size)
# Now we will get the transpose of the image and run the same filter again
# Better for cash performance
image_3_3_seperate_first_transpose = tranpose_image(image_3_3_seperate_first)
image_3_3_seperate_second = box_filter_function_separate(m,n,image_3_3_seperate_first_transpose,box_filter_size)
image_3_3_seperate_second_transpose = tranpose_image(image_3_3_seperate_second)
cv.imshow('output1_2_2', image_3_3_seperate_second_transpose)
cv.imshow('output1_3_2', image_3_3_openCv)
differenceImage_2_3_1 = getDifferenceImage(m,n,image_3_3_seperate_second_transpose,image_3_3_openCv)
cv.imshow('Difference_2_3_1', differenceImage_2_3_1)

#11x11 Filter Part 2 
box_filter_size = 11
# We pass through with first filter 
image_11_11_seperate_first = box_filter_function_separate(m,n,image,box_filter_size)
# Now we will get the transpose of the image and run the same filter again
# Better for cash performance
image_11_11_seperate_first_transpose = tranpose_image(image_11_11_seperate_first)
image_11_11_seperate_second = box_filter_function_separate(m,n,image_11_11_seperate_first_transpose,box_filter_size)
image_11_11_seperate_second_transpose = tranpose_image(image_11_11_seperate_second)
cv.imshow('output2_1_2', image_11_11_seperate_second_transpose)
cv.imshow('output2_2_2', image_11_11_openCv)
differenceImage_2_3_2 = getDifferenceImage(m,n,image_11_11_seperate_second_transpose,image_11_11_openCv)
cv.imshow('Difference_2_3_2', differenceImage_2_3_2)

#21x21 Filter Part 2 
box_filter_size = 21
# We pass through with first filter 
image_21_21_seperate_first = box_filter_function_separate(m,n,image,box_filter_size)
# Now we will get the transpose of the image and run the same filter again
# Better for cash performance
image_21_21_seperate_first_transpose = tranpose_image(image_21_21_seperate_first)
image_21_21_seperate_second = box_filter_function_separate(m,n,image_21_21_seperate_first_transpose,box_filter_size)
image_21_21_seperate_second_transpose = tranpose_image(image_21_21_seperate_second)
cv.imshow('output3_1_2', image_21_21_seperate_second_transpose)
cv.imshow('output3_2_2', image_21_21_openCv)
differenceImage_2_3_3 = getDifferenceImage(m,n,image_21_21_seperate_second_transpose,image_21_21_openCv)
cv.imshow('Difference_2_3_3', differenceImage_2_3_3)

cv.waitKey(0)