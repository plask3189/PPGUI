import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time

# The website that I used for help: https://pythonguides.com/upload-a-file-in-python-tkinter/

window = tk.Tk()
window.title('Photo Phenosizer')
window.geometry('800x200') # width by height
canvas = Canvas()

#------------------- Introduction Text -------------------------------------------------------------
introTextLine1 = Label(window, text = 'Welcome to PhotoPhenosizer.')
introTextLine1.grid(row = 0, column = 0, padx = 10)

#------------------- Prerequisits Text -------------------------------------------------------------
introTextLine1 = Label(window, text = 'Ensure that you have the weights.pt file in the same folder as the images you would like to run.')
introTextLine1.grid(row = 2, column = 0, padx = 10)

# ------------------ Downloads check ---------------------------------------------------------------
# Ensuring all of the packages are downloaded which are necessary to run pp.


#-------------------- Upload folder with cell images and weights.pt --------------------------------
def open_file():
    file_path = askopenfile(mode = 'r', filetypes = [('Image Files', '.tif .pt')])
    if file_path is not None:
        pass

def uploadFiles():
    pb1 = Progressbar(window, orient=HORIZONTAL, length=300, mode='determinate')
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        window.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(window, text='File Uploaded Successfully!', foreground='green').grid(row=100, columnspan=3, pady=10)


uploadCellImageFolderLabel = Label(window, text='Upload a folder of cell photos to be analyzed.')
uploadCellImageFolderLabel.grid(row=120, column=0, padx=10)

uploadCellImageFolderButton = Button(window, text ='Choose File',command = lambda:open_file())
uploadCellImageFolderButton.grid(row=120, column=1)

#---------------- 




#canvas.pack()
window.mainloop()
