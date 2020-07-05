# -*- coding: utf-8 -*-
import os
import subprocess
from tkinter import *
from functools import partial

LOCAL_DEFAULT_LINUX = "/home/luxu/Desktop/"
homepath = os.path.expanduser(os.getenv("USERPROFILE"))
desktoppath = "Desktop"
LOCAL_DEFAULT_WINDOWS = os.path.join(homepath, desktoppath, "fpython/")


class Application(Frame):

	def __init__(self, master=None):

		# holerite = Button(text="Holerite", command=self.holerite)
		# royale = Button(text="Royale", command=self.royale)
		# youtube = Button(text="Youtube", command=self.youtube)
		# guiabolso = Button(text="GuiaBolso", command=self.guiabolso)
		# guiabolsow = Button(text="GuiaBolsoW", command=self.guiabolsow)
		# verocard = Button(text="Verocard", command=self.verocard)
		# listamais = Button(text="ListaMais", command=self.listamais)
		# bdo = Button(text="Bdo", command=self.bdo)
		# list_apps = (
		# 	holerite,
		# 	royale,
		# 	youtube,
		# 	guiabolso,
		# 	guiabolsow,
		# 	verocard,
		# 	bdo,
		# 	listamais,
		# )
		Frame.__init__(self, master)
		top = Frame()
		top.pack(fill="both", expand=True)
		self.f = Frame(top)
		self.f.pack(fill="x")
		rotulo = Label(self.f, text="Scripts", foreground="white")
		rotulo.pack()
		rotulo.configure(
			relief="ridge", font="Arial 26 bold", border=5, background="black"
		)
		list_bts = (
			'holerite',
			'royale',
			'youtube',
			'guiabolso',
			'guiabolsow',
			'verocard',
			'bd',
			'listamais',
		)
		for bt in list_bts:
		# for bt in list_apps:
			bt = self.bt(bt)
			bt.configure(relief="groove", border=10, font="Times 20 bold")
			bt.pack(side="left", fill="both", expand=True)
		# for w in list_apps:
		# 	w.configure(relief="groove", border=10, font="Times 20 bold")
		# 	w.pack(side="left", fill="both", expand=True)
	def comando(self, texto):
		subprocess.Popen(["ipython", f"{LOCAL_DEFAULT_WINDOWS}{texto}.py"], shell=True)


	def bt(self, texto):
		return Button(text=f'{texto.capitalize()}', command=lambda: self.comando(texto))


	# def holerite(self):
	# 	if os.name != "posix":  # windows
	# 		os.system(f"ipython.exe {LOCAL_DEFAULT_WINDOWS}holerite.py")
	# 	else:
	# 		os.system(f"ipython {LOCAL_DEFAULT_LINUX}fpython/holerite.py")
	# 	self.quit
	#
	# def royale(self):
	# 	if os.name != "posix":  # windows
	# 		os.system(f"ipython.exe {LOCAL_DEFAULT_WINDOWS}royale.py")
	# 	else:
	# 		os.system(f"ipython {LOCAL_DEFAULT_LINUX}fpython/royale.py")
	# 	self.quit
	#
	# def jupyter(self):
	# 	if os.name != "posix":  # windows
	# 		os.chdir(f"{LOCAL_DEFAULT_WINDOWS}jupyter_virtual_env/venv/Scripts/")
	# 		subprocess.Popen(["start", "activate"], shell=True)
	# 	else:
	# 		subprocess.Popen(["start", "jupyter notebook"], shell=True)
	# 	self.quit
	#
	# def guiabolso(self):
	# 	if os.name != "posix":  # windows
	# 		os.system(f"ipython {LOCAL_DEFAULT_WINDOWS}guiabolso.py")
	# 	else:
	# 		os.system(f"ipython {LOCAL_DEFAULT_LINUX}fpython/guiabolso.py")
	# 	self.quit
	#
	# def guiabolsow(self):
	# 	if os.name != "posix":  # windows
	# 		os.system(f"ipython {LOCAL_DEFAULT_WINDOWS}guiabolsow.py")
	# 	else:
	# 		os.system(f"ipython {LOCAL_DEFAULT_LINUX}fpython/guiabolso_by_requests..py")
	# 	self.quit
	#
	# def youtube(self):
	# 	if os.name != "posix":  # windows
	# 		os.system(f"ipython {LOCAL_DEFAULT_WINDOWS}youtube.py")
	# 	else:
	# 		os.system("python3.6 python/pegar_video.py")
	# 	self.quit
	#
	# def verocard(self):
	# 	if os.name != "posix":
	# 		os.system(f"python.exe {LOCAL_DEFAULT_WINDOWS}verocard.py")
	# 	else:
	# 		os.system("python3.6 python/verocard.py")
	# 	self.quit
	#
	# def bdo(self):
	# 	if os.name != "posix":  # windows
	# 		os.system(f"ipython.exe {LOCAL_DEFAULT_WINDOWS}bd.py")
	# 	else:
	# 		os.system("python3.6 python/selenium/badoo.py")
	# 	self.quit
	#
	# def listamais(self):
	# 	if os.name != "posix":
	# 		os.system(f"ipython.exe {LOCAL_DEFAULT_WINDOWS}listamais.py")
	# 	else:
	# 		os.system("python3.6 python/Desktop/jenis.py")
	# 		subprocess.Popen(["mousepad", "royale.txt"])
	# 	self.quit


app = Application()
app.master.title("Painel de Controle")
mainloop()
