import os
# from time import sleep

import PySimpleGUI as sg
# import cv2
# import matplotlib.pyplot as plt

# For Windows Only
# 1 - You need to have Tesseract OCR installed on your computer.
#       get it from here. https://github.com/UB-Mannheim/tesseract/wiki
#       Download the suitable version.
# 2 - Add Tesseract path to your System Environment. i.e. Edit system variables.
# 3 - Run pip install pytesseract and pip install tesseract
# 4 - Add this line to your python script every time
# pytesseract.pytesseract.tesseract_cmd = 'C:/OCR/Tesseract-OCR/tesseract.exe'  # your path may be different
# 5 - Run the code.

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract as ocr


class Gui:

    def __init__(self, list_imgs):
        self.list_imgs = list_imgs

    def list_folder(self):
        layout = [
            [sg.T("Escolha a IMAGEM")],
            [sg.Combo(self.list_imgs, size=(20, 12), enable_events=False, key="choiceimage")],
            [sg.Button("Submit"), sg.Exit()],
        ]
        window = sg.Window("Transformar IMG em Texto", grab_anywhere=False).Layout(layout)
        while True:
            event, values = window.read()
            if "Submit" in event:
                if values["choiceimage"]:
                    img_selected = values["choiceimage"]
                    return img_selected
                else:
                    path_filename = values["filename"]
                    print(path_filename)
                    # erase_file(path_filename)
                values = None
            elif "viewdirs" in event:
                filename = values["folder_selected"]
                list_files_directory = []
                for (_, dirnames, filenames) in os.walk(filename):
                    if dirnames:
                        list_files_directory.append(f"DIRS..:{dirnames}")
                    if filenames:
                        list_files_directory.append(f"FILES..:{filenames}")
                        list_files_directory.append(f'{"*" * 96}')
                sg.Print(list_files_directory, size=(100, 20), sep="+")
            elif event == sg.WIN_CLOSED or "Exit" in event:
                sg.popup_auto_close("Exit...", auto_close_duration=0.5)
                break
        window.close()

    def get_text_to_imgr(self, filename):
        homepath = os.path.expanduser(os.getenv("USERPROFILE"))
        desktoppath = "Desktop"
        path_to_desktop = os.path.join(homepath, desktoppath)
        os.chdir(path_to_desktop)
        path_to_img = os.path.abspath("fpython/ImageToText/img")
        path = os.path.join(path_to_img, filename)
        ocr.pytesseract.tesseract_cmd = (
            "C:/Users/luxu/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
        )
        return ocr.image_to_string(Image.open(path))
        # return ocr.image_to_string(Image.open(path), lang='por')


if __name__ == "__main__":
    # Mapeia para a pasta 'img'
    homepath = os.path.expanduser(os.getenv("USERPROFILE"))
    desktoppath = "Desktop"
    path_to_desktop = os.path.join(homepath, desktoppath)
    os.chdir(path_to_desktop)
    path_to_img = os.path.abspath("fpython/ImageToText/img")
    # Pega todas as imagens da pasta 'img'
    list_imgs = [f for f in os.listdir(path_to_img)]
    tela = Gui(list_imgs)
    img = tela.list_folder()
    texto = tela.get_text_to_imgr(img)
    print(texto)
