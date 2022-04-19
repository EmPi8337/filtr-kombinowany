from tkinter import Image

import cv2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from matplotlib import pyplot as plt
import cv2 as cv
from numpy import uint8

import Filter
import tkinter as tk


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

#     root = tk.Toplevel()
#
#     klyk = tk.Button(root, text="inny obrazek", command=root.destroy)
#     klyk.pack()
#
#
#     img_scaled = cv2.resize(combinated_image, dsize=(500, 500), interpolation=cv2.INTER_CUBIC)
#     img1 = ImageTk.PhotoImage(image=Image.fromarray(img_scaled))
#
#     img2 = ImageTk.PhotoImage(image=Image.fromarray(grad_v_left))
#     imedz = Image.fromarray(img)
#     canvas = tk.Canvas(root, width=1920, height=1080)
#     canvas.pack()
#
#     # canvas.create_image((100, 100), image=img1)  # center
#
#     canvas.create_image((0, 150), image=img1, anchor='nw')  # top, left corner
#
#     # canvas.create_image((1000, 150), image=img2, anchor='nw')  # top, right corner
#     # canvas.create_image((200, 200), image=img, anchor='se')  # bottom, right corner
#     # canvas.create_image((0, 200), image=img, anchor='sw')  # bottom, left corner
#
#     root.mainloop()
#
#
#
#
#
# def okno():
#
#     filename = askopenfilename()
#     src = cv.imread(filename, cv.IMREAD_COLOR)
#     a, b, c, d = Filter.sobel(src, False)
#     show(a, b, c, d)