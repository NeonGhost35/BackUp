import os
import zipfile 
from tkinter import *

def clickclack():
    userdir = txt.get()
    dirtobackup = txt2.get()

    backup = zipfile.ZipFile(userdir, "w")

    for floder, subfloders, files in os.walk(dirtobackup):
        for file in files:
            backup.write(os.path.join(floder, file), os.path.relpath(os.path.join(floder, file), dirtobackup), compress_type = zipfile.ZIP_DEFLATED)
    comp = ("Complete!")
    lbl3.configure(text = comp)
window = Tk()
window.title("BackUp v 1.0")

lbl = Label(text = "Welcome!")
lbl.grid(column = 0, row = 1)

lbl1 = Label(text = "path/to/backup.zip: ")
lbl1.grid(column = 0, row = 3)

lbl2 = Label(text = "Enter Dir to BackUp: ")
lbl2.grid(column = 0, row = 4)

lbl3 = Label(text = "")
lbl3.grid(column = 0, row = 6)

txt = Entry(window, width=20)
txt.grid(column = 1, row = 3 )

txt2 = Entry(window, width=20)
txt2.grid(column = 1, row = 4 )

btn = Button(window, text = "BackUp", command=clickclack, width = 10)
btn.grid(column= 1, row = 7)

window.geometry('400x250')
window.mainloop()
