import os
from time import sleep
import PySimpleGUI as sg
# import cv2
# import matplotlib.pyplot as plt

try:
  from PIL import Image
except ImportError:
  import Image
import pytesseract

PATH_IMG = os.path.abspath('img')
LIST_IMG = [f for f in os.listdir(PATH_IMG)]


def main(filename):
  try:
    image = getImage(filename)
    cv2.imshow("My Image", image)
    cv2.waitKey(0)
    result = ocr_core(filename)
    if len(result) > 0:
      print(result)
      sleep(10)
    cv2.destroyAllWindows()
    # if k == 27:
    #     # cv2.destroyAllWindows()
    #     print(ocr_core(filename))
    # elif k == ord('s'):
    #     print(f"Touch {k} ")
    #     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #     cv2.imshow("in Gray",gray)
    #     cv2.waitKey(0)
    # cv2.imwrite('joaoCopy.png', img)
  except Exception as e:
    print(f'Error: {e}')


def getImage(filename):
  imageName = os.path.join(PATH_IMG, filename)
  return cv2.imread(imageName)


def plotar(filename):
  image = getImage(filename)
  plt.imshow(image, cmap='gray', interpolation='bicubic')
  plt.xticks([]), plt.yticks([])
  plt.show()


def isExitsImage():
  return [f for f in os.listdir(PATH_IMG)]


def menu():
  os.system("cls")
  print(u"\nThat Image load?\n")
  cont = 0
  for item in LIST_IMG:
    print(f"({cont}) {item}\n")
    cont += 1
  print(f"({cont}) Exit\n")
  submenu = input("Choice options up:")
  return main(LIST_IMG[int(submenu)])
  # return plotar(LIST_IMG[int(submenu)])
  # return ocr_core(LIST_IMG[int(submenu)])


def ocr_core(filename):
  pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
  """
  This function will handle the core OCR processing of images.
  """
  path = os.path.join(PATH_IMG, filename)
  # import ipdb; ipdb.set_trace()
  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
  text = pytesseract.image_to_string(Image.open(path))
  return text


class Gui:

  def __init__(self):
    ...

  def list_folder(self):
    layout = [
      [
        sg.Frame(
          layout=[
            [sg.T("Diretório a ser apagado:")],
            [
              sg.In(key="input"),
              sg.FolderBrowse(
                "Folder", target="input", key="folder_selected"
              ),
            ],
            [sg.Button("ViewDIRS", key="viewdirs")],
          ],
          title="Dirs",
          title_color="yellow",
          relief=sg.RELIEF_SUNKEN,
          tooltip="Use these to set flags",
        )
      ],
      [
        sg.Frame(
          layout=[
            [sg.Text("Arquivo que será apagado:")],
            [
              sg.In(key="-OUTPUT-"),
              sg.FileBrowse(
                "Files",
                target="-OUTPUT-",
                key="filename",
                file_types=(("Text Files", "*.*"),),
              ),
            ],
            [sg.Button("ViewFILES", key="viewfiles")],
          ],
          title="Files",
          title_color="yellow",
          relief=sg.RELIEF_SUNKEN,
          tooltip="Use these to set flags",
        )
      ],
      [sg.Text("_" * 80)],
      [
        sg.Frame(
          "Botões",
          [[sg.Button("Submit"), sg.Exit()]],
          background_color="lightblue",
          title_color="red",
        )
      ],
    ]
    window = sg.Window("Gerenciador", layout, size=(430, 310))
    while True:
      event, values = window.read()
      print(values)
      if "Submit" in event:
        if values["folder_selected"]:
          folder = values["folder_selected"]
          print(folder)
          self.erase.secure_delete_recursive(folder)
        else:
          path_filename = values["filename"]
          print(path_filename)
          # erase_file(path_filename)
        values = None
      if "viewfiles" in event:
        filename = values["filename"]
        with open(filename, "r", encoding="utf-8") as _f:
          archive = _f.read()
        sg.Print(archive)
      if "viewdirs" in event:
        filename = values["folder_selected"]
        list_files_directory = []
        for (_, dirnames, filenames) in os.walk(filename):
          if dirnames:
            list_files_directory.append(f"DIRS..:{dirnames}")
          if filenames:
            list_files_directory.append(f"FILES..:{filenames}")
            list_files_directory.append(f'{"*" * 96}')
        sg.Print(list_files_directory, size=(100, 20), sep="+")
      if event == sg.WIN_CLOSED or "Exit" in event:
        sg.popup_auto_close("Saindo...", auto_close_duration=0.5)
        break
    window.close()

if __name__ == '__main__':
  tela = Gui()
  tela.list_folder()
  # print(menu())


