from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.geometry('400x200+100+200')

def open():
    root.filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select A File",
        filetypes=(
            ("jpg files", "*.JPG"),
            ("all files", "*.*")
        ),
    )
    my_label = Label(root, text=root.filename).grid(row=2, column=10)
    number1 = StringVar()
    entryNum1 = Entry(root, text=root.filename).grid(row=3, column=1)

my_btn = Button(root, text="Open files", command=open).grid(row=1, column=0)
# entry box
txt2 = Entry(root).grid(row=2, column=1)
# txt2.place(x=10, y=45)

root.mainloop()
