import cv2 as cv
import numpy as np
from cv2 import COLOR_BGR2GRAY


def prepare(src: int):
    # convert color to grayscale
    src_gray: int = cv.cvtColor(src, COLOR_BGR2GRAY)
    # reduce noise
    src_gray = cv.GaussianBlur(src_gray, (3, 3), 0)

    return src_gray


def perwitt(src: int, normalization: bool):
    # get converted image
    img = filter.prepare(src)
    # initialize  kernels
    vertical = np.array([[-1, 0, 1],
                         [-1, 0, 1],
                         [-1, 0, 1]])
    horizontal = np.array([[1, 1, 1],
                           [0, 0, 0],
                           [-1, -1, -1]])

    # compute vertical gradients from left to right and vice versa
    grad_v_left = cv.filter2D(img, -1, vertical, borderType=cv.BORDER_DEFAULT)
    grad_v_right = cv.filter2D(img, -1, np.fliplr(vertical), borderType=cv.BORDER_DEFAULT)
    # compute horizontal gradients from up to down and vice versa
    grad_h_up = cv.filter2D(img, -1, horizontal, borderType=cv.BORDER_DEFAULT)
    grad_h_down = cv.filter2D(img, -1, np.flipud(horizontal), borderType=cv.BORDER_DEFAULT)

    """
    # combine vertical gradients together
    grad_v = cv.addWeighted(grad_v_left, 1, grad_v_right, 1, 0)
    #grad_v = np.add(grad_v_left,grad_v_right)
    # combine horizontal gradients together
    grad_h = cv.addWeighted(grad_h_up, 1, grad_h_down, 1, 0)
    #grad_h = np.add(grad_h_up, grad_h_down)
    """

    # normalize image
    if normalization == False:
        combinated_image = euklides(grad_v_left, grad_h_up)
    elif normalization == True:
        combinated_image = sum_of_abs(grad_v_left, grad_h_up)

    return combinated_image


def roberts(src: int, normalization: bool):
    # get converted image
    img = filter.prepare(src)
    # initialize sobel gradients
    vertical = np.array([[0, 0, 0],
                         [-1, 0, 0],
                         [0, 1, 0]], dtype=np.int8)
    horizontal = np.array([[0, 0, 0],
                           [0, 0, -1],
                           [0, 1, 0]], dtype=np.int8)

    # compute vertical gradients from left to right and vice versa
    grad_v_left = cv.filter2D(img, -1, vertical, borderType=cv.BORDER_DEFAULT)
    grad_v_right = cv.filter2D(img, -1, np.fliplr(vertical), borderType=cv.BORDER_DEFAULT)
    # compute horizontal gradients from up to down and vice versa
    grad_h_up = cv.filter2D(img, -1, horizontal, borderType=cv.BORDER_DEFAULT)
    grad_h_down = cv.filter2D(img, -1, np.flipud(horizontal), borderType=cv.BORDER_DEFAULT)

    """
    # combine vertical gradients together
    grad_v = cv.addWeighted(grad_v_left, 1, grad_v_right, 1, 0)
    #grad_v = np.add(grad_v_left,grad_v_right)
    # combine horizontal gradients together
    grad_h = cv.addWeighted(grad_h_up, 1, grad_h_down, 1, 0)
    #grad_h = np.add(grad_h_up, grad_h_down)
    """

    # normalize image
    if normalization == False:
        combinated_image = euklides(grad_v_left, grad_h_up)
    elif normalization == True:
        combinated_image = sum_of_abs(grad_v_left, grad_h_up)

    return combinated_image


def sobel(src: int, normalization: bool):
    # get grayscale image with reduced noise
    img = filter.prepare(src)
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

    """
    # combine vertical gradients together
    grad_v = cv.addWeighted(grad_v_left, 1, grad_v_right, 1, 0)
    #grad_v = np.add(grad_v_left,grad_v_right)
    # combine horizontal gradients together
    grad_h = cv.addWeighted(grad_h_up, 1, grad_h_down, 1, 0)
    #grad_h = np.add(grad_h_up, grad_h_down)
    """

    # normalize image
    if normalization == False:
        combinated_image = euklides(grad_v_left, grad_h_up)
    elif normalization == True:
        combinated_image = sum_of_abs(grad_v_left, grad_h_up)

    return combinated_image, grad_v_left, grad_h_up


def euklides(grad_v_left: int, grad_h_up: int):
    # compute sqrt of vertical and horizontal gradients
    grad_magnitude = cv.addWeighted(grad_v_left, 1, grad_h_up, 1, 0)

    return grad_magnitude


def sum_of_abs(grad_v_left: int, grad_h_up: int):
    # compute abs of vertical and horizontal gradients
    abs_v = cv.convertScaleAbs(grad_v_left)
    abs_h = cv.convertScaleAbs(grad_h_up)
    # sum of gradients
    grad_magnitude = cv.addWeighted(abs_v, 1, abs_h, 1, 0)

    return grad_magnitude
