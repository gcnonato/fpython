from PIL import Image
import pytesseract
import os

filename = 'programador.jpg'

homepath = os.path.expanduser(os.getenv("USERPROFILE"))
desktoppath = "Desktop"
path_to_desktop = os.path.join(homepath, desktoppath)
os.chdir(path_to_desktop)
path_to_img = os.path.abspath("fpython/ImageToText/img")
fileimg = os.path.join(path_to_img, filename)

path_to_tesseract = r'C:/Users/luxu/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

print(pytesseract.image_to_string(Image.open(fileimg)))
