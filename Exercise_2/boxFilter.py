import cv2 as cv
import os

print(os.getcwd())
image = cv.imread('lena_grayscale_hq.jpg',cv.IMREAD_GRAYSCALE)

m,n = image.shape

box_filter_size = 0
print(str(m)+"   "+ str(n))
# Getting filter size
while True:
    try:
        user_input = input("Enter an integer: ")
        box_filter_size = int(user_input)
        if box_filter_size<0:
            raise ValueError("Box filter size cannot be negative")
        elif box_filter_size == 0:
            raise ValueError("Box filter size cannot be zero")
        elif box_filter_size > m or box_filter_size >n:
            raise ValueError("Box filter size cannot be greater than row or column size of image")
        print("Successfully converted to integer:", box_filter_size)
        break  # Exit the loop if conversion is successful

    except ValueError as e:
        print("Error:",e)

print(type(box_filter_size))

cv.imshow('Deneme 1',image)

cv.waitKey(0)