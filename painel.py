#!/usr/bin/ python3.7
# -*- coding: utf-8 -*-
from tkinter import *
import os, subprocess, shutil

ROOT_DIR = '/home/luxu/Desktop/'

class Application(Frame):

	def holerite(self):
		if (os.name != 'posix'):
			os.system("python.exe C:/Users/luxu/Desktop/python/selenium/holerite.py")
		else:
			os.system("python3.6 python/Desktop/holerite.py")
		self.quit

	def zap(self):
		if (os.name != 'posix'):
			os.system("luxucode zap")
		else:
			os.system("python3.6 python/Desktop/royale.py")
			subprocess.Popen(['mousepad','royale.txt'])
		self.quit

	def royale(self):
		if (os.name != 'posix'):
			os.system("ipython.exe C:/Users/luxu/Desktop/python/royale_with_selenium.py")
		else:
			os.system(f"ipython {ROOT_DIR}fpython/royale.py")
		self.quit

	def guiabolso(self):
		if (os.name != 'posix'):
			source = 'C:\\Users\\luxu\\Desktop'
			os.system("ipython.exe C:/Users/luxu/Desktop/python/guiabolso.py")
			files = [f for f in os.listdir('.') if f.startswith('Cheats')]
			for file in files:
				print(file)
				shutil.move(file, source)  ## to move files from
				print()
		else:
			os.system(f"ipython {ROOT_DIR}fpython/guiabolso.py")
			# subprocess.Popen(['gedit', 'royale.txt'])
		self.quit

	def youtube(self):
		if (os.name != 'posix'):
			os.chdir("C:/Users/luxu/Desktop/")
			os.system("python.exe C:/Users/luxu/Desktop/python/pegar_video.py")
		else:
			os.system(f"ipython {ROOT_DIR}fpython/pegar_video.py")
		self.quit

	def gastos(self):
		if (os.name != 'posix'):
			os.chdir("C:/Users/luxu/.virtualenvs/djangox-CVI14up0/Scripts/")
			subprocess.Popen(['start', 'activate'], shell=True)
		else:
			os.chdir("gastosluxu/venv/Scripts/")
		self.quit

	def verocard(self):
		if (os.name != 'posix'):
			os.system("python.exe C:/Users/luxu/Desktop/python/selenium/verocard.py")
		else:
			os.system("python3.6 python/selenium/verocard.py")
		self.quit

	def bdo(self):
		if (os.name != 'posix'):
			os.system("ipython.exe C:/Users/luxu/Desktop/python/selenium/badoo.py")
		else:
			os.system(f"ipython {ROOT_DIR}fpython/badoo_with_ff.py")
		self.quit

	def jenis(self):
		if (os.name != 'posix'):
			os.chdir("python/imparcial/")
			subprocess.Popen(["scrapy", "crawl", "jenis"], shell=True)
		else:
			os.system("python3.6 python/Desktop/jenis.py")
			subprocess.Popen(['mousepad','royale.txt'])
		self.quit

	def botoes(self, nome):
		return f'%s=Button(text=%s,command=self.%s)' % (nome,nome,nome)

	def __init__(self, master=None):
		Frame.__init__(self, master)
		top = Frame()
		top.pack(fill='both', expand=True)
		f = Frame(top)
		f.pack(fill='x')
		rotulo = Label(f, text="Scripts",foreground="white")
		rotulo.pack ()
		rotulo.configure(relief="ridge",font="Arial 26 bold",border=5,background="black")
		holerite = Button(text="Holerite", command=self.holerite)
		zap = Button(text="Zap", command=self.zap)
		royale = Button(text="Royale", command=self.royale)
		youtube = Button(text="Youtube", command=self.youtube)
		gastos = Button(text="Gastos", command=self.gastos)
		guiabolso = Button(text="GuiaBolso", command=self.guiabolso)
		verocard = Button(text="Verocard", command=self.verocard)
		jenis = Button(text="Jenis", command=self.jenis)
		bdo = Button(text="Bdo", command=self.bdo)

		for w in (holerite, zap, royale, youtube, gastos, guiabolso, verocard, bdo, jenis):
			w.configure(relief="groove",border=10,font="Times 20 bold")
			w.pack(side='left',fill='both',expand=True)

app = Application()
app.master.title("Painel de Controle")
app.master.geometry("1300x100+100+40")
mainloop()
