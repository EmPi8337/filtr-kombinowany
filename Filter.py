import math
from math import sqrt

import cv2 as cv
import numpy as np
from cv2 import COLOR_BGR2GRAY, CV_32F, CV_16S, CV_64F, CV_8U
import matplotlib.pyplot as plt

import Filter
def prepare(src: int):

    #convert color to grayscale
    src_gray: int = cv.cvtColor(src, COLOR_BGR2GRAY)
    # reduce noise
    src_gray = cv.GaussianBlur(src_gray, (3, 3), 0)

    return src_gray

"""
def sobel(src: int, normalization: bool):

    #get converted image
    src_gray=Filter.prepare(src)
    #src_gray = src
    #initialize sobel gradients
    vertical_left = np.array([[-1, 0, 1],
                                [-2, 0, 2],
                                [-1, 0, 1]])
    vertical_right = np.array([[1, 0, -1],
                              [2, 0, -2],
                              [1, 0, -1]])
    horizontal_down = np.array([[1, 2, 1],
                                [0, 0, 0],
                                [-1, -2, -1]])
    horizontal_up = np.array([[-1, -2, -1],
                               [0, 0, 0],
                               [1, 2, 1]])



    #compute vertical gradient
    grad_vl = cv.filter2D(src_gray, -1, vertical_left, borderType=cv.BORDER_DEFAULT)
    grad_vr = cv.filter2D(src_gray, -1, vertical_right)
    #compute horizontal gradient
    grad_hd = cv.filter2D(src_gray, -1, horizontal_down)
    grad_hu = cv.filter2D(src_gray, -1, horizontal_up)

    #normalization and concatination of image
    if normalization == True:
        abs_grad_vl = cv.convertScaleAbs(grad_vl)
        abs_grad_vr = cv.convertScaleAbs(grad_vr)
        abs_grad_hd = cv.convertScaleAbs(grad_hd)
        abs_grad_hu = cv.convertScaleAbs(grad_hu)
        grad_norm1 = cv.addWeighted(abs_grad_vl, 0.5, abs_grad_vr, 0.5, 0)
        grad_norm2 = cv.addWeighted(abs_grad_hd, 0.5, abs_grad_hu, 0.5, 0)
        grad_norm = cv.addWeighted(grad_norm2, 0.5, grad_norm1, 0.5, 0)
    elif normalization == False:
        grad_norm = cv.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

    return grad_norm
"""

def perwitt(src: int, normalization: bool):

    #get converted image
    src_gray=filter.prepare(src)
    #initialize sobel gradients
    perwitt_v=np.array([[-1, 0, 1],
                      [-1, 0, 1],
                      [-1, 0, 1]])
    perwitt_h=np.array([[1, 1, 1],
                      [0, 0, 0],
                      [-1, -1, -1]])

    #reduce noise
    src_gray = cv.GaussianBlur(src_gray, (3, 3), 0)
    #compute vertical gradient
    grad_y = cv.filter2D(src_gray, -1, perwitt_v)
    #compute horizontal gradient
    grad_x = cv.filter2D(src_gray, -1, perwitt_h)

    #normalization and concatination of image
    if normalization == True:
        abs_grad_x = cv.convertScaleAbs(grad_x)
        abs_grad_y = cv.convertScaleAbs(grad_y)
        grad_norm = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    elif normalization == False:
        grad_norm = cv.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

    return grad_norm

def roberts(src: int, normalization: bool):

    #get converted image
    src_gray=filter.prepare(src)
    #initialize sobel gradients
    roberts_v = np.array([[0,0,0],
                          [-1,0,0],
                          [0,1,0]])
    roberts_h = np.array([[0,0,0],
                          [0,0,-1],
                          [0,1,0]])
    #reduce noise
    src_gray = cv.GaussianBlur(src_gray, (3, 3), 0)
    #compute vertical gradient
    grad_y = cv.filter2D(src_gray, -1, roberts_v)
    #compute horizontal gradient
    grad_x = cv.filter2D(src_gray, -1, roberts_h)

    #normalization and concatination of image
    if normalization == True:
        abs_grad_x = cv.convertScaleAbs(grad_x)
        abs_grad_y = cv.convertScaleAbs(grad_y)
        grad_norm = cv.addWeighted(abs_grad_x, 1.5, abs_grad_y, 1.5, 0)
    elif normalization == False:
        grad_norm = cv.addWeighted(grad_x, 1.5, grad_y, 1.5, 0)

    grad_norm = np.multiply(grad_norm,2)
    print(np.max(grad_norm))
    return grad_norm

def sobel_better(src: int, normalization: bool):

    # get grayscale image with reduced noise
    img = prepare(src)
    # initialize kernels
    vertical = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]], dtype=np.int8)
    horizontal = np.array([[-1, -2, -1],
                            [0, 0, 0],
                            [1, 2, 1]], dtype=np.int8)

    # compute vertical gradients from left to right and vice versa
    grad_v_left = cv.filter2D(img, -1, vertical, borderType=cv.BORDER_DEFAULT)
    grad_v_right = cv.filter2D(img, -1, np.fliplr(vertical), borderType=cv.BORDER_DEFAULT)
    # compute horizontal gradients from up to down and vice versa
    grad_h_up = cv.filter2D(img, -1, horizontal, borderType=cv.BORDER_DEFAULT)
    grad_h_down = cv.filter2D(img, -1, np.flipud(horizontal), borderType=cv.BORDER_DEFAULT)

    # combine vertical gradients together
    grad_v = cv.addWeighted(grad_v_left, 1, grad_v_right, 1, 0)
    #grad_v = np.add(grad_v_left,grad_v_right)
    # combine horizontal gradients together
    grad_h = cv.addWeighted(grad_h_up, 1, grad_h_down, 1, 0)
    #grad_h = np.add(grad_h_up, grad_h_down)




    # normalize image
    if normalization == False:
        combinated_image = euklides(grad_v, grad_h)
    elif normalization == True:
        print("asd")
        #combinated_image = absolute(grad_v, grad_h)

    return combinated_image

def euklides(grad_v: int, grad_h: int):

    # compute sqrt of vertical and horizontal gradients
    grad_magnitude = np.square(grad_v) + np.square(grad_h)
    ###
    #plt.imshow(grad_magnitude, cmap='gray')
    #plt.show()
    cv.imshow('okno',grad_magnitude)
    cv.waitKey(0)
    cv.destroyAllWindows()
    ###
    #for x in grad_magnitude:
    #    math.trunc(sqrt(x))
    # normalize it between 0 and 255
    #grad_magnitude *= 255 / grad_magnitude.max()

    #return grad_magnitude