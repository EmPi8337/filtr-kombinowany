
from tkinter.filedialog import askopenfilename

import cv2 as cv


import Filter
import display
import tkinter as tk
import cv2
from PIL import Image, ImageTk


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


filename = "images/people&animals/lena_std.tif"
lang="EN"
root = tk.Tk()


def okno(lang):
    filename = askopenfilename(filetypes=[('Images',('*.png','*.tif','*.jpg','*.bmp'))])
    main(filename,lang)


def main(filename,lang):
    # path = display.okno();
    # select = menu()

    # True for ABS False for square root(euklides metod)
    # normalization = select.test_image

    # load a image
    # image_name = './'+select.normalization_metod
    path = "./images/" + "artificial/"
    name = "test-easy.png"

    src = cv.imread(filename, cv.IMREAD_COLOR)


    s_euk_comb, s_abs_comb, s_grad_v_left, s_grad_h_up, s_img = Filter.sobel(src, True)
    r_euk_comb, r_abs_comb, r_grad_v_left, r_grad_h_up, r_img = Filter.roberts(src, True)
    p_euk_comb, p_abs_comb, p_grad_v_left, p_grad_h_up, p_img = Filter.perwitt(src, True)



    tk_image = ImageTk.PhotoImage(
        image=Image.fromarray(cv2.resize(s_img, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)))

    tk_s_euk_comb = ImageTk.PhotoImage(
        image=Image.fromarray(cv2.resize(s_euk_comb, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)))
    tk_s_abs_comb = ImageTk.PhotoImage(
        image=Image.fromarray(cv2.resize(s_abs_comb, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)))
    tk_s_grad_v_left = ImageTk.PhotoImage(
        image=Image.fromarray(cv2.resize(s_grad_v_left*-1+128, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)))
    tk_s_grad_h_up = ImageTk.PhotoImage(
        image=Image.fromarray(cv2.resize(s_grad_h_up*-1+128, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)))

    tk_p_euk_comb = ImageTk.PhotoImage(
        image=Image.fromarray(cv2.resize(p_euk_comb, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)))
    tk_p_abs_comb = ImageTk.PhotoImage(
        image=Image.fromarray(cv2.resize(p_abs_comb, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)))
    tk_p_grad_v_left = ImageTk.PhotoImage(
        image=Image.fromarray(cv2.resize(p_grad_v_left*-1+128, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)))
    tk_p_grad_h_up = ImageTk.PhotoImage(
        image=Image.fromarray(cv2.resize(p_grad_h_up*-1+128, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)))

    tk_r_euk_comb = ImageTk.PhotoImage(
        image=Image.fromarray(cv2.resize(r_euk_comb, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)))
    tk_r_abs_comb = ImageTk.PhotoImage(
        image=Image.fromarray(cv2.resize(r_abs_comb, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)))
    tk_r_grad_v_left = ImageTk.PhotoImage(
        image=Image.fromarray(cv2.resize(r_grad_v_left*-1+128, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)))
    tk_r_grad_h_up = ImageTk.PhotoImage(
        image=Image.fromarray(cv2.resize(r_grad_h_up*-1+128, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)))
##################
    podpis1 = tk.Label()
    podpis2 = tk.Label()
    podpis3 = tk.Label()
    podpis4 = tk.Label()

    varlang = tk.StringVar()
    varlang.set(lang)

    def langchange():
        if varlang.get() == "EN":
            root.title("Combination Filter")
            podpis1.config(text="Prepared image")
            podpis2.config(text="Vertical gradient")
            podpis3.config(text="Horizontal gradient")
            podpis4.config(text="   Result image  ")
            file.config(text="Choose image")
            norm1.config(text=" ABS \n method ")
            norm2.config(text=" Euclidean \n method ")
        if varlang.get() == "PL":
            root.title("Filtr Kombinowany")
            podpis1.config(text="Obraz wejściowy")
            podpis2.config(text="Gradient pionowy")
            podpis3.config(text="Gradient poziomy")
            podpis4.config(text="Obraz wynikowy")
            file.config(text="Wybierz obraz")
            norm1.config(text="Formuła\nmodułowa")
            norm2.config(text="Formuła\nEuklidesowa")



    en = tk.Radiobutton(root, text="EN", variable=varlang, value="EN", command=langchange)
    pl = tk.Radiobutton(root, text="PL", variable=varlang, value="PL",command=langchange)

    ###################
    file = tk.Button(root, command=lambda: okno(varlang.get()))


    mylabel1 = tk.Label(image=tk_image)
    mylabel2 = tk.Label(image=tk_s_grad_h_up)
    mylabel3 = tk.Label(image=tk_s_grad_v_left)
    mylabel4 = tk.Label(image=tk_s_abs_comb)
    ###########
    podpis2.grid(row=0,column=3,columnspan=3)
    en.grid(row=1,column=1)
    pl.grid(row=1,column=0)
    podpis1.grid(row=3, column=0, columnspan=2)
    podpis4.grid(row=3, column=7 )
    podpis3.grid(row=6, column=3, columnspan=3)
    ############3
    mylabel1.grid(row=4, column=0,columnspan=2,rowspan=2)
    mylabel2.grid(row=1, column=3, columnspan=3,rowspan=2)
    file.grid(row=2, column=0,columnspan=2)
    mylabel3.grid(row=7, column=3, columnspan=3)
    mylabel4.grid(row=4, column=7,rowspan=2)

    varnorm = tk.BooleanVar()
    varnorm.set(True)

    vargrad = tk.StringVar()
    vargrad.set("Sobel")

    def zmianka():

        if vargrad.get() == "Sobel":
            mylabel2.config(image=tk_s_grad_h_up)
            mylabel3.config(image=tk_s_grad_v_left)
            if varnorm.get() == True:
                mylabel4.config(image=tk_s_abs_comb)
            else:
                mylabel4.config(image=tk_s_euk_comb)

        elif vargrad.get() == "Roberts":
            mylabel2.config(image=tk_r_grad_h_up)
            mylabel3.config(image=tk_r_grad_v_left)
            if varnorm.get() == True:
                mylabel4.config(image=tk_r_abs_comb)
            else:
                mylabel4.config(image=tk_r_euk_comb)

        elif vargrad.get() == "Perwitt":
            mylabel2.config(image=tk_p_grad_h_up)
            mylabel3.config(image=tk_p_grad_v_left)
            if varnorm.get() == True:
                mylabel4.config(image=tk_p_abs_comb)
            else:
                mylabel4.config(image=tk_p_euk_comb)

    norm1 = tk.Radiobutton(root, variable=varnorm, value=True, command=zmianka)
    norm1.grid(row=5, column=3)
    norm2 = tk.Radiobutton(root, variable=varnorm, value=False, command=zmianka)
    norm2.grid(row=5, column=4,columnspan=2)

    grad1 = tk.Radiobutton(root, text="Sobel", variable=vargrad, value="Sobel", command=zmianka)
    grad1.grid(row=4, column=3)
    grad1 = tk.Radiobutton(root, text="Roberts", variable=vargrad, value="Roberts", command=zmianka)
    grad1.grid(row=4, column=4)
    grad1 = tk.Radiobutton(root, text="Perwitt", variable=vargrad, value="Perwitt", command=zmianka)
    grad1.grid(row=4, column=5)
    langchange()
    root.mainloop()


main(filename,lang)
