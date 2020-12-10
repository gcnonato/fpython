# -*- coding: utf-8 -*-
from tkinter import (
    Tk, Label, StringVar, Entry, Button
)
from tkinter import filedialog

root = Tk()
root.geometry("400x200+100+200")


def open():
    root.filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select A File",
        filetypes=(("jpg files", "*.JPG"), ("all files", "*.*")),
    )
    Label(root, text=root.filename).grid(row=2, column=10)
    StringVar()
    Entry(root, text=root.filename).grid(row=3, column=1)


my_btn = Button(root, text="Open files", command=open).grid(row=1, column=0)
txt2 = Entry(root).grid(row=2, column=1)
root.mainloop()
