from matplotlib import pyplot as plt
import cv2 as cv


def show(combinated_image: int, grad_v_left: int, grad_h_up: int, img: int):

    plt.figure(1)
    plt.subplot(221)
    plt.imshow(img, cmap='gray')
    plt.title("Przygotowany")

    plt.subplot(222)
    plt.imshow(grad_v_left, cmap='gray')
    plt.title("Gradient pionowy")

    plt.subplot(223)
    plt.imshow(grad_h_up, cmap='gray')
    plt.title("Gradient poziomy")

    plt.subplot(224)
    plt.imshow(combinated_image, cmap='gray')
    plt.title("Kombinacja")
    plt.show()