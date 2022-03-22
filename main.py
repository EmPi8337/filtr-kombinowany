import cv2 as cv
import Filter
import display


def menu():
    print("[1] lena_std.tif")
    print("[2] jet.bmp")
    print("[3] test-easy.png")
    print("[4] test-hard.png")
    test_image = input("Select File: ")
    print("[1] sum of abs")
    print("[2] euklidesian")
    normalization_metod = input("Select normalization metod: ")


    return test_image, normalization_metod


def main():

    select = menu()

    # True for ABS False for square root(euklides metod)
    normalization = select.test_image

    # load a image
    image_name = './'+select.normalization_metod
    src = cv.imread(image_name, cv.IMREAD_COLOR)

    out = Filter.sobel(src, normalization)

    display.show(out.combinated_image, out.grad_v_left, out.grad_h_up)



main()
