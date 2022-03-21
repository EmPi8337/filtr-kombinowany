import cv2 as cv
import numpy as np
from cv2 import COLOR_BGR2GRAY

import Filter
def prepare(src: int):

    #convert color to grayscale
    src_gray: int = cv.cvtColor(src, COLOR_BGR2GRAY)

    return src_gray

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

    #reduce noise
    src_gray = cv.GaussianBlur(src_gray, (3, 3), 0)
    #compute vertical gradient
    grad_vl = cv.filter2D(src_gray, -1, vertical_left)
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