from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename



def open_file():

    filetypes = (
        ('png files', '*.png'),
        ('jpeg files','*.jpg'),
        ('bmp files','*.bmp'),
        ('tif files', '*.tif','*.tiff'),

    )
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename(filetypes==filetypes)  # show an "Open" dialog box and return the path to the selected file

    return filename
