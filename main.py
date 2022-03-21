import cv2 as cv
import numpy as np
import Filter
import matplotlib.pyplot as plt


def main():
    #True for ABS False for square root(euklides metod)
    normalization = False


    #load a image
    image_name='./test-easy.png'
    src=cv.imread(image_name,cv.IMREAD_COLOR)





    out=Filter.sobel(src,normalization)


    cv.imshow('okno',out)
    cv.waitKey(0)
    cv.destroyAllWindows()

    #plt.imshow(out,cmap='gray')
    #plt.show()


main()




