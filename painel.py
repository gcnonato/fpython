#!/usr/bin/env ipython
# -*- coding: utf-8 -*-
import os
import subprocess
from tkinter import *
import platform

LOCAL_DEFAULT_LINUX = "/home/luxu/Desktop/fpython/"
homepath = os.path.expanduser(os.getenv("USERPROFILE"))
desktoppath = "Desktop"
LOCAL_DEFAULT_WINDOWS = os.path.join(homepath, desktoppath, "fpython/")


class Application(Frame):

	def __init__(self, master=None):

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
			'vivo',
		)

		for bt in list_bts:
			bt = self.bt(bt)
			bt.configure(relief="groove", border=10, font="Times 20 bold")
			bt.pack(side="left", fill="both", expand=True)
	
	def run(self, cmd):
		proc = subprocess.Popen(
			cmd,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE
		)
		stdout, stderr = proc.communicate()
		return proc.returncode, stdout, stderr
	

	def comando(self, texto):
		if os.name != "posix":  # windows
			code, out, err = self.run([sys.executable, f"{LOCAL_DEFAULT_WINDOWS}{texto}.py"])
		else:
			code, out, err = self.run([sys.executable, f"{LOCAL_DEFAULT_LINUX}{texto}.py"])
		print(f"{out}")


	def bt(self, texto):
		return Button(text=f'{texto.capitalize()}', command=lambda: self.comando(texto))


app = Application()
app.master.title("Painel de Controle")
mainloop()
