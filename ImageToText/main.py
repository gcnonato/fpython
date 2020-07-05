import os
import time
from datetime import date
from pathlib import Path
from time import strftime
from tkinter import *
from tkinter.ttk import Combobox

from PIL import Image, ImageTk

PATH_IMG = os.path.abspath('img')
LIST_IMG = [f for f in os.listdir(PATH_IMG)]
ASSET_DIR = Path(__file__).parent / Path('assets')

hj = date.today()
dias = ('Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom')
mes = {1: 'jan', 2: 'fev', 3: 'mar', 4: 'abr', 5: 'maio', 6: 'jun',
       7: 'jul', 8: 'ago', 9: 'set', 10: 'out', 11: 'nov', 12: 'dez'}
janela = Tk()
dia_la = Label(
  janela,
  text=(f'{dias[hj.weekday()]}, {str(hj.day)} de {str(mes[hj.month])} de {str(hj.year)}'),
  font='Helvita 25 bold',
  fg='blue'
)
dia_la.place(x=200, y=350)

rel = Label(janela, font='Helvita 20 bold', fg='blue')
rel.place(x=625, y=350)


def contador():  # funcao contador
  agora = strftime('%H:%M:%S')
  if rel['text'] != agora:
    rel['text'] = agora
  rel.after(100, contador)


contador()

welcome = Label(janela, text=['text'], font='Helvita 30 bold', fg='blue')
welcome.place(x=1500, y=1500)


def upwel():
  agora = strftime('%H:%M:%S')
  if agora <= str(12):
    welcome['text'] = ('Good Morning!')
  elif agora <= str(18):
    welcome['text'] = ('Good Afternoon!')
  else:
    welcome['text'] = ('Good Night!')
  welcome.after(100, upwel)


upwel()

janela.title('Sistema - Image to Text')
janela.config()
janela.geometry('750x600')


def load_image(filename):
  image = Image.open(filename)
  photo = ImageTk.PhotoImage(image)
  return photo


class Aplication:
  def __init__(self, master, *args, **kwargs):
    self.master = master
    self.Date1 = StringVar()
    self.Date1.set(time.strftime("%d/%m/%Y"))

    self.menu = Frame(master,
                      width=200, height=500, bg='#222125', bd=10, relief='raise')
    self.menu.pack(side=LEFT)

    self.title = Label(master,
                       text='Transform image to text', font=('arial', 25, 'bold'))
    self.title.pack()

    altura = 2
    largura = 12

    self.caixa = Button(self.menu, text='List Images', fg='#f97303',
                        bg='#505157', bd=10, relief='raise',
                        width=largura, height=altura,
                        font=('comic sans ms', 15, 'bold'),
                        command=self.home_caixa).place(x=1, y=3)

  def home_caixa(self):
    # call(['python','read_images.py'])
    self.tela1 = Toplevel()
    self.imagem3 = load_image(f'{ASSET_DIR}/logo.gif')

    self.frame1 = Frame(self.tela1,
                        width=400, height=600, relief="raise")
    self.frame1.pack(side=LEFT)

    self.btn_logo = Label(self.frame1, text='Testar...', bg='light blue',
                          width=127, height=150,
                          image=self.imagem3)
    self.btn_logo.place(x=12, y=0)

    # self.lblDate = Label(self.frame1, textvariable=self.Date1,
    #         font=('arial', 18, 'bold'), padx=1, pady=1,
    #         bd=10, bg="#004400", fg="Cornsilk", justify=LEFT,
    #         width=20
    #         )
    # self.lblDate.place(x=158, y=0)

    self.images = Combobox(self.frame1, height=4, width=20, )
    self.images['values'] = self.getImages()
    image_choice = self.images.get()
    self.images.place(x=12, y=160)

    self.btn_busca_Totais = Button(self.frame1,
                                   text='OK', bg='RoyalBlue1',
                                   pady=1, padx=1, bd=2, width=5, height=2,
                                   font=('Arial', 12, 'bold'), fg='black',
                                   command=self.cadastraContas
                                   )
    self.btn_busca_Totais.place(x=12, y=190)

    self.frame2 = Frame(self.tela1,
                        width=600, height=700, bd=8, relief="raise")
    self.frame2.pack(side=RIGHT)

  def getImages(self):
    arrayImages = []
    for item in LIST_IMG:
      arrayImages.append(item)
    return arrayImages

  def cadastraContas(self, id_conta=None):
    image_choice = self.images.get()
    ASSET_DIR = Path(__file__).parent / Path('img')
    self.imagem = load_image(f'{ASSET_DIR}/{image_choice}')

    self.btn_logo = Label(self.frame2,
                          pady=1, bg='light blue', padx=1, bd=2, width=497, height=590,
                          image=self.imagem)
    self.btn_logo.place(x=0, y=0)


app = Aplication(janela)
janela.mainloop()
