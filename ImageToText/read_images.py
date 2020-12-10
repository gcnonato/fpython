import os
import time
from subprocess import call
from tkinter import StringVar, Label, Frame, Button, Toplevel, Tk
from tkinter import PhotoImage, LEFT
from tkinter.ttk import Combobox

PATH_IMG = os.path.abspath("img")
LIST_IMG = [f for f in os.listdir(PATH_IMG)]


class Caixa:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.Date1 = StringVar()
        self.Date1.set(time.strftime("%d/%m/%Y"))

        self.img = PhotoImage(file="image/joao.gif")
        self.la_img = Label(master, image=self.img)
        self.la_img.place(x=1170, y=100)

        self.create_widgets(master)

    def create_widgets(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.images = Combobox(master, height=4, width=25)
        self.images["values"] = self.getImages()
        # self.images['values']=('SIM','NAO')
        # self.images.current(0)
        self.images.place(x=120, y=35)

        # =============================================================================================================
        #                                                   BOTÕES                                                    =
        # =============================================================================================================

        self.confirm = Button(
            master,
            text="Confirm Image",
            bg="#f17215",
            bd=2,
            relief="raise",
            width=15,
            height=2,
            command=self.cadastraContas(),
        )
        self.confirm.place(x=170, y=60)

    def novavenda(self):
        call(["python", "nova_venda.py"])

    def getImages(self):
        arrayImages = []
        for item in LIST_IMG:
            arrayImages.append(item)
        return arrayImages

    def button_images(self):
        ...

    def cadastraContas(self, id_conta=None):
        self.tela1 = Toplevel()
        image_choice = self.images.get()

        self.lblDate = Label(
            self.tela1,
            textvariable=self.Date1,
            font=("arial", 18, "bold"),
            padx=1,
            pady=1,
            bd=10,
            bg="#004400",
            fg="Cornsilk",
            justify=LEFT,
            width=20,
        )
        self.lblDate.pack()

        print(image_choice)

    def load_image(self):
        image_choice = self.images.get()
        return image_choice


janela = Tk()
app = Caixa(janela)
janela.title("Sistema - Image to Text")
# janela.state('zoomed')
janela.config()
janela.geometry("500x400")
janela.mainloop()
