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
    #initialize sobel gradients
    sobel_v=np.array([[-1,0,1],
                      [-2,0,2],
                      [-1,0,1]])
    sobel_h=np.array([[1,2,1],
                      [0,0,0],
                      [-1,-2,-1]])

    #reduce noise
    src_gray = cv.GaussianBlur(src_gray, (3, 3), 0)
    #compute vertical gradient
    grad_y = cv.filter2D(src_gray, -1, sobel_v)
    #compute horizontal gradient
    grad_x = cv.filter2D(src_gray, -1, sobel_h)

    #normalization and concatination of image
    if normalization == True:
        abs_grad_x = cv.convertScaleAbs(grad_x)
        abs_grad_y = cv.convertScaleAbs(grad_y)
        grad_norm = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
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