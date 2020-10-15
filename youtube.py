# -*- coding: utf-8 -*-
import os
import subprocess
import sys
from time import sleep


class YoutubeDlScript():

	def __init__(self):
		self.ID = ''
		self.location_script = os.getcwd()


	def repeat_script(self):
		# print("\nDeseja realizar outra operação com o script? [S/N]")
		# REPEAT = input("Digite 'S' para sim ou 'N' para não: ")
		# REPEAT = REPEAT.upper()
		REPEAT = "M"
		if REPEAT == "S":
			if (os.name != 'posix'):  # windows
				os.system("cls")
			else:
				os.system("clear")
			self.main_function_get_id()
		else:
			print("\nSaindo...\n")
			# subprocess.run(["ls", "-l"])  # Run command
			sleep(0.3)
			os._exit(0)

	# Passo 1
	def main_function_get_id(self):
		print(f"Por favor, digite APENAS a ID do vídeo desejado (Exemplo: https://www.youtube.com/watch?v=ID_DO_VÍDEO):\n{'='*80}")
		link_video = input("Link do vídeo: ")
		self.ID = self.separar_id_video(link_video)
		
	
	def separar_id_video(self, link_video):
		posicao_do_igual = link_video.find("v=")
		if posicao_do_igual < 0:
			return posicao_do_igual
		posicao_do_igual += 2
		#print(posicao_do_igual)
		print("Tudo OK! Vamos lá...\n")
		return link_video[posicao_do_igual:]

	# Passo 2
	def video_function_path(self):
		self.location = os.chdir(os.path.expanduser(self.location_script))

	# Passo 3
	def video_function_default_mp4(self):
		if os.name != 'posix':  # windows
			os.chdir('C:\\Users\\luxu\\Desktop')
		else:
			os.chdir('/home/luxu/Desktop')
		# print(os.getcwd())
		if self.ID == -1:
			print("Link inválido")
		else:
			os.system("youtube-dl --format mp4 https://www.youtube.com/watch?v=" + self.ID)
			sleep(0.5)

	
	def option_function_update(self):
		# os.system("youtube-dl --update")
		os.system("pip3 install --upgrade youtube_dl")
		sleep(0.5) # Time in seconds.


	def menu(self):
		if os.name != 'posix':  # windows
			os.system("cls")
		else:
			os.system("clear")
		print("O que deseja fazer?\n(1) Downloads\n\n(2) Atualizar Youtube-Dl\n\n(3) Sair\n")
		ESCOLHA = input("Escolha uma das opções acima:")
		if ESCOLHA == "1":
			self.main_function_get_id()
			self.video_function_path()
			self.video_function_default_mp4()
			self.repeat_script()
			# return self.repeat_script()
		elif ESCOLHA == "2":
			self.option_function_update()
			self.repeat_script()
		elif ESCOLHA == "3":
			print("\nSaindo...\n")
			sleep(0.3) # Time in seconds.
			os._exists(1)
		else:
			print("Esta não é uma opção válida!")
			sleep(0.5)  # Time in seconds.
			self.repeat_script()

if __name__ == '__main__':
	yt = YoutubeDlScript()
	repeact = yt.menu()
	# ytnv = YoutubeDlScript()
	# ytnv.main_function_get_id()
