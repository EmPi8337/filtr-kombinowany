from matplotlib import pyplot as plt


def show(combinated_image: int, grad_v_left: int, grad_h_up: int):
    plt.imshow(combinated_image, cmap='gray')
    plt.imshow(grad_v_left, cmap='gray')
    plt.imshow(grad_h_up, cmap='gray')
    plt.show()